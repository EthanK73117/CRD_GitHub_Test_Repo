---
source_file: "2024_03-05_LNL-Mx Customer Readiness Update_CMEE.pptx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (Mobile)/2024 Q2 CLIENT OEM SJR TESTING/2024_03-05_LNL-Mx Customer Readiness Update_CMEE.pptx"
file_type: "pptx"
size_bytes: 30926827
content_hash: "e01ecde6f9b1"
converted_at: "2026-10-08T11:29:45"
---

# 2024_03-05_LNL-Mx Customer Readiness Update_CMEE

## Slide 1

**LNL-Mx Customer Readiness Summary**

- Intel Corporation
- CMEE Team
- Mar 5, 2024

- INTEL CONFIDENTIAL –
- ONLY SHARE IF NECESSARY – HIGHLY SENSITIVE CUSTOMER INFORMATION


## Slide 2

**Customer SJQ & SJR Enabling Efforts for Reverse Hybrid (RH)**

- Large number of LNL-Mx collaterals provided by CME to external customers for Mfg Validation Enabling Activities (2023):
- Qty=2474 Buck Bay, Qty=115 YTBs, Qty=160 ETBs
- Enabled Customer List: Dell (Compal, Wistron), HP (Quanta, IEC), Asus (IEC), Lenovo (LCFC, Japan), Huaqin NC, Wistron (Taiwan, CD), Samsung, Pegatron CQ, Microsoft (Pegatron SZ), MSI, Panasonic, ORS Program

- LNL DESIGN WIN CUSTOMERS (As of Q4’23): ACER, ASUS, DELL, HP, Lenovo, MSI, Samsung, Compal, Inventec, Quanta, LCFC


## Slide 3

**LNL-Mx Help Needed**

- T=0 Micro Crack Issue:
- Provide T=0 micro-crack corrective action(s), such as land pattern/board design updates, best FA techniques & other MAS BKMs, ASAP (per HP-3/22 & per Microsoft’s-Date TBD to intercept May builds) -> need to address both corner crack & edge crack cases
- Provide the LNL-Mx BFI Strain limit (per HP, Microsoft & others request)
- SMT Process:
- Provide reflow process optimizations to reduce SJ voiding (per HP, Quanta, MSI, Asus & other OEMs request)?
- Verify if N2 (O2 PPM) can be relaxed to 4000 PPM (per Microsoft’s request)?
- Need Intel’s help to recommend a 2nd glue supplier (per Dell’s request)?
- When creating the QS stencil design, consider incorporating our customer’s stencil designs.
- X-Ray:
- SJ VOID AI SOFTWARE: Can the SW help to distinguish between via’s (under pads) & voids using Intel’s AI software? (per HP/Quanta’s request)
- RAD LIMIT: TPTD to evaluate feasibility of a lowered 10RAD limit across the necessary x-ray process steps (multiple Customers)


## Slide 4

**Customer LNL-Mx Readiness (Data Links)**

- Lenovo SMT/FA
- Lenovo Reliability
- Dell SMT/FA
- Dell Reliability
- HP SMT/FA
- HP Reliability
- Asustek SMT/FA
- Asustek Reliability
- Microsoft SMT/FA
- Microsoft Reliability

- Samsung SMT/FA
- Samsung Reliability
- Acer SMT/FA
- Acer Reliability
- Huaqin SMT/FA
- Huaqin Reliability
- Panasonic SMT/FA
- Panasonic Reliability


## Slide 5

**Lenovo Readiness**

- IdeaPad = Consumer Division
- ThinkPad = Commercial Division

- Lenovo Thinkpad, full LTS process, 100% SMT yield, detail is customer confidential


## Slide 6

**Lenovo Readiness**

- LNL-Mx ETB build 1st Wave (Full LTS/4CCSB)
- Buck Bay Build Qty: 200pcs ( 4 DOE groups )
- Manufacturing site: Wistron & LCFC
- SMT Yield:  Closed – Good Yield
- ASEC (AS3910) corner fill/thermal cure
- 4 LTS Pastes:  Senju L29, Senju Lxx, ShenMao PF735-PQ10-10L, Cookson OM565 HRL3
- Initial test (T=0): Side-view/E-test/X-ray/Dye pry/X-section: Closed – Acceptable
- Stencil aperture design
- Paste Volume /Ball Volume Ratio:
- LCFC: 0.29 round, 0.1mm, P/B 46.7%
- Wistron: 0.28 square,0.1mm, P/B 52.8%
- IR reflow profile setting
- Follow Lenovo near-eutectic LTS common spec
- Peak Temp: 173 +/- 3 degrees

- Full LTS Builds

- 2nd Wave, new paste:
- Added Senju L204 (new alloy, optimized for EM performance)

- (Full LTS/8CCSB)


## Slide 7

**Lenovo Readiness**

- Lenovo (Local ODM built, FA at LCFC) IdeaPad, LNL-Mx ES1
- Lenovo’s First Reverse Hybrid build
- Warrior Project
- 46/48 = 95.8% yield.  2 units with NWO & suspect hot tearing found, U1-ROW7.
- Follow Intel MAS stencil, but used all square apertures vs. round apertures
- Shenmao PF606-P Type 5 paste

- Reverse Hybrid Build

- Unable to get the 2DID (Bing Confirmed)


## Slide 8

**Lenovo Readiness**

- Lenovo IdeaPad / Qixia Project: ES2 Functional Parts
- SMT yield: 91% (162/178); SBB & NWO Observed
- Totally built 6 batches
- Stencil: 2 type stencils used
- Solder paste: Shen MaoPF606-P Type 4 & Shen MaoPF606-P Type 5
- PCB: 0.8 mm PCB, supplier: VGT
- Pallet used for reflow
- N2 reflow

- Reverse Hybrid Build


## Slide 9

**Lenovo Readiness**

- 6 Batches Run/2 Stencils: Lenovo IdeaPad / Qixia Project (Reverse Hybrid)

- Generally speaking, Lenovo prefers to see SBB vs. Open defects (SBB easier to detect)


## Slide 10

**Lenovo Readiness**

- SBB Position (Including all of the builds)

- Reverse Hybrid Build/IdeaPad

- Batch 1, 2, 4, 6

- 6 Batches Run/2 Stencils: Lenovo IdeaPad / Qixia Project (Reverse Hybrid)


## Slide 11

**Lenovo Readiness**

- SBBs

- NWOs

- Jan 26’24

- Reverse Hybrid Build / IdeaPad

- Batch 4

- 6 Batches Run/2 Stencils: Lenovo IdeaPad / Qixia Project (Reverse Hybrid)

- 2DID: U346F14900081
- Per Patrick, this was a typical unit (slightly more concave, but within distribution)-Next Page


## Slide 12

**Lenovo Readiness**

- Reverse Hybrid Build / IdeaPad

- 6 Batches Run/2 Stencils: Lenovo IdeaPad / Qixia Project (Reverse Hybrid)

- Patrick’s Analysis of the prior page unit: 2DID: U346F14900081
- Per Patrick, this was a typical unit (slightly more concave, but within distribution)

- Part Within Distribution:


## Slide 13

**Lenovo Readiness**

- HoP SJ Found
- (per Yunfei)

- DOE Build on Feb 6, 24

- X-Ray Suspect HoP Failure.
- X/S Confirmed OK

- Reverse Hybrid Build/IdeaPad

- SMT Yield: 5/6 = 83.3%

- Unable to get the 2DID (Bing Confirmed)

- LNL-MX ES2
- Followed Intel MAS


## Slide 14

**Lenovo Readiness**

- Lenovo used “Proposal 2” stencil design, after experiencing NWO & SBB issues (prior builds)
- Lenovo built ~150 pcs with this stencil design, resulting in good yields
- Lenovo’s latest & greatest stencil design

- Lenovo’s Shangri-la/IdeaPad ES2 Build

- Reverse Hybrid Build


## Slide 15

**Lenovo Readiness**

- ATC Standard Test [-40 to +85C, 30 min cycle, 7.5 min soak, 7.5 min rise/fall time, ~16.6 C/min ramp rate] (resistance test): 1000 cycles Closed – Acceptable
- ATC Extended Test [Same conditions as above] 2000 cycles (Done) Closed – Minor crack found on solder joint but still in spec
- Hot storage test (125 Deg C x 600 hrs): Closed – No SJ issue found
- Mechanical Bending (resistance test):
- Without glue bonding, LNL-Mx ETB board could 100% pass 10K+ counts @ 450ue bending test
- With glue protection, LNL-Mx ETB board could 100% pass 100K counts @ 1000ue or 1200ue bending test

- Reliability Testing (Full LTS) – ThinkPad (First Wave/4CCSB)

- Daisy Chain/Buck Bay:

- Functional:
- - ATC test is run on functional boards for all Intel SKUs, every generation.
- Sample size 3-5 pieces.

- ATC Test performed with Lenovo’s glue applied


## Slide 16

**Lenovo Readiness**

- Accelerated Thermal Cycling (ATC): -40 to +85C, 30 min cycle, 7.5 min soak, 7.5 min rise/fall time, ~16.6 C/min ramp rate.
- No thermal solution attached during ATC test
- Pass/Fail Criteria: Take board out of chamber, send back to SMT line & put into board level functional test station. Perform standard board level functional test, total test time ~10+ minutes.
- This is the different with Dell/Compal case. For Dell/Compal, the engineer take board and manual assemble into product chassis to perform the test.
- FYI: Per Lenovo/Tony, they have a Thermal Shock Chamber, but it cannot control the ramp rate. The method is to spray liquid nitrogen into the chamber when needed to cool it down. Lenovo doesn’t perform Thermal Shock (TS) test for complex assembly like PCBA. They only perform TS for homogenous object, like Raw PCB, Resistor/Capacitor, Solder Joint only etc.

- Reliability Testing

- Intel asked Lenovo’s IdeaPad (consumer) team for their reliability testing plans, but declined to share.


## Slide 17

**Lenovo Readiness**

- Reliability Testing (Full LTS) – ThinkPad (Second Wave/8CCSB)

- Daisy Chain/Buck Bay:

- Functional:
- - ATC test is run on functional boards for all Intel SKUs, every generation.
- Sample size 3-5 pieces.

- ATC without glue, seeing cracks (up to 100%) early in corner NCTFs


## Slide 18

**Dell Readiness**


## Slide 19

**Dell Readiness**

- Sawtooth (Rugged) SBB Defects
- SMT Yield: 82/88=93% (Center SBB & 2 Corner Opens reported) -> Buckbay Parts

- SBB

- Sawtooth Daisy Chain board top layers (L1-L5) have Cu voided area under center of BGA footprint that appears to be an import from previous –Y sku design (using recess or hole in motherboard), possible source of convex reflow temp warpage due to Cu % imbalance.

- SMT Issues root caused to improper Dell test board design


## Slide 20

**Dell Readiness**

- General:
- Dell preparing Wistron & Compal
- Dell has communicated “great SMT yields” so far for Buck Bay & LNL-Mx using Reverse Hybrid process
- LNL-Mx Package Shape Noted:
- Center SJ’s=Bows up/stretched
- But Buck Bay is more compressed in center
- Corner SJ’s=Stretched
- Dell requested Intel’s help to find a 2nd Glue Supplier

- [Intel recommends 9 mil in center & no corner over-printing]

- Compal’s latest & greatest stencil design

- It’s common for Compal to add extra paste in BGA corners, as they typically see corners up during reflow. Bigger SJ’s also add strength.


## Slide 21

**Dell Readiness**

- Wistron’s latest & greatest stencil design


## Slide 22

**Dell Readiness**

- Reliability Testing (Mainstream)

- Mainstream:
- Zymet 2625B corner glue/thermal cure (projected)
- Thermal Shock: -40 to 85C; 40C ramp, up to 3K cycles (success criteria 1K cycles), 21 units. Functional Test in a system.
- Drop Test*: 20” drop to steel plate, 20 units.
- HALT*: Need more info from Dell on test conditions
- * Pre-test pre-condition:  storage @71C for 60 days + hot ops @ 63C for 60 days

- Dell performs initial testing on Daisy Chain Parts, then repeats testing when Functional (ES, QS) Silicon Available


## Slide 23

**Dell Readiness**

- Reliability Testing (Rugged)

- Dell’s Glue Requirements:
- Dell Mainstream = Corner Glue
- Dell Rugged = Corner + Edge Glue

- Key Finding: Running rugged storage test on daisy chain board (71C for 61 days, in oven). Measured unexpected decrease in daisy chain resistance. Issue root caused to crystallized flux residue, or foreign metal particle on the PCB, can short between DC test points and common ground.

- Rugged Tests follow
- MIL-STD-810


## Slide 24

**Dell Readiness**

- Reliability Testing (Rugged)

- Rugged:
- Zymet 2625B corner + edge glue/thermal cure (projected)
- Thermal Shock: -40 to 85C; 40C ramp, up to 3K cycles (success criteria 1K cycles), 14 units, Functional Test in a system.
- Drop Test*: 8 feet drop, 12 units
- Rugged Shock*: 10 units
- Rugged Vibe*: 10 units
- HALT*: 10 units
- Sequential (Micro drop 3K+ TS 46)*: 8 units
- * Pre-test pre-condition:  storage @71C for 60 days + hot ops @ 63C for 60 days

- Need more info from Dell on their rugged reliability tests

- Dell performs initial testing on Daisy Chain Parts, then repeats testing when Functional (ES, QS) Silicon Available


## Slide 25

**HP Readiness**


## Slide 26

**HP Readiness**

- LNL-Mx Readiness:
- Quanta & Inventec completed RH Evaluations - Phase 1 & 2.  Phase 3 (rework) is WIP.
- HP is currently meeting SMT yield targets for Functional LNL Regis platform!
- HP’s Pain Points:
- RH SJ voiding, provide BKMs to reduce as much as possible (Intel to help)
- Adoption/consistency of running Intel’s AI SJ void software @ 2-3 ODMs; and how to distinguish between via’s & voids? (Intel to help)
- Concern LNL pkg X-Ray dosage limit too low (20 RADs), now going lower (10 RADs)!! (Intel to help)
- Request to provide additional collaterals to help enable a 3rd ODM: “LNL Go Big Initiative” (Intel to help)
- Resolve the T=0 micro-crack issue, and why Intel tell them about this issue earlier, before HP’s ODMs found the issue (Intel to help)
- ODMs DnP process non-optimal for thin boards (board pads pull-out) (Intel provided a BKM) -> Quanta’s results have shown a vast improvement!
- Quanta’s x-ray equipment too old (needs replacement, looking at the Dage Quadra 7) (HP-Supplier Issue)


## Slide 27

**HP/Quanta RH Voiding**

- Intel Hypothesis: Extended soak at lower half of range is not activating much of the flux. Then, the quick ramp from ~170C to 220C is not allowing flux to dissipate before the paste hits liquidus and mixes with the LTS ball.
- Next Step: Adjust soak profile to between a 2:1 and 3:1 ratio spent 175-200C vs. 150-175C
- This guidance was shared with multiple ODMs & greatly improved their SJ void reductions for reverse hybrid.
- Dudi is working on further detailed RH profile optimizations. Help Needed: We need to share these learnings in the LNL-M MAS for all customers benefit!

- Pain Point: Quanta seeing increased SJ voiding with new RH process
- ~WW37’23 Quanta observed large voids on RH (>Full LTS), many in excess of desired 20% limit and others >30% IPC Class II limit
- Intel voiding measured smaller voids when using the same collaterals
- Comparison of SAC profiles and soak times, between Quanta & Intel, showed differences (ack: Jason)


## Slide 28

**HP/Inventec: T=0 Micro Crack Report**

- Qty=125 pieces SMT on Intel’s Buck Bay YTBs (OSP) IPN N27404-001, 0.6mm thick, using RH process. 3rd party supplier conducted D&P on 1 panel (1/6 locations showed SJ cracks “U4”):
- Issue Noted: Dye stain was detected in the outmost row of location U4.

- January 10th, 2024; Buck Bay DCTV (IPN M66590-003/8GB Samsung Memory)

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- Intel told customer, it’s likely a handling issue.  FYI: Add’n D&P and X/S will be done by the 3rd party supplier.

- Should have
- MD Pads in this
- region

- Cu Core Balls

- Type 2/51-75%

- Type 4/76-100%

- Type 4/76-100%

- Type 4/26-50%

- Type 4/1-25%

- Per Yunfei, this T2 crack may just be dye smearing

- Unit 2DID: D3YJ689700085


## Slide 29

**HP/Inventec: T=0 Micro Crack Report**

- Intel YTB Board Design

- January 10th, 2024; Buck Bay DCTV

- A1

- DL93

- DL1

- A93

- = Location of
- Micro-cracks
- From HP/Inventec


## Slide 30

**HP/Inventec: T=0 Micro Crack Report**

- Qty=125 pieces SMT on Intel’s Buck Bay YTBs (OSP) IPN N27404-001, 0.6mm thick, using RH process. 3rd party supplier conducted D&P on 1 panel (1/6 locations showed SJ cracks “U3”):
- Issue Noted: Inventec conducted 2nd round of D&P using a screwdriver. Dye stain was detected in the DL93 corner-most pad.

- January 23th, 2024; Buck Bay DCTV (IPN M66590-003/8GB Samsung Memory)

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- FYI: Cu Core Balls

- Type 2A (Middle of Solder Ball)/1-25%


## Slide 31

**HP/Inventec: T=0 Micro Crack Report**

- Intel YTB Board Design

- January 23rd, 2024; Buck Bay DCTV

- A1

- DL93

- DL1

- A93

- = Location of
- Micro-cracks
- From HP/Inventec


## Slide 32

**HP/Inventec: T=0 Micro Crack Report**

- 2nd round of T=0 Dye Stain was performed,
- 1 panel/4 DCTV’s having multiple cracks identified

- Feb 20th, 2024; Buck Bay DCTV (IPN TBD?/?GB ? Memory)

- Unit 2DID: TBD?

- DL93

- U1

- U2

- U3

- U4

- U5

- U6

- DL1

- A93

- A1

- DL93

- DL1

- A93

- A1

- DL93

- DL1

- A93

- A1

- DL93

- DL1

- A93

- A1

- DL93

- DL1

- A93

- A1

- DL93 & DL1 Corners

- DL1 Corner

- DL93, DL1 & A1 Corners

- All 4 Corners

- Type 3/1-25%

- Type 3/1-25%

- Type 4/
- 50-75%

- Type 3/25-50%

- Type 4/
- 50-75%

- Type 4/
- 25-50%


## Slide 33

**HP Readiness**

- Zymet 2625B corner glue/thermal cure (projected)
- PCA Level Tests: (3rd party lab to perform testing)
- PCA shock testing at room temp and elevated temperature
- Cyclic spherical bend testing (next page)
- System Level Rel Tests (Std notebook-level tests/SVTP):
- We are requiring more stringent versions of some of the mechanical system tests.
- *Initially test 3 LTS units.  If LTS units do not meet SVTP and/or exhibit solder joint damage in FA, apply more glue to 3 new units for every relevant test, and repeat that test.
- For any test of the MS or MD tests  where the tests do not pass OR if LTS BGA solder joint or partial pad cratering are seen in the failure analysis, more glue is required. Contact HP to determine the appropriate glue and glue usage.
- Extended stress testing/cumulative stress testing (e.g. includes thermal & current stressing, done in series on similar units, until MB failure)

- Reliability Testing

- Mechanical Shock Test Procedure
- Testing shall proceed as follows:
- Preconditioning for each test board shall be as follows: bake the boards at 60 °C for 24 hours, followed by at least 72 hours at room temperature, then place them into test within one week of preconditioning.  Baking shall be performed in air.
- Test 32 components for each combination of LTS paste alloy (if testing more than one) and adhesive solution, including controls
- Monitor daisy chain resistance during test in-situ.
- Test methods shall be one of the following:
- JEDEC JESD22-B111A (using test condition B per JESD22-B110B [1500 G, 0.5 ms duration, half-sine pulse]).  Test all boards until electrical failure.
- Cliff finding.  Determine the shock acceleration level that causes electrical opens during 6 drops, starting at 100g and increasing by 10g if no daisy chain opens are detected.


## Slide 34

**HP Readiness**

- Cyclic Spherical Bend Test Method (per Aileen Allen)
- Same test fixture as in Transient Spherical Bend (per IPC/JEDEC 9707), but done at temperature!!
- Sample size: 6 boards per test leg (plus validation boards to correlate displacement to strain)
- Test at 50 °C, 70 °C and 90 °C
- Evaluate the performance of the different glues and solder alloys in cyclic bend
- Load boards to 300 με diagonal strain (4 strain gage rosettes in 9704 recommended location on PCB adjacent to BGA), in a 3 Hz sine wave or clipped sine wave
- Monitor DC resistance in-situ
- Measure number of cycles until electrical failure
- FA to validate electrical failures

- Reliability Testing


## Slide 35

**Asustek Readiness**


## Slide 36

**Asustek Readiness**

- SMT Yield: 48/48=100% (But Voids >20 and >30% found)
- Buckbay RH build at Inventec
- Follow Intel’s solder stencil
- 2 pastes evaluated:
- -SHENMAO-PF606-P214
- -TAMURA TLF-204-93IVT (SH)
- Evaluated 9 solderball regions in x-ray for voids
- Provided Jason S RH Reflow Optimize Recomm for Void Reduction.

- Void Summary


## Slide 37

**Asustek Readiness**

- Pin 1 Corner NWO issue observed on LNL-Mx ES2 Product Build (Feb 2024) at INVENTEC, UX5306 Project
- Yield: 73/76 = 96.1%
- 8+8 GB Samsung Parts
- TAL 70-75 seconds
- Paste: TAMURA TLF-204-93IVT (SH)
- Following Intel’s stencil design
- 2DID for units with NWO’s:
- -U346F20800076, U346F20800293, U346F20800078
- Patrick’s analysis didn’t find anything unusual wrt pkg shape, and within the Distribution (next page)
- Intel recommended that Asustek tries Shenmao Paste


## Slide 38

**Asustek Readiness**

- Parts Within Distribution:

- Patrick’s Analysis, per the issue on the prior page
- 2DID for units with NWO’s:
- U346F20800076, U346F20800293, U346F20800078
- Patrick’s analysis didn’t find anything unusual wrt pkg shape, and within the Distribution


## Slide 39

**Asustek Readiness**

- Glue usage for LNL-Mx: Setiho SE8311, this is a local thermal cure glue supplier in China, they don’t have any plan to switch to Zymet (Inventec tested this glue).

- Reliability Testing

- 1) What reliability tests & conditions are you planning to run?
- Boot up  / Function / Aging
- 2) Are the tests run on daisy chain parts/boards or functional parts/boards?
- PCBA Test
- 3) What board thickness will be used for the tests?
- 0.65mm, 2-6-2 plus
- 4) Is the test run on bare boards, or run on bare boards with thermal solution attached, or run inside a fully populated system/chassis?
- PCBA with Dummy cooler
- 5) What is the quantity of units to run for each test?
- SR2 & SR3;  Over 20 PCS/State
- 6)What is the pass/fail criteria for each test?
- Boot up with no SMT issue


## Slide 40

**Microsoft Readiness**

- FYI: Hanna = Harper (Intel code name vs. the JDM1 code name that Surface uses).


## Slide 41

**Microsoft Readiness**

- 185/186=99.5% (1 SBB defect found)
- LNL ES1 Unit: 8+8 GB Samsung
- OSP board surface finish.
- 3 mil Stencil design = Follow Intel MAS
- Paste = Senju M705-S101HF(N4)-S5 (Type 5)
- Unable to get the 2DID (Bing Confirmed)
- Possible Pad Design Issue:
- Spoked MD pads appear more like SMD defined, higher risk for SBB. Need to open up the SROs, per MAS recommendations.

- SBB

- X-Ray Image

- Bare Board Image


## Slide 42

**Microsoft Readiness**

- 29/30 = 96.7% (1 HoP defect found in DnP)
- LNL ES1 Unit
- OSP board surface finish.
- Stencil = Follow Intel MAS
- S/N of HoP Unit: D3074AH001022.
- HoP Fail location = DE12.
- Paste = Senju M705-S101HF(N4)-S5 (Type 5)
- Patrick’s Analysis: The package has only a minor bend signature (~15um), not significant –>next page

- HoP

- A1 Corner


## Slide 43

**Microsoft Readiness**

- Patrick’s analysis of the defective unit from the prior page:
- S/N of HoP Unit: D3074AH001022.
- Patrick’s Analysis: The package has only a minor bend signature (~15um), not significant

- A1

- HoP


## Slide 44

**Microsoft/JDM1: T=0 Micro Crack Report**

- SMT, Harper DOE boards w/ ENIG SF, 0.85mm thick, Reverse Hybrid, UMT = Bd Supplier
- D&P discovered SJ cracks on SOC of DOE1-4, 1-5 and 7-5 samples (3 out of 6 total)

- January 5th, 2024; Lunar Lake-Mx, ES1 Samples

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- Microsoft’s “Mode 4/Type D” = Intel’s “Type 3 @ 76-100% area”


## Slide 45

**Microsoft/JDM1: T=0 Micro Crack Report**

- DOE1-4 Sample, DnP Results

- January 5th, 2024; Lunar Lake-Mx Engineering Samples

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- DOE1-5 Sample, DnP Results

- DOE7-5 Sample, DnP Results

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- Per Intel Input; ENIG has an elevated risk for T=0 micro crack health


## Slide 46

**Microsoft/JDM1: T=0 Micro Crack Report**

- DOE1-4 Sample, DnP Results

- January 5th, 2024; Lunar Lake-Mx Engineering Samples

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner


## Slide 47

**Microsoft/JDM1: T=0 Micro Crack Report**

- DOE1-5 Sample, DnP Results

- January 5th, 2024; Lunar Lake-Mx Engineering Samples

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner


## Slide 48

**Microsoft/JDM1: T=0 Micro Crack Report**

- DOE7-5 Sample, DnP Results

- January 5th, 2024; Lunar Lake-Mx Engineering Samples

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner


## Slide 49

**Microsoft/JDM1: T=0 Micro Crack Report**

- SMT, Harper DOE boards w/ ENIG SF, 0.85mm thick, Reverse Hybrid, UMT = Bd Supplier
- X/S discovered SJ cracks on SOC of DOE7-1, 7-2 and 7-3 samples (3 out of 3 total)

- January 5th, 2024; Lunar Lake-Mx Engineering Samples

- Microsoft’s “Mode 4/Type D” = Intel’s “Type 3 @ 76-100% area”

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner


## Slide 50

**Please refer to Microsoft’s X/S Report for the Cross-Sectional Images & Information**


## Slide 51

**Patrick’s Nardi’s / MCC Analysis**

- Total

- One unit is a bit on the convex side, but otherwise the shapes are all typical.
- These are all ES1 units.


## Slide 52

**Microsoft Readiness**

- Zymet 2625B corner glue/thermal cure (projected), to primarily protect against temperature cycling stresses (per John Godfrey) -> But JDM1 may be trying to save cost and push back on the glue requirement
- Temperature Cycling (-40C to 100C, TCT Test Profile) is their primary concern.
- Shock testing not as critical, because if a system drops the screens typically fail first, before the SOC

- Reliability Testing


## Slide 53

**Samsung Readiness**

- Samsung’s Readiness:
- They said they have “no critical issue on RH process we’ve done. We will keep monitoring the effect of voids.”
- No other SMT information provided


## Slide 54

**Samsung Readiness**

- Glue solution planned is corner underfilm (Preco-Miwa RP11317842).
- MX Standard Test Board used for reliability testing (based on JEDEC), with daisy chain samples mounted on it. Board thickness = 0.65mm.
- PKG verification is conducted with mechanical samples before starting a product development project. Functional samples are usually used for set level tests (power supplied).
- Thermal Shock Test (they call it “thermal shock” but really it isn’t): -40 to +85C, 40min/cycle, ramp rate up & down = 10C/minute, test takes ~10 days. Success Criteria: There should be no failures at least from 360 cycles. And we conduct Marginal evaluation for 500 cycles or more if it is necessary. We check DC after 7 days. After that, daily checking until marginal evaluation. Prefer sample size of 100 pcs. No thermal solution attached during testing.
- No TC test fails observed on LNL-Mx. In the case of Lunar lake-MX, only 20 pcs were used for each adhesive candidates (low temp. underfilm / underfilm / corner glue / underfill) because the PKG quantity was insufficient.
- Drop test: 1500G, 0.5m/s with corner underfilm.
- First LNL-Mx fail @ 166 drops, meets MX drop spec.

- Reliability Testing

- Samsung passed reliability tests: Thermal Shock & Drop Testing on LNL-Mx
- Samsung will continue to monitor the effects of voids on LNL-Mx


## Slide 55

**Acer Readiness**


## Slide 56

**Acer Readiness**

- Reliability Testing

- What reliability tests & conditions are you planning to run?
- Vibration test, high temperature and high humidity test, thermal shock test, then do X-ray, F/T, X-section and D&P
- Are the tests run on daisy chain parts/boards or functional parts/boards?
- No answer
- What board thickness will be used for the tests?
- No answer
- Is the test run on bare boards, or run on bare boards with thermal solution attached, or run inside a fully populated system/chassis?
- No answer
- What is the quantity of units to run for each test?
- Totally 14 Pcs for reliability test
- What is the pass/fail criteria for each test?
- Based on IPC standard
- 7) What adhesive make/model & application process is planned to be used on Intel’s SOC?
- Follow Intel Recommendations


## Slide 57

**Huaqin Readiness**

- Huaqin did not apply any glue after SMT for this build or for their sample rel testing


## Slide 58

**Huaqin: T=0 Micro Crack Report**

- Huaqin built Intel’s Buck Bay YTBs (OSP) IPN N27404-001, 0.6mm thick, using RH & Full LTS processes. T=0 D&P on 2 pcs RH & 2 pcs full LTS. All samples having all Type 3, T=0 micro-cracks. D&P was conducted AFTER YTB de-panel process (cutting it into 6 pieces).
- Reverse Hybrid D&P Results:

- January 19th, 2024; Buck Bay DCTV (IPN M66978-001/16GB Samsung Memory)

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- Reverse Hybrid, T=0
- Unit #1

- Type 3/76-100%
- PCB Side

- Type 3/0-25%
- PCB Side

- Type 3/0-25%
- PCB Side

- Reverse Hybrid, T=0
- Unit #2

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- Type 3/76-100%
- PCB Side

- Type 3/76-100%
- PCB Side

- Type 3/76-100%
- PCB Side

- Type 3/0-25%
- PCB Side

- Type 3/0-25%
- PCB Side

- Huaqin Next Steps: Customer temperature low, as they believe de-panel operation main cause.
- They plan to build 5-10 more YTBs, add dye stain, then de-panel, then perform D&P.


## Slide 59

**Huaqin: T=0 Micro Crack Report**

- Full LTS D&P Results:

- January 19th, 2024; Buck Bay DCTV

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- Full LTS, T=0 / Unit #1

- Type 3/76-100%
- PCB Side

- Type 3/0-25%
- PCB Side

- Type 3/0-25%
- PCB Side

- Full LTS, T=0 / Unit #2

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- Type 3/0-25%
- PCB Side

- Type 3/0-25%
- PCB Side


## Slide 60

**Huaqin: T=0 Micro Crack Report**

- RH & Full LTS X/S Results:

- January 19th, 2024; Buck Bay DCTV

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- X/S Summary:
- 2 pcs X/S from Reverse Hybrid
- -No cracks found in Cross Section
- 2 pcs X/S from Full LTS
- -1, 50-75% T3 crack identified,
- in either the DL93 or DL1 corner

- Type 3/50-75%

- This is the Cut line for this X/S
- Crack either found in the DL93 or DL1 corner (not clear from the image provided)

- Full LTS, T=0 / Unit #12


## Slide 61

**Huaqin: POST 85C/85% HUMIDITY Crack Report**

- Reverse Hybrid/AFTER 85/85 for 72 Hrs, D&P Results:

- January 19th, 2024; Buck Bay DCTV

- Reverse Hybrid, After 85/85 for 72 Hrs

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner


## Slide 62

**Huaqin: POST 85C/85% HUMIDITY Crack Report**

- Full LTS/AFTER 85/85 for 72 Hrs, D&P Results:

- January 19th, 2024; Buck Bay DCTV

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- Full LTS, AFTER 85C/85 Humidity for 72 Hours


## Slide 63

**Huaqin: POST REL/VIBRATION Crack Report**

- Huaqin built Intel’s Buck Bay YTBs (OSP) IPN N27404-001, 0.6mm thick, using RH & Full LTS processes.
- Rel Stress Run:  Reverse Hybrid + YTB/Vibration

- January 19th, 2024; Buck Bay DCTV (IPN M66978-001/16GB Samsung Memory)

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner

- Reverse Hybrid, Post Vibration


## Slide 64

**Huaqin: POST REL/VIBRATION Crack Report**

- Huaqin built Intel’s Buck Bay YTBs (OSP) IPN N27404-001, 0.6mm thick, using RH & Full LTS processes.
- Rel Stress Run:  Full LTS + YTB/Vibration

- January 19th, 2024; Buck Bay DCTV (IPN M66978-001/16GB Samsung Memory)

- Full LTS, Post Vibration

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner


## Slide 65

**Huaqin: POST REL/THERMAL CYCLE Crack Report**

- Huaqin built Intel’s Buck Bay YTBs (OSP) IPN N27404-001, 0.6mm thick, using RH & Full LTS processes.
- Rel Stress Run:  Reverse Hybrid + YTB/Thermal Cycle

- January 19th, 2024; Buck Bay DCTV (IPN M66978-001/16GB Samsung Memory)

- Reverse Hybrid, Post Thermal Cycle

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner


## Slide 66

**Huaqin: POST REL/THERMAL CYCLE Crack Report**

- Huaqin built Intel’s Buck Bay YTBs (OSP) IPN N27404-001, 0.6mm thick, using RH & Full LTS processes.
- Rel Stress Run:  Full LTS + YTB/Thermal Cycle

- January 19th, 2024; Buck Bay DCTV (IPN M66978-001/16GB Samsung Memory)

- Full LTS, Post Thermal Cycle

- A1 Corner

- DL93 Corner

- DL1 Corner

- A93 Corner


## Slide 67

**Huaqin Readiness**

- Reliability Testing Plans

- Glue Plans: They will build LNL-MX product for ASUS in May. Plan to use SYSCOTECH UV Glue SCT 219A. They previously used Loctite 3705, but now plan to switch to SYSCOTECH.
- High Temp & Humidity:  85C, 85%RH, 72-168 hours. Bare PCBA w/out thermal solution. Success Criteria: Pass D&P test (no SJ crack).
- Drop Test: Fully assembled system level test, from 45cm, 6 sides/4 corners. Success Criteria: Functional test & Pass D&P test (no SJ crack).
- Thermal Cycle: -40 to 85C, Ramp rate ~15C/minute, Dwell time 10-15 minutes, 100 cycles. Success Criteria: Functional test & Pass D&P test (no SJ crack).
- Vibration: All 3 axes, 1.04G RMS random 15 min/axis, 2~200Hz. Success Criteria: Functional test & Pass D&P test (no SJ crack).


## Slide 68

**Panasonic Readiness**


## Slide 69

**Panasonic Readiness**

- Reliability Testing

- As of Feb 27, 2024: Panasonic’s LNL-Mx Design Win is pending, so no rel. test plan available at this point.
- If a design win goes through, we will reach out to try and get their rel plans.


## Slide 70

