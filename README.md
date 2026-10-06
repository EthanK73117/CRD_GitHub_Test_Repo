# CRD_GitHub_Test_Repo

A document knowledge base: converts `.pptx`, `.docx`, `.xlsx`, and `.pdf`
files into Markdown so GitHub Copilot Chat (`@workspace`) can answer
questions about their contents directly in VS Code.

## Folder structure

```
CRD_GitHub_Test_Repo/
├── source_docs/        # original source files (.pptx, .docx, .xlsx, .pdf)
├── docs_md/             # converted Markdown output (generated)
├── doc_to_markdown.py   # conversion script
├── requirements.txt     # Python dependencies
└── .github/
    └── copilot-instructions.md
```

## Setup

```
pip install -r requirements.txt
```

## Usage

Convert all files in `source_docs/` to Markdown in `docs_md/`:

```
python doc_to_markdown.py --source source_docs --output docs_md
```

Or run with no arguments to use the interactive GUI folder/file picker:

```
python doc_to_markdown.py
```

## Asking questions in Copilot Chat

1. Open this folder in VS Code.
2. In Copilot Chat, ask using workspace context, e.g.:
   ```
   @workspace What does the Q3 report say about revenue?
   ```
3. Or attach a specific file from `docs_md/` via the Add Context (📎) button
   for a guaranteed, precise answer from that document.
