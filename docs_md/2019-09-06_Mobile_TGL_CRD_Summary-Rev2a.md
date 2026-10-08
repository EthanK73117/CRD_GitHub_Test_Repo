---
source_file: "2019-09-06_Mobile_TGL_CRD_Summary-Rev2a.pptx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (Mobile)/2019 Tiger Lake/2019-09-06_Mobile_TGL_CRD_Summary-Rev2a.pptx"
file_type: "pptx"
size_bytes: 4521980
content_hash: "6e7eb9e5a23a"
converted_at: "2026-10-08T11:29:44"
---

# 2019-09-06_Mobile_TGL_CRD_Summary-Rev2a

## Slide 1

**2019 TGL Customers CRD Summary Report**

- Prepared by:
- Harry Yu, SA Moy


## Slide 2

- 11/7/2019

- 2

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- General SMT Line Layout

- Solder Paste Inspection (SPI)

- Pre-Reflow Automated Optical Inspection (AOI) - Optional

- Post-Reflow Automated Optical Inspection (AOI)


## Slide 3

**Objectives**

- 11/7/2019

- 3

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Share Findings from CMEE Mobile Industry Data Collection (TGL platform customer survey) – 2019Q3 added wave 2 customers data
- Summarize data collected from the Mobile Customers manufacturers
- (TGL Wave1 target 5 ODMs):
- Quanta CQ (Hp Line)
- Inventec CQ (Hp Line)
- LCFC (Lenovo)
- JDM1 (MSFT)
- Compal KS (Dell Line)
- (TGL Wave2 target 7 ODMs):
- Compal CD (Dell Line)
- Compal CQ (Acer Line)
- Huaqin (Acer Line)
- MSI KS
- Pegatron CQ (Asus Line)
- Samsung Suzhou
- Wistron KS (Lenovo Line)


## Slide 4

**High Level Intel pkg design and validation requirement based on customer data (1/2)**

- 11/7/2019

- 4

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Continue use type 4 solder paste to do SMT cert: 9/11 customers still using type 4 paste 
- 4mil/5mil stencil thickness for UP3 package and 3mil/4mil for UP4 packages are the main stream, 5mil stencil still widely used because of other components requirement. 3mil for UP4 also emerged due to ultra small system design of customers 
- Keep stencil AR >0.66, 8/12 customers prefer >0.66 as their stencil design rule 
- >100~120mm print speed 
- Use machine block to support during print, only 3 customer capable for vacuum block 
- Panasonic is the main PnP machine vendor, Fuji the 2nd: 8/11 customer use Panasonic, 3/11 use Fuji 
- >=0.4mm pitch preferred, All customer capable for 0.4 pitch BGA 
- No pallet support during PnP, only support pins 


## Slide 5

**High Level Intel pkg design and validation requirement based on customer data (2/2)**

- 11/7/2019

- 5

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Most customer use 13 zones reflow oven 
- N2 <= 3000PPM, Air reflow still needed, Compal use 40,000 O2 PPM as their reflow environment 
- Belt speed 110~140cm/min preferred 
- >60s TAL. Some other component, for example black nickel coating type C connector, require longer TAL to form reliable solder joint 
- Almost all customer use Aluminum to fabricate their reflow pallet 
- Verify tape on board edge reflow, not all customer have spring clamps on their reflow pallet 
- No adhesive or UV corner glue, UV glue is more popular than other type of adhesive 
- Looks like QUICK is a popular rework station at ODM site 
- At least 2, prefer 3 LTS paste vendor is required 
- Nobody have thinner film pressure sensor capability in mfg site, all rely on their RD. We should minimize die crack risk in our package design 


## Slide 6

**SOLDER PASTE PRINT**

- 11/7/2019

- 6

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 7

- 11/7/2019

- 7

- SAC Solder Paste Formulation (Brand and Model)

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Type 4 paste still the main steam, except JDM1/MSFT
- Majority aligned with Intel MAS recommendation
- Compal introduced a new local brand paste (Yanktai), but not using it for Intel BGA

> **Speaker notes:**
> Put full name for compal KS - Done
> % of paste Inventec use? - Done
> % for compal - Done


## Slide 8

- 11/7/2019

- 8

- SAC Solder Paste Formulation (Brand and Model)

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Mobile/Client
- MAS:


## Slide 9

- 11/7/2019

- 9

- Printing machine/Stencil thickness/step stencil

- DEK/MPM still the Main stream
- GKG, A China branded print machine is starting used by ODM

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

> **Speaker notes:**
> Try to get the print model name.
> % of 4mil and 5mil? For future survey
> MSFT ask for 3mil for ICL U for modeling.


## Slide 10

- 11/7/2019

- 10

- Printing machine/Stencil thickness/step stencil

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Various products require various stencil thickness. 3mil for U package in customer wish list but not so many
- 01005 start be used in some premium product, 2 customers now capable
- 5mil for U still have needs because of other component requirement
- All customers except Huaqin are capable for step stencil

> **Speaker notes:**
> Try to get the print model name.
> % of 4mil and 5mil? For future survey
> MSFT ask for 3mil for ICL U for modeling.


## Slide 11

- 11/7/2019

- 11

- Stencil mfg process/Print process

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Some customer able to achieve lower AR
- High end customer are start using advanced stencil mfg process
- However, for big volume/low price customer (HP/Dell consumer), cost still a big concern
- Quanta said they didn’t feel Nano coating helps (Maybe vendor related), thus they’d rather use thinner stencil to keep the AR >=0.66 than use advanced stencil technology


## Slide 12

- 11/7/2019

- 12

- Stencil mfg process/Print process

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 13

- 11/7/2019

- 13

- Printing Support mechanism/Print machine handing size

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- JDM1 always use print pallet (whole process pallet)
- They use both pallet + support block to support PCB during print
- few customers are capable for vacuum block


## Slide 14

- 11/7/2019

- 14

- SPI machine

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 15

- 11/7/2019

- 15

- SPI machine

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- KOH YOUNG, TRI, Cyber Optic and Holly are common used SPI machine


## Slide 16

- 11/7/2019

- 16

- PNP

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 17

- 11/7/2019

- 17

- Pick and Place

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 18

- 11/7/2019

- 18

- Pick and Place

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Panasonic have the biggest market share, followed by Fuji


## Slide 19

**REFLOW**

- 11/7/2019

- 19

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 20

- 11/7/2019

- 20

- Reflow oven

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 21

- 11/7/2019

- 21

- Reflow profile

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 22

- 11/7/2019

- 22

- Reflow pallet

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 23

- 11/7/2019

- 23

- Reflow pallet

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Almost all customers are using Aluminum as pallet material
- Except JDM 1, who always use whole process pallet, other ODMs use reflow dedicate pallet (Use whole process pallet when needed in few cases)
- Quanta CQ and Inventec CQ developed automatic clamps process ( \\VMSPFSFSSH06\AsiaCQR_Data\Harry Yu\Videos\Inventec CQ reflow pallet auto clamp.mp4)


## Slide 24

**ADHESIVE**

- 11/7/2019

- 24

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 25

- 11/7/2019

- 25

- Adhesive

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Those blank cells have been surveyed previously, refer to CNL/ICL CRD at back up slide
- LCFC and JDM1 apply adhesive after FCT, other ODMs apply before ICT test
- ODM only do visual inspect after adhesive application, no deep validation on voiding, coverage, adhesion etc


## Slide 26

- 11/7/2019

- 26

- Adhesive

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Samsung start to remove the needs of under film, current ~70% of their product have no adhesive for Intel BGA. Only thin PCB project will use underfilm


## Slide 27

**REWORK**

- 11/7/2019

- 27

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 28

- 11/7/2019

- 28

- Rework

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 29

- 11/7/2019

- 29

- Rework

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- QUICK (4/9) and Shuttle Star (2/9) is top 1 and 2, only JDM1 use SRT
- BGA replacement circle time range between 5min to 35min


## Slide 30

**PCB**

- 11/7/2019

- 30

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 31

- 11/7/2019

- 31

- PCB

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 32

**LTS**

- 11/7/2019

- 32

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 33

**LTS**

- 11/7/2019

- 33

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- Among the 12 customers we surveyed, only LCFC in HVM, other customers either no reply those question, or reply based on their common sense or own study


## Slide 34

**LTS**

- 11/7/2019

- 34

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 35

**THERMAL MODULE ASSEMBLY/DISASSEMBLY**

- 11/7/2019

- 35

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 36

- 11/7/2019

- 36

- Thermal module assembly/disassembly

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary

- None of the ODMs have thin film pressure sensor capability and die crack risk evaluation procedure in their factory
- ODM RD at TW (or elsewhere) can do the measurement during thermal module design and provide assembly SOP to factory team


## Slide 37

**Back up**

- 11/7/2019

- 37

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2019 CRD Summary


## Slide 38

**Adhesive on Intel BGA**

- 11/7/2019

- 38

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2017 CRD Summary

- Adhesive questions that were recently asked during Cannon Lake Platform Introduction, in 2017:
- Previously we had not been asking                                           customers about adhesive usage


## Slide 39

**Adhesive on Intel BGA**

- 11/7/2019

- 39

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2017 CRD Summary

- Updated adhesive questions to be asked (Jan 2018) for a deeper understanding of adhesive usage across the ODM customer base:


## Slide 40

**Adhesive on Intel BGA**

- Pre-SMT Underfilm - Concept

- 11/7/2019

- 40

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2017 CRD Summary

- Corner “L-Shaped” Adhesive

- Corner Dot (Big or Small) Adhesive

- 1 Dot

- 3 Dots


## Slide 41

**Adhesive on Intel BGA**

- 11/7/2019

- 41

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2017 CRD Summary

- Corner Underfill (Lenovo Confidential)


## Slide 42

- 11/7/2019

- 42

- Adhesive on Intel BGA (Focused on Laptop & 2-in-1 Manufacturing)

- All major customers applying adhesive on Intel BGA except MSFT (adhesive decision is based on the reliability test results-to prevent SJ cracks)
- All major customers are applying adhesive after SMT but before FT test (to prevent SJ crack during FT test), except with the underfill process (it is hard to rework)
- Lenovo’s corner underfill covers a minimum of 5 solderballs in all 4 corners
- UV glue is more popular than thermal glue, due to less factory floor space & easy to cure
- *We know Samsung uses underfilm but the CMEE team did not visit them
- Top DT customers (Gigabyte & MSI) seldom add adhesive on Intel PCH (one exception: Asustek)

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2017 CRD Summary

- Note: Apple uses Dynamics 26663. Microsoft uses Zymet UA2605.


## Slide 43

**Corner Glue Video (HVM Factory)**

- 11/7/2019

- 43

- CMEE – Customer Manufacturing Enabling & Engineering / Intel Confidential / Collected Under NDA                                     Mobile 2017 CRD Summary

