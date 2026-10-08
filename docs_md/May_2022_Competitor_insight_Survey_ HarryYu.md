---
source_file: "May_2022_Competitor_insight_Survey_ HarryYu.xlsx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (Mobile)/2022 Competitor Ease of Manufacturability/May_2022_Competitor_insight_Survey_ HarryYu.xlsx"
file_type: "xlsx"
size_bytes: 22436
content_hash: "3fdb98d34feb"
converted_at: "2026-10-08T11:29:44"
---

# May_2022_Competitor_insight_Survey_ HarryYu

## Sheet: Sheet1

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
