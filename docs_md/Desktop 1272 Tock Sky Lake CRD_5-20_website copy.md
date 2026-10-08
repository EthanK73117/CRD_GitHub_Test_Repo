---
source_file: "Desktop 1272 Tock Sky Lake CRD_5-20_website copy.docx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (DT)/2013 Sky Lake/Desktop 1272 Tock Sky Lake CRD_5-20_website copy.docx"
file_type: "docx"
size_bytes: 450131
content_hash: "5ec2ecae2d44"
converted_at: "2026-10-08T11:50:09"
---

# Desktop 1272 Tock Sky Lake CRD_5-20_website copy

|  |
|  |

|  |
| --- |

## Introduction

This Joint Business Unit / CPTD Customer Requirements Document (CRD) provides Industry Boundary Conditions for technology capability pathfinding / development.

Intended for both ATTD and Business Unit usage with focus on requirements that impact:

Technology Development

Business Unit / ATTD Design of Enabling Components

Supplier Enabling

Teams that will benefit from this documents are Technology Competency Teams (TCTs), Pathfinding Integration Teams (PFIMs), Design Integration, Platform Engineering (PEBs), Enabling Component Teams, and Socket Engineering

This document will support current development documents such as TMDG, TTS and Socket Requirements.

See appendix for key customer requirements process and related customer documents.

Do not share this customer sensitive information without prior approval.

### Document Scope

This document concerns requirements for enabling components from customers either explicitly (i.e. requests coming directly from Intel’s customers) or implicitly (i.e. requirements that are based on industry capability such as SMT or reflow requirements).  Both types of requirements are included below.  Other important distinctions are as follows.

In Scope:

Mechanical, thermal and manufacturing related ingredients for the design and manufacture of products which are sold by Intel’s customers. This includes products manufactured by Intel and Enabled Components as described below:

An Enabled component is a component not sold by Intel and is necessary for the proper function of the platform.  Enabled components are categorized into the following groups.

Power delivery (e.g. VR heatsinks, Voltage Regulator Test Tool)

Thermal solution (processor and power delivery and includes TIM2)

Socket

Retention (e.g., back plate, spring, standoffs, etc.)

Tools, jigs, fixtures, etc. required for assembly / disassembly, measurements

Out of scope:

Requirements for debug and probing tools

Requirements for Validation tools (thermal test tools, etc.)

### Key Deployment Forums

ATTD Deployment and Action Planning will be managed by Customer Enabling TCT (Vijay Wakharkar)

Divisional Deployment will be managed by Dan Gerbus

## Platform Description

### Overview

| Parameter | Definition |
| --- | --- |
| Market Segment | Desktop |
| Socket | H4 or TLGA (TBD) – Target decision by EOY |
| Lead processor product | 1272 Tock Skylake |
| Socket Compatible Processors | 1274 Tick (TBD) |
| Processor Silicon Technologies | 1272 |
| Chipset / Package Technology | 1271 – Sunrise Point? (ask Dave Lober) |
| Memory Buffer / Package Technology | DDR memory or PCIe level (TBD)? |
| LAN Technology | (ask Dave Lober)? |

### Platform Key Messages

The Key Technical Changes with impact to customer enabling are:

Potential for new DT Socket (H4 or TLGA)?

Thin core for LGA and/or reduced pitch?

Potential for BGA processor support?

### Key Dates

#### Platform Key Dates

| Platform Checkpoint | Owner | Date |
| --- | --- | --- |
| Rev -300 POC | ATTD – Sriram Srinivasan | WW03 2011 |
| Rev -200 AP | ATTD – Sriram Srinivasan | Q4 2011 |
| Rev -100 TTS | ATTD – Sriram Srinivasan | Q2 2012 |
| LEC | ATTD – Sriram Srinivasan | Q3 2014 |
| POP1 | BU – Dan Gerbus | TBD |
| POP2 | BU – Dan Gerbus | TBD |
| POP3 | BU – Dan Gerbus | TBD |
| PRQ | ATTD – Jose Gomez | Q3-Q4 2014 |

#### Enabling Key Dates (Dan B)

“Pure Technology” Customer Feedback:	Q3 / Q4 2011 (IF TLGA STILL POR) – need to align with internal decision

Sky Lake Platform Introduction: 	Q3 / Q4 2012

Sky Lake MV Customer Collaborations:	Q3’2013 – Q3’2014

Sky Lake MV Milestone:			Q3 / Q4 2014

### Platform Components

Socket TBD (include socket cover)

LGA Processor (Skylake)

BGA Processor (Skylake) -> (Per Dan G, BGA is an option currently on the table)

Processor heatsink, retention, backplate and ILM (separate backplate & ILM mounting from heatsink/retention mounting)

Chipset

Chipset heatsink and retention

LAN component

Memory uDIMM or SODIMM

Hotham Test Technology

Low Halogen PCB Technology

PCB Technology (HDI / Type 3? TBD-Juan Landeros)

### Cost Targets

Customers are expecting to have a zero platform cost increase change from legacy platform

## CRD Key Messages

This CRD is the initial Desktop CRD. Many requirements are defined using current state of art. Customer engagements during early pathfinding are planned and document may have interim updates after these meetings.

Focus for this Platform is:

LGA Socket H4 or TLGA (TBD): Expected to be a socket change.

Shock, TC, Rework, SMT solutions & Customer Enabling would all have potential risks.

Contact technology is TBD for TLGA.

BGA processor TBD:

Shock, TC, Rework, SMT solutions & Customer Enabling would all have potential risks.

Chipset TBD:

Shock, TC, Rework, SMT solutions & Customer Enabling would all have potential risks.

2D matrix for Unit Level Traceability is not expected to change. It is not yet known if complimentary technology, like RFID or alternative traceability, will be targeted to this platform.

CPI requirements are not known.

Component ESD capabilities are not known.

## Design Requirements

### System

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| System Form Factor | Enabling solution shall comply with the following system form factors thermal/mechanical boundary conditions.  ATX uATX mini-ITX  No enabling solution support provided by Intel. Dan G-What about the PCCG solution? AIO (All in One) | Legacy |  | Biz Impact | PXT |
| System Thermal | Maximum Processor HS Mass: 500 g (Dan G-What about the Extreme Edition Platform, up to 550 - 900g?) Maximum Chipset HS Mass: TBD | Legacy |  | Market Share | PEB |
| System Mechanical | Board Level Shock: 50g Trapezoidal, ∆V 170 in/sec, 6 faces (3 shocks per face) Board Level Vibration (unpackaged): 3.13 grms, 0.01 g2/hz at 5 hz ramping to 0.02 g2/hz at 20 hz, 0.02 g2/hz at 29 hz to 500 hz, 10 minutes per axis, 3 axis Edge sharpness shall comply with UL1439 Flammability is UL60950/00 class 94 V2 or better (for non SMT component) | Legacy |  | Reliability | PEB |
| Product Marking | Intel components (assemblies) require marking and lot identification. | Legacy (40-0404) |  | Quality Inconvenience Part Mix Ups Legal Violations | PEB / DIWG |
| Mother Board Design and PCB Thickness | PLEASE REVIEW PCB IN GENERAL REQUIREMENTS SECTION OF THIS CRD |  |  |  |  |

### Processors

#### LGA Processor (Socket attach) (Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Marking, Labels, Colors | Pin 1 – must be marked on top side and bottom (LAND) side 2D Matrix – comply with 2D mark industry standard and readable by MAS documented scanners Labels – per Mark Intel spec Colors – none specified  Contact customer team (PTR/CME) if introducing new colors or marks | Legacy (40-0404) |  | Quality Inconvenience Part Mix Ups Legal Violations | DIWG |
| Installation Features | The processor must have accommodations to be handled by both humans and tools (to support both HVM mfg & end user environments). BU has 10 years of history to say tool-less is our preference. BU desire is to be tool-less, as much as practical, but bent contact issues must be considered. Solution must accommodate a finger size of (Socket T baseline) Finger Breadth/Width (X): 13mm Rqmt, 18mm Best Case Finger Thickness (Y): 4mm Rqmt, 10mm Best Case Finger Depth (Z): 5mm Rqmt, 8mm Best Case Finger and Tool Access needed when removed from shipping trays (same KOZ as above) Finger and Tool Access needed to Install into socket (same KOZ as above) Processor / Tray must have features so tool can pick it directly from the tray. In addition to pin A1 package depopulation,  add visible marks for alignment / orientation with the pin A1 corner on both socket and package | Socket Health WG |  |  | Socket TCT / Socket WG / DIWG / Desktop PTR |
| IHS Requirement | IHS flatness requirement: 0.035 mm TIM1 material performance comparable to legacy (Dan G – team recommends to remove this, not customer visible) Robust IHS design to not deform processor and has to sustain a minimum of 50,000 test cycles | Legacy (Skt H1 IHS LID DWG D96904)  Foxconn Wuhan |  |  | PEB |
| General package | LAND side pads to sustain a minimum of 50,000 test cycles IHS features on LGA package for easy finger gripping is needed.  Customers have requested a more easily graspable solution | Socket Health WG |  |  | Socket TCT / Socket WG / DIWG |

#### Processor (2nd Level direct attach)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Max x-y-z of stack including KOZ | TBD |  |  |  |  |
| Marking, Labels, Colors | TBD |  |  |  |  |
| Board Attach | TBD |  |  |  |  |
| IHS requirements | TBD |  |  |  |  |
| Max Heatsink Mass | TBD |  |  |  |  |
| Dynamic Strain | TBD |  |  |  |  |
| Warpage | TBD |  |  |  |  |

### Processor Stack

#### Socket  (Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Max x-y-z of stack including KOZ | Motherboard to IHS KOZ: TBD   Heatsink KOZ (Add Definition, is this the space required to attach the heatsink? Do we even need this requirement?): TBD | Legacy |  |  | PEB |
| Socket Material | Thermoplastic or equivalent, UL 94 V-0 flame rating, temperature rating and design capable of maintaining structural integrity following a temperature of 260 °C for 40 seconds | Legacy |  |  | Socket TCT / Socket WG |
| Contacts | Ensure no exposed contacts prior to Processor Installation or after Processor Removal If not possible to ensure contact non-exposure, then contact / socket design must eliminate bent contact susceptibility by… Limit the number of total contacts in the LGA socket to no greater than 2011? (discuss with Dan Gerbus. This was MSI’s feedback…Would this actually help? No correlation…) Ensuring a robust contact design (in X, Y & Z axis) for bent contact resistance, that is equal to or greater than Socket T’s contact robustness Guard contacts against permanent deformation from side or top impacts, such as dropped packages, LANs on bottom of packages, dropped covers or bare / gloved hands Ensure ISP (“Local Contact Partitions”) are added to protect every contact location and by all socket vendors This list not an exhaustive list… just some comments… | Socket Health WG |  |  | Socket TCT / Socket WG |
| Socket body marking, labels, colors | All markings & colors must align with the LGA Socket ILM BP Consistency Marking Guide, SPEED DOC# G14577 (owner = Sathya Ganesan). This document must be updated with all new socket versions. Date code and/or Lot code for the purposes of identification. Markings required on socket body (for all samples/revisions being shipped by suppliers during development)  Pin 1 - triangle needs to be marked on the ILM (wrong section, move to ILM?), and the socket key posts pad printed for better identification. Color – dark on bottom-side, as compared to the solder balls, to provide the contrast needed for PnP vision systems.  Visual marking able to withstand three SMT reflows  Contact customer team (PTR/CME) if introducing new colors or marks | Socket Health WG  Legacy |  |  | Socket TCT / Socket WG |
| Board attach | Socket will be attached to the board with SMT solder.  Contact customer team (PTR/CME) if introducing new attach mechanisms (i.e. adhesives, screws, etc) | Legacy |  |  | Socket TCT / Socket WG |
| Socket / Finger Access Features | Recessed cutouts on all four sides of the socket are required to facilitate the manual install or removal of inserted package (unless a grip-ability feature has been provided on the IHS) Cut Outs must accommodate a finger size of (Socket T baseline) Finger Breadth/Width (X): 13mm Rqmt, 18mm Best Case Finger Thickness (Y): 4mm Rqmt, 10mm Best Case Finger Depth (Z): 5mm Rqmt, 8mm Best Case | Socket Health WG  Customer Feedback |  |  | Socket TCT / Socket WG |
| Socket / Processor Insertion and Removal Features | Keying or Socket alignment features that prevent processor from interfacing with the socket contacts unless properly oriented.  Package co-planarity with enabling solution to enable good TIM2 bond line | Legacy –Skt H1, H2, H3 |  |  | Socket TCT / Socket WG |
| Socket Durability | Reference GS25-3000 (client) 30 insertion / removal cycles | Legacy –Skt H1, H2, H3 |  |  | Socket TCT / Socket WG |
| Max compressive static load (from Heatsink) | Max load applied to top of IHS: 50 lb Max load applied to top of IHS, including ILM compressive load: 50 lb + 135 lb = 185 lb | Legacy –Skt H1, H2, H3 |  |  | PEB |
| Max Heatsink Mass | TBD – Dan Gerbus? | Legacy –Skt H1, H2, H3 |  |  | PEB |
| Dynamic Strain | No requirement at this time |  |  |  |  |
| Board Flexure Initiative | Socket BFI ue Rqmt (Higher than or equivalent to previous socket limits): ≥600 ue for 62 mil thick PCB | Legacy –Skt H1, H2, H3 |  |  | BLI WG |
| Warpage | Characterize socket dynamic warpage to make available to customers | OEM Customer Request (Dell) |  |  | Socket TCT / Socket WG |
| Unpopulated socket | Not Applicable (Dan Gerbus – do we have any multi-socketted platforms?) |  |  |  |  |

#### PnP Cover (Dan B / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| PnP cover marking, labels, colors | All markings & colors must align with the LGA Socket ILM BP Consistency Marking Guide, SPEED DOC# G14577 (current owner = Sathya Ganesan). This document must be updated with all new socket versions. The default color for PnP cover is black.  The color must work with customer’s PnP systems.   Contact customer team (PTR/CME) if introducing new colors or marks | Socket Health WG  Legacy |  |  |  |
| Install and Removal Features | The socket shall have a detachable cover to support the vacuum type PnP system. The cover needs to prevent damage to the contact field during motherboard assembly. PnP cover feature of PnP cover should not interfere with motherboard components placed inside socket cavity. The removal of the PnP cover should not cause any possible damage to the socket body nor the cover itself. PnP Cap Removal Tool grip locations to match prior socket family PnP cap grip locations, and made CTF to ensure consistency across suppliers (to ensure industry tool consistency) – Some customers develop automated tooling to remove & replace this cap by robot. The cover must not fall off or require Kapton Tape to be used during the rework process. Ensure the PnP Cover design has the same consistent “flick off” design, similar to prior generation of Socket H PnP Cover (Dan to align with King, look across all Intel socket families) | Socket Health WG  Legacy  FTS Feedback on Grip Locations (CTF) |  |  |  |
| Cover Venting Features | The cover venting design must achieve these minimum requirements, but not too excessive to allow major solder splashing (below): Socket Delta T ≤10 Deg C MB Delta T of ≤12 Deg C Belt Speed of ≤100 cm/min on Heller oven (worst case oven)  The cover venting design to prevent the majority of flux or solder splashing from the reflow / wave solder ovens. | Legacy |  |  |  |
| Ergo | 1.4 lbf MAX removal force (assumes the use of PnP cap removal tool and that end customer’s won’t see the PnP cover, only the ILM Cover) The cover design shall meet or exceed the applicable requirements of SEMI S8-0999 Safety Guidelines for Ergonomics/Human Factors Engineering of Semiconductor Manufacturing Equipment. | Legacy |  |  |  |
| Supplier compatibility | Socket cap must be interchangeable between suppliers (e.g. Tyco cap on Foxconn socket) Tool used to remove Socket cap must be able to be used across all suppliers | Legacy |  |  |  |
| Durability | 20 insertion / removal cycles | Historical req’mt |  |  |  |

#### Backplate (Dan G / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Backplate marking and colors | All markings & colors must align with the LGA Socket ILM BP Consistency Marking Guide, SPEED DOC# G14577 (current owner = Sathya Ganesan). This document must be updated with all new socket versions. Contact customer team if introducing new colors or marks | Socket Health WG |  |  |  |
| X-Y-Z constraints | 5.08mm max normal to board Add server BP thickness Note: Evaluate moving to the thinnest spec Add MAX fastener protrusion length (considering Worst Case Workstation racks) | ATX spec |  |  |  |
| Attach | Backplate should not be captive to the PCB. Backplate is allowed to “float” slightly so that ILM can correctly locate to the socket.  No knurl features on backplate stud Backplate shall not be designed to attach directly to the chassis. |  |  |  |  |
| Insulation | Backplate assembly (includes insulator) must be non-conductive.  Insulator must resist puncturing from backside vias. |  |  |  |  |
| Rework-ability | Backplate must be reworked easily (e.g. no adhesive to board, etc. |  |  |  |  |
| Deflection | Combined Backplate thickness, insulator thickness, and backplate deflection does not exceed 5.08mm under maximum loading. Need to add server BP |  |  |  |  |

#### Load Mechanism and Actuation Tools (Dan G / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Load Mechanism Type (ILM, DSL, PGA, etc) | Equal to or less than prior generation in cost and equal to or greater than in mechanical and electrical performance |  |  |  |  |
| Volumetric  (KOZ width, height) | All LM components must remain below the plane defined by the surface of IHS for all package stackups ILM must accommodate board thicknesses as defined in “General requirements” section  ILM metal is not to contact adjacent mother board components (This is a Customer DFM violation). | Gigabyte Cap Scratch Issue |  |  |  |
| Marking and Keying | All markings & colors must align with the LGA Socket ILM BP Consistency Marking Guide, SPEED DOC# G14577 (current owner = Sathya Ganesan). Components / assemblies require marking and lot identification. Must be keyed for one-way assembly over socket Must be marked with Pin1 locater on load plate viewable with ILM cover on |  |  |  |  |
| Attach | No sequencing of fasteners required for performance or reliability of the processor-stack ILM fasteners to backplate must use T20 captive fasteners ILM load plate and load lever must not touch board at any time (during install / remove, populated or unpopulated condition)  Mylar must be used to protect any PCB surface that could come in contact with LM metal surfaces. |  |  |  |  |
| Actuation Mechanism | Do not exceed Ergo force recommendation (currently 4.7 lbf nominal) The load plate must not close when processor is incorrectly oriented  ILM Actuation requires intuitive lever rotation. No more than one ILM lever  The design of the actuation mechanism (levers, socket walls, etc) shall allow for finger space for processor remove / install |  |  |  |  |
| Load | ILM applies sufficient load for electrical continuity at Time0. Loading from thermal solution is not required to maintain electrical continuity at EOL |  |  |  |  |
| Heatsink Attach | ILM allows for flat-bottom heatsink ILM Must be validated with 500g heatsink under Intel Bluebook testing |  |  |  |  |
| ILM Durability | 30 insertion / removal cycles Robust ILM design to not deform the IHS, during minimum of 50,000 test cycles | Legacy  Foxconn Wuhan |  |  |  |

#### ILM Cover (Dan B / Tom Pearson)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| ILM cover marking, labels, colors | All markings & colors must align with the LGA Socket ILM BP Consistency Marking Guide, SPEED DOC# G14577 (current owner = Sathya Ganesan). See image below for cover mark example, including caution text in both English & Chinese. Marked with proper orientation, vendor and date/lot code information similar to legacy ILM Covers | LGA Socket ILM Cover – Design Rqmts (Rev 1.6) |  |  |  |
| Material | Lowest cost, ESD [LESS THAN (+/-) 50V/IN] safe (measured by ESD champion), Material recycle identification per ISO 11469, Finish MT-11020 (Top surface only), Meet Halogen Free/RoHS rqmts Material Flammability Rating will be V0 for >1 processor system markets or V2  for single processor system markets Surface Finish is to be specified the same as LGA775/LGA771 | LGA Socket ILM Cover – Design Rqmts (Rev 1.6) |  |  |  |
| Install and Removal Features | Comes pre-Assembled to the ILM load plate Remains engaged to the ILM load plate while load plate is opened or closed and latched, unless a Processor is installed. Can be installed while the ILM is open or closed Flip off feature design is similar to LGA775/LGA771 ILM Cover will “pop off” if a Processor is installed. ILM Cover will not be compatible with the PnP Cover (to ensure the PnP Cover is removed in PCBA factory). Latching points on outside of ILM frame. If not possible, need larger size cover that can’t drop into the ILM opening hole. Latch point locations on the ILM will be coined to prevent plastic from being shaved off Will not change the original designed angle of the load plate, when open, with the ILM cover attached Will not pop off or interfere with the Torx screwdriver, when the ILM is being screwed down to the motherboard | LGA Socket ILM Cover – Design Rqmts (Rev 1.6) |  |  |  |
| Ergo | Similar ergonomic force to remove the ILM Cover snap (legacy force rqmt from LGA775/LGA771) of 1.7 lbs / 0.77kgf of force MAX Meets Intel ergonomic requirements for assembly / disassembly Operator may wear gloves (must accommodate glove / no glove operation) | LGA Socket ILM Cover – Design Rqmts (Rev 1.6) |  |  |  |
| Unpopulated socket requirements | Must not protrude 6.35mm (0.25 inch) above the height of the load plate in order to be compatible with ‘dummy’ heatsinks in un-populated sockets (>1 processor system consideration) | LGA Socket ILM Cover – Design Rqmts (Rev 1.6) |  |  |  |
| Supplier Compatibility | ILM Cover must be interchangeable between suppliers within the same socket family (e.g. Tyco cover on Foxconn ILM) | LGA Socket ILM Cover – Design Rqmts (Rev 1.6) |  |  |  |
| Durability | Cycle requirement = 20 (1 cycle = assemble + disassemble) No visible debris will come off during ILM Cover install or removal Will not dislodge during shipping & handling, including packaged level drop testing (which can subject the cover to >150g acceleration) Pass unpackaged Shock and Vibration test, Temp/humidity test (85°C, 85% RH, 168hrs) and Bake test (100°C, 48 hrs) | LGA Socket ILM Cover – Design Rqmts (Rev 1.6) |  |  |  |

#### Example ILM Cover markings. See SPEED DOC# G14577 for latest marking requirements

#### Intel-enabled Heatsink & Retention (Dan G)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Chassis / board configurations | Heatsink mounting hole pattern should match prior generation (75mm) |  |  |  |  |
| Weight (Mass) | Must not exceed 5oog(includes retention) |  |  |  |  |
| Pedestal options | Flat bottom heatsink required (no pedestal) |  |  |  |  |
| Chassis Attach | Heatsink retention does not require direct chassis attach |  |  |  |  |
| Fasteners | No sequencing of fasteners required for reliability or performance of the processor stack Heatsink fasteners must be toolless |  |  |  |  |
| Compatibility |  |  |  |  |  |
| Assembly Cycles | Heatsink fastener cycle requirement = 6 cycles (1 cycle = assemble and disassemble) |  |  |  |  |

### Chipsets

#### PCH (Dan G / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Board KOZ | Placement & Rework Rqmt Driven (DAN B TO CHECK DFM) | Intel DFM |  |  |  |
| Component Pick Up KOZ | Unknown if can go smaller than 7x7 mm component pick up zone.         (FYI: For 7x7mm, would use universal nozzle size of 0.234” or 5.9436mm nozzle size, which considers a 0.5mm on each side for tolerance) | Universal PnP Vendor |  |  |  |
| Component Pitch | Minimum package pitch, for machine placement capability, is currently 0.3mm with proper configuration.  This will be verified in Q4 with Intel TVs for FCMB6. | PnP Rep (Todd Harris) |  |  |  |
| Marking, Labels, Colors | Mark per Intel spec (Spec #?) Human readable Visual marking able to withstand three SMT reflows  Contact customer team if introducing new colors or marks |  |  |  |  |
| Board Attach | Minimum BGA solder ball diameter is a function of Field of View.  It is different for each camera and each vendor.  Low risk size for desktop would be 12mils.  Lower is possible but proper equipment configuration needs to be verified at all ODMs. | Legacy |  |  |  |
| Heatsink and retention attach | Must contain design feature preventing damage to the die during installation. Must contain design features preventing excessive load onto the die (e.g. Z-stop) Provide sufficient pressure to maintain TIM BLT and activation |  |  |  |  |
| Max Heatsink Mass |  |  |  |  |  |
| Board Flexure Initiative | Higher or equivalent to previous platform, BFI limits : ≥500ue (on 40 and 62 mil thick PCBs) | Legacy (Cougar Point / Panther Point / Lynx Point) |  |  |  |
| Dynamic Strain | Published shock / strain limits are needed. | Legacy |  |  |  |
| Warpage | BGA products meet the JEDEC High Temperature Flatness Requirement (SPP-024)                                       FYI: The PnP machine has a camera focal length >1mm, which is much greater than package coplanarity, so required flatness to enable SMT placement is a low risk. | BGA Flatness Spec SPP-024 |  |  |  |

### Other (LAN Component)

#### LAN  (Dan B)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Pitch | Minimum QFN pitch 0.4mm | Legacy / Customer Feedback |  |  |  |
|  |  |  |  |  |  |

## Manufacturing and Serviceability Requirements

### Board Assembly

#### SMT (Dan B / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Beat Rate | SMT: ≥ 100 cm / min belt speed | Legacy |  |  |  |
| Yield (eTest, AXI) | SMT: ≥ 98% (T=0) | Survey of the 5 largest DT ODMs Q4 2010 (Foxconn, Gigabyte, ECS, MSI, Pegatron) |  |  |  |
| Paste / Stencil Stencil Pastes | Typical stencil thickness = 5mil Halogen Pastes used at HVM DT ODMs:  Shenmao (PF606) – Highest Usage KESTER (909HPS & EM907) Senju (M705) YunNan Tin (YW9-3005-98CY04) Union Soltek (ULF-308-98)  Low Halogen Pastes used at HVM DT ODMs: Shenmao PF606-P26 Alpha(Cookson) OM338PT  Kester EM923 & NXG1-HF YunNan Tin (YW9-3005-98CY04) Contact customer team if introducing new pastes or stencils | Survey of the 5 largest DT ODMs Q4 2010 (Foxconn, Gigabyte, ECS, MSI, Pegatron) |  |  |  |
| PnP capability Pitch / Size PoP Ball recognition | Min passives 0201 Min BGA pitch 0.5mm, xx by yy (Dan B asked Todd Harris) Ball recognition not mandated but customers prefer high % ball inspection. If needed, software upgrades may be needed.  Accurate placement which supports industry standard capability with HVM beat rate | Legacy |  |  |  |
| Reflow Peak Temp N2 usage Warpage management ∆T Oven capability | Reference reflow process for both air and N2 (02<3000 PPM).  N2 must not be required due to the already low customer profit margins in this segment. SJ Peak Temp: 235 °C to 250 °C (Socket, BGA and LAN) Meet requirements with 12 zone oven ∆T across the Socket ≤ 10˚ ∆T across the Mother Board ≤ 12˚ | Legacy |  |  |  |
|  |  |  |  |  |  |

#### SMT Rework (Dan B / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| PnP retention | No Kapton tape required | Legacy |  |  |  |
| Yield | Socket and BGA: 90% confidence with a possibility of a ~15% defect rate based on a Zero defect sample size | Legacy |  |  |  |
| Adjacent passives (including in cavity) | Process definition must include either method to prevent damage to adjacent passives or replace process | Legacy |  |  |  |
| Component Pitch Limitation | MSI is facing rework difficulty when BGA reach 0.5mm pitch. MSI suggest to me that BGA pitch don’t smaller than 0.5mm pitch unless we have a very good rework process (Dan asked SA Moy for more details here -> exactly what part of the rework process is causing trouble?) | MSI Customer Request |  |  |  |
| Paste or flux print | 0.7 mm pitch Vision accy. ±30 μm Flux applied to Pads on board Paste printed on balls | Legacy |  |  |  |
| TAL | BGA: 60 – 120 sec Socket: 60 – 180 sec | Legacy |  |  |  |
| Peak temp | BGA: 230-245 ˚C Socket: 230-250 ˚C | Legacy |  |  |  |
| Reflow | Air and N2 compatible process.  N2 not required. | DT Customer Survey |  |  |  |
| Glue/ Underfill  removal success rate | Not needed (desktop) |  |  |  |  |

#### Adhesives (Dan B)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Purpose | Adhesives must not be required for Desktop components, due to the already low customer profit margins in this segment |  |  |  |  |
| Materials | N/A |  |  |  |  |
| Material selection criteria (I.E storable, pot life, cost, availability, env friendly) | N/A |  |  |  |  |
| Rework | N/A |  |  |  |  |
| Geometry / Dispense pattern | N/A |  |  |  |  |
| Where applied (where in process flow) | N/A |  |  |  |  |
| Equipment limitations | N/A |  |  |  |  |

### System Assembly

#### HVM System Assembly (Tom Pearson)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Beat rate (TPT) | ILM assembly ≤ 15 sec CPU insertion ≤ 6 sec  (desktop specific) Open ILM Insert processor Close ILM Heatsink assembly ≤ 30 sec | Socket Health WG |  |  |  |
| Socket stack damage (includes bent contacts, skiving, foreign material, etc.) | ≤500 DPM at 90% CI for board assembly and system integration consistent | Socket Health WG |  |  |  |
| ILM Loading Tool (type, DPM, cost, beat rate) | Preference is no tool. However, screws / torques may be acceptable using industry standard tools (T20 Torx* bit) Tools should not be “Intel Specific” Tools / torque drivers may be used in heatsink assembly. | Desktop PTR |  |  |  |
| Processor Insertion Tool | HVM Priority is tool less operation, but if a tool is required:  All markings & colors must align with the LGA Socket ILM BP Consistency Marking Guide, SPEED DOC# G14577 (owner = Sathya Ganesan). Factory tool + stage cost ≤ $10 ESD [LESS THAN (+/-) 50V/IN] safe Ergonomically-friendly Life Goal >300,000 cycles before tool stops working, with ≤ 60 mis-picks Pick Processor directly from Tray Has an accidental Processor Drop Feature Tool handle size Ø50 mm Stage configurable to accommodate multiple socket generations Stage footprint target is to be no larger than 100 mm x 100 mm  Tool drop durability – 12” and 1 meter Max force before took break MIN 25 lbs Tool must be able to pick processor directly from the tray (System Factory Rqmt). | Socket Health WG |  |  |  |
| PnP Cap Removal Tool | HVM Priority is tool less operation , but if a tool is required: All markings & colors must align with the LGA Socket ILM BP Consistency Marking Guide, SPEED DOC# G14577 (owner = Sathya Ganesan). PnP Cap tools cost ≤ $10 ESD [LESS THAN (+/-) 50V/IN] safe Ergonomically-friendly Life Goal >300,000 cycles before tool stops working Tool drop durability – 12” and 1 meter | Socket Health WG |  |  |  |

#### Field Serviceability / Upgrade / Rework (Dan G / Tom Pearson)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
|  | SEE ALSO SYSTEM ASSEMBLY SECTION IN THIS DOCUMENT FOR ADDITIONAL REQUIREMENTS |  |  |  |  |
| Typical Environments (i.e. lighting, work surface, etc. ) | Process must be viable in a wide range of environments – range from desktops to tables |  |  |  |  |
| ILM Loading Tool (type, DPM, cost, beat rate) | Field environment has wide range of users. Preference is no tool. However, screws / torques may be acceptable using industry standard tools Tools should not be “Intel Specific” Tools / torque drivers may be used in heatsink assembly. | Socket Health WG |  |  |  |
| Package Insertion Tool | HVM Priority is tool less operation , but if a tool is required: All markings & colors must align with the LGA Socket ILM BP Consistency Marking Guide, SPEED DOC# G14577 (owner = Sathya Ganesan). Field serviceability has a requirement for tool-less solution. ESD [LESS THAN (+/-) 50V/IN] safe Ergonomically-friendly Life goal ~10 cycles, before tool stops working Not required for tool to pick processor directly from the tray (processor placed manually into the tool) Tool is able to place and remove a processor from the socket Has an accidental Processor Drop Feature FIELD tool cost ≤ $1 Tool step time: 30-60 seconds | Socket Health WG |  |  |  |

#### Ergo (Dan B / Tom Pearson)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Ergo Features | Edge features that interface with operator’s skin should be rounded to prevent operator discomfort in HVM. | Legacy |  |  |  |
| Ergo Forces | Force / pressure: equal to or better than previous sockets, Maximum nominal force <5lbf 1.4 lbf MAX removal force for PnP Cover removal (assumes the use of PnP cap removal tool) 1.7 lbs MAX removal force for ILM Cover removal (Skt T legacy rqmt) The maximum actuation torque of new socket up to 5 cycles shall not exceed 3.5 in-lbs.  For sockets that have been actuated more than 5 cycles, the maximum allowable actuation torque is 5 in-lbs. | Socket Health WG / Legacy |  |  |  |
| Repetitive Cycles | ILM and PnP cap: No serious pain or discomfort reported after 200 consecutive cycles (~100 minutes) simulated HVM work with 3 operators (200 cycles each) | Legacy |  |  |  |

### Test and Provisioning Requirements

#### Customer Test (Dan B / Bill Van Dick)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Coverage (assembly manufacturing defects) | Component Test (coverage of pins/contacts and I/O signals)  ≥ 85% ICT/MDA SKT and BGA CPU ≥ 90% PCH Note: coverage strategy may include using Hotham or combo of test methods including ICT/ATE | Legacy / 2009 Hotham visits |  |  |  |
| Silicon Design for Test Technologies used in board/system manufacturing | IEEE 1149 boundary scan IBIST (interconnect built-in self test) Run time tools (test CPU w/o OS) | Hotham / Test mtgs (IBM, etal) |  |  |  |
| Processor installation for automated test volumetric | ILM lid able to open ≥ 90 angle | Legacy |  |  |  |
| Golden Unit Durability | Capability up to50K cycles (maybe able to leverage existing customer data) | Foxconn Wuhan |  |  |  |

#### Customer Provisioning (Dan B / Zhong Cao or George Arrigotti)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Configuration/ Provisioning Location | Not at ICT only:  Need options for offline or FT programming | CPI Team |  |  |  |
| Test Time | CPI test no more than 10% of total FT time | CPI Team |  |  |  |
| Reboots / Host Resets | No more than one, unless changing configuration or updating ME FW (then two OK) | CPI Team |  |  |  |
| CMOS Reset | Not required for provisioning or test on main line (OK at debug) | CPI Team |  |  |  |
| CPI Rework (reprogram) | No scrap due to CPI Must have way to rewrite flash at any time (factory, field) without de-soldering | CPI Team |  |  |  |
| Test Tool Coverage | Detect data corruption Cover 90% of CPI features Checks for common customer errors, e.g. MEManuf -EOL | CPI Team |  |  |  |
| Test Tool Stability (false failures) | No more than 5,000 DPM | CPI Team |  |  |  |
| Test Tool Impact | Test tools don’t cause data corruption on good platforms | CPI Team |  |  |  |
| Test Tool Backward Compatibility | Latest tools work on earlier PV FW releases (in same generation) | CPI Team |  |  |  |
| Test Tool Commonality | Similar tools across market segments (FITC, FPT, FWUpdate, MEManuf, MEInfo, UpdParam) | CPI Team |  |  |  |

#### Inspection Tools and Other Metrologies (Dan B / Chonglun Fan)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Tool / requirement | None identified. |  |  |  |  |

## General Requirements

### PCB Technology (Dan G / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Pad Design | CPTD design guide must provide documentation to support: Minimized pad size mix (oblong, round) Minimized multidirectional oblong pads Pad definition for all components: metal define pad vs solder mask defined pad  Via in pad: | PCB TD Team |  |  |  |
| Thickness / layer count by segment | Desktop nominal thickness 62mils | Legacy |  |  |  |
| Glass transition temperature (Tg) | Must be capable on Mid Tg | Legacy |  |  |  |
| Dielectrics | Must be capable on FR4 and HFR-Free | Legacy |  |  |  |
| Surface Finish | Must be capable on a variety of finishes – ImAg, OSP and Lead Free HASL | Legacy |  |  |  |
| PTH Mechanical Drill Pad Stack | Not collected yet (default documented in CPTD design guides) (Ask Juan?) |  |  |  |  |
| Pad size tolerance | Industry spec JEDEC or IPC 20%? (Ask Juan) | Legacy |  |  |  |
| Other material properties CTE Modulus Strength | Not collected yet (some data available for HF team) (Ask Gary Long)? What are the real drivers – and can we specify the customer board property ranges of HVM boards? (Ask Gary Long)? | Legacy |  |  |  |

### SJR / Reliability (Dan G)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Shock Strain | Shock strain values required for PCH | Legacy |  |  |  |
| Metrology or Reliability requirement changes | No Changes |  |  |  |  |
| New segmentation or use conditions | Adaptive AIO | Marketing |  |  |  |

### Board Flexure (Dan B / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Board Flexure Initiative | Transient Bent ue Requirements: Socket BFI (Higher than or equivalent to previous socket limits): ≥600 ue for 62 mil thick PCB  BGA Higher or equivalent to previous platform, BFI limits : ≥500ue (on 40 and 62 mil thick PCBs) Unknown if capable at lower number  Contact customer team if lower number is required | Legacy |  |  |  |

### Traceability (Dan B / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Unit Level Traceability (ULT) | Maintain unique id for each device for all Intel products | Corporate Traceability Policy |  | Quality Inconvenience | PFIM (Raja) |
| ULT Deliver Mechanism  2D Mark (current) | Comply to common industry 2D mark standard Equivalent readability to prior generation and meet MAS document expectation Transparent roadmap and change control system Equivalent “acceptable fallout” to previous generation | MAS document, LM spec |  | Quality Inconvenience | PFIM (Raja) |
| Alternative ULT deliver mechanism Example: RFID | Cost equivalent to 2D Mark Obtain X% industry acceptance Consistent scheme in regards to delivery mechanism | CQE |  | Quality Inconvenience | PFIM (Raja) |
| ULT Content | Ensure uniqueness for each and every Intel device for X years (Kevin Fong?) Consistent scheme for all Intel products Consistent scheme regardless of delivery mechanism | Corporate Traceability Policy |  | Quality Inconvenience | PFIM (Raja) |
| Data Retention | Ensure data availability at unit level consistent with either corporate traceability spec and / or any specific customer agreement | Corporate Traceability Policy and CQN customer agreement |  | Quality Inconvenience | PFIM (Raja) |

### EOS / ESD  (Dan B / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| ESD CDM | Customers capable ESD CDM 250kV (per 2010 JEP157 or Industry Council White Paper 2) | ESD Industry Council |  | Lines down | PFIM (Raja) |
| ESD HBM | Customers capable ESD HBM 1kV (per 2009 JEP155 or Industry Council White Paper 1) | ESD Industry Council |  | Lines down | PFIM (Raja) |
| Handling, Packing and shipping media | ESD sensitive materials required | ESD team |  | Manufacturing Costs | PFIM (Raja) |
| Connectors, cables | ESD sensitive materials required | ESD team |  | Manufacturing Costs | PFIM (Raja) |

### Shipping and Handling Media (Dan B / Jose Gomez)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Requirements for trays and tape and reel | Must be compatible to customer manufacturing environment. Must not allow parts to be damaged during handling / shipment. |  |  |  |  |
| Incoming inspection | Not collected |  |  |  |  |
| New requirements for box and/or media marking | Not collected |  |  |  |  |
| Handling or special requirements for partial boxes or shipments | Not collected |  |  |  |  |
| Manufacturability - Intel ATM, ODMs, OEMs (Trays, Tape & Reel) | Product protection.  No mechanical or electrical (EOS) product damage.  E.g. substrate damage and solder sphere damage.  Trays / T&R compatible with ODM / OEM processing (e.g. PnP)  Preferred:  Compliant to JEDEC Publ 95 (Design Guide for generic S&H matrix trays | CPLG |  |  |  |
| Product protection - Outer shipping box for trays and T&R. | Outer shipping box must provide adequate protection for normal shipping and handling during product shipment. (Shock and Vibr requirements listed in Blue Book) Moisture protection | CPLG: |  |  |  |
| Material Content - All shipping media (e.g. Corr cardboard, cushions, MBB, HICs, pallets) | Compliant to all regulatory requirements for substance restriction.  E.g. RoHS and REACH (Contact Intel CPRS with questions)  Must comply with Intel EPC spec 18-1201 | Corp Prod Regs and Stds |  |  |  |
| Design for the Environment | Shipping media design must consider Design for the Environment Materials must be recyclable | EHS |  |  |  |

### Environmental and Safety (Dan G / Bill Vander Weyst)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| EU RoHS | Continue to comply with 6 banned materials Ensure no materials utilizing exemptions are in use beyond the specified expiration dates | Legal requirement |  |  |  |
| JEP-709 (Solid State Devices) IPC-4101C (PCB only) | All new component products must meet the low halogen (halogen free) requirements outlined in JEDEC guideline New cards (Wireless and NICs) must meet both the IPC and JEDEC requirements for finished assembly | Customer / Marketing Requirement |  |  |  |
| REACH | All products must declare whether they contain any of the most up to date list of SVHCs (Substances of Very High Concern) >1000ppm | Legal Requirement |  |  |  |
| Recycling | All plastic materials within the sockets when tested by volume per BS EN 14582 for halogen should meet: 900ppm maximum Cl, 900ppm maximum Br, and 1500ppm maximum total halogens Cadmium should not be used in the painting or plating of the socket. CFCs and HFCs shall not be used in manufacturing the socket. It is recommended that any plastic component exceeding 25g must be recyclable as per the European Blue Angel recycling design guidelines |  |  |  |  |
| Safety | Design, including materials, shall be consistent with the manufacture of units that meet the following safety standards: UL 60950 most current edition and amendments CAN/CSA-C22.2 – 60950 most current edition and amendments EN 60950 most current edition and amendments IEC 60950 most current edition and amendments |  |  |  |  |

### Supplier Management (Dan B)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Supplier Collateral | Supplier to provide collaterals to customers that demonstrate the heat sink solution capability and compatibility with Intel processor as indicated in the components design guides, i.e. Datasheet, mechanical model, thermal model, electrical model, independent test house test report, samples, etc. |  |  |  |  |
| Enabling Timeline | Suppliers will provide enabled solution within Intel’s thermal/mechanical Product Life Cycle schedule |  |  |  |  |
| Supplier capacity | Capable of supporting customization, LVM, HVM, and QA requirements of targeted customers. |  |  |  |  |
| Geography to support | Able to support and distribute locally to APAC, IJKK, N America, EMEA |  |  |  |  |
| Manufacturing support | Suppliers will provide handling and manufacturing app notes to customers. |  |  |  |  |
| Supplier and Subcontractors | Existing suppliers and sub cons will facilitate transition from old to new components. |  |  |  |  |
| Number of Supplier per component | Number of enabled suppliers required to support the program is 2. |  |  |  |  |

### Engineering Sample (Dan G)

| Attribute | Requirement | Source (Name) | Engineering Response (“OK” or “Action”) | Describe Action | Action Plan Forum (Target Date) |
| --- | --- | --- | --- | --- | --- |
| Thermal / Mechanical Test Vehicle (TMTV) | Powered through bottom side pads  Bottom side sense pads required  Include imprinted gage (Pat Johnson?) Include Daisy Chain BKM |  |  |  |  |
| Functional samples | Must include 2D mark | CQN |  |  |  |
| Thermal Test Vehicle (Processor) | Power at TDP not to exceed safety…Chuck Power and sense through bottom pads |  |  |  |  |
| Daisy Chain TV (Processor) | May be combined with TTV Follow BKM for corner tracking Shah |  |  |  |  |

## Appendix

### CRD Timing

CRD is intended to be available throughout the platform development cycle. The key revisions will occur in pathfinding to provide the maximum solution time for meeting customer requirements.

Rev 0.1 is targeted at or before ATTD PMT checkpoint -300

Rev 0.5 is targeted at or before ATTD PMT checkpoint -200 (Architecture Plan)

Rev 1.0 is targeted at or before ATTD PMT checkpoint -100 (TTS)

See below for alignment between PPLC and PMT.

### Customer Requirements Process

Customer selection:

ODM: The objective of the engagement is to cover 80% of the market segment by unit volume.

OEM:  SMG and BU have well defined tier 1 customer list

STRATEGIC and EMERGING: Customers with strategic value will likewise be engaged.

NOTE: The Customer Requirements Document will contain a prioritized set of Requirements targeted at known technology direction. It is not all inclusive and is a subset of other customer information. Sources of this information include:

| Focused Technology  Feedback | Customer Technology Outlook  Customer Evaluations, FMEA, DOE |
| --- | --- |
| MV Collaboration Customer Data | PTR sharepoint |
| Previous /Current Platform Knowledge | Ramp data  PF  and MV Bluebooks  Post Mortem |
| Equipment and Supplier Capability | PCB Roadmaps Equipment Database |
| Customer issues (TD misses) | CQN Trackers |
| ODM process, equipment | CQE |
| System Assembly process tools | Under Development (MVE) |
|  |  |

Customer impact:

The Impact column is intended to assist Intel negotiations when technology or design constraints are encountered.

CRD owners will identify impact per list below:

Liability / Biz Impact: Serious Customer Business Impact (Prevents Customer Sales)

Customer Returns / Reliability: Results in Customer Returns

Lines down/Capability Upgrade needed: Limits Customer Ability to Sell in Segment

Manufacturing Costs / Capacity: DPM / Yield / Beat rate impacts

Quality Inconvenience: Results in Special Handling or Screens

### Other related customer documents

| Document | Generator / Owner | Distribution Method | Customer’s Primary Target Audience |
| --- | --- | --- | --- |
| MAS | MVE and CQ&R | ILN and CQE Direct | Mfg Engineering, Test Engineering and PCB Layout |
| EMTS and EDS | TME | IBL and FAE Direct | Design Engineering and PCB Layout |
| Platform Design Guide | Division | IBL and FAE Direct | Design Engineering, Test Engineering, and PCB Layout |
| Daisy Chain User Guide | ATTD | IBL and CQE Direct | Mfg Engineering and PCB Layout |
| Thermal Mechanical Design Guide | MPAD, CTME, BCG (Division) | FAE / IBL | Design Engineering and PCB Layout |
| Socket Validation Reports | ATTD | FAE / IBL | Reliability Engineering |
