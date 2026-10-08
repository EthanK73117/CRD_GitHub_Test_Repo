---
source_file: "TGL_CRD_032019_Final_English_ Wave 1 all customers response.xlsx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (Mobile)/2019 Tiger Lake/TGL_CRD_032019_Final_English_ Wave 1 all customers response.xlsx"
file_type: "xlsx"
size_bytes: 35272
content_hash: "6d87f2ff31c5"
converted_at: "2026-10-08T11:29:44"
---

# TGL_CRD_032019_Final_English_ Wave 1 all customers response

## Sheet: Client-Mobile

|  |  |  | Quanta CQ | Inventec CQ | LCFC | JDM1 | Compal KS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SMT Module | Process Parameters | Comments | Answers | Answers | Answers | Answers | Answers |
| Solder Paste Printing | SAC Solder Paste model (Vendor Name, Formulation Name, Particle Mesh Size) | List top 3 SAC pastes used in your production line | Shenmao PF606-P SAC305 Type 4 (Only use this one paste) | Shenmao PF-606P Tamura TLF-204-93(IVT) Yunnan Tin YW9-3005-98CY04 | 1. SHENMAO     PF606-P         Type 4 2. SENJU M705-S101HF (NL3) Type4 | Senju M705 S101HF(N4)-S5 | Shenmao, Yunnan Tin, Yanktai(type4) |
|  | Printing Machine (Vendor Name, Model Number, Model ID, Model Year) | List top 3 printing machine used in your production line | DEK | DEK; MPM; Hitach MS310 | 1.HITACH / MS-710/ 13MS0078-1 / 2014-06 2.DEK / DEK-GEMINI L-R /  308696 / 2014 | DEK  (Horizon 03iX) | GKG,Panasonic |
|  | Stencil Thickness Range | Please separate it by Intel Y series, U series and H series | U: 4mil/5mil, Y: 3mil | U: 4mil/5mil; Y: 3mil/4mil | Y series: 0.08mm  U&H series : 0.12mm | Both Y and U use 4mil | Y: 3mil, 4mil, U: 4mil(less) 5mil (more) |
|  | Will you use 01005 chip on U series platfrom? If yes, estimate when? |  | No | No | We start to use 01005 at Thinkpad X1 from 2018 | No 01005 chip on u series platform | Yes, already in using |
|  | Do your require Intel provide 3mil stencil recommendation for U series CPU? If yes, can you specify the reason? |  | No need | Yes, some special layout design may require 3mil stencil | Yes, other fine pitch component on the same mother board may need 3mil stencil | No | Yes, because of 01005 chip |
|  | Do you use step stencil? If yes, what's the smallest step size (mm) |  | Yes, 0.02mm | Yes, 0.02mm | Yes, 0.02mm | Yes. 1mil | Yes, 0.02mm |
|  | Stencil Aperture mfg process | Laser Cut, Electroform, 3D Stencil - state preferred type | Laser Cut | Laser Cut | Majority still Laser Cut, Some project start use Nano coat | laser cut | laster cut |
|  | Stencil Coating | No Coating or Nano Coating. If Nano coating is used, Please specify how the nano coat applied to the stencil: 1. wipe on 2. spray+cure. 3 others (please specify) | No coat | Spray and cure | Nano material sputtering process | spray+cure | No coat |
|  | Smallest Area Ratio Preferred |  | >=0.66 | >=0.55 | >=0.66 | >=0.6 | >=0.66 |
|  | Smallest Area Ratio Capable - State conditions to achieve if <0.66 AR (paste mesh size, coating etc) |  | Use thinner stencil | Use smaller mesh size paste and Nano coating stencil | 1. Use thinner stencil 2. Use nano coat or FG material 3.Use type 5 paste | Paste mesh size | No-plan yet |
|  | Stencil vendor name (Top 3) |  | Fosen | Sunshine, Fosen | Corcreate | DESCO | Compal Internal LAB(90%~95%), GuangHong, ZuoLiDa |
|  | Print Speed Range (mm/sec) |  | 120mm/Sec | 100mm/sec | 60-140mm/sec | 80--120 mm/S | 100~120mm/sec |
|  | Print Pressure (Kg) |  | 10kg | 10kg | 10~19KG/0.18Mpa~0.26Mpa | 5KG-12 KG | 9kg |
|  | Print Separation Speed (mm/sec) |  | 5mm/S | 2mm/s | 0.5mm/s~3mm/s | 0-3mm | 2mm/s |
|  | Typical frequency of stencil ultrasonic wash |  | No ultrasonic wash. Use Air gun and solvent to clear every 24 hrs | every 12Hours | Use solvent, no ultrasonic. Every 12H | 12H/time | 6H |
|  | Is Print Pallets used? - If yes is this unique for Print or common for Print and Place, Reflow |  | No | No | No, so far only 1 project use whole process pallet | All process pallet | No |
|  | Is the PCB supported with Pins or block frame or Vacuum ? State PCB thickness range for each type if it applies |  | Support block with vacuum | Support block | Use support Pin at NPI, use vacuum support block after HVM | Pallet + block | Support Block |
|  | Min & Max board handling capability (Length x Width X thickness (mm) |  | Size: Max 370mm*420mm，Min 100mm*100mm Thickness: Min: 0.3mm Max: 1.6mm | Size: Max 370mm*510mm，Min 40mm*50mm | L*W 460*366-->50*50  Thickness: 0.2-->5.0 | Min:50*50mm Max:510*508mm Thickness:0.3~6.0mm |  |
| Solder Paste Inspection | Solder Paste Inspection Machine (Vendor Name, Model Number, Model ID, Model Year) | List the top 3 models and the most recent models | Cyber optic SE500,2011 | TR7006 ,TR7007，KOHYOUNG, Most recent machine: TR7007 SII PULS and Holly H510 | KOH YOUNG  KY8030-3XDL  SPI -83XDL  2012 | Kohyoung (KY-8030L) | holly D686 |
|  | Is SPI done 100% of board printed pads or 100% of BGA, QFN, LGA, BTC (Bottomside Termination Component) components ? | If sampling is done (HVM) state sampling rates | Yes, 100% on all pads | Yes, 100% for all pads | 100% all pads | 100% all pads | yes |
|  | SPI volume control limits (+/- %) |  | 50%~150% | 60%~160% | 40%--170% | 50%--150% | 70%-140% |
|  | How frequently is callibration block (NIST or equivalent standard) used in tool program set-up | How offen the SPI machine is calibarated (Not PM)? | Once a year | Twice a year | 6 months | One time/quarter |  |
|  | Equipment Tool GRR (Gauge Repeatability and Reproducibility) Capability in Percentage (during last validation) |  | N/A | Average of GRR value    4% | 10 | GR&R  V （1.82%） GR&R H（1.29%） GR&R H（1.29%） |  |
|  | Min & Max board handling capability (Length x Width X thickness (mm) |  | Size: Max 370mm*420mm，Min100mm*100mm Thickness: Min: 0.3mm Max: 1.6mm | Size: Max 510mm*460mm, Min 50mm*50mm Thickness: Min: 0.5mm Max: 3mm | single track: L*W 510*600 double track: L*W 510*330 thickness 0.4--4mm | MAX W*L:510mm*460mm MIN  W*L :70mm*70mm Thickness:0.6~5mm | max：570*480 min：50*50 |
| Placement Machine (PNP) | PNP Machine (Vendor Name, Model Number, Model ID, Model Year) for Intel products | List the top 3 models and the most recent models | Panasonic, NPM,2011 | Panasonic DT401-F, CM602-B Type, 2007&2008 | Panasonic NPM-D NM-E-JM1D  2012 | Panasonic NPM-TT, 2012 | Panasonic NPM-TT |
|  | Placement Accuracy in um (+/- 3 sigma) |  | 0.03mm | 0.03mm | 0.03mm | ±40 um | 0.02mm |
|  | Largest BGA size capability (L X W in mm) |  | 40mm*40mm*2mm | 100mm*90mm*25mm | L*X*W 45*45*12mm | 80mm*80mm | 120*90,T:30 |
|  | Largest BGA weight capability (grams) |  | 30g | 100g | 30g max | 30g | NA |
|  | Smallest BGA/CSP pitch capability (mm) |  | 0.4mm | 0.35mm | 0.5mm | 0.3mm | 0.3mm |
|  | Are Pallets Used during placement |  | No | No | NO, use pin support | yes | No |
|  | Intel component to other components spacing keep out (mm) and component height (mm) constraints |  | KOZ: 2mm; Height: 5mm | KOZ: 1~2mm, Height: 10mm | KOZ 40mil, no requirement for component height | KOZ 0.2mm, Components height 1.2mm | keep out 1mm |
|  | Do you have in line 2DID barcode component traceability |  | No | No | NO | no | No, we have offline tracebility |
|  | Do you have Nozzle Traceability |  | Yes | No | NO | no | No |
|  | Min & Max board handling capability (Length x Width X thickness (mm) |  | Size: Max 370mm*420mm，100mm*100mm Thickness: Min: 0.3mm Max: 1.6mm | Size: Max 510mm*460mm, Min 50mm*50mm | Double track: W 50--300mm  L 50--510mm Single track: 50--590mm   L 50--510mm Thickness: 0.3--8.0mm | MAX W*L:510*510 mm MIN  W*L :50*50mm Thickness:0.4~5.0mm | 50*50 510*590 |
|  | BGA Flux Dipping Capability |  |  |  |  |  |  |
|  | Flux Material -Vendor and Formulation Name |  |  |  |  |  |  |
|  | BGA ball percent coverage capability (%) |  |  |  |  |  |  |
|  | Flux dwell time (msecs) |  |  |  |  |  |  |
|  | BGA retraction rate from Flux (m/sec) |  |  |  |  |  |  |
|  | SJEM Dipping Capability | SJEM is Solder Joint enforced Material to help Reliability and as an alternate to Corner Glue/BLUF process |  |  |  |  |  |
|  | SJEM Material -Vendor and Formulation Name |  |  |  |  |  |  |
|  | BGA ball percent coverage capability (%) |  |  |  |  |  |  |
|  | SJEM dwell time (msecs) |  |  |  |  |  |  |
|  | What is the load force during dipping process |  |  |  |  |  |  |
|  | BGA retraction rate from SJEM (m/sec) |  |  |  |  |  |  |
| Reflow (Convection) Oven | Reflow Machine (Vendor Name, Model Number, Model ID, Model Year) |  | REHM,2011 | Rehm VXP945N RP-2041 7/2018 | Rehm VXS944 RS-0448 2012/03 | HELLER | Heller 2043 |
|  | Number of Heating & Cooling Zones |  | 13 heating zones; 4 cooling zones | 13 heating zones; 4 cooling zones | 13 heating zones; 5 cooling zones | 13 Zones | 14 Zones |
|  | Is N2 used ?  If yes what O2 PPM control |  | Yes, O2 < 3000PPM | Yes, O2 < 3000PPM | Yes, O2<1000PPM | Yes, O2 800~1200PPM;2000-3000PPM | Yes, O2<30000PPM |
|  | What is Delta T across Intel Component | Difference in Temp from outside ball to inside ball) | <5C | 2~3℃ | <5C | <3C |  |
|  | For SAC Solder |  |  |  |  |  |  |
|  | Peak Temperature Range |  | 240-250C | 235~250℃ | 235--250C | 237-245C | 235~250C |
|  | TAL time in seconds |  | 60-90s | 60~120s | 60--90s | 50-65s | 40~70s |
|  | Ramp Rate & Cooling Rates (degree C/sec) |  | 3C/S | 1~3C/S | 1~3C/S | Ramp up rate0.8~1.3℃/S(40~237)  Ramp down:250℃~220℃≦3℃ | <3c/s |
|  | Belt Speed (cm/sec) |  | 1400mm/min; 2.33cm/sec | 120cm/min | 100-140cm/min | 100-120cm/min | 130cm/min |
|  | Min & Max board handling capability (Length x Width X thickness (mm) |  | Size: 400mm*500mm,Thikcness: 0.8mm. | Size: Max 460mm; Min 50mm (w/o central support), 80mm (w/ central support) | 40-500mm | Min: 50mm Max: 508mm Thickness:29mm | Max 390*450 |
|  | Pallet Design |  |  |  |  |  |  |
|  | Pallet material |  | Aluminum | Aluminum | Aluminum | Aluminum | Aluminum |
|  | Is this pallet universal to Print/PNP or custom |  | For reflow only | For reflow only | For reflow only | All SMT process | For reflow only |
|  | Are there tooling pins used to secure PCB. If yes, what is the minimum quantity? |  | No tooling pins | No tooling pins | No tooling pins | Two Tooling Pins | No Tooling Pins |
|  | What is minimum clearance (mm) from board edge to pallet recess edge ? |  | 1mm | 0.5mm | 0.5mm | Calculated CTE by PCB length. | 0.5mm |
|  | What are the types of board-clamps used (flip-tab, top plate, kapton tape, etc.) |  | Automatic clamps | Automatic clamps | Spring clamps | Tape on edge. | No board clamps |
|  | When using print pallets, How are the PCB handled in the print module? Do you manually tape the PCB for both passes, or not (fully automated)? |  | Yes, manual tape if use print pallets, at both pass | Yes, manual tape if use print pallets, at both pass | Yes, manual tape at both pass, but very few project use it | Tape at both pass | No, not using print pallet |
|  | How do you decide if need a top hat or not |  | We do not use top hat | Depend on PCB warpage measured by our QA lab, and NPI SMT yield | Normally no top hat. If PCB T<0.6mm, will consider top hat | Depends on PCB thickness and if have shielding/connector and DIP component need to hold down | When there are big shielding/connector and DIP component need to hold down |
|  | The pallet thickness you are using |  | 10mm | 10mm | 8mm | 5mm | 8mm |
|  | Board  Warpage Controls at room temprateure | how you control PCB warpage at room temp | < 0.5% diagonal length | Follow IPC standard | < 0.7% diagonal length | Follow IPC standard | Follow IPC standard |
| Adhesive (Solder Joint Reliability) | Are you currently using adhesive for Intel BGA in HVM? | Survey only new customers |  |  |  | Not on Intel BGA, Only for touch IC and WLCSP. |  |
|  | What are you using (Example: Corner Glue, Corner dot, underfill, underfilm, corner fill)? | Survey only new customers |  |  |  | Corner Glue, Underfill, but not Intel BGA |  |
|  | What's the vendor name and model of the adhesive material you are using? | Survey only new customers |  |  |  | Zymet,UA-2605-B |  |
|  | Dispense Machine (Vendor Name, Model Number, Model ID, Model Year) |  | N/A | HTD-420-1C | axxon /  AU77s / 0Au77s1711026/ 2017.11.21 EL / EM-5701N /DS-M2990/2012.10 | ANDA | EM-5701L |
|  | Curing Oven (Vendor Name, Model Number, Model ID, Model Year) |  | N/A | MA-9CR | TUNG SING /BAT-1500-VF/DS20130301/2013.25 | HELLER | EM-5701U （UV) |
|  | Where in the board manufacturing process is the adhesive applied (Ex. Before SMT (or) After SMT/Before Functional Test (or) After SMT/After Functional Test)? | Survey only new customers |  |  |  | After FCT, Per customer request |  |
|  | Is the adhesive reworkable? | Survey only new customers |  |  |  | Yes |  |
|  | Is the adhesive applied in-line or off-line process? | Survey only new customers |  |  |  | Inline |  |
|  | How is after cure validated (voiding, area coverage, adhesion to pcb and component) non destructively |  | Visual inspection only | No | Visual inspection only | Visual inspection | Visual inspection only |
| Rework 维修 | BGA Rework Tool (Vendor Name, Model Number, Model ID, Model Year) |  | Quick, EA-H00.2016 | Ye Ou electric TP500: Year 2015*2  Year 2013*3  TP580:2019*1 | shuttle star / RW-SV600 /90105120067 /2012.10 | SRT，SRT Micra | QUICK EA-H15 |
|  | Paste or Flux | Some applications or design layouts may require one or the other | paste | Paste | Paste and Flux | Solder paste | Paste and flux |
|  | Paste/Flux Vendor Name and Formulation name | Identify Names accordingly for SAC and LTS types (if used) | Shenmao PF606-P | Shenmao PF606-P | Paste: SHENMAO  PF606-P   Type 4          SENJU M705-S101HF (NL3) Type4 Senju L28-143HF(L)Type4(LTS) Flux: AMTECH /NC-559-ASM | senju/ shengmao, same as printing paste | Shenmao PF606-P (Paste), AIM(NC-254, Flux) |
|  | For HiMB, how is Delta T (top-bottom) on BGA site controlled | If Hole is covered, what material is used | No we don't have HIMB design | Cut scrapped PCB | Not cover hole | Not cover hole | Not cover hole |
|  | For SAC Solder |  |  |  |  |  |  |
|  | Peak Temperature Range |  | 240-250C | 230-250℃ | 235--250 | 235~245℃ | 230~250C |
|  | TAL time in seconds |  | 60-90S | 40-100S | 60-90s | 50~70s | 30~90s |
|  | Ramp Rate & Cooling Rates (degree C/sec) |  | 3 C/S | 1~3 degree C/sec | 1--3 | ＜3℃ | <4C |
|  | Cycle Time (average)  in mins to replace/remove |  | 10 min | 20 min | 5 min | about 12 mins | 15min |
| PCB | PCB thickness Range (mm) |  | 1-1.5mm | 0.8mm~1.2mm | 1.0mm | 0.44-0.85mm, 0.85mm for mother board with CPU | 0.8~1.2mm |
|  | PCB type (3,4) |  | Type 3 | Type 3 & Type 4 | type3 | Type4 | Type 3 & Type 4 |
|  | Line Width/Spacing (mm or mils) | You can check with your RD to get the answer | 3mil line width, 3.5mil line spacing | HDI PCB Width/Spacing: 2.3/2.3 mil | Line width 3mil, Line space 3mil | Width:75μm Spacing:75μm |  |
|  | Smallest BGA pad size (mm) - MD and SMD |  | SMD, C10M8 | Pitch 0.4 BGA all use SMD pad : Pad 11.7 mil     SRO: 9 mil | 0.2 mm circle | MD pad: 210μm SMD pad: 250μm | 0.2mm |
|  | RIMB and HIMB Capability | RIMB - Recess in Mother Board, HIMB - Hole in Mother Board | NA, we don't have such design | Yes | yes | NPI now, no HVM product before | HIMB - yes; RIMB - No |
|  | Surface finish( OSP, ImAg, ENIG, HASL, Other) |  | OSP | OSP Intek | OSP | ENIG,OSP | OSP |
| LTS related | Which OEM have discussed on LTS validation or implementation |  | NA | No | Think pad all introduced LTS from 2018.05 at Intel platform | NA | No |
|  | What are the pastes you are currently evaluating or tested with confident? What is your build plans or currently utlizing? |  | NA | We qualified 3 LTS paste, but not use in production | qualifying : Alpha OM550LP-HRL2 qualified: Senju L28-143HF(L)Type4 | NA | NA |
|  | What is your expectation of benefits for LTS adoption / in order for you to adopt LTS? |  | NA | N/A | To have similar reliability with SAC joint | NA | NA |
|  | Do you see obstacle / challenges in LTS implementation if LTS can meets the rel performance of your customers? |  | NA | cost | CPU solder ball are still SAC | NA | NA |
|  | Have you utilize LTS for your products (any type of products)? |  | NA | No, we just qualified it | Yes | NA | NA |
|  | If you implement LTS, do you prefer to have  dedicated line for LTS or switch between LTS and SAC designs on the same line? |  | NA | Dedicate line | Dedicate line | NA | NA |
|  | Are there any classes of components that with special concern to you if building with LTS? |  | NA | Fine pitch component, like QFN | All component need to be qulified with LTS process our current experience shows the component with Tin covered terminal is not suitable for LTS process, will have open solder issue. We have to switch to electroplate terminal components. | NA | NA |
|  | What is the minimum number of LTS paste options you would need to qualify to support an HVM product? |  | NA | 3 | 2 | NA | NA |
|  | Would you consider LTS to be benifitial if the solder paste pricing is still the same with SAC? |  | NA | Depends on market acceptance | No, current LTS have short life span compare to SAC paste (per paste vendor recommendation:1. Short Stencil life (LTS 0.5hr, SAC 7~8 hour), 2. Short PCB life (LTS 1hr, SAC 2hours), 3. After open the jar: LTS: 8hours; SAC 12hours | NA | NA |
|  | Any restriction on only use Halogen free solder paste? |  | NA | Yes, need use HF paste | Yes | NA | NA |
|  | Any restriction on Antimony (锑 Sb) content in solder paste? and to what level? |  | NA | No | N/A | NA | NA |
|  | LTS Solder Paste model (Vendor Name, Formulation Name, Particle Mesh Size) | List top 3 LTS pastes that you’re using now or plan for future production line. | NA | Alpha HRL1 alloy  Tumura Sn Bi58 Yunnan tinSn Bi57 | Senju L28-143HF(L)Type4, 0.43 and 0.35 pitch use type 5 | NA | NA |
| Thermal solution assembly/dis-assembly | Do you have process to evaluate die crack during thermal solution assembly/dis-assembly? | Yes/No, please provide details | No | No | No, RD will verify it at RD lab. Factory just follow the process instruction from RD | No | No |
|  | How do you evaluate die pressure during thermal solution assembly/dis-assembly? | Pressure Paper or Film Sensor | Pessure paper | Pressure paper | No | Pressure paper | No |
|  | If you are using film sensor,  do you follow Intel's recommended process to condition, equalize and calibrate the film sensor? | Yes/No, please provide details | N/A | N/A | N/A | N/A | N/A |
