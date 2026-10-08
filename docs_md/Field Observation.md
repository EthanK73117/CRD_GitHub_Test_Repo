---
source_file: "Field Observation.pptx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Server/2021/Field Observation.pptx"
file_type: "pptx"
size_bytes: 9754264
content_hash: "3597dfcc6012"
converted_at: "2026-10-08T11:29:03"
---

# Field Observation

## Slide 1

**Field Observation**


## Slide 2

**Package Form Factor and Packaging**

- Need early package FF roadmap/changes update - customer capital cost impact
- FF changed significantly in short period, from Purely (2017 PRQ)  Eagle Stream (PRQ EO 2021)  Birch Stream-AP (PRQ EO 2022)
- Au pad corrosion – multiple triggers, multiple products, multiple customers, multiple MRBs for ~ 10 years and fixes still WIP
- XEON SP unit selling price between from USD 200 (Bronze) – 10K (Platinum). The product deserved seal pack to stop “external” air pollutants interacting with pad condition/crevice that coherent in the package technology/assembly process.
- Provide pack/shipping options : e.g.  Ship with Thermoform Tray (TFT), JEDEC tray or Tape & Reel (PCH), or CPU w/carrier pre-attached
- Some customers had been manually transferred PCH from T&R to trays and TFT to hard trays for their mfg process.
- Fix marking KIZ, content, FOV, location, optimum font size and ensure documentation in CRD – customer unit traceability and inventory mgmt/control


## Slide 3

**Socket PCBA / Rework**

- Customer expects 1 SMT recipe to assemble socket for all suppliers and SPC controls.
- Need socket supplier transparency for SMT, equivalent output CTF and shipping tray (e.g. quality control/SPC, # socket/tray, orientation & etc)
- Socket tray CTF pilot in socket P4 and P5. Continue to keep proliferate.
- Recent supplier excursion : FIT skt-P4 T0 DP, LOTES skt-P0 sys int failure, FIT skt-P4 Bolster out of spec, FIT skt-V0 lever height and load plate angle issue
- some data showed process drifted, beyond LCL/UCL established during DG1.0
- RT and HT warpage requirement/control concerns for socket and PCB
- Rumors of competitor product (SP5) to be launched with Low Temperature Solder (LTS) and another competitor with Thermal Chip Bonding for PCB assembly
- Also, there are customers looking forward for feasibility of LTS and/or Thermal Chip Bonding in Intel Server products


## Slide 4

**LM, Socket cover, PnP tool, FTT**

- Customer expects – automation friendly, easy to install, easy to uninstall (易装，易拆)
- FTT – POR for Purely but Non- POR for skt-P4/skt-E and broken PEEK nuts issue
- Strong demand from varies customers due to their dual POR process (automated test fixture for 2S and manual test for 4S/8S, test fixture cost approx. USD40K).
- Broken PEEK nuts due to torque driver hitting PEEK nuts and/or torque with an angle
- FTT/system assembly tool is being developed (non-POR support) to address customer concerns – need to include as POR for future platform for automation
- Socket cover  – customer expects automation friendly and easy to install/ uninstall.
- Other CPU PnP / PHLM / ILM / carrier concept


## Slide 5

**Back Up**


## Slide 6

**Purley Processor (Cascade Lake)**

- 2DID Matrix (PPIN + SSPEC)
- Dimensions: 2.4mm x5.2mm – alternate traceability

- Example of Marking on Package Top Side

- Example of Marking on Package Bottom Side

- SN (00042)

- FPO (L928F212)

- 2DID Matrix
- FPO + SN
- (L928F21200042)

- (Traceability purpose  -- content is different to top side 2DIDs)

- Pin 1

- Pin 1

- Standard 2DID Matrix for traceability  (random numbers)

- FPO = Finish Processing Order

> **Speaker notes:**
> EGS – FPO marking  is removed due to limited space.


## Slide 7

**Whitley/Cedar Island Processor (Ice Lake & Cooper Lake)**

- Example of Marking on Package Top Side

- Example of Marking on Package Bottom Side


## Slide 8

**Sapphire Rapids Processor Marking and Identification**

- Pin 1 Mark

- 2DID (Must Keep)

- SN – no good meaning to keep once the FPO human readable marking  is removed.

- Many customers had implemented bottom 2DID as traceability and inventory control (FPO contained Datecode information)
- Need to ensure to keep for future package designs and document in CRD

- FPO = Finish Processing Order


## Slide 9

**FTT / Sys Assm Tool (Manual)**

- 1-push to lock anti-tilt wires at 1-time
- Guide torque driver bit, prevent bit hitting PEEK nuts and/or nuts tightening with angle.
- Need nuts sequencing


## Slide 10

**FTT / Sys Assm Tool (Auto)**

- 1-push to lock anti-tilt wires at 1-time
- Guide torque driver bit, prevent bit hitting PEEK nuts and/or nuts tightening with angle.
- 4 nuts tighten at single torque.


## Slide 11

**Dust Cover, easy to install, easy to uninstall (易装，易拆 – no ergo spec concerns）**

- DELL socket cover
- (Available on eBay)
- -  works together with retention clips on bolster

- HPE socket cover
- (FOXCONN had similar concept)

- Retention clips

- protection for metal debris ?

> **Speaker notes:**
> https://www.youtube.com/watch?v=a7spFUjNTek
> https://www.youtube.com/watch?v=alXFJ-p_nNw


## Slide 12

- https://cdn.cnetcontent.com/a1/49/a149014d-d35a-444f-8752-2dc0898e107f.pdf

- Retention clips act as Anti tilt, lock/unlock PHM


## Slide 13

**Example (Dell):Power Edge T440, R740XD2 (Purley) & R7525 (EPYC SP3)**

- https://www.youtube.com/watch?v=a7spFUjNTek
- https://www.dell.com/support/kbdoc/en-sg/000063913/dell-emc-poweredge-t440-how-to-remove-and-install-a-system-board-qrl-video

- EPYC

- https://www.youtube.com/watch?v=wIx2GSRjIIE

- No label on heatsink for nuts sequence for Purley, probably due to the bolster design only required to tighten 2 nuts ?

- Partially nuts tightened and diagonal sequence.

> **Speaker notes:**
> https://cdn.cnetcontent.com/a1/49/a149014d-d35a-444f-8752-2dc0898e107f.pdf


## Slide 14

**Example: Huawei XH321 V5(Purley)**

- Customer claimed their PHLM is giving 30% in cost saving

- Phillips screw driver to tighten all 4 + 2 screws
- Will similar concept works in Whitley/EGS ?

- 1

- 2

> **Speaker notes:**
> https://support.huawei.com/enterprise/en/doc/EDOC1000171910/bdd76eef/installing-a-processor
> https://support.huawei.com/enterprise/en/doc/EDOC1000183891/a4cc5fae/installing-a-processor


## Slide 15

**HPE/Inventec CPU PnP Tool (Purely)**


## Slide 16

**ILM Concept, carrier for CPU handling**

- Gripping from both short edges

- Carrier installation at the short edges

> **Speaker notes:**
> https://support.huawei.com/enterprise/en/doc/EDOC1000078548/89014b24/installing-a-cpu


## Slide 17

- Suspected carrier damaged during assembly resulting bend contacts during automation (different boundary condition)


## Slide 18

- Observed debris at package edges/corners

