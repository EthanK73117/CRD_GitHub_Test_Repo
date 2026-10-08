---
source_file: "2024_ww08_LNL-M_X-ray_Process_Questions_Harry_Replied.pptx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/Client (Mobile)/2024 0229 ODM X-Ray Inspection Instance Survey/2024_ww08_LNL-M_X-ray_Process_Questions_Harry_Replied.pptx"
file_type: "pptx"
size_bytes: 318116
content_hash: "d479aa0beae0"
converted_at: "2026-10-08T11:29:44"
---

# 2024_ww08_LNL-M_X-ray_Process_Questions_Harry_Replied

## Slide 1

**LNL-M Customer X-ray Inspection Process Questions**


## Slide 2

- X-ray machine make/model that will be used for LNL-M PCBA inspection?

- Data source: 2021 MTL CRD


## Slide 3

- Tube Voltage and Power of the X-ray machine (Max and Normal usage value for LNL-M)

- Data source: 2019 KBL G X-ray Exposure Survey


## Slide 4

- LNL-M PCBA inspection time (Total inspection time of LNL-M BGA including AXI and MXI)
- So far, I don’t see client ODM use AXI, all of them use offline MXI
- Total inspection time varies, typical normal operation (quick scan of SBB issue) 0.5~2min. Can up to 5~10min when engineering judgement is need to inspect suspect SJO issue

- Instant survey at 2/29/2024. The reply reflects ODM x-ray inspection practice for normal PCBs, doesn’t consider the requirement of SJ void inspection which is special for RH process


## Slide 5

- LNL-M PCBA inspection rate (100% or sampling). If yes for sampling, please share the sampling rate frequency
- In NPI build, 100% scan for SBB issue
- During HVM, only sampling check. Sampling rate depends on customer request. Typical operation is 1~2 Pcs per hour


## Slide 6

- Do you use any filters in the X-ray inspection (AXI and MXI) process to mitigate the Memory X-ray exposure risk? If yes, please share the filter thickness and material
- No ODM use filters
- Wistron said they can meet 3~12 RAD (30~120 mGy) with their latest machine (measured by dosimeter)

- Data source: 2020 ADL CRD


## Slide 7

- Do you have access to a dosimeter for X-ray exposure measurements? If yes, please mention the supplier and accuracy of the dosimeter
- No ODM ever have experience of using dosimeter, except Wistron
- X-ray machine vendor normally have connection with dosimeter suppliers


## Slide 8

- Do you have issues with inspecting the LNL-M package with the package facing away from the X-ray source (AXI and MXI)?
- Dage machine have the largest market share among ODMs, per my understanding, Dage machine have x-ray tube at bottom side, and all customers inspect PCBA with BGA facing up (BGA facing way from x-ray source). So it should not be a big issue

