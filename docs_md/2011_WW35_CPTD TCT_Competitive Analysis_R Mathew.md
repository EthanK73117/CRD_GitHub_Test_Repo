---
source_file: "2011_WW35_CPTD TCT_Competitive Analysis_R Mathew.pptx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (Mobile)/2011 Shark Bay/2011_WW35_CPTD TCT_Competitive Analysis_R Mathew.pptx"
file_type: "pptx"
size_bytes: 22666102
content_hash: "49e062ee3247"
converted_at: "2026-10-08T11:29:41"
---

# 2011_WW35_CPTD TCT_Competitive Analysis_R Mathew

## Slide 1

**CPTD TCTCompetitive Analysis Key Messages Prepared by R.Mathew WW36/11**

- Contributors : DMIA team


## Slide 2

- Key Messages


## Slide 3

- Board Adhesive Strategy by Segment in DMIA Client Mobile studied

- Corner Glue widely adopted on Client Mobile Notebooks, excepting Samsung .


## Slide 4

- 4

- HP Dv 6 Cougarpoint with Corner Glue

- HP Dv 6 AMD FCH with Corner Glue

- Corner Glue in AMD Llano vs Intel SNB Platforms

- HP is using corner glue on both DV6 platforms  , regardless of AMD or Intel CPU /chipset


## Slide 5

- 5

- AMD Hudson chipset ( for AMD Llano )
- Gateway  NV55SO5u  15 inch

- Different OEM’s are using 2  glue dots per corner

- Corner Glue dot dispense examples

- AMD Zacate
- Acer Aspire ( P5WEG) 15” Notebook


## Slide 6

- Design Methods and Industry Analysis

- AMD Mobile Hudson FCH footprint and NCTF vs Cougar Point Mobile

- VSS

- FCH  Hudson
- 640 b, 24.5X24.5mm
- 0.8mm   ball pitch
- 1 NCTF per corner
- No corner depop/ physical test KOZ
- No die shadow NCTF trends with 45 deg die orientation

- Cougar Point  Mobile

- Cougar Point Mobile
- 989 b, 25X25mm.
- 0.6mm   ball pitch
- 8 NCTF per corner
- 2 corner depop
- No die shadow NCTF


## Slide 7

- 7

- Samsung Series 9

- No corner glue evident for either CPU or chipset
- 8 lyr 950 um single sided Type 3 board

- SNB core i5              ( 2+2)

- Cougar Point Mobile  PCH


## Slide 8

- Board Adhesive Strategy by Segment in DMIA Netbook/Tablet/Ultramobile systems studied

- BLUF prevalent in Smartphones , excepting Nokia
- Board level adhesives not used consistently in Tablets and Netbooks.


## Slide 9

**BACKUP**

- 8/22/2011

- 9


## Slide 10

- Design Methods and Industry Analysis

- Board Level Underfill ( BLUF ) and Corner Glue for mechanical shock protection

- Corner glue on Geneva
- in HP Pavilion  dm3Z

- BLUF seen on Apple A4 POP Pkg


## Slide 11

- 11

- 100% useage on Calpella platforms sampled
- Increasing conversion of BGA CPU to Corner Glue

- Corner Glue application prevalence is 100% in Calpella platforms sampled

- Extract / Glue Usage Trends on Mobile Platforms / Santi Rodriguez et al / WW40

- Client Mobile Corner Glue Scan


## Slide 12

- 12

- Notebook Volumes

- Carlos Morales / MPG Finance


## Slide 13

- List of current corner glue materials in Client Mobile platforms
- ( includes observations from Santi Rodriguez Calpella platform reports)

- Mike Kochanowski/ Eric Brigham / WW19

- Properties completed as available


## Slide 14


## Slide 15

- Design Methods and Industry Analysis

- AMD Client vs Intel NCTF Example

- AMD Zacate has “zero” NCTF’s vs ~ 28 NCTF’s in Cedarview


## Slide 16

- TI OMAP 4430 Pin Map and NCTF’s

- 3 NCTF’s per corner ( vs 4 per corner for Penwell )
- 12X12mm, 0.4mm pitch

- Mark Jamieson/ Rudy Ramirez / WW23

- RIM Playbook used TI OMAP 4430 without any BLUF with this ball map & NCTF pattern


## Slide 17

- 17

- 17

- Geneva

- Nvidia
- MCP89

- AMD SB

- AMD NB

- Intel Estimate
- no Corner Glue Passes Shock + Temp Cycle

- Competitive Mobile BGA Corner NCTF

- Min Number of Corner NCTF Assignments

- Body  Size   ( X = Y mm )

- Observed Comp. Corner NCTF

- Estimated NCTF required to meet Intel shock spec
- (62mil MBL board @150G

- Intel DR’s would require 3-4 additional corner NCTF balls
- Competition is equivalent to Intel corner glue requirements

- Ack : Prasanna Raghavan

- Intel Estimate
- with Corner Glue


## Slide 18

- 8/22/2011

- 18

- Geneva Motherboard footprint with approx Pkg/Die outline and  key Electrical NCTF/CTF locations

- == SMD VSS

- == MD VSS

- == MD VCC

- = MD
- NOT VSS
- NOR VCC

- Corner glue on Geneva
- in HP Pavilion  dm3Z

- Geneva uses ~2 corner ball NCTF assignments with CTF assignments in die shadow .


## Slide 19

- Geneva CPU A1 Package Corner View

- All package pads appear to be uniform SMD and 500 mil chamfered square pads


## Slide 20

- Geneva CPU motherboard A1 Corner

- 2 Corner NCTF balls are SMD
- 3 Pad opening sizes with mix of MD/SMD
- Largest opening at corner ~ 520 um on CTF
- Outer edge ~ 420 um on NCTF
- Inner area ~ 320um CTF

- Corner SMD NCTF openings connected to VSS bus  with inward thicker traces

- Approx Corner Glue location

- SMD to common plane

- Corner pads are Via-Off Pad ( VOP )


## Slide 21

**Zacate Vs Cedarview – Rel Capabilities**

- ASSUMPTIONS :
- Pineview data (shock/TCQ) and modeling utilized to make projections for Cedarview.
- Glue predictions are based on learnings from uSFF platform (Glue - L3519).
- Based on past modeling learning's, projections are made for AMD Zacate’s package.

- Performance will be glue material dependent

- Cedarview has 7 nCTFs in all 4 corners.
- Limiting cases for reliability – 62 mil for shock, 40 mil for enabled TC that impacts corner nCTFs

- Prasanna Raghavan / WW09


## Slide 22

- 22

- Adapted from Surinder Tuli / WW07/11  LCIA/Tablets  Key Messages

- Dual nVIDIA Tegra 2 Package offerings

- Note : 1) Viewsonic tablet did not use corner glue or BLUF with Type 3 boards
- 2) Nvidia offers 2 package outlines with the same silicon to support LDI or HDI boards.

- LDI

- HDI


## Slide 23

**TI  3430 POP Published Mechanical Drawing**

- 8/22/2011

- 23

- TI offers three package options for their OMAP
- 12x12mm PoP -0.4mm pitch 515 lead (CBB)
- 14x14 mm PoP – 0.5mm pitch, 515 lead (CBC)
- 15x15mm MMAP  - 0.65mm pitch, 423 lead (CUS)

- Adapted from TI OMAP 3430 12X12mm POP / Palm Pre
- report / Mark Jamieson /


## Slide 24

- MacBook Air GPU vs Samsung Series 9 PCH section comparison

- Single sided motherboard design in Samsung allows taller component + thermal enabling assemblies on board topside compared to Macbook Air .

- Tapered profile reduces from 17 to ~ 12mm

- 16.3 mm flat profile


## Slide 25

**Tablet Platform Thickness Drivers & Trends**

- Implementation of a single sided SMT motherboard in the iPad 2 enabled much of
- the reduction in thickness relative to the iPad 1
- Reduction in display thickness accounted for the remaining improvement

- iPad 1

- iPad 2

- 8.6 mm

- 5.90 mm

- Single sided motherboards will likely be a standard element of
- future tablet designs

- 12.8 mm

- 2.59 mm*

- Display

- CPU

- Board

- Case

- * The thickness of the iPad 2 battery = 2.60 mm

- Mark Jaimieson/ WW34 ATTPM  extract


## Slide 26

- TI OMAP 5432 Client/ Mobile and 5430 Smartphone Dual SOC Options

- Potential ARM based product targeted to Client mobile platform in a 17X17mm , 0.5mm depopulated pitch BGA


## Slide 27

- BGA SLI Scan

- 0.8 to 1.0 mm Balls anywhere with Type 3 motherboards in effect for Client/Server /GPU and netbook BGA
- Tablets have 0.5 to 0.8mm BGA’s that support both Type 3 and Type 4 .
- 0.4 to 0.65 mm fixed pitch packages used on Type 4 / HDI  ultramobile/smartphone boards.

- OEM’s use Corner glue for Mobile BGA’s

- BLUF seen on  65nm and 45nm Tablets and Ultra-mobile  POP products
- Netbooks use corner glue

- Design Methods and Industry Analysis

