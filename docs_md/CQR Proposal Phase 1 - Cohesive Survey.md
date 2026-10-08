---
source_file: "CQR Proposal Phase 1 - Cohesive Survey.pptx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Server/2021/CQR Proposal Phase 1 - Cohesive Survey.pptx"
file_type: "pptx"
size_bytes: 11694638
content_hash: "cfbed7533a6c"
converted_at: "2026-10-08T11:29:03"
---

# CQR Proposal Phase 1 - Cohesive Survey

## Slide 1

**Customer SurveyProposed Questionnaires (CQR)**


## Slide 2

**Package Form Factor and Packaging**

- Need early package FF roadmap/changes update - customer capital cost impact
- FF changed significantly in short period, from Purely (2017 PRQ)  Eagle Stream (PRQ EO 2021)  Birch Stream-AP (PRQ EO 2022)
- Au pad corrosion – multiple triggers, multiple products, multiple customers, multiple MRBs for ~ 10 years w/o good resolution to closure
- XEON SP is selling from USD 3K – 10K price/unit, can we add few cents per shipping box on seal pack, to stop the moisture from interacting with pad condition that coherent in the assembly process and promotes pad corrosion ? . (note typical FPO size ~0.5 to 1Ku depend on lot yield)
- Provide pack/shipping options : e.g.  Ship with Thermoform Tray (TFT), JEDEC tray or Tape & Reel (PCH), or CPU w/carrier pre-attached
- Fix marking KIZ, content, FOV, location, increase font size – customer unit traceability and inventory mgmt/control


## Slide 3

**Socket PCBA / Rework**

- Customer expects 1 SMT recipe to assemble socket for all suppliers and SPC controls.
- Need socket supplier transparency for SMT, equivalent output CTF and shipping tray (e.g. quality control/SPC, # socket/tray, orientation & etc)
- Recent supplier excursion : FIT skt-P4 T0 DP, LOTES skt-P0 sys int failure, FIT skt-P4 Bolster out of spec, FIT skt-V0 lever height and load plate angle issue
- RT and HT warpage requirement/control for socket and PCB.
- Customer specially requested Low Temperature Solder and/or Thermal Chip Bonding for and will liquid cooling be POR ?


## Slide 4

**LM, Socket cover, PnP tool, FTT**

- Customer expects – automation friendly, easy to install, easy to uninstall (易装，易拆)
- FTT – POR for Purely but Non- POR for skt-P4/skt-E and broken PEEK nuts issue
- Strong demand from varies customers due to their dual POR process (automated – 2S and manual – 4S/8S).
- Broken PEEK nuts due to torque driver hitting PEEK nuts and/or torque with angle
- FTT/system assembly tool (non-POR support) to address customer concerns – need to include as POR for future platform
- Socket cover  – customer expects automation friendly and easy to install/ uninstall.


## Slide 5

**Board/System Functionality Debug and fault isolation**


## Slide 6

**Back Up**


## Slide 7


## Slide 8

**Example : EPYC**

- Clockwise and anti-clockwise sign for tightening /loosening nuts
- Diagonal nuts sequencing
- Torque at 8 in-lb

- Pin 1 label (triangle sign)

- Non symmetrical h/sink nuts layout – fixed orientation

- Torque 8 IN-LB


## Slide 9

- Rumors of product to be launched with Low Temperature Solder (LTS) PCBA processes

- Will LTS happen with liquid cooling ?


## Slide 10

**Sapphire Rapids Processor Marking and Identification**

- Pin 1 Mark

- 2DID

- SN – not good meaning to keep once the FPO human readable is removed


## Slide 11

**Whitley/Cedar Island Processor (Ice Lake & Cooper Lake)**

- Example of Marking on Package Top Side

- Example of Marking on Package Bottom Side


## Slide 12

**Purley Processor (Cascade Lake)**

- 2DID Matrix (PPIN + SSPEC)
- Dimensions: 2.4mm x5.2mm – alternate traceability

- Example of Marking on Package Top Side

- Example of Marking on Package Bottom Side

- SN (00042)

- FPO
- (L928F212)

- 2DID Matrix
- FPO + SN
- (L928F21200042)

- (Traceability purpose  -- content is different to top side 2DIDs)

- Pin 1

- Pin 1

- Standard 2DID Matrix for traceability  (random numbers)

> **Speaker notes:**
> Whitley – FPO marking  is removed due to limited space.


## Slide 13

**FTT / Sys Assm Tool (Manual)**

- 1-push to lock anti-tilt wires at 1-time
- Provide a guide rail for the torque driver bit, prevent bit hitting PEEK nuts and nuts tightening with angle.
- Need nuts sequencing


## Slide 14

**FTT / Sys Assm Tool (Auto)**

- 1-push to lock anti-tilt wires at 1-time
- Provide a guide rail for the torque driver bit, prevent bit hitting PEEK nuts and nuts tightening with angle.
- Clutch to driver 4 nuts tighten at single torque.


## Slide 15

**Dust Cover, easy to install, easy to uninstall (易装，易拆 – no ergo spec concerns）**

- DELL socket cover
- (Available on eBay, w/additional feature attached on bolster)

- HPE socket cover
- (FOXCONN)

- Anti tilt features

- protection for metal debris ?


## Slide 16

**Example: Huawei XH321 V5(Purley)**

- Customer claimed their PHLM is giving 30% in cost saving

- Phillips screw driver to tighten all 4 + 2 screws

> **Speaker notes:**
> https://support.huawei.com/enterprise/en/doc/EDOC1000171910/bdd76eef/installing-a-processor
> https://support.huawei.com/enterprise/en/doc/EDOC1000183891/a4cc5fae/installing-a-processor


## Slide 17

**ILM Concept**

> **Speaker notes:**
> https://support.huawei.com/enterprise/en/doc/EDOC1000078548/89014b24/installing-a-cpu


## Slide 18


## Slide 19


## Slide 20

**Example (Dell):Power Edge T440, R740XD2 (Purley) & R7525 (EPYC SP3)**

- https://www.dell.com/support/kbdoc/en-sg/000063913/dell-emc-poweredge-t440-how-to-remove-and-install-a-system-board-qrl-video

- https://cdn.cnetcontent.com/a1/49/a149014d-d35a-444f-8752-2dc0898e107f.pdf

- EPYC

- https://www.youtube.com/watch?v=wIx2GSRjIIE

- No label on heatsink –
- For Purley, probably due to the bolster design only required to tighten 2 nuts.


## Slide 21

**HPE/Inventec CPU PnP Tool**


## Slide 22

**Example : LGA4189 /Cedar Island**

- https://www.servethehome.com/installing-a-3rd-generation-intel-xeon-scalable-lga4189-cpu-and-cooler/3rd-gen-intel-xeon-scalable-heatsink-top/

- Pin 1 label (triangle sign)

- Diagonal nuts sequence

- http://www.hojettech.com/pageId34/

- https://www.youtube.com/watch?v=GsYUKQyNGwM


## Slide 23

**Example (Cisco):B200M5 (Purely)**

- https://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-b-series-blade-servers/b200m5-specsheet.pdf

- 2 different labels (FRONT & REAR  orientation)
- Using triangle sign as Pin 1 indicator

- Clockwise sign for tightening nuts

- https://www.ebay.com/itm/Cisco-Systems-UCSC-HS-C220M5-Heatsink-/273943848392


## Slide 24

**Example (HPE):DL360, DL580 & Synergy 660 (Purley)**

- https://techlibrary.hpe.com/docs/synergy/660_Gen10/setup_install/GUID-CC673F5D-4456-4C60-883A-F242360251F0.html
- https://intelligentservers.co.uk/hpe-dl580-gen10-intel-xeon-gold-6136-3-0ghz-12-core-150w-processor-kit-878135-b21-875724-001

- Orientation


## Slide 25

**Example (Lenovo):Thinksystem (Purley)**

- https://thinksystem.lenovofiles.com/help/index.jsp?topic=%2F7X07%2Fsetup_install_a_microprocessor.html

- Using triangle sign as Pin 1 indicator

