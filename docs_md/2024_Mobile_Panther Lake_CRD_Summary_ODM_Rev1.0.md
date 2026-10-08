---
source_file: "2024_Mobile_Panther Lake_CRD_Summary_ODM_Rev1.0.pptx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (Mobile)/2024 Panther Lake CRD/2024_Mobile_Panther Lake_CRD_Summary_ODM_Rev1.0.pptx"
file_type: "pptx"
size_bytes: 17043054
content_hash: "a51eeca32c5d"
converted_at: "2026-10-08T11:29:45"
---

# 2024_Mobile_Panther Lake_CRD_Summary_ODM_Rev1.0

## Slide 1

**2024 Panther Lake CRD_ODM Summary Report**

- Rev1.0, CQ&R CMEE Team, 2024Q3

- Stop
- Customers confidential information under NDA, Intel internal use only


## Slide 2

**General SMT Line Layout**


## Slide 3

**Objectives**

- Data Collected From 11 ODM Customers/Sites
- Compal (Kunshan – Build for Dell/HP/Lenovo, Chengdu – Build for Dell, Chongqing – Build for Acer)
- Huaqin (Build for Huawei/Asus/Lenovo/Samsung)
- Inventec Chongqing (Build for HP/Asus)
- LCFC (Build for Lenovo)
- MSI KunShan (Own Brand)
- Pegatron (Suzhou - Build for Microsoft, Chongqing – Build for Asus)
- Quanta (Chongqing – Build for HP)
- Wistron Chongqing(Build for Lenovo)

- Share Findings From CMEE Mobile Industry Data Collection (Panther Lake Platform Customer Survey)


## Slide 4

**Agenda**

- Reliability Test
- Functional Test
- SMT Process & Rework
- Solder paste & Solder ball
- Equipment Related
- BFI Related
- Adhesive Related
- Others


## Slide 5

**Highlights**

- All customers perform TC/Shock/ Thermal Humidity test, but thermal test conditions were different
- Thunderbolt is the most difficult feature to test and causes most false failures. Most ODMs don’t know how to test AI.
- Most customers follow Intel MAS guidance for land pattern creation. Please make sure the reference board is consistent with the land pattern in MAS!
- Less than half ODMs use NCTF testable pin design for testing. Half of them prefer NCTF testable pins to be connected to GND plane. All ODMs hope to keep NCTF testable feature.
- Only Pegatron Suzhou used to use recycled Tin solder paste Senju M705R S101-N4, requested by MSFT. Reliability and cost are the main concern.
- Half customers hope Intel don’t remove solder paste recommendation in MAS, otherwise they have to qualified by themselves.
- TI uses SAC105, AMD uses SAC305, Qualcomm uses SAC405. Most customers concern on the soldering quality if Intel change SAC405 to SAC305 and will do some qualifications.
- Most customers don’t use dosimeter for X-ray exposure measurement.
- All customers apply adhesives to Intel BGAs except Pegatron Suzhou(MSFT ODM).


## Slide 6

**Reliability Test**


## Slide 7

**Reliability Test(1 Of 4)**

- All customers perform TC test, but thermal test conditions and sample size were different.


## Slide 8

**Reliability Test(2 Of 4)**

- Most customers perform shock test at system level, the test conditions were different. Some customers perform vibration test only.


## Slide 9

**Reliability Test(3 Of 4)**

- Most customers perform Thermal Humidity test, but test conditions were different.


## Slide 10

**Reliability Test(4 Of 4)**


## Slide 11

**Functional Test**


## Slide 12

**Functional Test(1 Of 3)**

- Most customers use ICT tester. Keysight is the most popular ICT tester, all customers have USB-based functional test.


## Slide 13

**Functional Test(2 Of 3)**

- Customer tested 1-6 times before thermal solution attach.
- Most customers use tray and lay flat when transport boards.


## Slide 14

**Functional Test(3 Of 3)**

- Thunderbolt is the most difficult feature to test and causes most false failures.
- Most ODMs don’t know how to test AI.


## Slide 15

**SMT Process & Rework**


## Slide 16

**SMT Process & Rework(1 Of 6)**

- All customers follow Intel MAS adhesive KOZ, but the requirement for rework is different, range from 1 mm to 2 mm.
- Most customers follow Intel land pattern guidance by referring to Intel reference board. Thus, it is critical to make sure the reference board is consistent with the land pattern in MAS!


## Slide 17

**SMT Process & Rework(2 Of 6)**

- Most customers use OSP board and reflow pallet.
- Few ODMs have experience on placing small passive parts underneath a taller SMT parts.
- Q2 PPM range from 1000 PPM to 4000 PPM.


## Slide 18

**SMT Process & Rework(3 Of 6)**

- Less than half ODMs use NCTF testable pin design for testing. Half of them prefer NCTF testable pins to be connected to GND plane.


## Slide 19

**SMT Process & Rework(4 Of 6)**

- All ODMs think it is nice to keep NCTF testable feature.


## Slide 20

**SMT Process & Rework(5 Of 6)**

- All customers prefer mini-stencil to rework, only Compal KS has paste jetting machine and minimum KOZ is 2 mm.


## Slide 21

**SMT Process & Rework(6 Of 6)**

- Most customers use Aluminum or Synthetic stone to make pallets. And manual remove is the most popular way to remove the solder paste residues.


## Slide 22

**Solder paste & Solder ball**


## Slide 23

**Solder paste & Solder ball (1 Of 4)**

- Only Pegatron Suzhou used to use recycled Tin solder paste Senju M705R S101-N4, requested by MSFT. Reliability and cost are the main concerns.


## Slide 24

**Solder paste & Solder ball (2 Of 4)**

- Half customers hope Intel don’t remove solder paste recommendation in MAS, otherwise they have to qualified by themselves. Others follow OEM’s request.


## Slide 25

**Solder paste & Solder ball (3 Of 4)**

- TI uses SAC105, AMD uses SAC305, Qualcomm uses SAC405. Most customers worry about the soldering quality and reliability if Intel change SAC405 to SAC305 and will do some qualifications.


## Slide 26

**Solder paste & Solder ball (4 Of 4)**

- Most customers follow 30% spec to inspect void size, except Quanta and Wistron. Half customers used to find void >30%. Adjust the profile and stencil is the most popular actions if they find void >30%.


## Slide 27

**Equipment Related**


## Slide 28

**Equipment Related(1 Of 4)**

- All customers use MXI for FA, rework, process set-up. The Voltage and Power settings are different, since different machines were used. Inspection time range from 1 min to 5 min.


## Slide 29

**Equipment Related(2 Of 4)**

- Most customers don’t have any experience on dosimeter for X-ray exposure measurement. Only Wistron have issues with inspecting the package with the package facing away from the X-ray source.


## Slide 30

**Equipment Related(3 Of 4)**


## Slide 31

**Equipment Related(4 Of 4)**


## Slide 32

**BFI Related**


## Slide 33

**BFI Related(1 Of 4)**

- Different customers have different BFI strain spec.


## Slide 34

**BFI Related(2 Of 4)**

- All customers collect some solder joint FA data(DnP, XS, X-Ray ) after board assembly, test, and handling steps.


## Slide 35

**BFI Related(3 Of 4)**

- Intel BGA is the largest BGA that most customers can handle. Test fixture design and handling is the main concern if packages grow larger. Few customers willing to share BFI data.


## Slide 36

**BFI Related(4 Of 4)**

- For shock board strain, most ODMs didn’t reply. Please refer OEM’s report for more information.


## Slide 37

**Adhesive Related**


## Slide 38

**Adhesive Related(1 Of 10)**

- Most ODMs apply glue after reflow. Corner glue is the most popular adhesive application.


## Slide 39

**Adhesive Related(2 Of 10)**

- UV glue is more popular than thermal glue. Most ODMs use Jetting method to dispense adhesive.


## Slide 40

**Adhesive Related(3 Of 10)**

- GKG is the most popular equipment for dispensing and curing.


## Slide 41

**Adhesive Related(4 Of 10)**

- All customers use automated to apply adhesive. Manual application is only for rework. HVM adhesives lines is 1:1 with SMT lines, except Pegatron Suzhou(MSFT ODM).


## Slide 42

**Adhesive Related(5 Of 10)**

- Different customers have different preference on adhesive. UV glue is more popular than thermally cured glue.


## Slide 43

**Adhesive Related(6 Of 10)**

- All customers apply adhesives to Intel BGAs except Pegatron Suzhou(MSFT ODM).


## Slide 44

**Adhesive Related(7 Of 10)**

- All customers don’t perform compatibility testing between solder flux residue and adhesive.


## Slide 45

**Adhesive Related(8 Of 10)**

- All customers perform after-cure quality validation. Only Compal CD uses scanning calorimetry to check validation after-cure quality.


## Slide 46

**Adhesive Related(9 Of 10)**

- Different ODMs have different dispense time requirement and cure time requirement. All ODMs use hot air gun and tweezer to manual remove the adhesive.


## Slide 47

**Adhesive Related(10 Of 10)**

- All customers apply adhesive to non-Intel components, like GPU, DRAM, PCH, etc. Customers thought applying adhesives will increase thermal margin capability.


## Slide 48

**Others**


## Slide 49

**Others**


## Slide 50

**Customer Recognition to Intel MAS Recommendation**

- During F2F meeting with ODM customers, customers appreciated Intel’s MAS recommendations. They understand Intel team had done huge amount of work to figure out those recommendations, which help customers ramp Intel products more smoothly compared to our competitors.


## Slide 51


## Slide 52

**Back Up – Images of transport boards**

- Inventec CQ

- Compal CD

- MSI

- Compal KS


## Slide 53

**Back Up – Dosimeter**

- Quanta

- Pega SZ

- Inventec CQ


## Slide 54

**Back Up –LCFC ICT Equipment**

