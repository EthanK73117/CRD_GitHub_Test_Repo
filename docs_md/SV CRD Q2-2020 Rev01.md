---
source_file: "SV CRD Q2-2020 Rev01.pdf"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Server/2020/SV CRD Q2-2020 Rev01.pdf"
file_type: "pdf"
size_bytes: 745971
content_hash: "85fcfce7983f"
converted_at: "2026-10-08T11:29:02"
---

# SV CRD Q2-2020 Rev01

## Page 1

CONFIDENTIAL
Contained customer process
information under NDA
Eagle stream ODMs CRD survey Report
(server segment)
Customer participated :
Inventec (SH & TW), Wistron ZS, Quanta (SH & TW), Foxconn TJ, Pegatron TW
20ww32 Rev 1
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only

## Page 2

Agenda
❖ Server Customer Manufacturing
❖ PCBA Material / Consumables
– Technology & Process
❖ PCBA Machine / Equipment
– Process Parameter & Capability
• Paste Print, PnP, Reflow, Wave Solder, Rework, Inspection (SPI, AOI)
❖ Others & Automation
– PHM Assembly, Manufacturing Test, System Integration
❖ Key Takeaway
❖ Next Step
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 2

## Page 3

Server Manufacturing Level & Customer Landscape
Enterprise Customer : Dell, HP, Lenovo
CSPCustomer : FB, Amazon, MSFT,Google
ODM ODM Sys OxMSys
(Board) Integration Integration
PCBA &
Board
assembly
Level Description
L6 Board
L6 Integrationofmotherboardintochassisenclosureandpowerontest.
L10 Fullassemblyofserverwithfullsystemandcomponentlevel
testing,OS/softwareintegration,productkittedwithusermanualand
other required. Documentation and delivered as a fully-integrated
L10 System L10 System L10 System
serversolution.
L11 Node-level assembly, testing, OS/software loading of all server
nodes followed by rack cabinet assembly of nodes into racks with
L11/L12
System full cable networking (including switches), and tested as a working
totalsolutionattherackormultiracklevel.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 3

## Page 4

PCBA Material / Consumables
Data Source:
Server ODMs
Material Inventec Quanta Foxconn TJ WistronZS Pegatron TW
Foxconn; 深精藝-
Iden
Stencil Local supplier Local supplier SHENJINGYI; 蒙瑞- Local supplier
Win-laser
MENG RUI
Hannstar, Boardtek,
PCB Local supplier Gold Circuit, Tripod, ISU GCE; BTK; Tripod ACCL, GCE, Compeq
GCE
ALPHA OM338PT ShenmaoPF606-P
Solder Paste ShenmaoPF606-P ShenmaoPF606-F
ShenmaoPF606-P Senju M705-S101HF- SMIC M705-
(SMT) ShenmaoPF606-P245 Henkel GC-10
S4 S101HF(N6)-S5
Conceptronic/ SRT 1100LX, 2200LX
Rework Not provided SRT/Summit 1800 SUMMIT-Lxi
Feedom2000
Paste/Flux ShenmaoPF606-P
Not provided Alpha OM338PT ShenmaoSMF-2 Not provided
(Rework) ShenmaoPF606-P245
ShenmaoSM816,
Flux
ShenmaoSM816 ShenmaoSM816 Not provided AlphametalEF- ShenmaoSM-827
(Wave solder)
6808HF
KeyMessage:
• PreferStencillocal vendors forfast response, delivery time &on-site support.
• Wavesolderprocess isstill requiredfor thru-hole components.
• Shenmao paste/fluxiscommonly usedexceptFoxconn.
o Shenmao paste is generally used during early development; will be used as back-up during mass
production (MP).
o Alternate solder paste ismandatory forSMTper theircustomer requirement.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 4

## Page 5

PCBA Material / Consumables & Technology
Data Source:
Server ODMs
Material Technology Inventec Quanta Foxconn TJ Wistron ZS Pegatron TW
electroform, laser cut
laser cut + Laser cut with Laser cut with
Cut / Coating Laser cut with electro polish +
nano coat electro polished etching
nano coat
Stencil Thickness 4 5
4 & 5 5 5
(mils) (typical) (per MAS)
Step up/down Yes, Yes, Yes, Yes, Yes,
(mils) 4, 6 & 8 4 -6 3, 5, 6, 7, 8 & 10 +1 4 –6
Surface OSP (majority),
OSP ENIG, OSP, ImAu& etc OSP OSP
Finished ENIG (few)
PCB Thickness
Not provided 62, 79, 98 & 118 62 & 98 62, 98, &118 79
(mils)
Type Not Provided Type 4 Not Provided Not Provided Type 4
Key Message :
• Stepped stencil is very common for server ODMs, due to board design complexity (eg, large
socket/ connectors and small passive components). Stepped up/down range between 3 – 10
mils.
• Stencil thicknessfor Intel component 4 – 5 mils .
• PCB thickness is within TMDG guideline.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 5

## Page 6

PCBA Machine (Brand & Model)
Data Source:
Server ODMs
Area Inventec Quanta Foxconn TJ WistronZS Pegatron TW
ASM DEK/ Infinity API;
ASM DEK/horizon DEK/ Neo Horizon
Paste Print Fuji/GPX-C ASM DEK/DEK 03i Horizon; Neo Horizon
03IX 03iX
03iX
Universal/GSM,
Genesisa Panasonic/CM602F0,DT
PnP Fuji/NXTII Fuji/AIMEXIII, NXTIII, NXTII Fuji/NXT M6*14
Panasonic/CM602&CM 401,NPM
402
REHM/VXP-945 REHM/ VXP-944,
Reflow REHM Vitronics/XPM21240 Heller/2043 MK5
ERSA/Hotflow3/26 XL VXP945 (N)
Conceptronic/
Rework Not provided SRT/Summit 1800 SRT 1100LX, 2200LX SUMMIT-Lxi
Feedom2000
Speed line/ JT Smart610-H,
Wave Solder Ersa HotflowPowerFlowN2 Not provided JYI DIANN JT-620L
electra ChanLong/600CNP-HA
ParmiSigma XXL, SAKI BF-3Si
SPI TRI-7007L Not provided TRI-7007L TRI-7007 SII
(3D SPI), Cyber Optic SE5000L
Phynix-2D Xray, Nordson DAGE JADE
SMT X-ray VTROX VTROX V810 XXL Not provided
TRI TR7500L FP
Auto SAKI BF10Z, (S/S, C/S)
TRI-7700 Not provided Not provided Not provided
Inspection BF-3Di-ZS2 (Post W/S)
Key Message :
• Wide variety of machine in server ODMs. More challenges in equipment capability assessment &
development forfuture package design.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 6

## Page 7

PCBA Process Parameter/Capability – Paste Printing
Data Source:
Server ODMs
Parameter / Capability Inventec Quanta Foxconn TJ WistronZS Pegatron TW
Squeegee Speed (mm/s) 20 -60 1 -200 45 40 40
1 –25.5
Squeegee Pressure (Kg) 8-15 10 6 -9 11 -14
(automatic control)
Stencil Separation Speed
0.2-1 5.5 0.5 0.2~0.8 0-1
(mm/s)
Under Screen Cleaning Bottom side : 3 Bottom side : 4
1~3 1 (Top Side) 1~4
frequency (per print) Top side : 2 Top side : 2
Stencil Cleaning Frequency
12 2 12 6 Not provided
(hrs)
The machine
Cleaning Process Ultrasonic Ultrasonic Ultrasonic Ultrasonic
automatically to clean
PCB support type Vacuum & clip Panel Vacuum support block Pin or Block Vacuum and pin
Do you use the same pallet Yes, Yes,
for paste print, PnP and No if use pallet for paste if use pallet for paste No By model
reflow? print (case by case) print (case by case)
Maximum board handling
24 x 20 24 x 24 24 x 20 24 x 20 24 x 20
(inch, length x width)
KeyMessage :
• Varies PCBsupport type used atpaste print. Pallet use depend oncase/model.
• PCB maximum size >20inch (width) may require tool upgrade formost customers.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 7

## Page 8

PCBA Process Parameter/Capability – PnP
Data Source:
Server ODMs
Parameter / Capability Inventec Quanta Foxconn TJ WistronZS Pegatron TW
Nozzle size / φ(mm) H08M (45 x 45) 8.65, 15,
20, 15 20
(LGA socket & Intel BGA) H01/H02 (74 x 74) (Universal 340F) (#5401 Nozzle)
BGA Socket
Max BGA/socket size X:74 X:74 X: 100 X:74
X: 55 X: 83
capability (mm, x & y) Y:74 Y:74 Y: 80 Y:74
Y: 55 Y: 64
Max BGA/socket weight
< 50 < 90 < 28.5 < 100 < 38.5
capability (g)
Yes,
Using pallet during Board type dependent By model
No if use pallet for paste No
placement (<1.6 mm thickness) (pin support)
print (case by case)
Maximum board handling
24 x 21 30 x 30 24 x 20 26 x 18 21 x 16
(inch, length x width)
Lead: 0.24mm
min pitch/ball recognition 0.4 pitch/0.25
Bump: 0.40mm 0.4 pitch 0.3 mm 0.4 mm
capability bump
Pin: 0.40mm
KeyMessage :
• LGA/BGA beyond socket-E had reached max weight capability for some customer, need early development
roadmap& engagement.
• PCB maximum size >16/18inch (width) require tool upgradefor Pegatron/Wistron.
• PnP ball/lead recognition capability > 0.4mm pitch.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 8

## Page 9

PCBA Process Parameter/Capability – Reflow
Data Source:
Parameter/ Server ODMs
Inventec Quanta Foxconn TJ WistronZS Pegatron TW
Capability
Bottom : Center support Main board usually use the
Use of PCB support Carrier Not provided Special carrier
Top : Alloy Carrier carrier to support PCB.
N2 purging Yes Yes Yes Yes Yes
O2 PPM control < 3000 < 3000 < 1000 < 1000 < 2000
Yes, Left to Right (facing
Air flow control Yes Yes No Not provided
the machine)
Belt Speed (mm/min) 900 900 250 -2030 900 850-1000
Ramp Rate (°C/s) ≦3 ≦3 ≦3 ≦3 ≦3
Cooling Rate (°C/s) ≦3 ≦3 ≦3 ≦3 ≦3
Peak Temp Range 230-250 °C 230-250 °C 235-255 °C 230-250 °C 230-250 °C
Time above Liquidus (s) 60 -90 60 -90 60 -120 60 -90 60 -120
Soak Temp Range (s) 90 -120 90 -120 60 –120 (145 –175°C) 90 -120 60 -120
Delta T across Intel
15℃ 10°C 5°C 10°C 10°C
component
Number of reflow and 8-ramp,3- REHM:9/5 9-ramp, 4-reflow, 13 heating, 3
12-reflow, 4-cooling
cooling zones reflow,3-cooling ERSA: 9/3 5-cooling cooling
KeyMessage:
• Customer’s NPI typically followed MAS recommended profile. They customize mass production (MP) profile in order
toachievegoodyield.
o Peak Temp range of 20 °C due to large components on PCB. Foxconn required range 235-255 °C, others
@230-250°C
o TALrange60–90sformostcustomer,Foxconn&Pegatronrequiredrange60-120s.
o InventecisDelta_T<15°C(vsMAS<10°C).
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 9

## Page 10

PCBA Process Parameter/Capability – Wave & Rework
Data Source:
Server ODMs
Area Parameter Inventec Quanta Foxconn TJ Wistron ZS Pegatron TW
Preheat Time (s) <180 Not provided 192 -240 by product 90 -130
Solder Pot Temperature (℃) 265 -275 265 -275 260 -270 263 -270 270
Conveyor Speed (mm/min) 900 500 -2500 600 -750 600 -800 850
Wave
E-Cap, DIMM/IO
soldering Components / pitch undergo connector, dip TH component, All PTH component
Not provided Connectors, etc...
wave solder capacitor >2.5mm pitch (DIP type)
> 1.57mm pitch
O2 PPM monitor Notprovided <3000 O2 PPM <1000 O2 PPM NA NA
Peak Temp Range (°C) 235 -250 50 -400 (typo?) 235 -255 230 –250 230 -250
Socket: 60 -120
Time above Liquidus (s) 30 -120 60 -90 60 -120 60 -90
BGA: 60 –90
60 –120 Socket: 60 -100
Soak Temp Range and Time 90 -120 90 -120 90 –120
(145-175 °C) BGA: 60 –120
Rework
Max BGA/socket weight
Not provided < 900 < 28.5 < 100 < 38.5
capability (grams)
Is N2 used& O2 PPM control Yes, No, Yes,
Not provided Not provided
? <3000 O2 PPM no O2 PPM control < 3000 O2 PPM
Key Message :
• Rework PnP had reached maximum weight capability for Foxconn & Pegatron (<28g).
• Rework @ air is still required.
• Peak Temp range of 20 °C required to achieve good yield (same as SMT).
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 10

## Page 11

PCBA Process Parameter/Capability – Inspection (1)
Data Source:
Server ODMs
Area Process Inventec Quanta Foxconn TJ Wistron ZS Pegatron TW
Sampling rate 100% 100% 100% 100% 100%
Min/Max Spec and
not provided not provided not provided not provided not provided
control limit
Is SPI Performed on
SPI selective components or 100% 100% 100% 100% Yes, selective
100%?
Maximum board
handling capability 26 x 24 32 x 24 24 x 20 26 x 24 24 x 20
(inch, length x width)
AXI for In-line,
In line / offline offline In-line offline offline
2DX-ray for offline
NPI: 100%
X-Ray Sample 5 pcs/lot NPI: 100%
Per customer MP: Selective
sampling rate start, follow by 1 pcs Not provided MP: 1 pcs every 2
requirement (BGA, Socket, TH
per hour hrs
component)
Key Message :
• SPI is performed 100% for every PCB.
• Post SMT X-ray sampling plan varies by customer due to different run rate & line set-up.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 11

## Page 12

PCBA Process Parameter/Capability – Inspection (2)
Data Source:
Server ODMs
Area Process Inventec Quanta Foxconn TJ Wistron ZS Pegatron TW
Before in line /
In line / offline ? In-line In-line In-line In-line
After off line
100% for 100% for
sampling rate ? 100% 100% 100%
production production
How many AOI's are
2 4 2 Not provided 4
used?
Pre-reflow: 2 (CS/SS)*, Pre-reflow: 2,
AOI Where is AOI located? Post Reflow Post Reflow Post reflow
Post wave solder: 2 (CS/SS) Post-reflow: 2
Is AOI Performed on
NPI: 100% Yes (no detail
selective components 100% 100% 100%
MP: Selective provided)
or 100%?
Maximum board
handling capability 26 x 24 34 x 27 24 X 20 26 x 24 24 X 20
(inch, length x width)
*C/S –Chip Shooter; S/S –Socket Shooter
Key Message :
• 100% post-reflow AOI is performed during MP phase by in-line process for all customers.
• Only 2 customers performed pre-reflow AOI for early issue detection.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 12

## Page 13

PCBA – Operation & Others
Data Source:
Server ODMs
Area Inventec Quanta Foxconn TJ Wistron ZS Pegatron TW
inventory check, shop floor scanning inventory check, inventory check,
Purpose Traceability
traceability for traceability traceability traceability
IQC, SMT,
SMT & System Final Assembly/Testing
2D Scanner Which process kitting,SMT, etc. All process SMT
assembly process, Rework
process
In-line assembly Both In line and
In line or offline In line In line traceability In-line
(SMT/System Assy) offline
Using adhesive Yes,
no no no no
for BGAs *not on Intel part
Type of adhesive
N/A N/A N/A N/A Not provided
used
Adhesive
Brand of adhesive N/A N/A N/A N/A Not provided
When adhesive
N/A N/A N/A N/A Not provided
applied
Key Message :
• 100% In-line 2DID (SubMark) scanned is a general practices across all ODMs for traceability.
• Marking quality on 2DID is critical for flawless process execution.
• No adhesive process performed/capability; Pegatron is equipped with adhesive process but not
performed on Intel component.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 13

## Page 14

Others / Automation (L5/L6) - 1
Data Source:
Server ODMs
Inventec/
Area Quanta Pegatron TW WistronZS
Foxconn TJ
Partial: automated test machine
(eg.DIMM, display card & etc)
Partial / Full
Full automation (suggest test automation Not provided
assembly process
development assessment align to
NPI direction)
In-line / off-line
Board In-line in-line in-line
automation
Test
Not provided
Type of Quanta in-house Semi-automated test machine
fixed auto test box
equipment/machines design (eg.Oceancat)
Vacuum nozzle, gripper for CPU,
Pick & Place used ? vacuum nozzle and fixture for opening the CPU NA
socket cover
Assembly PHM assembly No No N/A
Fixture Carrier to the CPU No yes NA
Key Message :
• Customers are exploring automated test at board functional test.
• ODMs’ automation development is a continuous learning process, for improvement & enhancement. It is a
trend / journey toward Industrial 4.0 (smart factory).
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 14

## Page 15

Others / Automation (L5/L6) - 2
Data Source:
Server ODMs
Inventec/
Area Quanta Pegatron TW WistronZS
Foxconn TJ
Assembly of one PHM (CPU
30 -40 s ~ 10 s N/A
+ carrier + heatsink)
Assembly Attaching PHM assembly < 60 s ~ 15 s 12 -22 s
Time
Throughput for standard 2S < 120 s 50 s N/A
(Target)
Dissemble PHM from < 120 s for 2S board
20 s N/A
motherboard (2S -2 Socket solution)
Any additional improvement *Socket cover need be
*Socket PnP cover No
Not provided
required designed for easy removal
Intel reference design, Need a special heat-sink for
Heatsink design Follow Intel reference
own customized design mfgtest (eg.PurleyFTT)
General
Not applicable,
Is the Intel PHM design No
Designed PHM in Test Yes
automation friendly? (PEEK nuts easily broken)
fixture
* Need details
Torque Driver used, Brand KILEWS SK-3120L
generic brand Conos from customer
and Model KILEWS SK-8140L
Key Message :
• EGS & beyond required automation friendly for retention assembly. Customers made request since Purley/2016.
• Retention design need to comprehend both manufacturing (automation) and field (manual) usage.
• Need continues support for assembly test tool development (Whitley →Eagle stream →future platform)
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 15

## Page 16

Others / Automation (L10) - 1
Data Source:
Server ODMs
Inventec /
Area Quanta Pegatron TW Wistron ZS
Foxconn TJ
Partial No automation (suggest test
Partial / Full * DIMM assembly automation development
NA
assembly process * HDD Tray Assembly assessment align to NPI
* Board screw assembly direction)
In-line / off-line Off-line In-line NA
System
Test (suggest test automation
Type of equipment/ Quanta in-house design
development assessment NA
machines are used? and assembly
Not provided
align to NPI direction)
Vacuum nozzle, gripper for
Pick & Place used ? Manual CPU NA
*Basedon Intel
PHM assembly No No
Assembly Design
Fixture *Based on Intel
Carrier to the CPU No yes
Design
Key Message :
• ODMs’ automation development is a continuous learning process, for improvement & *e nNheaedn cdeemtaeilns tf.r om customer
• Automation is a trend / journey toward Industrial 4.0 (smart factory).
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 16

## Page 17

Others / Automation (L10) - 2
Data Source:
Server ODMs
Inventec/
Area Quanta Pegatron TW WistronZS
Foxconn TJ
Assembly of one PHM (CPU
N/A ~ 10 s 35 –45 s
+ carrier + heatsink)
Assembly
Attaching PHM assembly < 60 s ~ 15 s Not provided
Time
Throughput for standard 2S < 120 s 50 s 15 -25 s
(Target)
Dissemble PHM from < 120 s for 2S board
20 s 5s for each screw
motherboard (2S –2 socket)
socket cover need be
Any additional improvement
No No designed for easy
required
removal Not provided
Intel reference
What heatsink design is
Follow Intel reference design, own N/A
used?
General customized design
N/A
Is the Intel PHM design
Manual process to manage Yes N/A
automation friendly?
1S/2S/4S variety
Torque Driver used, Brand KILEWS SK-3120L
generic brand Conos
and Model KILEWS SK-8140L
Key Message :
• Throughput time (TPT) target is varies by individual customer. Wistron showed lowest TPT.
• Higher manning ratio in Wistron to meet ~15s TPT for 2S PHM assembly (typical ~50s/operator).
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 17

## Page 18

Key Takeaway (1)
PCBA – Material / Consumables
▪ Stencil vendors preferable from local support for fast response, delivery time & on-site.
▪ Wave solder process is still required for thru-hole components.
▪ Shenmao paste/fluxis commonly used except 1 customer.
– Shenmao paste is generally used during early development; will be used as back-up during mass production
(MP).
– Alternate solder paste ismandatory forSMTpertheircustomer requirement.
▪ Stepped stencil is commonly used, due to design complexity & large variety of component/pad size
(varies in Area Ratio). Stepped up/down range between 3 – 10 mils.
▪ Stencil thicknessfor Intel component 4 – 5 mils.
▪ PCB thickness is within TMDG guideline.
PCBA – Process / Capability
▪ Wide variety of machine used and some reached maximum capability, need early development
roadmap & engagement for tool capabilityassessment
– PCBhandling capability reached maximumwidth of20inch (PastePrint,SPI&AOI);16inch (PnP).
– PnP(SMT&Rework)hadreached maximum weight capability (~28g).
▪ Varies PCB support type used at paste print.
▪ Pallet usage is case/model dependent for paste print & PnP.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 18

## Page 19

Key Takeaway (2)
PCBA – Process / Capability (continue)
▪ Customer’s NPI typically followed MAS recommended profile. Profile will be customized profile in
mass production(MP) to achieve good yield.
– Peak Temp range of 20 °C due to large components/socket on PCB. Required range 235-255 °C, and 230-250
°C(customerdepended)
– TALrange required 60–90s and60-120s(customerdependent).
– Delta_T <15°C (vsMAS<10°C).
▪ Rework @ air is still required.
Inspection Process (SPI / AOI / X-ray)
▪ 100% SPI & post-reflow AOI is performed during MP phase.
▪ Post-SMT X-ray sampling plan varies by customer.
Others / Automation
▪ 2DID (SubMark) is 100% scanned in-line for traceability. Marking output stability & quality is
required to ensure stable 2DID reading.
▪ The traditional ODM manufacturing is transforming toward Industrial 4.0. Customer is exploring
automationat board functional test processand other areas.
▪ Throughput time (TPT) target is varies by individual customer.
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 19

## Page 20

Next Step
❖ Conduct CRD survey for L10 factory in US region, to understand automation practice, requirement
& trend.
❖ Need continues support for assembly test tool development (Whitley → Eagle stream → future
platform). Possiblyaddress customer concerns for breaking PEEK nuts issue.
❖ Seek customer clarification for PnP cover (new) and socket cover concerns (if this is existing/new
issue).
DELL –available in
Foxconn eBay
design
Example of Purleysocket
HPE design
cover improvement request
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 20

## Page 21

Rev Tracking
# Rev Date Released Change Description
1 0 W26 Y2020 New doc
2 1 W32 Y2020 Updated machine information and (page 4 & 6, in blue)
CQR|CustomerQuality&Reliability Intel Confidential | For Internal Use Only 21
