---
source_file: "2020_06-29_EHL_MAS_And_Adhesive_Survey_Summary-Moy Updated.pptx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/IoTG/EHL Adhesive and SJR Survey/2020_06-29_EHL_MAS_And_Adhesive_Survey_Summary-Moy Updated.pptx"
file_type: "pptx"
size_bytes: 2816409
content_hash: "a883a4aaaefb"
converted_at: "2026-10-08T11:29:40"
---

# 2020_06-29_EHL_MAS_And_Adhesive_Survey_Summary-Moy Updated

## Slide 1

- Date: WW26’20

- Intel Confidential and Customer Confidential Information
- Never Share Outside of Intel

- EHL MAS and Adhesive Survey Update


## Slide 2

- 2

- Customer List:
- APAC:
- Advantech – Phase 1
- Adlink – Phase 1
- IEI - TEP
- Aaeon – Phase 1
- EMEA:
- SECO - TEP
- Congatech - TEP
- MSC – Phase 1
- Siemens (just email) - TEP

- Summary:
- Medium Risk: Pending to know customers reliability data and their final decision for corner glue application by end of June. QS will be WW36/38.
- Medium Risk: Potential schedule impact if required board design change and add KOZ for corner glue application after knowing reliability testing result.
- Options:
- Fab spin, potential schedule impact.
- Applying corner glue with make sure encapsulate adjacent passive part. This is a workaround solution but not so manufacturing friendly process.
- IoTG customers define product reliability based on whole system functionality and not focus on SJR.
- Opportunity to train IoTG customers about what is SJR during IPTS (Nov/Dec 2020).
- Adhesive is not a common process for IoTG customers. Customers may have some adhesive experience but depending on request either from OEM customers / R&D team.
- No EHL SMT yield issue encountered with limited samples build. Customers are well aware about stencil design recommendation in MAS.
- Legal: If customers don’t follow the MAS recommendation, a disclaimer on MAS is able to protect Intel and avoid compensation if any SJR issue related happen in future.

- EHL MAS and Adhesive Survey Update

- Risk Level:
- Medium


## Slide 3

- 3

- Next Steps:
- To ping all remaining TEP & Phase 1 Customers, ask these questions (due date June 26th)
- Based on the corner glue recommendation in the EHL MAS & TMDG, do you have any plans to add corner glue on the EHL package? (Expected Response: “Yes”, “No” or “Pending”)
- If answered “No”: No further information is needed from the customer.
- If answered "Yes": Are you working with a local corner glue vendor to help your factory add corner glue on the EHL package?
- If answered "Yes": Do you need any additional help from Intel's Enabling Team to add corner glue on the EHL package?
- If answered "Pending": By when and with what data is needed to make the EHL corner glue decision?
- EHL Temperature Cycle data review by August.

- Proactive Proposal Long Term Collaboration:
- Request customers EHL boards for temperature cycle testing. Preferred to use QS samples.
- Customers SJR risk assessment with using TCx profile.

- Bin
- Reason: More critical is to know what is customer true requirement


## Slide 4

**EHL Adhesives Guidance**

- 4

- Intel recommends the use of corner glue (CG) for Elkhart Lake for certain product use cases. The below chart is a guideline for temperature cycle risk based on solder ball temperature and power cycles.
- If your product falls above the “Product Capability” line, CG may be advisable to increase the capability of the package solder joints. For more information and manufacturing guidance, please see the documents titled “Manufacturing with the Intel Platform Code Named Elkhart Lake” (RDC #621789) and “Manufacturing with Intel Products Adhesive Guidance for Ball Grid Array and Package on Package” (RDC #573768).

- Tsb Guidelines:
- Tsb (Temperature at solder ball) is dependent on silicon  junction temperature as well as the heat dissipation of the thermal solution. The below ranges are a general guideline for determining Tsb range without having a full system thermal model available.
- High Tsb: E.x.: passive metal heat sink with no air flow, closed chassis
- Medium Tsb: E.x.: heavy heat sink with some air circulation (i.e.: vented chassis)
- Low Tsb: E.x.: heavy desktop-like heat sink with forced air flow (i.e.: integrated fan )

- Intel recommends that all customers perform their own reliability evaluation to make sure that the product meets their expected requirements based on their own methodology.

- Low


## Slide 5

**Assumptions/Definitions**

- 5

- Power cycle
- On to off cycle (assuming cooling down to ambient temperature when off)
- On to standby cycle (assuming cooling nearly to ambient when in standby)
- Ambient temperature
- Temperature external to system (room temperature)
- Assumed to be 24 C
- The given product temperature cycle risk was calculated assuming a minimum 1.6 mm board with a 15 lbf load and no backing plate. Changes in board thickness, loading, or presence of a backing plate can affect temperature cycle risk


## Slide 6


## Slide 7

- 7


## Slide 8

- 8


## Slide 9

**EHL Customer List**

- 9


## Slide 10

**Content:**

- 10

- Customer’s Surveyed -> IOTG Sales Volume
- Survey Summary Information
- Market Segment, Power Cycles & Temp Conditions
- Board Level Temperature (TC) Testing
- Adhesive Usage


## Slide 11

**Customer Survey IOTG Sales Volume**

- 11

- IOTG Sales Volume on Apollo Lake, Gemini Lake & Valley View:

- This Customer Survey represents ~18% of IOTG Sales Volume on APL, Gemini Lake & Valleyview

- This Customer Survey represents ~52% (14/27) of the EHL TEP & Phase 1 Customers


## Slide 12

**Survey Summary Information (Page 1 of 2)**

- 12

- EHL Customers Surveyed

- 14 Total Customers Surveyed. 12 Customers have responded, working on 2 more responses.


## Slide 13

**Survey Summary Information (Page 2 of 2)**

- 13

- Product Power Cycles
- Range of Industrial # power cycles (on to off) is 0 to 4 cycles per day
- Range of PC Client # power cycles (on to off) is 1 cycles per day
- Range of Industrial # power cycles (active-to-standby) is 0 to 20 cycles per day
- Range of PC Client # power cycles (active-to-standby) is 5 cycles per day
- Product Temperature Conditions
- Range of standby/idle temp of Intel SOC: -40°C to 100°C
- Range of active temp of the Intel SOC: -40°C to 105°C
- Range of ambient of system location: -40°C to 100°C
- Board Level Temperature Cycling (TC) Testing
- Range of Board thicknesses:  1.2mm (47mils), 1.4mm (55mils), 1.6mm (62mils), 2.0-2.4mm (79-94mils)
- 4 Customers appear to run an Accelerated SJR TC Test like Intel
- Congatec: Require 1850 cycles for a 10 year life (185 cycles per year)
- Hitachi: Require 545-1250 cycles, unloaded test, -55°C to 125°C [IOTG believes they have high rqmt’s]
- Omron: Require 1000 cycles, -40°C to 100°C [IOTG believes they have high rqmt’s]
- Siemens: Require 1000 cycles, loaded test, -40°C to 125°C
- 8 Customers – we are unsure if they perform an Accelerated SJR TC Test like Intel
- The testing they perform looks more like a factory infant mortality or ‘power cycling’ test, tests related more for performance & functionality. Need to clarify with these customers
- Adhesive Usage
- 4 customers have some type of board level adhesive experience & setup (but may not be for BGAs or using thermal cured adhesives)
- 8 customers don’t have any board level adhesive experience


## Slide 14

**Market Segment, Power Cycles & Temp Conditions (Page 1 of 2)**

- 14


## Slide 15

**Market Segment, Power Cycles & Temp Conditions (Page 2 of 2)**

- 15


## Slide 16

**Board Level Temperature Cycling (TC) Testing (Page 1 of 4)**

- 16


## Slide 17

**Board Level Temperature Cycling (TC) Testing (Page 2 of 4)**

- 17

- They appear to run an Accelerated SJR TC Test

- They appear to run an Accelerated SJR TC Test


## Slide 18

**Board Level Temperature Cycling (TC) Testing (Page 3 of 4)**

- 18

- They appear to run an Accelerated SJR TC Test

- They appear to run an Accelerated SJR TC Test

- Need to clarify with the customer


## Slide 19

**Board Level Temperature Cycling (TC) Testing (Page 4 of 4)**

- 19

- Need to clarify with the customer

- Need to clarify with the customer

- Need to clarify with the customer


## Slide 20

**Adhesive Usage (Page 1 of 1)**

- 20


## Slide 21

**Backup**

- 21


## Slide 22

**Blank Survey Info**

- 22


## Slide 23

**Enabled Temp Cycle Primer**

- 23

- What is temperature cycling? How does it compare to power cycle?
- In a power cycle test, the package is mounted on a board and is heated internally in a cyclic manner to generate thermal stresses. In temperature cycle, the package is mounted on a board which is placed in a chamber, and the temperature of the chamber is cycled to generate thermal stresses. In a temperature cycle test, the packages are in the “off” state as they are not functional. Intel does temperature cycling instead of power cycling because the setup is easier and it is easier to control the conditions. In power cycling the temperature distribution is not uniform and it is difficult to know the temperatures during power cycle at different locations.
- What is the TCX profile?
- TCX is a thermal cycling profile ranging from -40 to 85 C over a 60 minute cycle. There are other profiles (TCN, TCT, TCB) that cover different temperature ranges and may be used for different applications. Customers should be familiar with TCX (based on guidance from IOTG).
- How many years does the 1000 TCX capability represent?
- The 1000 cycles TCX is an industry standard for client-mobile products, and for those products, represents 5 years lifespan. However, desktop, industrial, and EBM products have very different use conditions, so this may not represent 5 years in any of these market segments. Intel recommends that customers evaluate their own reliability requirement based on use conditions and product configuration to determine if 1000 cycles TCX is sufficient for their expected lifespan.


## Slide 24

**Enabled (or) Non-enabled Temperature Cycle Primer**

- 24

- TCX (Temperature Cycling – X) Profile Specifications:

- +85°C

- -40°C

- 0°C

- Time (minutes)

- Dwell Time [Maximum/Hot] (17 min)

- Dwell Time
- [Minimum/Cold] (17 min)

- Ramp Rate
- (10°C/min)

- Cycle Time (60 min)

- Example TC-X Profile:

- Note:
- Enabled Temperature Cycle means the DUT is subjected to a constant load simulating the presence of a heatsink or thermal solution during the course of the testing.
- Non-enabled Temperature Cycle means the DUT is NOT subjected to a constant load simulating the presence of a heatsink or thermal solution during the course of the testing.
- This example plot is just one implementation of the table parameters (above)

- Min = Minutes

