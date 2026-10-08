---
source_file: "Anniedale_Merrifield+_CRD r2.docx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (Mobile)/2014 Anniedale PoP/Anniedale_Merrifield+_CRD r2.docx"
file_type: "docx"
size_bytes: 115996
content_hash: "0d754528a05c"
converted_at: "2026-10-08T11:29:42"
---

# Anniedale_Merrifield+_CRD r2

| Intel Corporation |
| --- |
| Anniedale |
| Rev 2.0 CRD |

| Q3, 2013 |
| --- |

Table of Contents

1	Introduction	4

1.1	Document Scope	4

2	Platform Description	5

2.1	Overview	5

2.2	Platform Key Messages	5

2.3	Key Dates	5

2.3.1	Platform Key Dates	5

2.3.2	Enabling Key Dates	6

2.4	Platform Components	6

2.5	Cost Targets	6

3	Design Requirements	7

3.1	Processors	7

3.1.1	Processor (2nd Level direct attach)	7

3.2	Processor Stack	8

3.3	Chipsets	8

4	Manufacturing and Serviceability Requirements	8

4.1	Board Assembly	8

4.1.1	SMT	8

4.1.2	SMT Rework	10

4.1.3	Adhesives	11

4.2	System Assembly	11

4.3	Test and Provisioning Requirements	11

4.3.1	Customer Test	11

4.3.2	Customer Provisioning	12

4.3.3	Inspection Tools and Other Metrologies	12

5	General Requirements	13

5.1	PCB Technology	13

5.2	SJR / Reliability	13

5.3	Board Flexure	15

5.4	Traceability	15

5.5	EOS / ESD	16

5.6	Shipping and Handling Media	16

5.7	Environmental and Safety	17

5.8	Supplier Management	17

5.9	Engineering Sample	17

6	Appendix	18

6.1	Customer Requirements Process	18

6.2	Other related customer documents	18

## Introduction

This Customer Requirements Document (CRD) provides Industry Boundary Conditions for design in and technology capability path finding / development.

Intended for both ATTD and Business Unit usage with focus on requirements that impact:

Technology Development

Business Unit / ATTD Design of Enabling Components

Supplier Enabling

Teams that will benefit from this documents are Technology Competency Teams (TCTs), Pathfinding Integration Teams (PFIMs), Design Integration, Platform Engineering (PEBs), Enabling Component Teams, and Socket Engineering

This document will support current development documents such as TMDG and TTS.

See appendix for key customer requirements process and related customer documents.

Do not share this customer sensitive information without prior approval.

### Document Scope

This document concerns requirements for enabling components from customers either explicitly (i.e. requests coming directly from Intel’s customers) or implicitly (i.e. requirements that are based on industry capability such as SMT or reflow requirements).  Both types of requirements are included below.  Other important distinctions are as follows.

In Scope:

Mechanical, thermal and manufacturing related items for the design and manufacture of products which are sold by Intel’s customers. This includes products manufactured by Intel and Enabled Components as described below:

An Enabled component is a component not sold by Intel and is necessary for the proper function of the platform.  Enabled components are categorized into the following groups.

Power delivery

Thermal solution

Tools, jigs, fixtures, etc. required for assembly / disassembly, measurements

Out of scope:

Requirements for debug and probing tools

Requirements for Test tools (thermal test tools, etc.)

## Platform Description

### Overview

| Parameter | Definition |
| --- | --- |
| Market Segment | Smartphone |
| Lead processor product | Anniedale |
| Processor Silicon Technologies | P1271 |
| Chipset / Package Technology | FCMB5T (SoC) |
| Memory Buffer / Package Technology | N/A |

### Platform Key Messages

The Key Technical Changes with impact to customer enabling are:

| Technology Element | Penwell | Tangier | Anniedale |
| --- | --- | --- | --- |
| Substrate Core | Coreless | Coreless | Coreless |
| Die Thickness | 235m | 215m | 90m |
| Package Style | FCMB4 with Interposer | FCMB5 with Interposer | FCMB5T with Through Molding Interconnect |
| BGA Ball Size (mil) | 8 | 8 | 8 |
| SLI Min. Pitch (mm) | 0.4 | 0.4 HexPak | 0.4 HexPak |
| Package Form Factor (mm) | 12x12 | 12x12 | 14x14 |

### Key Dates

#### Platform Key Dates

| Checkpoint | Owner | Date |
| --- | --- | --- |
| SMT | ATTD | End of ‘13 |
| FA | ATTD | End of ‘13 |
| ES1 | MCG | Q1’13 |
| PRQ | MCG | WwQ2’14 |
|  |  |  |
|  |  |  |

#### Enabling Key Dates (TBD)

| Checkpoint | Owner | Date |
| --- | --- | --- |
| CRD 1.5 | ATTD Q&R | Ww13’13 |
| Customer Strategy | MCG | Q1’13 |
| MAS kickoff |  | Ww37’13 |
| Platform Introduction | ATTD Q&R | Ww52’13 |
| MV 1.0 (customer collaborations) | ATTD Q&R | Q1’14 |
| MV completion | ATTD Q&R | Q4’14 |
| MAS 2.0 | ATTD Q&R | Q2’14 |
|  |  |  |

### Platform Components

Anniedale (CPU)

IMC Modem

PMIC – (3rd Party)

### Cost Targets

MCG cost target <$1.65 based on DPP.

## Design Requirements

### Processors

#### Processor (2nd Level direct attach)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Max x-y-z of stack including KOZ | X-Y 12x12 or 14x14mm  Z 1.5mm  Z 1.25 mm normal/1.4 mm max – with pre-stack memory | Legacy: FCMB4 & 5. SS Q&A | OK |  |
| Interposer | None | ODM enabling trips 20012 | N/A |  |
| Marking, Labels, Colors | Pin 1 – must be marked – No confusing fiducials visible 2D Matrix – must be human readable Labels – per Mark Intel spec Colors – none specified.  Visual marking able to withstand two SMT reflows | Legacy | OK |  |
| Board Attach | BGA Acceptable.  Minimum ball diameter = .2mm w/high resolution camera (several PnP vendors capable @ .1mm | PnP equip survey 2010 – Todd Harris CPTD ICC | OK |  |
| Max Thermal Solution Load | N/A |  | OK | 10lb enabling loading was Not part of Samsung request |
| Dynamic Strain | Published shock / strain limits are needed. | Legacy | OK |  |
| Copl (RT)/Warpage(HT) | JEDEC: +/- 100um max at room temp  Samsung current spec: 100um RT copl and -80um at reflow temp required  Competitor’s spec: 80um RT copl and -60um at reflow temp | Customer Enabling meetings ’13 | Action | ATTD plan in place. |

### Processor Stack: N/A

### Chipsets: N/A

## Manufacturing and Serviceability Requirements

### Board Assembly

#### SMT

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Beat Rate | SMT: ≥ 80 cm / min belt speed | Legacy: FCMB4 & 5 | OK |  |
| Yield (eTest, AXI) | SMT: 99.9% at 95% CI achieved on second reflow pass (precondition with one blank reflow).  Within ref process window. | Samsung visit Q1’13 | Action | Incorporate in the internal DOEs |
| Paste  (Bottom package to Board SMT) | Various suppliers in use. Common selections are;  Alpha OM338PT Alpha PoP-959 Henkel Multicore LF721 Indium 8.9 E Senju M705-GRN360-K2-VT. Tpye5 Shenmao P606-p26 Senju S70G | ODM enabling trips ’12 &’13 | Action | CPTD evaluation will cover Industry boundary condition. Do Not just provide a point solution |
| PnP capability Pitch / Size PoP Ball recognition | Min passives 01005 X-Y vs. SLI Pitch Limits: 20x20 @0.4mm;  18x18 @ 0.3 – equipment supplier dependent  Ball recognition:  See section 3.1.2 | 2010 PnP Equip RM | OK |  |
| Flux  (Bottom package to Top Memory package attach) | Alpha 707 Indium 23LV Kester TSF 6592LV  Senju deltalux 529D-1 | ODM enabling trips ’12 &’13 | Action | CPTD evaluation will cover Industry boundary condition. Do Not just provide a point solution |
| Reflow Peak Temp N2 usage Warpage management ∆T Oven capability | Same general guidelines as used with MB4 and MB5. Reference reflow process for air. Reflow capable for both non-inverted and inverted | ODM enabling trips ‘12 | OK | Need provide HVM solution for Air |
| Stencil | 0.003” – 0.004” thick 0.010” round aperture typical Samsung: 0.75 ~ 0.1mm thick, 0.21mm open, square, STS 304. ZTE: 3mil, 0.3mm square. | CQE visits ‘12 | OK | The component density on the board limits stencil design. Customer uses more 3 mile stencil. CPTD action in place/Alfa line |
| Pallet | SMT yield met with & without pallet Pallets generally used with boards thickness < 0.8mm | ODM enabling trips ‘12 | OK |  |

SMT Rework

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Paste or flux print | 90% yield  0.4 mm pitch. Vision accy. ±30 um Samsung requests paste dipping | ODM survey Q2’11 | OK | CPTD action plan in place |
| TAL | BGA: 60 – 120 sec | Pb Free Reflow Window | OK |  |
| Peak temp | BGA: 230-250 ˚C | Pb Free Reflow. | OK |  |
| Max rework cycles | 3 | ODM survey Q2’11 | OK |  |
| Glue removal success rate | 90% | ODM survey Q2’11 | OK |  |
| Package reuse | Yes after reball | ODM Survey Q2’12 | OK | Competitors provide detail instructions |
| Underfill removal success rate | 70% | ODM Survey Q2’11 | OK |  |
| Adhesive Flow+Cure Time (min) | < 5 | ODM survey Q2’11 | OK |  |
| Rework Beat Rate (min.) | 15 Based on Samsung’s production data: 1m unit/month, SMT yield 99.8-99.9%, the quantity of rework units will be 1000-2000 unit/month | CQE’13 visit | Action | ATTD/CPTD action in place |
| Memory rework | Customer (Samsung) requested | CQE’12 visits | Action | ATTD/CPTD need to ensure remove memory without damage it Competitors provide the detail instructions |

#### Adhesives

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Purpose | Higher drop performance | ODM survey q2’11 | OK |  |
| Materials | OEM specified Cost is primary consideration Corner Glue: Loctite 3609 & 3705 BLUF: Hysol UF3800 | ODM enabling trips ‘12 | OK |  |
| Material selection criteria (I.E storable, pot life, cost, availability, env friendly) | OEM specified | ODM enabling trips ‘12 | OK |  |
| Rework | BLUF reworkability  (WE-3008 S1 made by local Korean company Wonchemical.Co.,Ltd)   Apple uses full underfill | ODM survey Q2’11 | Action | CPTD to ensure a HVM BLUF removal process |

### System Assembly N/A

### Test and Provisioning Requirements

#### Customer Test

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| ICT/ATE: Node level coverage | N/A for phones | Legacy: FCMB4 & 5 |  |  |
| Silicon Design for Test Technologies used in board/system manufacturing | (Examples may include IEEE 1149 implementations, REUT, IOSAV, Run time tools) | Customer enabling trip ’12 & ’13 |  |  |
| Processor installation for automated test volumetric | N/A |  |  |  |

#### Customer Provisioning

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Configuration / Provision Location | Offline gang programmer or FT (not all have powered ICT) | CPI Team | OK |  |
| Data Correctness | Assume state of Art Tools | CPI Team | OK |  |
| Impact to ICT | No impact to yield due to CPI;  2000 DPM retest rate | CPI Team | OK |  |
| CPI rework yield (return to line) | 100% | CPI Team | OK |  |
| Impact to Functional TEst | No impact to yield due to CPI;  0 % retest rate | CPI Team | OK |  |
| Functional Test Coverage (ME Mfg meets) | 90% of CPI features | CPI Team | OK |  |
| Test time increase (including reboots) | 10% and no added reboots | CPI Team | OK |  |
| FOQM | 0 DPM | CPI Team | OK |  |
| Board return rates from system factory from end user | No increase | CPI Team | OK |  |
| Debug (for rework) | Samsung requests the methodology to debug PoP package | Account | Action | MCG needs to improve OSV- and create a HVM test socket for debug. MCG solution in place |
| Data Corruption | 2000 DPM | CPI Team | OK |  |
| Upgrades Correctness Server uptime Enabling ID | 100% correctly performed using current tools 97% uptime No errors by customer for enabling ID | CPI Team | OK |  |

#### Inspection Tools and Other Metrologies:  N/A

## General Requirements

### PCB Technology

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Thickness / layer count by segment | 0.026”-0.040” (0.65-1.0mm) Trending to lower values HDI, 8-10 layers | CQE visit’13 | Action | Thinner board need to be incorporated. Samsung used a 0.65mm thin board for testing. Samsung’s thin test board showed visible warpage post reflow. |
| Glass transition temperature (Tg) | 135°-170°C | ODM enabling trips 2012 | OK |  |
| Dielectrics | FR4 – HF, HFR Free | Legacy =FCMB4 & 5 | OK |  |
| Surface Finish | OSP | Legacy | OK |  |
| PTH Mechanical Drill Pad Stack | Per 032-062 Type 3 design guide 2013-2014 | Legacy | OK |  |
| Other material properties CTE Modulus Strength | No specified | Legacy | OK |  |
| Pad size tolerance | +12.5m, and -50m | Customer input | OK |  |

### SJR / Reliability

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Drop/Shock | Internal integrate test to cover customer board level or system boundary conditions – Samsung smartphone board level Drop spec available | Customer engagement input ’12 & ’13 | OK | Action in place in platform qual plan |
| Temp Cycle | Internal integrate test to cover customer board level or system boundary conditions | Customer engagement input ’12 & ’13 | OK |  |

### Board Flexure

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Transient Bend | N/A.  No ICT expected | Customer enabling trip ‘12 | OK |  |

### Traceability

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Unit Level Traceability (ULT) | Maintain unique id for each device for all Intel products Follow 40-0404 Corporate Marking Spec | Corporate Traceability Policy | OK |  |
| ULT Deliver Mechanism  2D Mark (current) | Comply to common industry 2D mark standard Equivalent readability to prior generation and meet MAS document expectation Transparent roadmap and change control system Equivalent “acceptable fallout” to previous generation | MAS document, LM spec | OK |  |
| ULT Content | Ensure uniqueness for each and every Intel device for X years Consistent scheme for all Intel products Consistent scheme regardless of delivery mechanism | Corporate Traceability Policy | OK |  |
| Data Retention | Ensure data availability at unit level consistent with either corporate traceability spec and / or any specific customer agreement | Corporate Traceability Policy and CQN customer agreement | OK |  |
| Box level traceability requirement | N/A |  |  |  |

### EOS / ESD

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| ESD CDM | Customers capable ESD CDM 250 (per 2010 JEP157 or Industry Council White Paper 2) | J. Montoya | OK |  |
| ESD HBM | Customers capable ESD HBM 1kV (per 2009 JEP155 or Industry Council White Paper 1) | J. Montoya | OK |  |
| Handling, Packing and shipping media | ESD sensitive materials required | J. Montoya | OK |  |

### Shipping and Handling Media

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Requirements for trays vs. tape & reel | Same as MB4 and MB5. Thermoformed Tray and T&R. | CPLG | OK | Both Tray and TnR available |
| Manufacturability - Intel ATM, ODMs, OEMs (Trays, Tape & Reel) | Product protection.  No mechanical or electrical (EOS) product damage.  E.g. substrate damage and solder sphere damage.  Trays / T&R compatible with ODM / OEM processing (e.g. PnP)  Preferred:  Compliant to JEDEC Publ 95 (Design Guide for generic S&H matrix trays | CPLG | OK |  |
| Product protection - Outer shipping box for trays and T&R. | Outer shipping box must provide adequate protection for normal shipping and handling during product shipment. (Shock and Vibr requirements listed in Blue BoOK) Moisture protection | CPLG | OK |  |
| Material Content - All shipping media (e.g. Corr cardboard, cushions, MBB, HICs, pallets) | Compliant to all regulatory requirements for substance restriction.  E.g. RoHS and REACH (Contact Intel CPRS with questions)  Must comply with Intel EPC spec 18-1201 | Corp Prod Regs and Stds | OK |  |
| Design for the Environment - Shipping media design must consider Design for the Environment | Design for minimal consumption of raw materials   Materials must be recyclable | EHS | OK |  |

### Environmental and Safety

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| EU RoHS | Continue to comply with 6 banned materials Ensure no materials utilizing exemptions are in use beyong the specified expiration dates | Legal requirement | OK |  |
| JEP-709 (Solid State Devices) IPC-4101C (PCB only) | All new component products must meet the low halogen (halogen free) requirements outlined in JEDEC guideline New cards (Wireless and NICs) must meet both the IPC and JEDEC requirements for finished assembly | Customer / Marketing Requirement | OK |  |
| REACH | All products must declare whether they contain any of the most up to date list of SVHCs (Substances of Very High Concern) >1000ppm | Legal Requirement | OK |  |
| Recycling | N/A |  |  |  |
| Safety | Design, including materials, shall be consistent with the manufacture of units that meet the following safety standards: UL 60950 most current edition and amendments CAN/CSA-C22.2 – 60950 most current edition and amendments EN 60950 most current edition and amendments IEC 60950 most current edition and amendments | Corp. Service | OK |  |

### Supplier Management: N/A

### Engineering Sample

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- |
| Thermal / Mechanical Test Vehicle (TMTV) | Represent final product form factor in order to allow customer modeling. Footprint compatible Full daisy chain for easy solder joint verification | Legacy –FCMB4 & 5 | OK |  |

## Appendix

### Customer Requirements Process

Customer selection:

ODM/OEM: The objective of the engagement is to cover as many customers as possible in this new market segment.

NOTE: The Customer Requirements Document will contain a prioritized set of Requirements targeted at known technology direction. It is not all inclusive and is a subset of other customer information. Sources of this information include:

| Current MV Collaboration Customer Data | PTR sharepoint |
| --- | --- |
| Previous Platform Key Learning | PF BlueboOKs - ICR and vMED (MVE sharepoint) MVTS (CPTD BlueboOK) Post Mortem (CPTD PM sharepoint)  Ramp data (CLT owner) |
| Customer Meetings | Customer Technology OutloOK (MVE sharepoint) Customer MV, Evaluations, FMEA, DOE (owner) Customer trip reports (owner) |
| Equipment and Supplier Capability | Equipment Database (sharepoint) PCB Roadmaps (sharepoint) |
| Customer issues (TD misses) | Tracker (CQN) |
| ODM process flow, equipment, capabilities | Local CQE |
| System Assembly process flow, tools | Under Development (MVE) |

### Other related customer documents

| Document | Generator / Owner | Distribution Method | Customer’s Primary Target Audience |
| --- | --- | --- | --- |
| MAS and CRD | MVE and CQ&R | ILN and CQE Direct | Mfg Engineering, Test Engineering and PCB Layout |
| EMTS and EDS | TME | IBL and FAE Direct | Design Engineering and PCB Layout |
| Platform Design Guide | Division | IBL and FAE Direct | Design Engineering, Test Engineering, and PCB Layout |
| Daisy Chain User Guide | ATTD | IBL and CQE Direct | Mfg Engineering and PCB Layout |
| Thermal Mechanical Design Guide | MPAD, CTME, BCG (Division) | FAE / IBL | Design Engineering and PCB Layout |
