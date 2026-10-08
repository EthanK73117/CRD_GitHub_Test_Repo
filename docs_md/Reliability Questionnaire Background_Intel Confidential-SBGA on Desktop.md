---
source_file: "Reliability Questionnaire Background_Intel Confidential-SBGA on Desktop.pptx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (DT)/2021 Desktop BGA Products/Reliability Questionnaire Background_Intel Confidential-SBGA on Desktop.pptx"
file_type: "pptx"
size_bytes: 6702263
content_hash: "680577919636"
converted_at: "2026-10-08T11:31:43"
---

# Reliability Questionnaire Background_Intel Confidential-SBGA on Desktop

## Slide 1

**BGA Desktop Use Condition and Expectation**


## Slide 2

**Legal Disclaimer**

- 2

- You may not use or facilitate the use of this document in connection with any infringement or other legal analysis concerning Intel products described herein. You agree to grant Intel a non-exclusive, royalty-free license to any patent claim thereafter drafted which includes subject matter disclosed herein.
- No license (express or implied, by estoppel or otherwise) to any intellectual property rights is granted by this document.
- Intel technologies’ features and benefits depend on system configuration and may require enabled hardware, software or service activation. Learn more at Intel.com, or from the OEM or retailer.
- No computer system can be absolutely secure. Intel does not assume any liability for lost or stolen data or systems or any damages resulting from such losses.
- The products described may contain design defects or errors known as errata which may cause the product to deviate from published specifications. Current characterized errata are available on request.
- Intel disclaims all express and implied warranties, including without limitation, the implied warranties of merchantability, fitness for a particular purpose, and non-infringement, as well as any warranty arising from course of performance, course of dealing, or usage in trade.
- Intel technologies’ features and benefits depend on system configuration and may require enabled hardware, software or service activation. Learn more at intel.com, or from the OEM or retailer.
- All information provided here is subject to change without notice. Contact your Intel representative to obtain the latest Intel product specifications and roadmaps.
- Copies of documents which have an order number and are referenced in this document may be obtained by calling 1-800-548-4725 or visit www.intel.com/design/literature.htm.
- Intel, and the Intel logo are trademarks of Intel Corporation in the U.S. and/or other countries.
- *Other names and brands may be claimed as the property of others.
- © 2021 Intel Corporation. All rights reserved.


## Slide 3

**Background**

- 3

- The solder joint reliability (SJR) requirement of desktop product is defined based on use condition. The goal of this survey is to collect feedback from customers to refine SJR requirement of desktop system.
- This survey focuses on the desktop products with soldered BGA CPU:
- Mini PC, set top box
- All-In-One PC

- Figure1. Examples of Mini PC, All-In-One PC and BGA CPU on motherboard


## Slide 4

**Solder Joint Reliability Fundamentals**

- Solder joint reliability (SJR) is the ability of the solder joints connecting a BGA package to a system board or card to withstand the stresses to which they are exposed during manufacturing, shipping, and End-User operation
- Stresses to the solder joint can come from different sources, including CTE (critical-to-function) induced stress, static mechanical loads, and dynamic mechanical loads
- To accommodate for solder joint stresses, BGA packages are designed with NCTF (non-critical-to-function) joints in high stress areas
- These joints can fail without negatively impacting package capability
- SJR risk is assessed based on package attributes and mechanical modeling, and if needed, empirical data collection

- 4


## Slide 5

**Solder Joint Reliability Overview**

- 5

- Intel certifies Client BGA products using data collection and/or mechanical modeling based on empirical data collection
- The primary reliability stresses that Intel uses for BGA Solder Joint Reliability certification are accelerated temperature cycling and shock tests. These tests envelope many of the stresses BGA packages will go through. Intel does not complete 4-point bend, thermal shock, or sequential temperature cycle and shock testing.

- 1 KBQ requirement calculated based on Intel models using Norris-Landzberg.
- 2 These shock conditions are for a 45 mm x 24 mm package form factor. Different form factors may have different equivalent shock conditions.


## Slide 6

**BGA Desktop Survey**

- 6

- The questions focus on desktop products with soldered BGA CPU:
- Mini PC, set top box
- All-In-One PC
- There are six sections:

- What Intel BGA products are used in desktop products?
- Do you perform board level SJR testing -  JEDEC standard temperature cycle testing?
- Do you perform system level SJR testing?
- What are the product temperature conditions?
- How many power cycles do you anticipate?
- Do you use board level adhesives?


## Slide 7

**JEDEC Standard Temperature Cycle**

- 7

- Scope: This test is conducted to determine the ability of components and solder interconnects to withstand mechanical stresses induced by alternating high- and low-temperature extremes.
- Boards are placed in the temperature cycling chamber and heated or cooled inside the chamber.
- Use Temperature Cycle – X (TCX) as an example:

- Reference: JESD22-A104F

- Temperature range: -40 ˚ C to 85 ˚ C
- Dwell time: 15 min at -40 ˚ C ; 15 min at 85 ˚ C Cycle time: 1 hour


## Slide 8

**Backup**

- 8


## Slide 9

**Norris-Landzberg Model**

- 9


## Slide 10

**Weibull Distribution**

- 10


## Slide 11

**Client Shock Certification Test Setup**

- 11

- Diagonal bend mode, -z direction, 2 ms half-sine pulse
- In-situ electrical monitoring of the daisy chain
- Intel Shock Test Board (STB)
- No Adhesives
- Shock requirements are based on translation from 6-axis system-level drop data
- Client  Req’ts:	5 drops @ 100G (Laptop)
- 5 drops @ 125G (Tablet)
- 5 drops @ 135G (Desktop)
- Success criteria:  No in-situ electrical opens on any CTF joint for above laptop or tablet req’ts
- To set G level, dropped boards from industry standard heights in all 6 orientations with strain gauges. Ran models based on board strain in different orientations to come up with equivalent -z only shock req.
- Drop parameters: 3 drops in each orientation from 0.6 m + 1 drop in worst case orientation from 1 m

- SG1

- SG3


## Slide 12

**Shock Strain Gauge Placement**

- 12

- Shock Strain Gage Placement
- Strain gauges are placed following IPC 9703
- Strain gages are located on the secondary side of the board at the package corners.
- The location of the strain gage is at the intersection of second row and second column of the BGA array (regardless of corner most ball depopulation)


## Slide 13

**Client Temperature Cycle (TC) Test**

- 13

- TC testing was performed per Intel test condition:
- Temp. Cycle-T (TCT) range: -40 ˚ C to 100 ˚ C
- 15min dwell; 1 hour cycle
- In-situ electrical monitoring of the daisy chain
- Intel Enabling Test Board (ETB) design
- No adhesives
- TCT requirements based on standards from client market
- Number of TCT cycles for desktop - use condition base
- Failure criteria - 1000 ohm resistance increase
- Test-to-Fail (TTF) until 60% of the population fails
- Other stresses are used as needed based on technical need and product specific use condition


## Slide 14

**Intel Proprietary SJR Modeling Methodology Example**

- 14


## Slide 15

