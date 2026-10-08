---
source_file: "2026_RZL-Ax MoP Equipment List_Rev1.pdf"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (Mobile)/2026 Q2 ECG MoP Capability Survey for RZL AX/2026_RZL-Ax MoP Equipment List_Rev1.pdf"
file_type: "pdf"
size_bytes: 671635
content_hash: "a95bc1688cb1"
converted_at: "2026-10-08T11:29:45"
---

# 2026_RZL-Ax MoP Equipment List_Rev1

## Page 1

Intel Confidential – Shared Under CNDA Only
RZL-Ax Memory on Package
(MoP) Equipment List
Intel Corporation
June 2026
Rev 1

## Page 2

Legal Disclaimer
Your costs and results may vary.
No product or component can be absolutely secure.
All product plans and roadmaps are subject to change without notice.
Intel technologies may require enabled hardware, software or service activation.
Intel does not control or audit third-party data. You should consult other sources to evaluate accuracy.
No license (express or implied, by estoppel or otherwise) to any intellectual property rights is granted by this document.
Customer is responsible for safety of the overall system, including compliance with applicable safety-related requirements or
standards.
Code names are used by Intel to identify products, technologies, or services that are in development and not publicly available.
These are not "commercial" names and not intended to function as trademarks.
Intel disclaims all express and implied warranties, including without limitation, the implied warranties of merchantability, fitness for
a particular purpose, and non-infringement, as well as any warranty arising from course of performance, course of dealing, or
usage in trade.
You may not use or facilitate the use of this document in connection with any infringement or other legal analysis concerning Intel
products described herein. You agree to grant Intel a non-exclusive, royalty-free license to any patent claim thereafter drafted
which includes subject matter disclosed herein.
© Intel Corporation. Intel, the Intel logo, and other Intel marks are trademarks of Intel Corporation or its subsidiaries.
*Other names and brands may be claimed as the property of others.
SPE | PQN -Product Quality Network Intel Confidential 2

## Page 3

Revision History
Revision Changes Date
Rev 1 Initial Release June 11, 2026
SPE | PQN - Product Quality Network Intel Confidential 3

## Page 4

General SMT Line Layout
Post-Reflow Automated
Optical Inspection (AOI)
Pre-Reflow Automated Optical
Inspection (AOI)
Solder Paste
Inspection (SPI)
To build with MoP (Memory on Package), a general SMT line layout is needed, but
with some additional tooling & material additions (see the following pages)
SPE | PQN - Product Quality Network Intel Confidential 4

## Page 5

Razor Lake-Ax MoP Equipment List
Placement Machine, Minimum Rqmt’s: Expected Outcome:
• Pick & Place placement machine: Accuracy • Align on PoP process
with BGA Flux Dip
recommendation ≤25um settings.
Capability for MoP
• Fiducials used for memory placement: Memory can be • Successful flux dip
placed on the SoC either using SoC local or PCB global or process (dip plate, dip
fiducials (based on specific equipment capabilities) dwell, flux height, etc.)
• Memory nozzle size: Work with your Pick & Place vendor to
determine the optimal nozzle diameter to accommodate
both memory flux dip & part placement
• BGA Flux Dip Unit: In a feeder slot
• Flux Material: Example: Shenmao SMBF-08*, a tinted flux
(example: black color) may be considered
• Dip plate cavity coplanarity: <35um
• Wet film gauge: To check flux height in dip plate cavity
*Other names and brands may be claimed as the property of others.
SPE | PQN - Product Quality Network Intel Confidential 5

## Page 6

Razor Lake-Ax MoP Equipment List
Pre-Reflow AOI Minimum Rqmt’s: Expected Outcome:
• Pre-Reflow Automated Optical Inspection (AOI) machine: To • Detect if any memory
Inspection for memory
ensure proper memory placement alignment & orientation / placements are incorrect,
polarity either from alignment,
• All 4 RZL-Ax memory devices have the same polarity, as shown orientation or polarity,
below, which the AOI machine should be able to detect. allowing repairs to be
made prior to units
entering the reflow oven
Memory Memory Memory Memory
Pin 1 Pin 1 Pin 1 Pin 1
SoC
Pin 1
*Other names and brands may be claimed as the property of others.
SPE | PQN - Product Quality Network Intel Confidential 6

## Page 7

Razor Lake-Ax MoP Equipment List
Reflow Oven, N2 Minimum Rqmt’s: Expected Outcome:
• Multi-Zone Reflow oven that is Nitrogen capable: • Reflow profile
Capable, to solder
Example: O2 ≤3000 PPM successfully developed,
MoP on SoC
• Reflow pallet used: To prevent motherboard sag meeting key attributes
or warpage • O2 levels are met
• Able to profile with a SAC reflow profile: As • Reflow pallet designed to
shown below prevent board sag or
warpage
*Other names and brands may be claimed as the property of others.
SPE | PQN - Product Quality Network Intel Confidential 7

## Page 8

Razor Lake-Ax MoP Equipment List
X-Ray Minimum Rqmt’s: Expected Outcome:
• 2D (2.5D) X-Ray inspection tool: With the ability to tilt or angle the images to inspect the • Able to
Inspection
solder joint quality for both the memory (MLI) and SoC (SLI) solderjoints successfully
Tool, to check
• 3D X-Ray inspection tool is optional: But it could be helpful to gain a finer level view of evaluate Memory
MLI solderjoint solderjoint quality (example: able to detect SJ open defects) SMT yield by X-
quality • X-Ray Shields and Dosimeters: To measure & control the amount of radiation (RAD) and Ray (X/S and
dosage exposure into the memories, to protect all memory components from radiation over DnP should also
safe dosage limits be used for NPI
• 2D (2.5D) X-ray should be used 100% during NPI and memory rework activities, with regular builds)
sampling during HVM
2D (2.5D) X-Ray 3D X-Ray
Note: Generic X-Ray images shown here to demonstrate a few different solder joint view options
*Other names and brands may be claimed as the property of others.
SPE | PQN - Product Quality Network Intel Confidential 8

## Page 9

Don Martinez to mark up this slide
Razor Lake-Ax MoP Equipment List
Board Level Testing Minimum Rqmt’s: Expected Outcome:
(Diagnostic)
Use case: Manufacturing On-Line Diagnostic or Offline Debug BIOS POST Error Codes Multi-Phase
BIOS POST Error Codes (Multi-Phase) • Detect memory-related boot failures
via Port 80 codes
• BIOS POST Debug Card.
• Isolate failing memory channel
Option 1: Customer legacy debug card (M.2, LPC, PCIE)
interfaces (e.g., ChA, ChB)
– Requires 4-LED Port 80 Display
• Display Output: Port 80 LED
Option 2: Intel recommended debug card via i2c bus (SDA, SCL)
– Platform Design Guide for i2c design requirement (WIP)
Memory Loopback Display
• Production BIOS to support Post Code Port 80 Multiphase
• Enable connectivity test (e.g., Open
Port 80 Debug Card *1 - Firmware codebase will be included as part of the RZL BKC
Solder) for memory DQ/DQS signals
• BIOS POST error code decoding table reference
• Display Output: IMDT App GUI
Use case: Offline Debug RMT MRC Serial Log
• Memory Loop Back Display • Check memory margin during initial
boot with simplified MRC error log
• DDRIO Loopback Firmware Image (Debug BIOS)
message & force flow test.
• UART (preferred) or DCI cable- To be enabled in Debug BIOS
DCI DBC Cable*1 UART Cable *1 • Display Output: IMDT App GUI
• Debug Host PC with Intel IMDT *2 Software Application installed
• RMT MRC Serial log and IBECC (In-Band ECC)
IBECC
• Debug BIOS
• Identify functional type failure (i.e.,
• If using DCI: Enable RMT and DCI/DAM, UART disable. Enable
BSOD, System Hang) related to
IBECC (Error Correction Disabled)
memory corruption.
• If using UART: Enable UART for RMT serial log
• Display Output: IMDT App GUI
• UART (for RMT MRC serial log) or DCI cable (for RMT or IBECC)
• Debug Host PC with IMDT Software Application installed
IMDT Software *1 *1 Other names and brands may be claimed as the property of others.
*2 IMDT: Intel Memory Diagnostic Tool.
SPE | PQN - Product Quality Network Intel Confidential 9

## Page 10

Razor Lake-Ax MoP Equipment List
Edge Bond Minimum Rqmt’s: Expected Outcome:
• Recommend glue is dispensed only after the
Adhesive
motherboard has passed functional testing (to
Jet
avoid unnecessary memory rework)
Dispense • Adhesive Dispense Equipment: Able to dispense
Equipment thermal cure edge bond adhesive on memories
(within 1mm KOZ) and on the SoC (Example: a
piezo electric jetting valve with 200um ID nozzle)
• Height Sense Feature: Dispense equipment has a
height sense feature to create a zero datum for
the Z-axis (targeting the Intel SoC)
• As different memories have different Z-heights,
need to ensure dispense nozzle maintains
≥200um spacing from the top of each memory
height
• Heated nozzle: Example: 60°C, to allow for a lower
viscosity to achieve smaller dot weights / more
accurate dispense
• Adhesive (edge bond) material: That performs
well in Temperature Cycling SJR Testing
(example: Zymet UA-2605B* or Zymet UA-
2625B*).
• Any adhesive used must be reworkable &
Ensure No Insufficient Volume of Glue
removeable, without causing damage to the Intel
Between Memories that prevents Full Wetting
SoC, for returns or FACR purposes
*Other names and brands may be claimed as the property of others.
SPE | PQN - Product Quality Network Intel Confidential 10

## Page 11

Razor Lake-Ax MoP Equipment List
Reflow Oven, to cure Minimum Rqmt’s: Expected Outcome:
• Basic Reflow Oven: Capable to cure the edge bond adhesive • Reflow oven completely
the edge bond
at a low curing temperature, per the adhesive cures the edge bond
adhesive
manufacturer’s specification (example: Zymet UA-2605-B * material that is applied on
cures at 140C for 5 minutes) the memory and SoC
• No Nitrogen requirement
*Other names and brands may be claimed as the property of others.
SPE | PQN - Product Quality Network Intel Confidential 11

## Page 12

Razor Lake-Ax MoP Equipment List
BGA Rework Minimum Rqmt’s: Expected Outcome:
• Automated rework tool with optical BGA alignment capabilities: Nitrogen • Successful
Equipment, to rework
capable (N2 turned on), with both top-side & bottom-side heating capabilities, memory
a memory package(s)
and a topside heating nozzle reworkability with
• Top-side Heating Nozzle Sizes: no SJ damage on
• Nozzle #1-to rework one memory (size 9x15mm) SLI or non-
• Nozzle #2-to rework two memories (size 9x30mm) reworked
• Nozzle #3-to rework three memories (size 9x45mm) memories
• Nozzle #4-to rework four memories (size 9x55mm)
• Hot air pencil: To apply heat used to remove the memory adhesives
• 3mm Torlon* scraper: Or another tool that does not cause any SoC soldermask
damage. Light force is applied when removing memory adhesives
• Memory Shielding Materials: Examples: Chemtronics* CM8 Chemask® or
Techspray* Wondermask P 2211®, to protect (provide a thermal barrier) the
“good” memories not being reworked, dispensed with either a spatula or syringe
• Cure Oven: To cure the memory shielding material
• Rework Pallet Top & Bottom: Example: Aluminum material, to provide robust
motherboard support to minimize PCB warpage during rework
• Fine-Braided Solder Wick, Flux, Wide-tip Soldering Iron: For site-dressing
• Flux Material: The same flux material used during the SMT MoP process,
manually dispensed from a syringe, then spread with a small brush and plastic
spatula.
*Other names and brands may be claimed as the property of others.
SPE | PQN - Product Quality Network Intel Confidential 12

## Page 13

Razor Lake-Ax MoP Equipment List
Enhanced Memory Minimum Rqmt’s: Expected Outcome:
• Pulling Tool MTS Criterion Model 43*: With a fixture and • Successful DnP
Dye and Pull Process,
spacer for customization operation of the memory
to remove it from the
• A thick backing plate attached to the PCB sample: (off the top of the SoC),
top of the SoC Especially important for thin motherboards to improve where 80-90% of the
pull results memory solderjoints can
• Dremel 4300* Hand Polisher: To make the surface be inspected for crack
rough type & crack size
• Red Dye: To highlight any solderjoint cracks
• Vacuum Chamber: Used for the red dye penetration into
potential BGA crack lines
• MIXPAC* Dispenser Gun: Used to control the epoxy
dispense
• 3M* Epoxy 460
• 3M* 501+ High Temperature Masking Tape
• Pull Nut: The nut size should be close to the memory size
• Cure oven: Used to cure the epoxy material
*Other names and brands may be claimed as the property of others.
SPE | PQN - Product Quality Network Intel Confidential 13

## Page 14

_(no extractable text — possibly a scanned image)_
