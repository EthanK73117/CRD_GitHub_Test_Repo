---
source_file: "DT CRD Q4-2020 Rev00-Nov-10 Updates.pdf"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/DT CRD Q4-2020 Rev00-Nov-10 Updates.pdf"
file_type: "pdf"
size_bytes: 2373799
content_hash: "b03ffb887a24"
converted_at: "2026-10-07T09:38:10"
---

# DT CRD Q4-2020 Rev00-Nov-10 Updates

## Page 1

CONFIDENTIAL
Contained customer process
information under NDA
Alder Lake-S OEM & ODM CRD Survey Report
(Desktop Segment)
Customer participated:
ACER, AS ROCK, ASUS, DELL, LENOVO, MSI, LITEON, FOXCONN, LCFC, ECS
2020 - WW45 Rev 0

## Page 2

Revision History
# Rev Date Released Change Description
1 0 W45 Y2020 New doc
CQR|CustomerQuality&Reliability 2
Intel Confidential

## Page 3

Agenda
❑ Desktop Customer Landscape ❑ PCBA Factory Process
▪ Automation
❑ Key Takeaway
▪ Paste Printing
❑ Additional Feedback / Concerns ▪ Pick and Place
▪ Reflow
❑ Observation / Next Step
▪ Wave Solder
❑ Printed Circuit Board (PCB) Design
▪ Board Level Adhesive Process
▪ ILM Cover / Lever / Assembly
▪ Process Inspection / Monitoring
▪ PCBA Test Process
▪ PCB X-Ray
▪ Rework
▪ Others
❑ Acknowledgment
❑ Back Up
CQR|CustomerQuality&Reliability 3
Intel Confidential

## Page 4

2020 Desktop Customer Landscape
Q1 2020 DESKTOP
OEM MSS% Customers Providing Survey Results
Q1 ’20 OEM ODM Site Design / SMT / SI Qty/Qtr
Lenovo 24.4% Acer Wistron DESIGN
AS Rock DESIGN
HP Inc 21.5%
Asus DESIGN
Dell Inc 19.7%
Dell Inc DESIGN
Apple 6.9%
Lenovo MSI DESIGN
Acer 5.6%
MSI DESIGN
Asus 5%
Foxconn Mexico - Juarez SI 400ku/qtr
Dell Inc
Others 16.8%
Foxconn Wuhan SMT & SI Unknown
Foxconn Wuhan SMT & SI 600ku/qtr
HP Inc
For Example:
Foxconn Czech Republic -Pardubice SI 600ku/qtr
• Gigabyte (1.8Mu/qtr)
Liteon Dongguan SMT 400ku/qtr
• MSI (1Mu/qtr)
LCFC Hefei SMT 230ku/qtr
• AS Rock (600Ku/qtr)
Lenovo
• SuperMicro MSI Unknown SMT Unknown
ECS Shenzhen SMT & SI 200ku/qtr
Note: For ODMs shown in blue, some limited MV/factory info was also collected
CQR|CustomerQuality&Reliability 4
Intel Confidential

## Page 5

Key Takeaway (1)
❑ PCB Design
▪ OEMs have design ownership of PCB, System and Thermal Solution.
▪ OSP is the most common PCB surface finish with 62 mils board thickness, followed by ~47/48mil
thickness and minimum via drill diameter of 8-10mil.
▪ Most customer choose Type 3 board with 4/6/8 layer and 140-150°C Tg PCB lamination.
▪ ATX is the most common form factor design, there are also other form factors used.
▪ Majority of the customers have capability to support double sided assembly process.
❖ Backside (secondary side) assembly process is fully automated for SMD components and capability
constraints/limitations vary by customer.
❖ 0201 is the smallest chip component size supported, across all board designs.
❖ Component spacing rules vary by customer.
▪ Approximately 60% of the surveyed customers allow for trace routing between chip component pads.
▪ Customers have more concerns and paying more cautious for large SMT connectors, eg. include
soldermask between the pins in their design to mitigate SMT risk.
▪ Customers perform reliability testing in board level and some in system level, the reliability tests are
different among all.
▪ Customers use both their proprietary and Intel designs for thermal solutions. They do follow thermal
relief rules.
CQR|CustomerQuality&Reliability 5
Intel Confidential

## Page 6

Key Takeaway (2)
❑ ODM PCBA Process & Rework
▪ Customer is trending to full automation for SMT assembly with in-line traceability capability set-up.
Approx. 50% of the surveyed customer achieved full automation while others are partial automation.
▪ Pin and vacuum PCB support are used at paste print process. Approx 50% of the surveyed customer
choosing pin type , while the remainder are using both pin and vacuum support.
▪ Customer preferred stencil thicknesses: 0.10, 0.12, 0.13 & 0.15mm for both SMT and rework.
▪ Pallets are generally used for board support during SMT reflow and rework. Most customers directly
applied solder paste on PCB pads for rework. Few customers also print solder paste onto the solder
balls.
▪ Approx 80% of the surveyed customers reflow with purging N2 (O2 ppm range between 1K-3K) and
other reflow @ Air environment.
▪ No O2 ppm control for wave soldering process for most customers and PCBA rework process mostly
performed at air environment.
▪ Many customers are not sharing their paste vendor info and machine/equipment model with Intel.
▪ PnP minimum ball pitch recognition capability is 0.3mm.
▪ Customer prefer peak reflow temp range from 230-250°C.
▪ Customers are not using adhesives for sockets but using it for BGAs. Customer common practice is to
apply adhesives before board testing.
CQR|CustomerQuality&Reliability 6
Intel Confidential

## Page 7

Key Takeaway (3)
❑ Inspection/Test/ILM/Others
▪ SPI is generally performed 100% and control limits range target between 60%-180%.
▪ AOI is performed on 100% of components and located after reflow.
▪ PCBA x-ray inspections is typically performed offline by sampling, no common sampling rate. Most
customers are performing bed of nails and functional tests
▪ Customers prefer the ILM cover to “pop off” with CPU inside socket & ILM cover closed.
▪ Beat rate to install or remove an Intel LGA CPU from the socket ranges between 12-15 seconds, they are
concerns with socket-V lever latching at opposite direction and manufacturing run rate impact due to
ILM assembly for socket-V (4-screw, 2-pcs top-plate) vs socket-H (3-screw, 1-pcs top-plate)
▪ Customers have not experienced any ESD issue related to the ILM cover for socket-H.
▪ Customers find the Desktop MAS helpful and think a System Assembly video is required. CPU assembly
and PnP tool video played during Intro meeting is customers’ favorite.
▪ Customer is looking for solution/tool that is “executable” for manufacturing process/variation (eg. ILM)
and design fungibility (eg. thermal solutions)
▪ SJQ concerns for potential insufficient total solder volume (~10% lesser?) in solder joint formation.
LOTES (0.45mm ball size) vs FIT/Deren (0.5mm ball size) but MAS recommended the same solder paste
volume.
CQR|CustomerQuality&Reliability 7
Intel Confidential

## Page 8

Additional Feedback/ Concerns (1)
Customer Area of Concerns
AS Rock Mixing & fungibility concerns, expects socket-H vs skt-V Thermal Solution is interchangeable. The hole pattern looks alike to
CML-S, with distance between hole 75mm vs ADL-S is 78mm. There are additional cost and manufacturing mixing concerns
when there are 2 different solutions for DT tooling, need to make it fungible due to the dimension is ~3mm delta that not
noticeable by operator.
LiteON Processor PnP tool /Stage > LiteON will be converting to automation, the PnP/assembly tool may not helpful. Automation
assessment is in progress (eg. assess utilizing Cobot with tool/fixture ). They plan to perform some SMT build in Oct/Nov.
Acer SJQ concern> LOTES socket with smaller solder ball (0.45mm, 10% smaller), compare to Deren/FIT (0.5mm) but MAS
recommended paste are same for FIT/Deren/LOTES. Need intel to perform more data collection to ensure the same amount
paste volume recommended in MAS is good for LOTES HVM. Meantime, need Intel technical explanation of why mechanical ball
attached in LOTES need smaller ball & still OK to use the same paste volume & etc.
Pin 1 indicator error> Different pin 1 indicator on PnP stage vs PnP tool vs PCB, ILM. Need Intel to ensure final design is correct.
Lenovo SZ • Interchangeable for backplate/load plate/screw/lever & etc > Need to allow mixed vendor to ease mfg process, due to there
(LIPC) are more pieces for socket-V (eg. allow mixed 2 vendor for lever and top plate due to 2 separate pcs). Need Intel to confirm
the 4 mounting screws/nuts PN# are same.
• CPU installation to socket/ILM > Need Intel to confirm any error in step, and when the cover pop-up.
• “Error Free” design requirement for backplate and ILM dimension for HVM assembly> Need Intel to provide back plate
dimension whether it is effective for LIPC can design an automation/fixture for backplate assembly to prevent 180°
orientation (the chamfer look insignificant in picture and looks symmetrical), also potential operator installing the load plate +
lever frame wrong side (vs skt-H, 3 screw, no way to install at wrong side).
• Socket Pin contact dimension> Due to tighter pitch in skt-V (0.8mm), need Intel to provide pin dimension & ensure type 3 x-y
axis shift always making “good” contact to the LGA pad center.
• SJQ concern> Need intel to perform more validation data collection to ensure 5 mils stencil is working for LOTES HVM.
• Socket & Tray> Need to ensure CTF dimension are same across all vendors, so that PnP only need to set-up 1 recipe.
• Confusing Pin 1 indicator for PCB/ILM vs PnP tool/stage.
CQR|CustomerQuality&Reliability 8
Intel Confidential

## Page 9

Additional Feedback/ Concerns (2)
Customer Area of Concerns
LCFC Run rate impact> Additional 1 screw (Skt-H 3-screw to skt-V 4-screw) and assemble 2-pcs topplate (vs skt-H 1-pcs topplate)
ILM lever latch direction > Skt-H is pulling the lever inward, but Skt-V is pushing the lever outward. This is not manufacturing
friendly as the same operator will be processing skt-H and skt-V.
FXWH • ILM > Quality control for the screw & nut thread tolerance among different vendors, variation by batch/datecodefor individual
vendors.
• Backplate/load plate/screw/lever & etc > Need to allow mixed vendor to ease mfg process, due to there are more pieces for
socket-V (eg. allow mixed 2 vendor for lever and top plate due to 2 separate pcs).
• ILM gap to PCB (Warpage?) > Per skt-H experience, FXWH observed gap/seperationbetween the ILM vs PCB. Worried if skt-V
ILM will hv similar issue especially there are 2 pcs for top plate and lever pcs, if there are PCB warpage, will the situation get
worsen ? And resulting poor socket contact pin to LGA pad. (eg.potential scenario with package tilted in socket, and not all
pin/package unable to get the similar compressive load resulting poor or marginal contact)
• Torque setting requirement and expectation > Need to “range” for manufacturing process, (eg. 8-in-lbf ± xx %) due to in
actual process/production there are no way for absolute value 8-in-lbf, there are variation between batches/vendor for the
screw/nuts, torque driver capability & etc.
Intel FAE Socket bend pin pass/fail criteria in MAS> Need to re-assess the type 3 x-y axis shift visual criteria for ±0.125mm, due to
tighter pitch in skt-V (0.8mm) vs skt-H pitch 0.914mm. Is the contact pin always making contact to the LGA pad center ? Will the
contact pin that passing 0.125mm still passing electrical test ? as the pin may be touching/ too close to the adjacent CPU LGA.
Key Message (combined both slides)
• Customer is looking for solution/tool, with design fungibility that is “error free“, “executable” for HVM process transparency or
variation, (eg. opposite lever latching direction, thermal solution design, orientation control, allow mixing piece parts & etc)
• Concerns is manufacturing run rate impact for socket-V for ILM assembly (additional top plate and screw)
• SJQ concerns due to potential insufficient total solder volume for solder joint formation
o LOTES (0.45mm solder ball) vs FIT/Deren (0.5mm solder ball) but MAS recommended same solder paste volume
CQR|CustomerQuality&Reliability 9
Intel Confidential

## Page 10

Observation & Next Step
❑ Observation
▪ Few customers were not excited about Intro meeting (eg. ECS, MSI, HPI, QCMC) or participate
in CRD survey (eg. QCMC, Gigabyte, MSFT)
❖ Customers already get used with the working model with Field Engineer/account team for ~10 years
without CQR/CME enabling
❑ Next Step
▪ Demonstrate our values and collaborate with Field Engineer/account team for future
customer enabling in DT segment
▪ Proactively follow-up with customer for their development activities/NPI for Socket-V and
offer help to re-build customer relation
▪ Follow-up with LiteON for their Oct/Nov SMT build result and automation assessment
▪ To seek clarification from customers for items label in this color
CQR|CustomerQuality&Reliability 10
Intel Confidential

## Page 11

Acknowledgment
Customer Account CQE
Acer Jeremy Chang
AS Rock Sean Bao
Asus David Wang
Dell Inc Allan Leal, Samer Alaiyoubi, Arturo Rios
ECS Sean Bao
Foxconn WH Sean Bao
HP Inc John Burtchaell
LCFC Shirley Zhang
Lenovo Jiang Art, Albert Tsai
Liteon Sean Bao
MSI David Wang, William Pan
QCMC Juanita Ren
CQR|CustomerQuality&Reliability 11
Intel Confidential

## Page 12

Back Up
Department or Event Name Intel Confidential 12

## Page 13

Printed Circuit Board Design (1)
Area of Interest LENOVO (MSI) DELL ACER (WISTRON) ASUSTEK MSI ASROCK
Do you have PCB design Yes Yes Yes Yes Yes Yes
ownership
Do you have Full System Yes Yes Yes Yes No, only for No, Motherboard
Design Ownership channel MB only
Do you have Thermal Yes Yes Yes, for AIO/miniPC, Yes Yes Yes, but only for
Solution Design No, for Tower (Owned by Acer) PCH and Vore
ownership MOS heatsink
Please list the PCB GBM, APCB, Not Answered 4 Layer: CEE(1st) / TRUSTECH(40%), Vendor A(30%), Trustech(50%),
suppliers used by % Hanstar, Junya(骏 GLOBALBRAN(2nd) / VICTORY(3rd) GECS(30%), VendorB(70%) Dingfu鼎富(50%)
亚),ECS (15%), 6 Layer: Hannstar(1st) / CEE(2nd) / DF(15%),
Palwonn, VGA, GLOBALBRAN(3rd) DYEC(15%)
etc… 8 Layer: Hannstar(1st) /
GLOBALBRAN(2nd)
Please list the PCB surface OSP OSP(100%) OSP(100%) OSP(100%) OSP(100%) OSP(100%)
finishes used by %
Please list the PCB board 62mil(90%), 62mil(70%), 62mil(75%), 62mil(100%) 62mil(80%), 62 mil(90%),
thicknesses used by % 48mil(10%) 47mil (30%) 47mil(25%) 59mil(20%) 59 mil(10%)
All of the "Micro" form factors in
Dell's Desktop portfolio use 47 mil
(1.2mm) thick PCBs. This equates
to ~4-5 million units of volume
and ~30% of their Desktop
volume. All other Dell Desktop
products use 62 mil (1.6mm) thick
PCBs, which equates to ~70% of
their Desktop volume.
Key Message
• OEMs have design ownership of PCB, System and Thermal Solution
• OSP is the most common PCB surface finish
• While 62mil is the most common PCB thickness, ~47/48mil are also commonly used by 3 customers
CQR|CustomerQuality&Reliability 13
Intel Confidential

## Page 14

Printed Circuit Board Design (2)
Area of Interest LENOVO (MSI) DELL ACER (WISTRON) ASUSTEK MSI ASROCK
Please list the PCB Laminate 150°C Tg(50%), 150°C Tg(100%) 145°C Tg(100%) 150°C Tg(50%), 150°C Tg(100%) 140°C Tg(80%),
Tgused by % 140°C Tg(50%) 140°C Tg(30%), 150°C Tg(20%)
170°C Tg(20%)
Please list the PCB type that Type 3(100%) Type 3(100%) Type 3(100%) Type 3(100%) Type 3(100%) Currently use Type
is used by %? 3(100%), but we will
validate type 4 for PCIE5
Please list the PCB layer 4 Layer(65%), 4 Layer(60%), 6 layers(50%), 6 Layer(40%), 6 Layers(70%), Currently use 6
count that is used by % 6 Layer(30%), 6 Layer(25%), 4 layers(25%), 4 Layer(30%), 4 Layers(20%), Layer(100%), but we will
8 Layer(5%) 8 Layer(15%) 8 layers(25%) 8 Layer(30%) 8 Layer(10%) validate 4 Layer PCB
Please list the PCB board Non-standard Custom(100%) mATX(25%), ATX(80%), ATX(43%), Our first project is ATX.
form factor that is used (by sizes, e.g. 267mm DTX(25%), uATX(20%) MATX(33%), Usually we might have
%)? x 245mm, 267mm AIO(25%), ITX(19%), ATX(40%), uATX(30%),
x 220mm, 170mm miniPC(25%) EATX(5%) mini-ITX(15%), and
x 170mm, etc... AIO(15%) in the future.
What % of your designs are Double Double Single Sided(90%), Double Sided(80%), Double Single Sided(70%),
double sided assembly ? sided(90%), sided(90%), Double sided(10%) Single Sided(20%) Sided(100%), Double Sided(30%),
Single sided(10%) Single Single Sided(0%)
sided(10%)
Is there capability to support Should be OK Yes Yes Yes Yes Yes, we can support 100%
100% of your volume with double sided components
double sided components?
Key Message
• 140-150°C Tg PCB laminate are the most common
• Type 3 and 4/6/8 layer PCB designs are the most common
• While ATX is the most common form factor design, many other various form factors are also used
• It is most common for customers to have the capability to support double sided assembly
CQR|CustomerQuality&Reliability 14
Intel Confidential

## Page 15

Printed Circuit Board Design (3)
Area of Interest LENOVO (MSI) DELL ACER (WISTRON) ASUSTEK MSI ASROCK
Via & Pad What is the minimum via 10mil drill / 8~10mil drill / 8mil drill (Finish hole 10mil drill / 12mil drill / 10mil drill /
pad stack (drill diameter / 20mil pad/ 18mil pad/ size) / 20mil pad/ 22mil pad/ 18mil pad /
via pad diameter / antipad 31mil antipad 28mil antipad 18mil pad / 30mil antipad 32mil antipad 28mil antipad
diameter)? 28mil antipad
Are the BGA land area vias covered with both are used covered with covered with plugged / Full covered
not covered with soldermask (covered & not soldermask soldermask covered with with soldermask
soldermask, or are they covered with soldermask ( 全塞孔)
capped / plugged / covered soldermask)
with soldermask (no
exposed vias)?
Component What is the smallest chip some are 0201 0201 0201 0201 0201 0201 is OK
Sizes component size that is and some are
supported for your desktop 0402
board designs?
Regarding the above Yes, across all Yes, across all Yes, across all board Yes, across all Yes, across all Yes, across all
question, is this true across board designs board designs designs board designs board designs board designs
all board designs (for
example, across all 4 or 6
layer board designs, and
across all Type 3
and Type 4 designs)?
Key Message
• 8-10mil is the most common minimum via drill diameter
• 0201 is the smallest chip component size supported, across all board designs
CQR|CustomerQuality&Reliability 15
Intel Confidential

## Page 16

Printed Circuit Board Design (4)
Area of Interest LENOVO (MSI) DELL ACER (WISTRON) ASUSTEK MSI ASROCK
Component Is backside Fully automated Fully Fully automated process Fully Fully automated process Fully automated
Placements assembly a process automated automated process
fully process process
automated
process
Any Part Height:Needs Quantity: Chip Min: 0201 Part Height: Placement: Backside SMT components must Quantity: No rule, so far
limitations to be less than Balance Only the part be placed away from the edge of board by at the maximum backside
on 3.5mm. component Component Max size: height is least 200mil (5mm) component quantity is
backside quantity for 100mm*90mm limited to Via/Through Hole: Distance between "VIA & 1243
SMT Constraints: top and 6mm on Through hole (PTH & NPTH)" and SMD PAD
component Cannot put bottom side BGA: backside must be equal or greater than 6mil (0.15mm) Chip size: No rule, so far
placement connector / socket Max pitch: 0.5mm Vias: It is strictly prohibited to lay VIA hole the maximum backside
(quantity, for most product, Size: 5x5mm to 45x45mm Quantity: (including PTH) beneath SMT component component is Intel
chip size)? need to be far Smallest Diameter: The quantity is Part Height: LGA1200 socket
away from the PCB 0.25mm not limited -Backside component height must be equal or
edge (more than less than 12mm for double-sided process Beat rate: The backside
6mm). QFP: board SMT will use a slower
Size: 5x5mm to 45x45mm -If SMT component height (t) ≦2mm, distance pick & place machine.
Smallest Spacing: 0.4mm between backside DIP pin and SMD
Smallest Lead Width: component (x) must ≧3mm.
0.2mm -If SMT component height (t) ≧2mm (The
height can't over 12mm), distance between
backside DIP pin and SMD component (x)
must ≧4mm.
Quantity: And the component Q'ty should be
≦1000pcs
Key Message
• The backside assembly process is fully automated for all customers
• Backside component constraints & limitations vary by customer
CQR|CustomerQuality&Reliability 16
Intel Confidential

## Page 17

Printed Circuit Board Design (5)
Area of Interest LENOVO (MSI) DELL ACER (WISTRON) ASUSTEK MSI ASROCK
Component Min spacing for 0402 to Min spacing: 1.5mm, pad-pad ≥0.3mm 0.25mm 0.3mm (12mils) 0.05mm 0.15mm
Spacing 0402 2mm is better (12mils)
Min spacing for 0603 to 1.5mm pad-pad≥0.3mm 0.30mm 0.3mm (12mils) 0.05mm 0.18mm
0603 (12mils)
Min spacing for 0805 to 1.5mm pad-pad≥0.3mm 0.40mm 0.3mm (12mils) 0.05mm 0.18mm
0805 (12mils)
For through-hole ≧0.5mm (20mil) 2.54mm to 3.0mm 2mm minimum body-to- 0.50mm each cap 0mm between
components (e.g. leaded (100 to 120mils), body spacing frame spacing component allegro
caps), what is the minimum ODM depedant requirements is (≧0.5mm (20mil) symbol outline
body-to-body spacing 0.61mm (24 mil)
requirements for assembly?
For large SMT components ≧0.5mm (20mil) 1.0mm to 2.54mm 2mm minimum body-to- Not answered 0mm between
(e.g. inductors), what is the (40 to 100mils), body spacing component allegro
minimum body-to-body ODM dependant requirements is symbol outline
spacing requirements for 0.30mm (12 mil)
assembly?
For components inside the ≧0.5mm (20mil) 2mm 1mm minimum chip-to- All the caps around 0mm between
socket cavity, what is the socket cavity-wall the CPU SKT should component allegro
minimum chip-to-socket spacing is 1.0mm be >0.2mm symbol outline
cavity-wall spacing (40 mil)
requirements for assembly?
For the above question, is Above spacing is set Above spacing is Above spacing is set Above spacing is set Above spacing is set Above spacing is set
this minimum spacing set for request for set for both rework for Chip to BGA for rework reasons for: Component for factory assembly
for rework reasons or for rework limitation and assembly 2mm Placement, Assembly,
other assembly and progress considerations Installing,
considerations? (please assembly in MFG Crashworthiness and
explain) maintenance
considerations
Key Message
• Component spacing rules vary by customer
CQR|CustomerQuality&Reliability 17
Intel Confidential

## Page 18

Printed Circuit Board Design (6)
Area of Interest LENOVO (MSI) DELL ACER (WISTRON) ASUSTEK MSI ASROCK
Thermal Do you follow any Yes Yes Not Answered Yes, we follow Yes Please refer to the graphic below
Reliefs rules / Intel's KOZ
requirements for Limit, and by
*
thermal reliefs? model (Mass /
Height, etc...)
*
Trace Routing Do you allow for No, not suggested, Yes No, concerns: Yes No, must Yes, but only when there is not other
for Passive trace routing because of the layout 1. The signal consider solution
Components between the pads, solution, due to performance will be soldermask
or underneath the interference problems. poor. application,
pads, of chip If were to modify the 2. It will cause a short especially in
components, such trace width to through issue due to poor the dark
as 0603 and 0805, the pad, the soldermask coverage soldermask /
etc...? impedance may not 3. It will cause poor registration
meet the SPEC. solderability due to
trace thickness is
higher than the pin
Key Message
• Customers do follow thermal relief rules
• 3 customers allow and 2 customers don’t allow for trace routing between chip component pads
CQR|CustomerQuality&Reliability 18
Intel Confidential

## Page 19

Printed Circuit Board Design (7)
Area of Interest LENOVO (MSI) DELL ACER (WISTRON) ASUSTEK MSI ASROCK
Trace Routing We see a trend with Yes, reliability is a Need to There are no concerns Need extra VIA for routing Yes, wait for test Yes. 1) The factory assembly failure
for Large SMT higher speed IO to concern for a long evaluate case for Desktop, this concern trace to TOP layer rate is much higher than DIP type
Connectors move to large SMT slot, such as PCIe by case should be for Server. slot, and 2) SMD type is difficult to
connectors (e.g. PCIe, Gen5 and DIMM Basically, we will follow rework / repair.
DDR UDIMMs). Do you DDR5. Another Intel's Demo board
concern is that it will design. Meanwhile, we
see any issues or
add more VIAs and will check with our EE
concerns with these
layers. and ODM.
types of connectors?
For large SMT We are forbidden to Need to have Trace between pins must Need to allow for soldermask Need to cover Alder Lake design is still in Layout
connectors (e.g. PCIe, do this type of 0.20mm (8 be covered with between the pins between the process, but we think soldermaskis
DDR UDIMMS, etc…) design. mils) air gap soldermask to prevent pins with a must for production quality
with pitch ~0.85mm to from trace to short issue soldermask control.
1.0mm, do you allow adjecent pin
pad We can route between the pins with
for soldermask
minimum
between the pins or
1. Trace width = 0.0889mm (3.5mil)
are ganged soldermask
2. Pad width = 0.1778mm (7mil)
openings a
3. Pad to trace = 0.12065mm
requirement? (see pic)
(4.75mil)
For the above We are forbidden to Soldermask is The spacing between the Yes, It's more challenging to Pin to line gap For 2DPC DDR5 design, Intel PDG
question, Intel do this type of required to pin and trace must be routing the DDR5 trace for 4 must be still shows TBD and no RVP board
is planning to route design. prevent short larger than 0.1143mm Layer PCB designs 0.127mm (5mil) file available for us to download.
traces between during (4.5mil), and the minimum to We will need to try this routing by
these pins (please assembly minimum trace width avoid shorting ourselves. From Intel's
process must be at least risk documentation: "DDR5 UDIMM
refer to graphic
0.0889mm (3.5mil) at 2DPC Design Guidelines are TBD"
on the right), do you
least
have any concerns?
Key Message
• Customers tend to be cautious and have some concerns with large SMT connectors
• If large SMT connector pins are used, Customers need to have soldermask present between the pins
CQR|CustomerQuality&Reliability 19
Intel Confidential

## Page 20

Printed Circuit Board Design (8)
Area of Interest LENOVO (MSI) DELL ACER (WISTRON) ASUSTEK MSI ASROCK
Reliability Do you perform any Yes Yes Yes Yes Yes Yes
reliability validation
on your sockets?
Are your reliability Both Board & Both Board & System Level Both Board & System Board Level Board Level Board Level
tests performed at a System Level (For Board level we use daisy Level
board and/or system chain test vehicles)
level?
Do you use the Intel Proprietary design Proprietary design for Acer is using both the Intel design for thermal Proprietary Proprietary
reference thermal for thermal solution thermal solution. It depends Intel reference thermal solution design for Design for VR
solution (heatsink on the amount of heat solution (for mobile) and thermal solution
design) or proprietary dissipation required vs fan proprietary design (for Not
design? speed to remove the heat. special form factors). The Answered for
Still being reviewed. Tower solution is Acer's thermal
AVAP (AVAP is Acer's solution
assigned Vendor).
If you use proprietary Thermal solution Thermal solution AIO (All in One) and BOX By model (Mass/Height etc.) Thermal Not available
thermal solutions characteristics are characteristics are form (small form factor like and Center of Gravity (CG), solution yet.
could you provide any case by case factor dependent. Thermal Intel's NUC design) will will follow Intel's design for characteristicts:
further information on Engineering still reviewing follow Intel's rules and thermal solution aluminum
your thermal solution options. Dell doesn't have a design requirements for design,
characteristics? minimum thermal solution Thermal solution extended
range and they typically don't characteristicts. If no heatsink,
exceed 550g. But for ADL-S specific design, will thermal pads.
(125W SKU) Dell is looking at follow NB standard
going up to a ~900g thermal design for Thermal
solution. solution.
Key Message
• Customers perform board level reliability testing (some also perform system level testing)
• Customers use both proprietary and Intel designs for their thermal solutions
CQR|CustomerQuality&Reliability 20
Intel Confidential

## Page 21

Printed Circuit Board Design (9)
ACER
Area of Interest LENOVO (MSI) DELL ASUSTEK MSI ASROCK
(WISTRON)
Reliability Which 1. Guardband: 0℃, 25℃, 60℃ Board level: Both reliability 1. Non-Operation Shock Test: 1. Windows Shutdown 1. Shock
type of Burninfor 20 mins 1. HALT Test: Temp (-15C to 75C) with 6 tests and stress Trapezoidal Shock (Square 2. Xcopy 2. Vibration
reliability 2. IC Guardbandtest: 0℃, 25℃, minutes Dwell, Vibration (30Grms, 5min). levels Wave Shock) 3. Heaven Benchmark
tests and 60℃Burninfor 1 hour Measuring all chains contact resistances a) Maximum faired 4. 3DMark
stress 3. Storage temperature & for continuity 10 cycles. Pass criteria: no Acer will acceleration: 50G 5. Windows reboot
levels do humidity test: -40 ~ 60 ℃for 96 opens provide b) Velocity change: 170 6. S3
you hours 2. Temperature/Voltage Margin Test additional inches/sec 7. Shock 10 times
perform 4. System Operation Vibration 3. Hot & Cold Operation (40C 24hsr, 0C details, and c) Test direction: 6 orientation 8. Vibration (X, Y, Z) 0.5
and Test: Grms= 0.27, 30 minutes per 24hrs) Intel can then face hrs
expect to axes. 4. High Humidity Operation (32C 80% provide the 2. Non-Operation Vibration 9. etc...
meet? 5. System Fragility Vibration Test: 24hrs) feedback (Mak Test:
Please list Grms= 1.04, 15 minutes per axes. 5. Power Cycling Test (40C 80% 1650 to follow up w/ Non Operating Random Mode
and 6. System Operation Shock Test: cycles , 0C 1650 cycles) Morris Yang). a) Axis: X, Y and Z.
describe 3ms(15G) for 4 Axis (+X, -X, +Y,-Y) 6. Thermal Cycling: Temp (0C to 100C), b) Fixture used (wooden or
each test. , 3ms(30G) for 2 Axis(+Z, -Z) ,half- 1000 cycles. plastic): fasten the unit to the
sine wave, each side will do 1 Measuring all chains contact resistance for table.
times. continuity. Pass criteria: no opens. c) 10 min/axis
7. System Fragility Shock Test:
45G/11ms, Trapezoidal wave, 6 System level: Vibration Frequency Levels
Sides, each side shock one time. 1. Non-Operational Random Vibration Tested:
8. High/Low temperature: Run (1.37Grms, 15min) 1) 5 Hz (Frequency), "-"
3Dmark 8hour under 40°C / 0°C 2. Non-Op Half Sine Shock Test dB/Oct (Slope), 0.01 G
9. Etc… (105G,2ms) squared/Hz (PSD)
3. Strain Measurement Test SetUp 2) 20 to 500 Hz (Frequency),
(105G,2ms) "-" dB/Oct (Slope), 0.02 G
4. Hot & Cold Operation (40C 24hsr, 0C squared/Hz (PSD)
24hrs)
5. High Humidity Operation (32C 80% 3. Thermal Shock Test
24hrs) Non-OP: -40℃~85℃,
6. Power Cycling Test (40C 80% 1650 1.5hr/cycle, 27 cycles
cycles, 0C 1650 cycles)
Key Message
• Customers perform vary different reliability tests
CQR|CustomerQuality&Reliability 21
Intel Confidential

## Page 22

PCBA Factory Automation
Process ECS LCFC FXWH LITEON
PCBA Automation Yes Yes Yes Yes
Full or Partial Full Partial Full Partial
automation
Test Automation (in-line In-line In-line In-line In-line
or off-line)
Automation machine Panasonic SMT machine mounter, printer, SPI, not answered SMT: NXT Gen I, II, III
TRI SPI/AOI reflow, AOI, ATE Panasonic :NMP&CM602
DIP:CY-450(超越)
What is used to pick vacuum nozzle vacuum nozzle vacuum nozzle GPRO SMT -- Intel PCH /
Intel’s component LAN Chip, vacuum nozzle
Purpose of scanning 2D traceability traceability, inventory traceability traceability, inventory
Matrix check check
Which process require IQC/SMT SMT incoming inspection to IQC, SMT, DIP, FPT
2D scanning ? outgoing shipment
In-line or Off-line In-line In-line In-line and Off-line Both In-line & Off-line
traceability? traceability
Key Message
• For PCBA factory, 2 Customers have full automation and 2 Customers have partial automation
• In-line traceability capabilities are most common to have across the customers
CQR|CustomerQuality&Reliability 22
Intel Confidential

## Page 23

Paste Printing Process
Parameter / Capability ECS LCFC FXWH LITEON MSI (LENOVO)
Squeegee Speed (mm/sec) 60-120 120 80-90 100 50
Squeegee Pressure (Kg/area?) 4.5-8kg/cm2 2 8~10g/mm 10 10
Stencil Separation Speed (mm/sec) 0-3 1 1 2 not answered
Under Screen Cleaning frequency 2-6 5 1 6 not answered
(per print)
Stencil Cleaning Frequency (hrs) 1 4 6 100 not answered
Cleaning Process Pneumatic Solvent clean Ultrasonic Manual wiped paper & Ultrasonic not answered
PCB support type Pin, Pin Pin, Pin, Pin
Vacuum Vacuum Vacuum
Do you use the same pallet for no no no yes not answered
paste print, PnP and reflow?
Maximum board handling (mm, 510 x 508.5 460 x 360 yes 610 x 510 not answered
length x width)
Stencil Cut / Coating Laser Nano coating yes Electroform, Laser cut Etching Laser. No
with electro polish + nano coat electropolish.
Stencil Thickness (mm) 0.13 0.13 0.10, 0.13, 0.15 0.10 (BGA), 0.13 (skt), 0.15 (other) Secondary: 0.12/0.15
Primary: 0.12
Stencil Step up/down (mm) Yes no Yes. Depends components, Yes. Depends components, 0.10 not answered
0.10/0.15 0.10, 0.13, 0.15 (BGA), 0.13 (skt), 0.15 (other)
Solder Paste Vendor not answered not answered Eunow EUP-148 not answered Shenmao PF606-P
Solder Paste Type type 4 SAC type 4 SAC305type 4 Type 4 SAC305 Type 4
Key Message
• Pin PCB support type is most common and several customers also using vacuum support
• Customer preferred stencil thicknesses: 0.10, 0.12, 0.13 & 0.15mm
• Many customers are not sharing their paste vendor info with Intel
CQR|CustomerQuality&Reliability 23
Intel Confidential

## Page 24

Pick & Place Process
Parameter /
ECS LCFC FXWH LITEON MSI (LENOVO)
Capability
Nozzle size (LGA socket & 1005 NPM 1003 Universal 1240F & Nozzle: 15.0G (skt) FUJI NXT1. Nozzle types
Intel component) Fuzion1-11 and Nozzle: 7.0G (BGA) 0.7/1.0/1.3/2.5/5.0/7.0 /10.0
Sony CF00900
Max Socket & BGA size 90-120 45 x 45 55 x 55 74 x 74 not answered
capability (x,y, mm)
Max Socket & BGA weight 28mm ? 30 not answered 60 not answered
capability (grams)
What component 0.5mm ? 0.3mm? 150g N/A Factory target is 0
placement force is used for
Intel components?
What method of board Tray Pin Pin Pin not answered
support is used during
placement?
Maximum board handling 510 x 590 Dual land : 510 x 300 610 x 813 (universal) 534 x 510 not answered
capability (length x width, Single land : 510 x 590
mm)
Min pitch/ball recognition 0.3-1.5 Not answered 0.4 0.3 not answered
capability (mm)
Key Message
• Minimum ball pitch recognition capability is 0.3mm
CQR|CustomerQuality&Reliability 24
Intel Confidential

## Page 25

Reflow Process (1)
Parameter / Capability ECS LCFC FXWH LITEON MSI (LENOVO)
Yield target 99.9% (1K DPM) Not Answered 99.9% (1K DPM) 98% not answered
Do you use a PCB support pallet Yes No Yes & No Depends (see below) No
at reflow?
Is the PCB support pallet No N/A No Yes - Pallet used for No
decision based on PCB thickness thin/big PCB
or something else?
PCB support pallet material? Synthetic stone N/A Not Answered Synthetic stone (合成石) not answered
Are PCB support pallet tooling No pins used N/A Yes, pin support Yes, pin support not answered
pins used, or can the board
move in the X or Y direction?
PCB support pallet minimum Not Answered N/A No ? 1 not answered
board clearance to pallet edge?
(mm)
PCB support pallet, Not Answered N/A No clamps used Not Answered No clamps used
type of clamps used?
Oven Purging with N2? Yes Yes No Yes Yes
O2 PPM control <1000ppm <3000ppm N/A <3000ppm <1000ppm
Key Message
• 4 Customers using N2 (1K-3Kppm O2) @ Reflow and 1 Customer using Air @ Reflow
CQR|CustomerQuality&Reliability 25
Intel Confidential

## Page 26

Reflow Process (2)
Parameter / Capability ECS LCFC FXWH LITEON MSI (LENOVO)
Belt Speed (cm/min) 85 130 85-90 100 105
Ramp Rate (°C/sec) 1-3 1-3 1-3 1-3 not answered
Cooling Rate (°C/sec) -1 to -3 -1 to -3 -1 to -3 -2 not answered
Peak Temp Range (°C) 240-245 230-250 235-250 235-245 235-250
Regarding the question above, N/A 1. oven character N/A N/A not answered
if you must run above 245°C, 2. reflow profile
please explain the reason. needed
Time above Liquidus (sec) 72-87 60-90 60-90 60-90 60-100
Soak Temp Range and Time (sec) 85-105 60-100 60-120 60-90 60-120
How many TC and what loc’s or used 8 (BGA, IC, Chip, 10 (CPU, GPU, 3 5 Follow Intel’s
on the Intel Parts during profiling? PCB) RAM) recommendations
What is the delta T across the Intel <10 not answered <10 <10 not answered
component/socket area? (°C)
What is the delta T across the whole <15 <10 <15 <15 not answered
motherboard? (°C)
What is the number of heating and 12 heating, 2 13 heating, Heller 1913. 12 13 heating, 4 cooling Heller 1900EXL. 12
cooling zones used? cooling zones 4 cooling zone heating, 2 cooling zones ? zone oven
Maximum board handling capability 457 x 510 width 500 406 x 610 width < 460 not answered
(length x width, mm)
Key Message
• Customer’s reflow belt speeds range from 85 to 130cm/min
• Customer’s peak reflow temp range from 230-250°C
• Customer’s delta T across the Intel component/socket area <10°C
CQR|CustomerQuality&Reliability 26
Intel Confidential

## Page 27

Wave Solder
Parameter / Capability ECS LCFC FXWH LITEON
Preheat Time (sec) 60-120 120 60 - 80 90-150
Solder Pot Temperature (°C) 260 - 270 260 - 270 270 – 310 260 - 270
Conveyor Speed (cm/min) 100.8 80 120 – 160 100 -140
What are the components and pitch DIP plug-in not answered not answered DIP Parts is OK.
that undergo wave soldering?
Are components hand placed or Manual & Auto – Manual Manual Manual & Auto –
machine placed? component component
dependent dependent
What is the O2 PPM control? no control no control no control no control
Yield Target 99.9% (1K DPM) not answered 99.9% (1K DPM) 98%
Key Message
• Customer’s wave conveyor speeds range from 80-160 cm/min
• There is no O2 ppm control for wave
CQR|CustomerQuality&Reliability 27
Intel Confidential

## Page 28

Board Level Adhesives
Process / Capability ECS LCFC FXWH LITEON
Are you currently using adhesive for No No No No
Sockets?
Are you currently using adhesive for Yes Yes Yes Yes. Depends on
BGAs? different BGA.
What are the primary reasons strengthening solder crack N/A? N/A?
adhesive is applied?
What type of adhesive do you use? Corner glue Under fill ? Corner glue Corner glue?
Is the adhesive dispensed manually Automated Automated Automated & Automated & Manual.
(by operator/hand) or automated (by Manual Depends on the
machine)? production forecast.
What is the vendor name and model Easyseal (易品) AXXON ME EAST PIVOT(易品) and
of adhesive material you are using? E-8369 MODEL:4058-2 Series
Is the adhesive reworkable? Not answered Yes No Yes
Where in the board manufacturing After SMT/Before Before Test After SMT/Before Before DIP (wave)
process is the adhesive applied? Test Test
Key Message
• Customers are not using adhesives for sockets, but they are using it for BGAs
• It is most common for customers to apply adhesives before Test
CQR|CustomerQuality&Reliability 28
Intel Confidential

## Page 29

ILM Cover/Lever/Assembly
Parameter / Capability ECS LCFC FXWH LITEON
Do you have any feedback on the Socket V Yes. Logo? No not answered not answered
ILM Cover design features or markings?
What is your ergo spec (maximum limit) for by manual operator not answered not answered Torque 5KG via electrical
install or remove ILM Cover (all 4 snap screw driver
features) by manual operator?
Do you prefer the ILM Covers to be No not answered Yes No preference
recyclable (per ISO 11469)?
Should the ILM Cover "pop off" (disengage) Yes not answered Yes Yes
when an Intel CPU is placed inside the
socket and the ILM cover is closed?
Did you see any ESD failures related to No not answered No No
Socket H ILM Cover?
Do you use a fixture for the assembly of the Yes, fixture not answered No (why no?) Yes, fixture
ILM components? If yes, what kind of
fixture?
What is your ergo spec (maximum limit) for not answered not answered not answered Torque 5KG via electrical
opening or closing the ILM lever by manual screw driver
operator?
What is the time required for attaching the 24 not answered not answered 18
ILM Assembly onto the motherboard? (sec)
Key Message
• Mixed feedback regarding ILM cover recyclability requirement
• Customers prefer the ILM cover to “pop off” with CPU inside socket & ILM cover closed
• Customers have not experienced any ESD failures related to the socket H ILM cover
CQR|CustomerQuality&Reliability 29
Intel Confidential

## Page 30

Process Inspection / Monitoring
Process Parameter / Capability ECS LCFC FXWH LITEON MSI (LENOVO)
SPI (Solder Sampling rate 100% 100% 100% 2 PCB/2.5hrs not answered
Paste Machine not answered not answered Holly S8030 not answered MSI-AOI
Inspection) Min/Max Spec and control limit 60%-180% not answered 50%-180% (paste 0-0.3mm (0,13 60%-150% (paste
area). 50%-160% skt, 0.1 BGA) ? area). 60%-180%
(paste height). (paste height).
Is SPI Performed on selective 100% 100% 100% Selective not answered
components or 100%?
What is the typical percentage 0.10% not answered not answered not answered not answered
rate of board wash?
Maximum board handling 510 x 460 width 500 510 x 460 460 x 510 not answered
capability (length x width, mm)
AOI In-line / offline ? In-line In-line In-line In-line not answered
(Automated
Sampling rate ? 100% 100% 100% 100% not answered
Optical
How many AOI's are used? not answered 2 2 1pcs/ 1 line not answered
Inspection)
Where is AOI located? After reflow after reflow/ After reflow After reflow not answered
before wave
Is AOI Performed on selective 100% 100% 100% 100% not answered
components or 100%?
Maximum board handling 510 x 460 width 500 510 x 460 460 x 510 not answered
capability (length x width)
Key Message
• SPI control limits range between 60%-180%
• AOI is performed on 100% of components and located after reflow
CQR|CustomerQuality&Reliability 30
Intel Confidential

## Page 31

PCBA Test Process
Process Parameter / Capability ECS LCFC FXWH LITEON
Bed of Nails Test For test, are you doing any kind of bed of nail Yes Not answered ICT Yes
testing?
For the above question, on which side of board Bottom & Top Not answered Bottom Bottom & Top
is the testing being done?
How many Bed of Nails tests are used? Maximum support 3584 Not answered 1800 -3000 Depend on
test nails production
Where is the Bed of nails test located? After dip before Not answered ICT After re-flow. Before
functional test function test.
Is Bed of Nails test Performed on selective not 100% , need detail Not answered 1 Required 90%. In
components or 100%? mode to analysis actual depend on
production
Maximum board handling capability (length x 520 x 400 Not answered 388 X 320 (Matira5) 500 x 380
width, mm)
Functional Test Factory beat rate target to meet maximum 15 Not answered ILM not suitable for 12
through put requirement for this entire process: PCBA test, the test is
Open ILM load plate --> Install or Remove an using automated
Intel LGA CPU --> Close ILM load plate (sec) fixture
For Test CPU and Test Heatsink Installation at When PCBA testing , we Not answered OBE test typically 1 minute to
Functional Test: What is the time required for place fan on CPU w/o complete within 10 complete
this entire operation? screw whole 4 corner sec
Key Message
• Most customers are preforming bed of nails and functional tests
• Beat rate to install or remove an Intel LGA CPU from the socket ranges between 12-15 seconds
CQR|CustomerQuality&Reliability 31
Intel Confidential

## Page 32

PCBA X-Ray
Process / Capability ECS LCFC FXWH LITEON MSI (LENOVO)
Brand/Model not answered not answered Brand: Dage, Model: not answered Brand: ELT/艾而特,
XD7500, 2D Model: ST100A, 2D
Performed In-line / offline Offline Offline Offline Offline not answered
Sampling rate 5 /day/line 5 / hrs 2 /6 hrs 3~5pcs/ hrs not answered
Is the Detector -Camera based or Flat Panel? not answered Is based Flat Panel not answered
Detector Resolution (Mega Pixel) 1um not answered 0.95um Pixel:1004*1004 not answered
Campo di Visione
(max): 102 x 102 mm
Built in filter to limit X ray Dosage & filter 1usv/h not answered None None not answered
material/thickness (mm)?
What is the maximum angle (+/-degrees) for 70 angle, (2.5D) not answered 0-70° 140° (Right:70°， not answered
Oblique (2.5D) viewing? viewing Left:70°)
What is the minimum distance of Xray tube not answered not answered 0.95 2000 not answered
Source to Object (BGA device)? (µm)
Is the Source emitting X ray radiation applied not answered not answered PCB bottom side PCB top side not answered
from top to BGA device or is it from bottom
below the PCB?
Is there a limitation specification for X-Ray ＜5uSv/h not answered Yes from bottom below not answered
(RADS/mGray) Dosage exposure? the PCB
What is the cumulative specification for not answered not answered 1uSv/ h < 1 µSv/ h not answered
maximum exposure in RADS/mGray per scan as
measured by a dosomiter?
Are Global metal shields used between X-ray not answered not answered Yes Yes not answered
source and target SOC/Memory devices to limit
dosage exposure?
Key Message
• Customers are performing PCBA x-ray inspections Offline
CQR|CustomerQuality&Reliability 32
Intel Confidential

## Page 33

Rework
Process Parameter / Capability ECS LCFC FXWH LITEON
Machine / Peak Temp Range (°C) High Temp process (235-245) 230-250 235-245 235-245
Profile Low Temp process (175-185)
Time above Liquidus (sec) 60-80 60-100 60-90 60-90
Soak Temp Range and Time (sec) 90-120 not answered 90-120 90-120
Max BGA weight capability (grams) 45mmX24mm 30g not answered N/A
Is rework done in air or N2? If N2, what is O2 PPM? N2, 0.3-0.5PPM Air not answered Air
Flux Apply flux on PCB pads? Yes Yes Yes No
LTS Any plans to use LTS (low temperature solder) paste Yes No No No
(e.g. peak reflow temp <= 190 Deg C)?
Process Print solder paste directly to Solder balls? Yes No Yes No
Print solder paste directly to PCB pads? Yes Yes Yes Yes
Rework Stencil Thickness used (mm)? 0.12 0.13 0.15, 0.18 0.10
Use a pallet to support the board on the tool or Yes Yes Yes Yes
other kind of fixtures?
Nozzle size used is the exactly same size of the 2, 3 not answered 2, 3 not answered
package to repair bigger than it? (mm)
Do you perform a manual site dress process or auto Semi-auto not answered Yes N/A
scavinging?
Rework Yield N/A ? not answered 99.9% (1K DPM) 98%
Target
Key Message
• Rework stencil thicknesses used: 0.10, 0.12, 0.13, 0.15, 0.18
• One customer performing rework in N2, others in Air
• Pallets are used for board support during rework
• Customers print solder paste directly to the PCB pads for rework (a few can also print onto the solder balls)
CQR|CustomerQuality&Reliability 33
Intel Confidential

## Page 34

Others
Process ECS LCFC FXWH LITEON
Misc Do DDR or connectors have a not answered not answered Yes No
different mfg. process than the Intel
CPU?
Heatsink How many times during the PCBA not answered not answered Yes 1x
assembly process is the socket and
package enabled and un-enabled
(with a heatsink)?
Shipping How do you ship your boards out of not answered not answered Without CPU Without CPU
the factory (with respect to the CPU
and Heatsink installed)?
MAS / Video Do you find the Desktop MAS helpful not answered not answered Yes Yes
to understand the PCBA & System
Assembly info and requirements?
Do you think a System Assembly not answered not answered Yes Yes
video (provided by Intel) is required or
optional?
Key Message
• Customers find the Desktop MAS helpful and think a System Assembly video is required (customer prefer
actual operator performing not animated)
CQR|CustomerQuality&Reliability 34
Intel Confidential

## Page 35

Socket-H5 (CML-S/RKL-S) Socket-V (ADL-S)
95mm
95mm
75mm
78mm
Any possibility in making both
hole pattern same for both
products to allow same
heatsink used ?
CQR|CustomerQuality&Reliability 35
Intel Confidential

## Page 36

LOTES solder ball size is
smaller than Deren & FIT,
customer’s concerns with
SJQ with the same paste
volume recommended in
MAS across all socket
supplier.
CQR|CustomerQuality&Reliability 36
Intel Confidential

## Page 37

Socket-H Socket-V
Lever latch Pin 1, diagonally
Lever latch inward outward (with opposite compare to Which Pin 1
(with right hand) left hand) skt-H & also PnP tool / label is
correct ?
stage
Consistent Pin 1
indication on tools and
PCB Pin 1
The Pin 1 mark
on tools are
inconsistent to
Pin 1 indicator
on PCB
Pin 1 Pin 1
Note:
1) Operator needs to rotate processor 180° from PnP tool/stage
This site facing operator
in order to align to PCB Pin 1.
(it will be inconvenient for same operator to process
2) Any possibility to make changes for socket-V the ILM to allow
skt-H and skt-V, and possibly error in execution, due
customer process transparency and mitigate execution error
to the need to rotate the processor 180° orientation)
for manual process ?eg. 180° marking orientation change on
ILM cover marking
CQR|CustomerQuality&Reliability 37
Intel Confidential

## Page 38

Skt-H, fool proof for
wrong orientation
Socket V0 ILM
Sub-Assemblies
Manual Asembly risk
Piece Parts Interchangability
1) PCB Top Side> Potential/risk for operator
1) Need to ensure all 4 mounting screws are
swapped lever frame and load plate locations
same part number# .
during assembly.
2) Allow mixed vendor for piece parts (including
2) Backplate> Potentially 180° orientation
different socket vendors to ILM vendors).
assembled.
CQR|CustomerQuality&Reliability 38
Intel Confidential

## Page 39

Automation Assessment/concerns:
1) Will the top plate & lever arm will stay permanently (height & Where is the locking position for
angle) when moving at conveyor belt to next process/operator load plate to push the ILM cover to
to install processor ? pop-up ? Should the cover pop-up
2) What is the height / angle of the top-plate and lever arm ? happen after lever is latch ?
(Machine PnP assessment)
CQR|CustomerQuality&Reliability 39
Intel Confidential

## Page 40

Socket-H Socket-V
4-screw
3-screw
2-pcs ILM : top plate
Customer needs to mix vendors
and lever frame
for backplate, load plate, lever
frame, screws & etc, is this
1-pcs ILM top plate allowable ?
CQR|CustomerQuality&Reliability 40
Intel Confidential

## Page 41

Socket-H MAS CDI# 561049 Socket-V, Socket-P and Socket P4/5 MAS
Is the pin contact always
contacted at the center of
the LGA pad or near pad
edge ? with the process
variation and X-Y shift,
will the pin be touching
LGA Au pad or outside the
Au pad (Solder resist area)
or adjacent Au pad ? --
Need Intel design to
>±0.125mm or ± 1.5 width of contact
>1 width of contact assess
Tighter pitch but more relax criteria ?
• original >1 width vs current >1.5 width
CQR|CustomerQuality&Reliability 41
Intel Confidential
