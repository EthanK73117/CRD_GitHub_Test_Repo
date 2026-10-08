---
source_file: "CQR - Cohesive Survey.xlsx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Server/2021/CQR - Cohesive Survey.xlsx"
file_type: "xlsx"
size_bytes: 32348
content_hash: "c8d80d64f341"
converted_at: "2026-10-08T11:29:02"
---

# CQR - Cohesive Survey

## Sheet: Brain Storm Ideas

| SMT Question |
| --- |
| <> *1- package size/ Roadmap, important for equipment  cost (cannot change too much in x years)-- BHR-AP/BHR-SP. |
| <> - socket supplier transperancy for SMT  ? quality control -> is there any quality issue or improvement at PHM/socket supplier that u would like Intel intervention ? |
| '- TFT Tray ? Tray polarity, package pin1 and supplier tranparency (include in JEDEC for long term, temporary let Inventec to get their own tray layout) |
| '- loose PnP Cap and tolorance by suppplier - Is there uniformity across all socket suppliers for PnP recipe? |
| '- PnP cap removal tool - Is the tool used in all builds and is there any design considerations that should be made? |
| '- clearer socket CTF drawings |
| <> - PCH, shipping media preferance - Is there a preference T&R vs tray? |
| SMT/rework profile uniformity across skt suppliers - Is there uniformity across socket suppliers for SMT reflow? |
| rework |
| '- PnP cap meterial melting - |
| '- *1 impact rework too |
| '- reball/touch-up - Is reball/touch-up used? |
| '- DDR5 SMD BKM sharing ? |
| brd layout |
| <?> open via ? -- Are open vias used underneath the CPU socket? are there any concerns with SMT impact of open vias? |
| Do you follow land pattern recommendation? |
| package & design |
| <> LGA pad corrosion ? |
| MBB ? |
| Au plating thickness - Typical socket plating thickness used? (get from supplier? the breakdown of 15 vs 30um) |
| What drives the decision to have different Au plating thicknessess? |
| <> Special sku for ODM testing (with high durability for LGA pads) |
| <> KIZ for bottom 2DID, top marking, font size, FOV window, location, content, type (2D vs human readable)-- in desgin |
| Do the current marks on the IHS and pkg substrate provide the information needed in the factory/field? |
| '    - Human Readable |
| '    - 2DM |
| IHS shape correlated to SKU |
| PMD vs Intel test pads (internal), KOZ to test pads, KIZ for carrier |
| <><> shipping CPU with carrier attached option, Would u like to hv option for receiving CPU shipping with carrier pre-attached ? |
| Automation (test/system integration) |
| what improvements can be made for automation friendliness |
| eg. CPU to PHM assembly |
| PHM to socket assembly |
| socket/dust cover removal ? (AMD usign ILM) |
| traceability - inventory control (FIFO), anti-fraud, |
| '- customer wants Intel to provide all units 2DID per shipment (scan FPO then & get 2DID, csv format) |
| 4S/8S manual process |
| FTT/assembly tool usage - will the current assembly tool be valuable for automated assembly? (check CCI Purley FTT to estimate) |
| <> Do u forsee the FTT/assm tool helps in your test and system int line ? |
| <> if yes, do you plan to implement this tool ? |
| Assembly |
| torque driver RPM |
| follow MAS torque recommendation or legacy torque value? (8 vs 12 in-lbf) |
| PEEK vs metal nuts preference - impact of debris |
| 30 cycle requirement for socket - will likely be asked by PAE as well |
| <> tray assembly vs fixture assembly of PHM --> Do you design own fixture for PHM assembly ? |
| Ergo concerns? |
| customerexpectation easy to attch/ easy to remove (HP and Dell) |
| test |
| Is there any debug capability you would like Intel to improve ? |
| <> *2) Do u think automated crash dump (ACD) is helpful/useful in your system debug during FACR ? ( this can probably link to include BIOS Writer Guide) |
| 3) What are the debug method you are using in isolating the failure to Intel processor ? |
| <> 4) How can Intel help to speed up your debug process ? |
| <> 5) Do you have any recommendation on desire debug feature for you board failure analysis ? |
| <> 6) What are the software/test/method that you typically use and can help to reproduce/debug failure for Intel processor ? |
| 7) Do you think automated debug tool on failure commonality study would help you to isolate issue easier? |
| 8) Do you think automated log analysis provided during debug validation is useful for further debug? |
| -- MCE log / crash log |
| DFDinostic, DFT, DFX |
| colleterals / colleberation (to ask customer to provide feedback whether need improvement or other than these. any additional they needs) |
| MAS (score 1 -5, if low suggest improvement) - PMD disclaimer |
| BFI Guidance (can we include MAS) - define timing for MCC to meet (mTPS/traincient bend?) |
| Design-In interposer SMT (internal to sort out) |
| TMSDG (score 1 -5, if low suggest improvement) |
| PMD |
| <> MV ? |
| how important is the 30 cycle requirement for socket durability? |
| How important is the no sequence vs sequence used based on overall cost? |

## Sheet: Test System Integration Process

| Test/System Integration Process |  |  | Category / Area | Note for Intel, Delete this column before sharing to customer | Additional Comment |
| --- | --- | --- | --- | --- | --- |
| Q1 | Is there any additional improvements can be made to ease automation ? |  | Automation |  |  |
|  | a) | Socket PnP Cover removal | Automation |  |  |
|  | b) | CPU to PHM assembly (attaching CPU to carrier and heatsink) | Automation |  |  |
|  | c) | PHM to socket/PCB assembly | Automation |  |  |
|  | d) | Socket cover installation and removal |  |  |  |
|  | e) | Do you perform CPU to PHM assembly on Intel shipping tray ? If not, pls share details. | Automation | AMD using ILM, no dust cover |  |
| Q2 | What is your current and future plan for System Assembly automation ? |  | Automation (Sys Assembly) |  |  |
|  | a) | Socket PnP Cover removal | Automation (Sys Assembly) |  |  |
|  | b) | CPU to PHM assembly (attaching CPU to carrier and heatsink) | Automation (Sys Assembly) |  |  |
|  | c) | PHM to socket/PCB assembly | Automation (Sys Assembly) |  |  |
|  | d) | Socket cover installation and removal | Automation (Sys Assembly) |  |  |
| Q3 | What is your current and future plan for board testing automation ? |  | Automation (Board Function Test) |  |  |
|  | a) | Do you design your own test fixture for test automation ? | Automation (Board Function Test) | Typially 2S boards high volume will hv test fixture, but for volume upside, manual test station will be set-up. |  |
|  | b) | Do you still require manual testing  with the test fixture ? | Automation (Board Function Test) | Typically for 4S/8S board testing. FTT/assembly tool usage - check CCI Purley FTT to estimate |  |
|  | c) | Do you forsee the FTT/assm tool helps in your test and system int line ? | Automation (Board Function Test) | Intel to share the tool video along with the survey |  |
|  | c-i) | if yes, do you plan to implement this tool ? | Automation (Board Function Test) |  |  |
| Q4 | What is your current and future plan for data automation (eg. big data anaylsis) ? |  | Automation (data) | traceability - inventory control (FIFO), anti-fraud, |  |
|  | a) What are the content on Intel product marking or box label that you will use for traceabillity ? |  | Automation (data) | Few customer had made requests Intel to provide all units 2DID per shipment (in soft copy or retrive from some database.  They can input these 2DID into their system, common format is acceptable, eg. CSV) |  |
|  | b) How do you like to use these information (in Q4a) for your traceability ? |  | Automation (data) | eg. any real time down stream triggering & etc |  |
|  |  | Special sku for ODM testing (with high durability for LGA pads) |  |  |  |

## Sheet: PCBA & Rework

| PCBA & Rework |  |  | Category / Area | Note for Intel, Delete this column before sharing to customer | Additional Comment |
| --- | --- | --- | --- | --- | --- |
| Q1 | Are there any quality issues or improvements needed at the PHM/socket suppliers that Intel should be aware of? |  | Supplier Quality |  |  |
| Q2 | Do you have a preference for the PCH shipping media (T&R vs tray)? |  | Shipping |  |  |
| Q3 | For board assembly, Is there any concern of impact of open/uncovered vias on the socket SMT or rework process success? |  |  | There are some designs with open/uncovered vias underneath the socket near the land pads potential risk for rework/SMT |  |

## Sheet: Test Debug & Fault Isolation

| Test Debug & Fault Isolation |  | Category / Area | Note for Intel, Delete this column before sharing to customer | Additional Comment |
| --- | --- | --- | --- | --- |
| Q1 | Would automated crash dump (ACD) be helpful/useful in your system debug during FACR ? | Fault Isolation | This can probably be included in the BIOS Writer Guide |  |
| Q2 | How can Intel help to speed up your debug process ? | Test Debug |  |  |
| Q3 | Do you have any recommendations for debug features to help with your board failure analysis ? | Test Debug |  |  |
| Q4 | What are the software/test/methods that you typically use and can help to reproduce/debug failure with Intel processors ? | Test Debug |  |  |
