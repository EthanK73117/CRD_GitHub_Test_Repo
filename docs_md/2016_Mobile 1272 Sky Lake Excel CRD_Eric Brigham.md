---
source_file: "2016_Mobile 1272 Sky Lake Excel CRD_Eric Brigham.XLSX"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (Mobile)/2015 Sky Lake/2016_Mobile 1272 Sky Lake Excel CRD_Eric Brigham.XLSX"
file_type: "xlsx"
size_bytes: 47552
content_hash: "652415353e9a"
converted_at: "2026-10-08T11:29:43"
---

# 2016_Mobile 1272 Sky Lake Excel CRD_Eric Brigham

## Sheet: Sheet1

|  | 1272 Tock Mobile Sky Lake |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Customer Requirements Rev 0.5 |  |  |  |  |  |  |
|  | Eric Brigham |  |  |  |  | Date |  |
|  | Overview |  |  |  |  |  |  |
|  | Teams that will benefit from this documents are Technology Competency Teams (TCTs), Pathfinding Integration Teams (PFIMs), Design Integration, Platform Engineering (PEBs), Enabling Component Teams, and Socket Engineering. The CRD document will support inputs into Intel development design documents such as TMDG, TTS and Socket Requirements and provide direction for reference solution development.   It is conceivable for customer requirements to evolve or have needs outside of this document. In such cases, engineering support may be requested on a case by case basis to aid in addressing customers’ challenges. |  |  |  |  |  |  |
|  | Scope |  |  |  |  |  |  |
|  | This document concerns requirements for enabling components from customers either explicitly (i.e. requests coming directly from Intel’s customers) or implicitly (i.e. requirements that are based on industry capability such as SMT or reflow requirements).  Both types of requirements are included.  Other important distinctions are as follows.   In Scope: Mechanical, thermal, and manufacturing related ingredients for the design and manufacture of products which are sold by Intel’s customers. This includes products manufactured by Intel and Enabled Components as defined below. An Enabled component is a component not sold by Intel and is necessary for the proper function of the platform.  Enabled components are categorized into the following groups. • Power delivery (e.g. VR heatsinks, Voltage Regulator Test Tool)    • Thermal solution (processor and power delivery and includes TIM2)  • Socket  • Retention (e.g., back plate, spring, standoffs, etc.)  • Tools, jigs, fixtures, etc. required for assembly / disassembly, measurements  Out of scope:  • Requirements for debug and probing tools  • Requirements for Test tools (thermal test tools, etc.) |  |  |  |  |  |  |
|  | Key Deployment Forums |  |  |  |  |  |  |
|  | • ATTD Deployment and Action Planning will be managed by CPE.  • Divisional deployment will be managed by Division TME Customer teams. |  |  |  |  |  |  |
|  | CRD Revision Timing |  |  |  |  |  |  |
|  | CRD is intended to be available throughout the platform development cycle. The key revisions will occur in pathfinding to provide the maximum solution time for meeting customer requirements. • Rev 0.1 is targeted at ATTD and Division Concept Pathfinding Activity  • Rev 0.5 is targeted at  ATTD Methodology 2.0 Pathfinding / Definition phase completion  • Rev 1.0 is targeted at ATTD Methodology 2.0 Technology Selection phase completion and closure of Divisional POP activity  All revisions will be stored on CPTD MOSS site. (Contact authors or segment PTR lead to obtain link) |  |  |  |  |  |  |
|  | Platform Summary |  |  |  |  |  |  |
|  | Description |  |  |  |  |  |  |
|  | Parameter | Definition |  |  |  |  |  |
|  | Market Segment | Client; enthusiast thru ULV |  |  |  |  |  |
|  | Socket | none |  |  |  |  |  |
|  | Lead processor product | Sky Lake |  |  |  |  |  |
|  | Socket Compatible Processors | na |  |  |  |  |  |
|  | Processor Silicon Technologies | P1272, P1274 |  |  |  |  |  |
|  | Chipset / Package Technology | Sunrise Point PCH / FCBGA9.e2 P1265 |  |  |  |  |  |
|  | Memory Buffer / Package Technology |  |  |  |  |  |  |
|  | Other |  |  |  |  |  |  |
|  | Key Dates |  |  |  |  |  |  |
|  |  | Platform Checkpoint | Date | Owner |  |  |  |
|  |  | Rev -300 POC | Q1 2011 | ATTD |  |  |  |
|  |  | POP1 |  |  |  |  |  |
|  |  | Pathfinding / Definition |  |  |  |  |  |
|  |  | POP2 |  |  |  |  |  |
|  |  | Technology Selection |  |  |  |  |  |
|  |  | POP3 |  |  |  |  |  |
|  |  | ES1 | W36'14 | ATTD |  |  |  |
|  |  | LEC |  |  |  |  |  |
|  |  | PRQ | W10'15 | ATTD |  |  |  |
|  | Customer Focus Areas |  |  |  |  |  |  |
|  | SKL ULX BGA Processor | Smaller pkg size (20x16.5mm), 0.4mm ball pitch, CUF + mold, full array (no collapse limiters), Cu-OSP surface finish, SAC1205Ni, coreless |  |  |  |  |  |
|  | SKL ULT BGA Processor | New form factor (42x24mm), 0.65mm ball pitch, CUF + Mold, 3 die configuration |  |  |  |  |  |
|  | Sunrise Point PCH | BoP (6x10 oval pads in the periphery), 23x23mm package, 0.5mm ball pitch |  |  |  |  |  |
|  | SKL 4+4e Halo BGA Processor | 42x28 pkg size, 0.65mm pitch, thinner core, CUF+mold, expected warpage above 250um limit |  |  |  |  |  |
|  | Design Requirements |  |  |  |  |  |  |
|  | System OVERVIEW |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | System Form Factor | N/A |  |  | Verify capabilites |  |  |
|  | System Thermal | N/A |  |  | Verify capabilites |  |  |
|  | Other Key System Information | N/A |  |  | Verify capabilites |  |  |
|  | Processors |  |  |  |  |  |  |
|  | Processor (Socket attach) |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Processor Marking, Labels, Colors | •  Pin 1 – must be marked and depopulated  •  2D Matrix – Comply with 2D mark industry standard and readable by MAS documented scanners.    •  Labels – per Mark Intel spec  •  Colors – none specified.   •  Visual marking able to withstand three SMT reflows   •  Cosmetic damage to comply with industry spec | Legacy | OK |  |  |  |
|  | Processor Installation Features | Insertion tool required to minimize bend pin occurance | Legacy | OK |  |  |  |
|  | Processor IHS Requirement | Thin HIS to minimize z-height impacts | Legacy | OK |  |  |  |
|  | Processor Form Factor Compatibility | N/A |  |  |  |  |  |
|  | Processor (ULT and Halo BGA) |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Max x-y-z of Stack including KOZ | •  No requirements | Legacy |  |  |  |  |
|  | Processor Marking, Labels, Colors | •  Pin 1 – must be marked and depopulated  •  2D Matrix – Comply with 2D mark industry standard and readable by MAS documented scanners.    •  Labels – per Mark Intel spec  •  Colors – none specified.   •  Visual marking able to withstand three SMT reflows   •  Cosmetic damage to comply with industry spec | Legacy |  |  |  |  |
|  | Board Attach | •  Need to stay within type 3 PCB design rules while meeting SMT yield requirements of 99.8%  •  Materials must meet ROHS and EHS regulations   •  Solution shall not preclude use of a third-party back-plate  •  Shall not require the use of adhesives for reliability or manufacturability  •  Need appropriate number of nCTFs to provide adequate reliability margins  •  SMT capability with standard industry available materials and equipment sets  •  One SMT process for all SKUs of ULT BGA required | 2013 Industry Survey |  |  |  |  |
|  | Die Flatness Requirements | •  Flatness equivalent to current product to enable industry heat sink attach.  •  Surface area must allow for PnP suction lift.  •  TIM material must withstand 2nd level solder reflow.  •  Must meet minimum pressure requirements of the TIM2 material | Legacy |  |  |  |  |
|  | Form Factors | •  Land side discrete component height shall not contact the motherboard to the point of impeding the solder joint formation | Legacy |  |  |  |  |
|  | Dynamic Strain | •  Published shock / strain limits are needed.   •  Generation to generation parity (ISO-G) | Legacy |  |  |  |  |
|  | Warpage | •  Must meet current proven SMT capability (250um pkg warpage) | 2013 Industry Survey |  |  |  |  |
|  | Processor (ULX BGA) |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Max x-y-z of Stack including KOZ | •  No requirements | Legacy |  |  |  |  |
|  | Processor Marking, Labels, Colors | •  Pin 1 – must be marked and depopulated  •  2D Matrix – Comply with 2D mark industry standard and readable by MAS documented scanners.    •  Labels – per Mark Intel spec  •  Colors – none specified.   •  Visual marking able to withstand three SMT reflows   •  Cosmetic damage to comply with industry spec | Legacy |  |  |  |  |
|  | Board Attach | •  Need to meet SMT yield requirements of 99.8%  •  Materials must meet ROHS and EHS regulations   •  Solution shall not preclude use of a third-party back-plate  •  Shall not require the use of adhesives for reliability or manufacturability  •  Shall not preclude the use of adhesives  •  Need appropriate number of nCTFs to provide adequate reliability margins  •  SMT capability with standard industry available materials and equipment sets  •  One SMT process for all SKUs of ULX BGA required | Legacy |  |  |  |  |
|  | Die Flatness Requirements | •  Flatness equivalent to current product to enable industry heat sink attach.  •  Surface area must allow for PnP suction lift.  •  TIM material must withstand 2nd level solder reflow.  •  Must minimum pressure requirements of the TIM2 material | Legacy |  |  |  |  |
|  | Form Factors | •  Land side discrete component height shall not contact the motherboard to the point of impeding the solder joint formation | Legacy |  |  |  |  |
|  | Dynamic Strain | •  Published shock / strain limits are needed.   •  Generation to generation parity (ISO-G) | Legacy |  |  |  |  |
|  | Warpage | •  Must meet current proven SMT capability (250um pkg warpage) | Industry Study |  |  |  |  |
|  | Processor Stack |  |  |  |  |  |  |
|  | Sockets - All segments |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Socket Material |  |  |  |  |  |  |
|  | Socket Contacts |  |  |  |  |  |  |
|  | Socket body marking, labels, colors |  |  |  |  |  |  |
|  | Socket to board attach |  |  |  |  |  |  |
|  | Socket: Processor Insertion and Removal Features |  |  |  |  |  |  |
|  | Socket Durability |  |  |  |  |  |  |
|  | Socket Max compressive static load (from Heatsink) |  |  |  |  |  |  |
|  | Socket Shock Dynamic Strain |  |  |  |  |  |  |
|  | Socket Warpage |  |  |  |  |  |  |
|  | Unpopulated socket requirements |  |  |  |  |  |  |
|  | PnP Cover |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | PnP cover marking, labels, colors |  |  |  |  |  |  |
|  | PnP Cover Install and Removal Features |  |  |  |  |  |  |
|  | PnP Cover Manufacturing Compatibility |  |  |  |  |  |  |
|  | PnP Cover: Socket Protection Features |  |  |  |  |  |  |
|  | PnP Cover Durability |  |  |  |  |  |  |
|  | PnP Cover Scalability |  |  |  |  |  |  |
|  | PnP Cover Supplier compatibility |  |  |  |  |  |  |
|  | Backplate |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Backplate marking and colors | Mobile does not require a backplate | Legacy |  |  |  |  |
|  | Backplate X-Y-Z constraints | Mobile does not require a backplate | Legacy |  |  |  |  |
|  | Backplate Attach | Mobile does not require a backplate | Legacy |  |  |  |  |
|  | Backplate Materials and Pre-Conditioning | Mobile does not require a backplate | Legacy |  |  |  |  |
|  | Backplate Insulation | Mobile does not require a backplate | Legacy |  |  |  |  |
|  | Backplate Rework-ability | Mobile does not require a backplate | Legacy |  |  |  |  |
|  | Backplate Deflection | Mobile does not require a backplate | Legacy |  |  |  |  |
|  | Load Mechanism and Actuation |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Load Mechanism Type (ILM, DSL, PHM, etc) |  |  |  |  |  |  |
|  | Load Mechanism Volumetric (KOZ width, height) |  |  |  |  |  |  |
|  | Load Mechanism Marking and Keying |  |  |  |  |  |  |
|  | Load Mechanism Assembly |  |  |  |  |  |  |
|  | Load Mechanism: Heatsink Attach |  |  |  |  |  |  |
|  | Load Mechanism Actuation |  |  |  |  |  |  |
|  | Load Mechanism System Assembly / Compatibility for tools / manual |  |  |  |  |  |  |
|  | Load Mechanism Load |  |  |  |  |  |  |
|  | Load Mechanism Durability |  |  |  |  |  |  |
|  | LM Cover (aka Protective Cover) |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | LM cover marking, labels, colors, materials |  |  |  |  |  |  |
|  | LM cover Install and Removal Features |  |  |  |  |  |  |
|  | SOCKET cover: Socket Protection Features |  |  |  |  |  |  |
|  | SOCKET cover: Unpopulated socket requirements |  |  |  |  |  |  |
|  | SOCKET cover Durability |  |  |  |  |  |  |
|  | SOCKET  cover Scalability |  |  |  |  |  |  |
|  | SOCKET cover Supplier Compatibility |  |  |  |  |  |  |
|  | Intel-enabled Heatsink & Retention |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Heatsink Chassis / configurations | No requirements |  |  |  |  |  |
|  | Heatsink Mass | Less than 50G |  |  |  |  |  |
|  | Heatsink Chassis Attach | Flat Bottom Heat Sink |  |  |  |  |  |
|  | Heatsink TIM | TIM 2 material reference solution developed in PCCG |  |  |  |  |  |
|  | Heatsink Assembly Cycles |  |  |  |  |  |  |
|  | Chipsets |  |  |  |  |  |  |
|  | PCH |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Chipset Volumetric |  |  |  |  |  |  |
|  | Chipset Marking, Labels, Colors | per Mark Intel spec 40-0404  1. Visual marking able to withstand three SMT reflows Contact customer team if introducing new colors or marks | Legacy |  |  |  |  |
|  | Chipset Board Attach | •  Need to stay within type 3 PCB design rules while meeting JEDEC high temp warpage spec and meet SMT yield requirements of 99.5%  •  Materials must meet ROHS and EHS regulations   •  Solution shall not preclude use of a third-party back-plate  •  Shall not require the use of adhesives for reliability or manufacturability  •  Shall not preclude the use of adhesives  •  Need appropriate number of nCTFs to provide adequate reliability margins  •  SMT capability with standard industry available materials and equipment sets | Legacy / Customer BCs |  |  |  |  |
|  | Chipset Heatsink and retention attach | Not specified in Mobile |  |  |  |  |  |
|  | Chipset Max Heatsink Mass | NA - heatsink not required |  |  |  |  |  |
|  | Chipset Performance Metrics | 1. Published shock / strain limits are needed.  2.  Meet Jedec SPP-024 warpage requirements  3. Reliability  Per Intel blue book |  |  |  |  |  |
|  | Other Platform Components |  |  |  |  |  |  |
|  | Title |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | MANUFACTURING AND SERVICEABILITY REQUIREMENTS - SKL |  |  |  |  |  |  |
|  | Board Assembly |  |  |  |  |  |  |
|  | SMT (ULT and Halo BGA) |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) | Impact if not met |
|  | Board Assembly Process compatibility | 1.      Process must be compatible with all components on board | Legacy |  |  |  |  |
|  | Board Assembly Yield (eTest, FA) | 1.      ESTR (ES1 Tech Readiness): 90% at 90% CI 2.      QSTR (QS Tech Readiness): 99% at 90% CI 3.      PRQ SMT: 99.5% at 90% CI (w/in ref process window) | 2013 Customer Survey |  |  |  |  |
|  | Paste Type | •  Shall not require the exclusive use of HF, ZH or Halogenated pastes  •  Shall not require the need for type 5,6 or 7 solder pastes  •  Shall work with previously established solder paste formulations (MAS) - Alpha OM363*, Alpha OM363H*,  Senju M705-GRN360-K2-VZH*, Senju M705-S101HF(N4)-S4*, Shenmao PF606-P*, Shenmao PF606-P26* | 2013 Industry Survey |  |  |  |  |
|  | Paste Print | •  Stencil thickness is 4mil and 5mil (requires the use of common stencil for both 2+2 and 2+3)  •  Stencil aperture design rules to be met: 7mil min air gap required for 5 mil thick stencil and 5.75mil min air gap required for a 4 mil thick stencil  •  Stencil manufacturing: Laser cut with electro-polish   •  Print speed between 70 - 100 mm/s  •  Print pressure between 7 - 9kg (15 - 20lbs) (more investigation needed... either add width or remove).  •  Solder paste volume inspection (SPI) control limits:  -50% to +50% (from design volume or nominal?  can we correlate SPI control limits to print speed). | 2013 Industry Survey | Action | DIWG: determine the difference in warpage between 2+2 and 2+3 CPTD: determine if the difference in warpage requires the need for 2 stencil designs. | PTR |  |
|  | Pick and Place | • 100% ball recognition required  • Max component height of 3mm  • Maximum Placement speed requirement is max setting (highest speed)  • Minimum passives 0201  • Min BGA pitch 0.65mm  • Max pkg size: 45x74 | 2013 Industry Survey |  |  |  |  |
|  | Reflow | •  Peak temp of 230-250 °C  •  TAL: 40-90 sec (N2) 60-90 sec (Air)  •  Soak temp and time: 60-120 sec between 150-180°C (could be paste supplier specific)  •  ∆T: <10°C  • Pallet required with clamp and no clamp (majority do not clamp)  • Belt Speed: 100-120 cm/sec   • Environment: Air and N2 (air worst case) | 2013 Industry Survey |  | Do customer prefer full ramp profile or ramp soak ramp profile? |  |  |
|  | SMT (ULX BGA) |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Board Assembly Process compatibility | 1.      Process must be compatible with all components on board | Legacy |  |  |  |  |
|  | Board Assembly Yield (eTest, AXI) | 1.      ESTR (ES1 Tech Readiness): 90% at 90% CI 2.      QSTR (QS Tech Readiness): 99% at 90% CI 3.      PRQ SMT: 99.5% at 90% CI (w/in ref process window) | 2013 Customer Survey |  |  |  |  |
|  | Paste Type | •  Shall not require the use of HF, ZH or Halogenated pastes  •  Shall not require the need for type 5,6 or 7 solder pastes  •  Shall work with previously established solder paste formulations (MAS) - Alpha OM363*, Alpha OM363H*,  Senju M705-GRN360-K2-VZH*, Senju M705-S101HF(N4)-S4*, Shenmao PF606-P*, Shenmao PF606-P26* | 2013 Industry Survey |  |  |  |  |
|  | Paste Print | •  Stencil thickness is 4mil (stepped acceptable but not required).  3mil thick under consideration but need Q1 PRC intro tour feedback.  •  Stencil aperture design rules to be met: 0.575mil min air gap required for 4 mil thick stencil.  3mil thick stencil air gap requirement TBD.  •  Stencil manufacturing: Laser cut with electro-polish (nano coat under evaluation)  •  Print speed between 70 - 100 mm/s  •  Print pressure between 7 - 9kg (15 - 20lbs)  •  Solder paste inspection (SPI) control limits:  -50% to +50% | 2013 Industry Survey |  |  |  |  |
|  | Pick and Place | • 100% ball recognition required  • Max component height of 3mm  • Maximum Placement speed requirement is max setting (highest speed)  • Minimum passives 0201 BSC minimum spacing requirement is 8mil  • Min BGA pitch 0.4mm  • Max pkg size: 45x74 | 2013 Industry Survey |  |  |  |  |
|  | Reflow | •  Peak temp of 230-250 °C  •  TAL: 40-90 sec (N2) 60-90 sec (Air)  •  Soak temp and time: 60-120 sec between 150-180°C  •  ∆T: <10°C  • Pallet required with clamp and no clamp  • Belt Speed: 100-120 cm/sec   • Environment: Air and N2 | 2013 Industry Survey |  |  |  |  |
|  | SMT REWORK (Halo, ULT, ULX, PCH) |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Rework Yield | • ≥80% | 2013 Industry Survey |  |  |  |  |
|  | Package Rework Reference Process | Customer request for rework process of the SKL PCH (BoP) Customer request for rework process for the BSC required for SKL Y (copy exactly design) | 2013 Intro Tour |  |  |  |  |
|  | SMT Rework flux or solder Paste before BGA package/socket socket placement | •  Flux and / or paste  •  Flux or paste printed on the PCB or BGA (wide variation within industry - No Standard)  Review CME database for customer specific information. | 2013 Industry Survey |  |  |  |  |
|  | SMT Rework Reflow | •  Peak temp of 230-250 °C  •  TAL: 60-120 sec  •  Soak temp and time: 60-120 sec between 150-180°C  •  ∆T: 5-10°C  •  rework pallet: yes  •  Rework speed: 15-20min (remove and replace) | 2013 Industry Survey |  |  |  |  |
|  | Adhesives |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Purpose | Mechanical reliability | 2013 Industry Survey |  |  |  |  |
|  | Materials | Panasonic 480D-1, Loctite 3619, Loctite 3705 | 2013 Industry Survey |  |  |  |  |
|  | Material Selection Requirements | Cost, ability to meet reliability requirements and reworkability | 2013 Industry Survey |  |  |  |  |
|  | Geometry / Dispense Pattern | L-Shaped 3-6 balls deep | 2013 Industry Survey |  |  |  |  |
|  | Rework | Required | 2013 Industry Survey |  |  |  |  |
|  | Where applied (where in process flow) | Pre and post reflow (pre ICT) | 2013 Industry Survey |  |  |  |  |
|  | System Assembly |  |  |  |  |  |  |
|  | HVM System Assembly (including PCBA test) |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | System Assembly beat rate | Not specified |  |  |  |  |  |
|  | System Assembly yield |  |  |  |  |  |  |
|  | System Assembly Tools |  |  |  |  |  |  |
|  | Serviceability / Upgrade / Rework |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Serviceability, Upgrade, Rework - DPM |  |  |  |  |  |  |
|  | Serviceability, Upgrade, Rework - Environments |  |  |  |  |  |  |
|  | Serviceability, Upgrade, Rework Tool - LM Actuations |  |  |  |  |  |  |
|  | Serviceability, Upgrade, Rework Tool - Package Insertion |  |  |  |  |  |  |
|  | Ergo |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Ergo Features - comfort | 1. All hardware must allow a 5th-percentile person (in terms of strength) to insert and remove all connectors and components.  2. Grip points must be comfortable and match the finger or hand grip expected.  3. Edge features that interface with operator's skin should be rounded to prevent operator discomfort in HVM.  4. Insertion, removal and actuation mechanisms must minimize operator discomfort.  5. The release retention mechanism of LM and cable connectors must be visible during service activities that require insertion, removal or activations. | Customer Collaboration 2011 and Intel Ergo Spec |  |  |  |  |
|  | Ergo Finger Access | 1. Internal connectors must provide sufficient finger access for connecting and disconnecting cables and processors so as to accommodate the 95th percentile male. One finger: Minimum 32 mm (1.25 in).    2. Sockets  • Finger Breadth/Width (X): 13mm Rqmt, 18mm Best Case  • Finger Thickness (Y): 4mm Rqmt, 10mm Best Case  • Finger Depth (Z): 5mm Rqmt, 8mm Best Case  3. SHIPPING TRAY Finger Access needed when removed from shipping trays:  • Finger Breadth/Width (X): 13mm Rqmt, 18mm Best Case  • Finger Thickness (Y): 4mm Rqmt, 10mm Best Case  • Finger Depth (Z): 5mm Rqmt, 8mm Best Case  4. IHS features on LGA package for easy finger gripping is needed. Customers have requested a more easily graspable solution (This grippability is needed for removal from trays as well as processor installation and removal processes) 5. LM KOZ must accommodate finger access | Customer Collaboration 2011 and Intel Ergo Spec |  |  |  |  |
|  | Ergo Hand Access | 1. Internal LMs and connectors must provide sufficient hand access to accommodate 95th percentile male.  2. Flat Hand to Wrist clearance needed:  • Height: Minimum 89 mm (3.5 in) Width: Minimum 114 mm (4.5 in)  3. Fist to Wrist clearance needed  • Height: Minimum height 89 mm (3.5 in) Width: Minimum width 127 mm (5.0 in) | Customer Collaboration 2011 and Intel Ergo Spec |  |  |  |  |
|  | Ergo Features – for alignment and keying | 1. When alignment features are utilized in a component that is slid into a socket or connector the key interference must be encountered in the first 25% of the install travel of the component. This is mostly used for large components such as heat sinks that have large installation travel distance  2. When keying is utilized in a component that is slid into a socket or connector the key should be visible to the installer.  3. Guide slots, guide pins, or other similar features must be used on heat sinks or heat sink assemblies with processors/ connectors | Customer Collaboration 2011 and Intel Ergo Spec |  |  |  |  |
|  | Ergo Forces | Maximum nominal force <5lbf  1. LOAD MECHANISM ACTUATION The maximum actuation torque of new socket  shall not exceed 5 in-lbs.  2. PICK AND PLACE COVER insertion and removal force must not exceed 10N (1 kgf or 2.3 lbf).  3. LM COVER 1.7 lbs / 0.77kgf of force MAX . Operator may wear gloves (must accommodate glove / no glove operation) | Customer Collaboration 2011 and Intel Ergo Spec |  |  |  |  |
|  | Ergo Repetitive Cycles | No serious pain or discomfort reported after 200 consecutive cycles (~100 minutes) simulated HVM work with 3 operators (200 cycles each) at both LVM and HVM beat rates | Customer Collaboration 2011 and Intel Ergo Spec |  |  |  |  |
|  | Test and Provisioning Requirements |  |  |  |  |  |  |
|  | Customer Test |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Customer Test – Component insert and removal | NA |  |  |  |  |  |
|  | Golden Unit Durability | NA |  |  |  |  |  |
|  | Customer Test - Coverage for assembly manufacturing defects | 1. Required capability: =80% of nets (equivalent legacy ICT/ATE)…  2. The coverage strategy may include using Hotham or combo of test methods including ICT/ATE | 2009 Hotham visits |  |  |  |  |
|  | Silicon Design features | Required features:  1. # IEEE 1149 boundary scan  2. # IBIST (interconnect built-in self test)  3. # Run time tools (test CPU w/o OS) | Hotham / Test mtgs |  |  |  |  |
|  | Customer Provisioning |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Customer Provisioning Accessibility / Coverage | 1. Configuration/ Provisioning Location Not at ICT only: Need options for offline or FT programming 2. Cover 90% of CPI features  3. Checks for common customer errors, e.g. MEManuf –EOL;  Detect data corruption; Checks for security features | CPI Team |  |  |  |  |
|  | Test Time Impact | 1. CPI test no more than 10% of total FT time 2. No more than one reboot or host resets, unless changing configuration or updating ME FW (then two OK); CMOS resets should Not required for provisioning or test on main line (OK at debug) 3. No more than 5000DPM false CPI fails | CPI Team |  |  |  |  |
|  | CPI Rework (reprogram) | 1. No scrap due to CPI  2. Must have way to rewrite flash at any time (factory, field) without de-soldering 3. Test tools don't cause data corruption on good platforms | CPI Team |  |  |  |  |
|  | Test Tool Backward Compatibility | 1. Latest tools work on earlier PV FW releases (in same generation) 2. Similar tools across market segments (FITC, FPT, FWUpdate, MEManuf, MEInfo, UpdParam) | CPI Team |  |  |  |  |
|  | General Requirements - Skylake |  |  |  |  |  |  |
|  | PCB Technology |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Pad / land design | Minimized land pattern definitions with match to division CRBs 2 mil tolerance | 2013 Land pattern customer feedback |  |  |  |  |
|  | Board Dimensions / Thickness / layer count by segment | •  Board thickness range: 0.7 - 1.4mm  •  Layer count ≥ 8 layers | 2013 Customer Survey |  |  |  |  |
|  | PCB Technology | Type 3 and 4 motherboards (HDI predominatley used in ULX segment - Type 3 in the ULT/Halo segments) |  |  |  |  |  |
|  | Dielectrics | HF Free Motherboard | Legacy |  |  |  |  |
|  | Surface Finish | OSP, Lead Free HASL, ENIG | Legacy |  |  |  |  |
|  | Reliability |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  |  | CUSTOMER REQUIREMENTS ARE FOUND IN 25-0032 USE CONDITION SPEC | GUC Forum |  |  |  |  |
|  | New segmentation or use conditions | Must meet Use Condition Reliability for all segments (listed in this design section of this document). | Legacy |  |  |  |  |
|  | Metrology or Reliability requirement changes |  |  |  |  |  |  |
|  | Board Flexure |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Transient Bend | •  BFi strain guidance at POR gage location should be atleast 400ue for 62 mil  •  BFi strain guidance at POR gage location should be atleast 450ue for 40mil  •  Needs validation for <40 mil thick boards  •  In addtion to POR gage location, BFi strain guidance is also needed at       2 alternate gage locations,( ALT1 and ALT2) as identified in latest rev of BFI MAS  •  All final guidances need to be available atleast 1 quarter prior to PRQ, to be       shared with customers | Legacy | Action | SKL Y and potentially U will utilize board thicknesses down to 28mil.  Need to validate 32mil and 28mil thick boards. |  |  |
|  | Traceability |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Unit Level Traceability (ULT) | 1.      Maintain unique id for each device for all Intel products. Marking per corporate spec 40-0404. | Corporate Traceability Policy |  |  |  |  |
|  | ULT Deliver Mechanism    - 2D Mark (current) | 1. Comply to common industry 2D mark standard  2. Equivalent readability to prior generation and meet MAS document expectation  3. Transparent roadmap and change control system  4. Equivalent "acceptable fallout" to previous generation | MAS document, LM spec |  |  |  |  |
|  | Alternative ULT deliver mechanism | 1. Cost equivalent to 2D Mark  2. Obtain X% industry acceptance  3. Consistent scheme in regards to delivery mechanism | CQE |  |  |  |  |
|  | ULT Content | 1. Consistent scheme for all Intel products  2. Consistent scheme regardless of delivery mechanism  3. Ensure uniqueness for each and every Intel device for 7-10 years | Corporate Traceability Policy |  |  |  |  |
|  | Data Retention | 1.      Ensure data availability at unit level consistent with either corporate traceability spec and / or any specific customer agreement | Corporate Traceability Policy and CQN customer agreement |  |  |  |  |
|  | EOS / ESD |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | ESD CDM | 1.      Customers capable ESD CDM 250 (per 2010 JEP157 or Industry Council White Paper 2) | ESD Industry Council |  |  |  |  |
|  | ESD HBM | 1.      Customers capable ESD HBM 1kV (per 2009 JEP155 or Industry Council White Paper 1) | ESD Industry Council |  |  |  |  |
|  | Handling, Packing and shipping media | 1.      ESD sensitive materials equivalent to legacy | ESD customer team (Montoya) |  |  |  |  |
|  | Connectors, cables | 1.      ESD sensitive materials equivalent to legacy | ESD customer team (Montoya) |  |  |  |  |
|  | Shipping and Handling Media |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) |  | Describe Action | Action Plan Forum (Target Date) |  |
|  | Requirements for trays and tape and reel | 1. Must be compatible to customer manufacturing environment.  2. Must not allow parts to be damaged during handling / shipment.  3. BGA media must be JEDEC compliant | CQN |  |  |  |  |
|  | Incoming inspection | 1.      Not known at this time. Assume legacy requirement | CQN |  |  |  |  |
|  | New requirements for box and/or media marking | 1.      Not known at this time. Assume legacy requirement | CQN |  |  |  |  |
|  | Handling or special requirements for partial boxes or shipments | 1.      Not known at this time. Assume legacy requirement | CQN |  |  |  |  |
|  | Manufacturability | 1. Product protection. No mechanical or electrical (EOS) product damage. E.g. substrate damage and solder sphere damage.  2. Trays / T&R compatible with ODM / OEM processing (e.g. PnP, Tools) - Customer have requested tool compatability w/tray for package removal.  3. Preferred: Compliant to JEDEC Publ 95 (Design Guide for generic S&H matrix trays | CQN |  |  |  |  |
|  | Product protection | 1. Outer shipping box must provide adequate protection for normal shipping and handling during product shipment. (Shock and Vibr requirements listed in Blue Book)  2. Moisture protection | CQN |  |  |  |  |
|  | Material Content | 1. Compliant to all regulatory requirements for substance restriction. E.g. RoHS and REACH (Contact Intel CPRS for Corp Regs and Standards questions)  2. Must comply with Intel EPC spec 18-1201 | Corp Prod Regs and Stds |  |  |  |  |
|  | Design for the Environment | 1.      Shipping media design must consider Design for the Environment  - Materials must be recyclable | CQN |  |  |  |  |
|  | Sustainability |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | EU RoHS | 1. Continue to comply with 6 banned materials  • Lead: 0.1%  • Cadmium: 0.01%  • Mercury: 0.1%  • Hexavalent Chromium: 0.1%  • PBBs: 0.1%  • PBDEs: 0.1%  2. Ensure no materials utilizing exemptions are in use beyong the specified expiration dates | Legal Requirement |  |  |  |  |
|  | JEP-709 (Solid State Devices), IPC-4101C (PCB only) | 1. All new component products must meet the low halogen (halogen free) requirements outlined in JEDEC guideline  2. New cards (Wireless and NICs) must meet both the IPC and JEDEC requirements for finished assembly | Customer / Marketing Requirement |  |  |  |  |
|  | REACH | 1.      All products must declare whether they contain any of the most up to date list of SVHCs (Substances of Very High Concern) >1000ppm | Legal Requirement |  |  |  |  |
|  | Recycling | 1. All plastic materials within the sockets when tested by volume per BS EN 14582 for halogen should meet: 900ppm maximum Cl, 900ppm maximum Br, and 1500ppm maximum total halogens  2. Cadmium should not be used in the painting or plating of the socket.  3. CFCs and HFCs shall not be used in manufacturing the socket.  4. It is recommended that any plastic component exceeding 25g must be recyclable as per the European Blue Angel recycling design guidelines | Legacy |  |  |  |  |
|  | Safety | 1. Design, including materials, shall be consistent with the manufacture of units that meet the following safety standards:  • UL 60950 most current edition and amendments  • CAN/CSA-C22.2 – 60950 most current edition and amendments  • EN 60950 most current edition and amendments  • IEC 60950 most current edition and amendments | Legacy |  |  |  |  |
|  | Supplier Management (Socket, HS Clip, ILM) |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Supplier Capacity | 1. Capable of supporting customization, LVM, HVM, and QA requirements of targeted customers.  2. Major, established supplier needed for On Package Cable / Connector introduction. | Legacy |  |  |  |  |
|  | Geography to support | 1. Able to support and distribute locally to APAC, IJKK, N America, EMEA  2. On Package Cable / Connector requires a Far East supplier | Legacy |  |  |  |  |
|  | Supplier and Subcontractors | 1.      Existing suppliers and sub cons will facilitate transition from old to new components. | Legacy |  |  |  |  |
|  | Number of Supplier per component | 1. Number of enabled suppliers required to support the program is 2 (This includes 2 integrated On Package Cable / Connector suppliers)  2. On Package Cable / Connector sub-components (cable, connector, fasteners, etc) must likewise have 2 established suppliers | Legacy + |  |  |  |  |
|  | Supplier Collateral | 1. Suppliers will provide handling and manufacturing app notes to customers.  2. Supplier to provide collaterals to customers that demonstrate the heat sink solution capability and compatibility with Intel processor as indicated in the components design guides, i.e. Datasheet, mechanical model, thermal model, electrical model, independent test house test report, samples, etc. | Legacy |  |  |  |  |
|  | Engineering Test Vehicles and Samples |  |  |  |  |  |  |
|  | Attribute | Requirement | Source (Name) | Engineering Response ("OK" or "Action") | Describe Action | Action Plan Forum (Target Date) |  |
|  | Thermal Test Vehicle  (TMTV) | 1. TMTV must be powered thru the top side pads and Bottom side Lands for uniform power distribution  2. TMTV must maintain package mechanical form factor and equivalent mechanical behavior of product for  • Testing  • Socket compatibility  • Interface with the heatsink  Interface with the LM  3. HVM test simulation must be complete to assess impacts of warpage induced test issues. 4. TMTV must be capable of accessing the temperature of the center of the package via top pads. | Legacy |  |  |  |  |
|  | Daisy Chain Test Vehicle DCTV | 1. Daisy chain test vehicle must provide 100% coverage daisy chain coverage for components/board mechanical evaluation.  2. HVM test simulation must be complete to assess impacts of warpage induced test issues. 3. Must maintain all processor mechanical form factor features  • Socket compatibility  • Interface with the heatsink  • Interface with the LM  (See platform development schedule for sample availability schedule.) | Legacy |  |  |  |  |
|  | Functional samples | 1. Must include 2D mark 2. HVM test simulation must be complete to assess impacts of warpage induced test issues. | CQN |  |  |  |  |
|  | END |  |  |  |  |  |  |

## Sheet: Sheet2

_(empty sheet)_

## Sheet: Sheet3

_(empty sheet)_
