---
source_file: "Copy of May_2022_Competitor_insight_Survey_ HarryYu.xlsx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Copy of May_2022_Competitor_insight_Survey_ HarryYu.xlsx"
file_type: "xlsx"
size_bytes: 91954
content_hash: "c88e48c024dd"
converted_at: "2026-10-08T11:28:47"
---

# Copy of May_2022_Competitor_insight_Survey_ HarryYu

## Sheet: NB

|  |  | Is SMT process on competition products easy or not? And why? | Any need of following a tight SMT window to makes things work? | High or low failure SMT rate? (how does it compare to Intel) | Anything worthy that you might have heard what competition is doing that is different (good or bad) compared to Intel? |
| --- | --- | --- | --- | --- | --- |
| Compal KS | AMD | No use | No use | No use | No use |
|  | Nvidia | SMT process is worse than Intel, Warpage model  different compare to Intel. Nvidia: flat (RT) -> smile face (HT), Intel: sad face (RT) -> flat (sock temp) -> smile face (HT). Nvidia major issue is HoP at corner, Compal always suspect Nvidia chip have solder ball surface cleanness problem | Yes, need tight control compare to Intel. Stencil design, print quality etc.. ~0.65~0.75mm pitch ~2000 Pins | Higher, 3000 DPM VS 1000DPM (Intel) | Field team is lack of customer service attitude compare to Intel. Compal keep on fighting the SMT failures for many years. A little better recent 1~2 years |
| Inventec CQ | AMD | AMD is easy. Customer think it is because of bigger pitch, thicker substrate, smaller package size, square (or near to square) shape, single die | Same with Intel | ~ 500 DPM, same as Intel. Almost no excursion (Intel has excursions, example: ICL corner SBB, TGL UP4 die shadow SBB - guess because of HIMB/RIMB design, ADL P NWO) | Functional failure worse than Intel, No MAS support. Field technical support not as strong as Intel |
|  | Nvidia | Worse than Intel, thicker and bigger BGA, See NWO and HoP failure. With process improvement effort it is under control now | Same with Intel | ~500 DPM, avg same with Intel. Sometime have excursions | Has MAS but not as good as Intel |
| Pega CQ | AMD | AMD is easy. Guess because it has small size and single die. It is unfair compare Intel and AMD because AMD BGA is simple | No need tight than Intel | Customer didn't share | Intel is doing better in terms of new platform introduction and SMT sample support |
|  | Nvidia | Worse than Intel, Has HiP issue, now under control | Same as Intel | Customer didn't share |  |
| Huanqin | AMD | AMD is easy compare to Intel, less SMT failure,AMD has small BGA size, more square shape. bigger pitch, less pin | No need tight than Intel | Better than <300DPM VS  Intel ~500-600DPM | Function failure is more than Intel. After failure validation service is not as better as Intel |
|  | Nvidia | No use | No use | No use | No use |
| Wistron CD (From ChenXi) | AMD | AMD is much easier from SMT process, because of some reasons like: 1. Shape of package, most of product is square or close to square 2. the solder ball array is more regular than us 3. ball pitch is bigger , most of them are 0.8 mm 4. No or less warpage. | AMD is almost same reflow profile as us currently, and current is ok, make SMT window tight will make process control not easy and customer mfg much harder. | AMD SMT DPM is very low compared with us, and FR is closed to zero, very few failure from SMT | In general, Customer feel AMD design for SMT is better than us, the product is almost keep flat and no warpage when incoming, it’s easier for mfg with low FR from SMT perspective |

## Sheet: Server

| Customer feedback/request | Customer | Segment | Intel | AMD / Other notes |
| --- | --- | --- | --- | --- |
| PEEK nuts (Whitley, Cedar Island & EGS) | Foxconn | Server | Preferred metal nuts for L6 test, with high durability, follow Purley solution to hold/cumulate metal debris  Note: Currently PEEK nuts also generate debris, Quanta is putting the same Purley grease on PEEK nuts to hold debris. Due to in production, it is difficult to classify metal/plastic debris w/o FA. | Metal nuts |
|  | Quanta | Server & CSP |  |  |
|  | Inspur | CSP |  |  |
|  | Wiwynn | CSP |  |  |
| Ship CPU with carrier attached (EGS and beyond) or  intergrate 1 package type to 1 carrier | Lenovo | Server | Purley - 3 carriers Whitley - 1 carrier (CPX4 - 1 carrier but product dev discontinue) Cedar Island - 1 carrier EGS - 3 carriers BHS - TBD | Already ship with carrier |
|  | HPE | Server |  |  |
|  | Baidu | CSP |  |  |
|  | Quanta | Server & CSP |  |  |
| immersion cooling | Alibaba | CSP | Request thru SMG. Heard from FAE DPG sr PE/PE involved (Ahuja, Sandeep & Ahuja, Nishi) | unknown |
| immersion cooling & LTS (as one) | Quanta | CSP | Request thru SMG. Heard from FAE DPG PE involved | unknown |
| 2D Marking on IHS | Inventec | Server | 2D mark on substrate is difficult to scan,  2D mark on IHS is small, prefer larger 2D mark (for automation friendly) | large 2D Mark on IHS |
| TFT tray | Inspur | CSP | Too soft, easily deformed; difficult for automation | hard tray ? |
|  | Inventec | Server |  |  |
| PHM Concept | Inspur | CSP | Too complex to assemble; need to set-up offline assembly process  note: in early PHM intro in Purley, Foxconn/Quanta/Inventec preferred ILM (same as AMD and previous platform); now they had used to PHM; They also implemented basic function testers (BFT 2.0/automation test for 2S board for high volume; 1S/4S boards, still manual test) | ILM |
|  | Inventec | Server |  |  |
|  | Alibaba | CSP |  |  |
| PnP Tool | Quanta | CSP | Durability is not meeting expectation at all. 1 tool <1000x and unable to last for 1 WO build. Willing to pay more $$ for high durability design/material. For 2U board (2U typically high vol model), it can last <500 boards or lower#. 	 	 Purley PnP Tool (~1000x):	 - FXTJ, QTMC & Inventec has owned designed tool to replace the POR plastic tool. FXTJ metal ~USD200 fabricated by FIT. Inventec metal tool (no image provided) and QTMC (no detail)	 	 Whitley PnP Tool (<200-1000x):	 QTMC has owned design tool, FR4 material made. FXTJ made a metal tool (no image). Inventec made a metal too but found  imperfect & need Intel help	 	 Wiwynn, Huaqin: Need Intel to improve tool durability Wiwynn recommend to use better material not necessary metal (may cause ergo issue due to weight), | AMD provide metal tool (no image)  QTMC Whitley (FR4)          FXTJ Purley (Metal) |
|  | FXTJ | Server |  |  |
|  | Inventec | Server |  |  |
|  | Huaqin | Server & CSP |  |  |
|  | Wiwynn | CSP |  |  |
