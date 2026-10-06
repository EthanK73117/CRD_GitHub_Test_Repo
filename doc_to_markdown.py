#!/usr/bin/env python3
"""
doc_to_markdown.py

Converts .pptx, .docx, .xlsx, and .pdf files in a source directory into
Markdown (.md) files in an output directory, for use as a knowledge base
with VS Code / GitHub Copilot Chat (@workspace) or any RAG pipeline.

Each generated .md file includes a small front-matter header with
traceability metadata (source file, type, conversion timestamp).

-------------------------------------------------------------------------
REQUIREMENTS (install with pip):

    pip install python-pptx python-docx openpyxl pdfplumber

-------------------------------------------------------------------------
USAGE:

    Command-line (explicit paths):

        python doc_to_markdown.py --source "C:\\path\\to\\repo" --output "C:\\path\\to\\repo\\docs_md"

        Optional flags:
            --recursive        Scan subdirectories as well (default: on)
            --overwrite        Overwrite existing .md files (default: off, skips unchanged)

    Interactive GUI (no arguments):

        python doc_to_markdown.py

        A dialog will prompt you to choose either:
            1) A single folder to scan (optionally including subfolders), or
            2) One or more individual files to convert
        You will then be asked to choose an output folder for the .md files.
        (Uses tkinter, which ships with standard Python installs — no extra
        install required.)

-------------------------------------------------------------------------
NOTES:
    - PPTX: extracts slide titles, body text, and speaker notes per slide.
    - DOCX: extracts paragraphs and tables, preserving heading levels.
    - XLSX: extracts each worksheet as a Markdown table.
    - PDF: extracts text per page using pdfplumber. Scanned/image-only PDFs
      will produce empty or near-empty output (no OCR is performed).
"""

import argparse
import datetime
import hashlib
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Optional dependency imports (checked individually so the script can still
# run and convert the formats whose libraries ARE installed).
# ---------------------------------------------------------------------------
try:
    from pptx import Presentation
except ImportError:
    Presentation = None

try:
    import docx  # python-docx
except ImportError:
    docx = None

try:
    import openpyxl
except ImportError:
    openpyxl = None

try:
    import pdfplumber
except ImportError:
    pdfplumber = None


SUPPORTED_EXTENSIONS = {".pptx", ".docx", ".xlsx", ".pdf"}


def make_front_matter(source_path: Path, file_type: str) -> str:
    """Build a small YAML front-matter block for traceability."""
    stat = source_path.stat()
    sha1 = hashlib.sha1(source_path.read_bytes()).hexdigest()[:12]
    converted_at = datetime.datetime.now().isoformat(timespec="seconds")
    return (
        "---\n"
        f"source_file: \"{source_path.name}\"\n"
        f"source_path: \"{source_path.as_posix()}\"\n"
        f"file_type: \"{file_type}\"\n"
        f"size_bytes: {stat.st_size}\n"
        f"content_hash: \"{sha1}\"\n"
        f"converted_at: \"{converted_at}\"\n"
        "---\n\n"
    )


# ---------------------------------------------------------------------------
# Converters
# ---------------------------------------------------------------------------
def convert_pptx(path: Path) -> str:
    if Presentation is None:
        raise RuntimeError("python-pptx is not installed. Run: pip install python-pptx")

    prs = Presentation(str(path))
    lines = [f"# {path.stem}\n"]

    for i, slide in enumerate(prs.slides, start=1):
        lines.append(f"## Slide {i}\n")

        title_text = None
        body_lines = []

        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            text = shape.text_frame.text.strip()
            if not text:
                continue
            if shape == slide.shapes.title:
                title_text = text
            else:
                body_lines.append(text)

        if title_text:
            lines.append(f"**{title_text}**\n")

        for body in body_lines:
            for line in body.splitlines():
                line = line.strip()
                if line:
                    lines.append(f"- {line}")
            lines.append("")

        # Speaker notes
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text.strip()
            if notes:
                lines.append("> **Speaker notes:**")
                for line in notes.splitlines():
                    line = line.strip()
                    if line:
                        lines.append(f"> {line}")
                lines.append("")

        lines.append("")

    return "\n".join(lines)


def convert_docx(path: Path) -> str:
    if docx is None:
        raise RuntimeError("python-docx is not installed. Run: pip install python-docx")

    document = docx.Document(str(path))
    lines = [f"# {path.stem}\n"]

    for element in document.element.body:
        tag = element.tag.split("}")[-1]

        if tag == "p":
            # Find matching paragraph object to get style/text
            para = next(
                (p for p in document.paragraphs if p._p is element), None
            )
            if para is None:
                continue
            text = para.text.strip()
            if not text:
                continue
            style = (para.style.name or "").lower()
            if "heading 1" in style:
                lines.append(f"## {text}\n")
            elif "heading 2" in style:
                lines.append(f"### {text}\n")
            elif "heading 3" in style:
                lines.append(f"#### {text}\n")
            else:
                lines.append(f"{text}\n")

        elif tag == "tbl":
            table = next(
                (t for t in document.tables if t._tbl is element), None
            )
            if table is None:
                continue
            lines.append(_table_to_markdown(
                [[cell.text.strip() for cell in row.cells] for row in table.rows]
            ))
            lines.append("")

    return "\n".join(lines)


def convert_xlsx(path: Path) -> str:
    if openpyxl is None:
        raise RuntimeError("openpyxl is not installed. Run: pip install openpyxl")

    wb = openpyxl.load_workbook(str(path), data_only=True)
    lines = [f"# {path.stem}\n"]

    for sheet in wb.worksheets:
        lines.append(f"## Sheet: {sheet.title}\n")

        rows = []
        for row in sheet.iter_rows(values_only=True):
            if all(cell is None for cell in row):
                continue
            rows.append(["" if cell is None else str(cell) for cell in row])

        if not rows:
            lines.append("_(empty sheet)_\n")
            continue

        lines.append(_table_to_markdown(rows))
        lines.append("")

    return "\n".join(lines)


def convert_pdf(path: Path) -> str:
    if pdfplumber is None:
        raise RuntimeError("pdfplumber is not installed. Run: pip install pdfplumber")

    lines = [f"# {path.stem}\n"]

    with pdfplumber.open(str(path)) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            lines.append(f"## Page {i}\n")
            text = page.extract_text() or ""
            text = text.strip()
            if text:
                lines.append(text)
            else:
                lines.append("_(no extractable text — possibly a scanned image)_")
            lines.append("")

    return "\n".join(lines)


def _table_to_markdown(rows: list[list[str]]) -> str:
    """Render a list of rows (list of cell strings) as a Markdown table."""
    if not rows:
        return ""

    def clean(cell: str) -> str:
        return cell.replace("\n", " ").replace("|", "\\|").strip()

    header = rows[0]
    out = ["| " + " | ".join(clean(c) for c in header) + " |"]
    out.append("| " + " | ".join("---" for _ in header) + " |")
    for row in rows[1:]:
        out.append("| " + " | ".join(clean(c) for c in row) + " |")
    return "\n".join(out)


CONVERTERS = {
    ".pptx": convert_pptx,
    ".docx": convert_docx,
    ".xlsx": convert_xlsx,
    ".pdf": convert_pdf,
}


# ---------------------------------------------------------------------------
# GUI picker (tkinter — ships with standard Python, no extra install needed)
# ---------------------------------------------------------------------------
def gui_pick_inputs() -> list[Path]:
    """
    Show a small dialog letting the user choose between selecting a single
    folder to scan, or selecting one or more individual files. Returns the
    resolved list of supported files to convert.
    """
    import tkinter as tk
    from tkinter import filedialog, messagebox

    root = tk.Tk()
    root.withdraw()  # we only want the dialogs, not a full window

    choice = messagebox.askyesnocancel(
        title="Select input",
        message=(
            "Convert a whole FOLDER?\n\n"
            "Yes = choose a folder to scan\n"
            "No = choose individual files\n"
            "Cancel = quit"
        ),
    )

    if choice is None:
        print("Cancelled.")
        root.destroy()
        sys.exit(0)

    files: list[Path] = []

    if choice:  # Yes -> folder mode
        folder = filedialog.askdirectory(title="Select a folder to scan")
        if not folder:
            print("No folder selected. Exiting.")
            root.destroy()
            sys.exit(0)

        recurse = messagebox.askyesno(
            title="Include subfolders?",
            message="Also scan subfolders of the selected folder?",
        )
        files = find_source_files(Path(folder), recursive=recurse)

    else:  # No -> individual file mode
        filetypes = [
            ("Supported documents", "*.pptx *.docx *.xlsx *.pdf"),
            ("PowerPoint", "*.pptx"),
            ("Word", "*.docx"),
            ("Excel", "*.xlsx"),
            ("PDF", "*.pdf"),
            ("All files", "*.*"),
        ]
        selected = filedialog.askopenfilenames(
            title="Select one or more files to convert", filetypes=filetypes
        )
        files = [
            Path(p) for p in selected
            if Path(p).suffix.lower() in SUPPORTED_EXTENSIONS
        ]

    root.destroy()
    return files


def gui_pick_output(default_dir: Path) -> Path:
    """Prompt the user to choose an output folder for the converted .md files."""
    import tkinter as tk
    from tkinter import filedialog, messagebox

    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo(
        title="Select output folder",
        message="Next, choose a folder where the converted .md files will be saved.",
    )
    folder = filedialog.askdirectory(
        title="Select output folder", initialdir=str(default_dir)
    )
    root.destroy()

    if not folder:
        print("No output folder selected. Exiting.")
        sys.exit(0)

    return Path(folder)


# ---------------------------------------------------------------------------
# Main driver
# ---------------------------------------------------------------------------
def find_source_files(source: Path, recursive: bool) -> list[Path]:
    pattern = "**/*" if recursive else "*"
    return [
        p for p in source.glob(pattern)
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
    ]


def convert_file(path: Path, output_dir: Path, overwrite: bool) -> str:
    ext = path.suffix.lower()
    converter = CONVERTERS[ext]

    relative_name = path.stem + ".md"
    out_path = output_dir / relative_name

    if out_path.exists() and not overwrite:
        return f"SKIP   (exists): {path.name}"

    try:
        body = converter(path)
    except RuntimeError as e:
        return f"ERROR  (missing dependency): {path.name} -> {e}"
    except Exception as e:
        return f"ERROR  (conversion failed): {path.name} -> {e}"

    front_matter = make_front_matter(path, ext.lstrip("."))
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_text(front_matter + body, encoding="utf-8")

    return f"OK     : {path.name} -> {out_path.name}"


def main():
    parser = argparse.ArgumentParser(
        description="Convert .pptx, .docx, .xlsx, and .pdf files to Markdown."
    )
    parser.add_argument(
        "--source", required=False,
        help="Source directory to scan. If omitted, a GUI picker is shown."
    )
    parser.add_argument(
        "--output", required=False,
        help="Output directory for .md files. If omitted, a GUI picker is shown "
             "(only used in GUI mode; required when --source is given)."
    )
    parser.add_argument(
        "--recursive", action="store_true", default=True,
        help="Scan subdirectories (default: on, CLI mode only)"
    )
    parser.add_argument(
        "--no-recursive", dest="recursive", action="store_false",
        help="Only scan the top-level source directory (CLI mode only)"
    )
    parser.add_argument(
        "--overwrite", action="store_true",
        help="Overwrite existing .md files (default: skip if already converted)"
    )
    args = parser.parse_args()

    if args.source:
        # ---- Command-line mode: explicit directory ----
        source = Path(args.source).expanduser().resolve()
        if not args.output:
            print("--output is required when --source is provided.", file=sys.stderr)
            sys.exit(1)
        output = Path(args.output).expanduser().resolve()

        if not source.is_dir():
            print(f"Source directory does not exist: {source}", file=sys.stderr)
            sys.exit(1)

        files = find_source_files(source, args.recursive)
        default_output_hint = source
    else:
        # ---- Interactive GUI mode ----
        files = gui_pick_inputs()
        if not files:
            print("No supported files (.pptx, .docx, .xlsx, .pdf) selected.")
            return

        default_output_hint = files[0].parent
        output = Path(args.output).expanduser().resolve() if args.output \
            else gui_pick_output(default_output_hint)

    if not files:
        print("No supported files (.pptx, .docx, .xlsx, .pdf) found.")
        return

    print(f"Found {len(files)} file(s). Converting to {output} ...\n")
    for path in files:
        result = convert_file(path, output, args.overwrite)
        print(result)

    print("\nDone.")


if __name__ == "__main__":
    main()
