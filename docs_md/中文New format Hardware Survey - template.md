---
source_file: "中文New format Hardware Survey - template.docx"
source_path: "C:/Users/ethankat/OneDrive - Intel Corporation/Documents/GitHub/CRD_GitHub_Test_Repo/source_docs/中文New format Hardware Survey - template.docx"
file_type: "docx"
size_bytes: 2109438
content_hash: "1771169e0843"
converted_at: "2026-10-08T11:28:47"
---

# 中文New format Hardware Survey - template

CPU-Stack Mechanical Hardware Survey

Intel Corporation

March 2022

Revision 1.0

Intel Confidential

Notice: This document contains information on products in the design phase of development. The information here is subject to change without notice. Do not finalize a design with this information.

Intel technologies’ features and benefits depend on system configuration and may require enabled hardware, software, or service activation. Learn more at intel.com, or from the OEM or retailer.

No computer system can be absolutely secure. Intel does not assume any liability for lost or stolen data or systems or any damages resulting from such losses.

You may not use or facilitate the use of this document in connection with any infringement or other legal analysis concerning Intel products described herein. You agree to grant Intel a non-exclusive, royalty-free license to any patent claim thereafter drafted which includes subject matter disclosed herein.

No license (express or implied, by estoppel or otherwise) to any intellectual property rights is granted by this document. The products described may contain design defects or errors known as errata which may cause the product to deviate from published specifications. Current characterized errata are available on request.

This document contains information on products, services and/or processes in development. All information provided here is subject to change without notice. Contact your Intel representative to obtain the latest Intel product specifications and roadmaps.

Intel disclaims all express and implied warranties, including without limitation, the implied warranties of merchantability, fitness for a particular purpose, and non-infringement, as well as any warranty arising from course of performance, course of dealing, or usage in trade.

Contents

Survey Purpose and Scope	5

Package Carrier	6

Processor Heatsink Module (PHM)	8

Manufacturing and Automation Discussion	12

Thermal Solution Development	14

TMSDG Thermal Solutions	17

CNDA Mechanical Documents & Development Hardware:  TMSDG, MAS, Drawings, CAD, TTVs, ETBs, etc.	19

Visual Markings & Plastic Colors	22

Other Related Feedback	24

## Survey Purpose and Scope

Understand customer perspective on the enabled CPU-stack hardware for:

了解客户对CPU 整体组件的观点

Whitley / Cedar Island:  Ice Lake, Cooper Lake

Eagle Stream / Fishhawk Falls:  Sapphire Rapids, Emerald Rapids

Includes:  Bolster Plate, Backplate, Carrier, Socket, Socket Cover, & HSHW (Heatsink Hardware: PEEK nut, Rotating Wire, Nut Captivation)

Intel would appreciate the chance to discuss the topics in this document in a future meeting.

英特尔希望以后有机会在会议上讨论文档中这个话题

Please consider them beforehand and align with your related stakeholders on a unified, one-voice insight for your company.  It is understood that some responses may have varying viewpoints.

可以事先和贵公司内部相关人员统一观点.  有时候回复里有一些不同的观点是可以了解的。

The answers provided will be considered in the development of CPU-stack hardware and requirements for future platforms.

所有提供的回复会被考虑加入到新组件开发或新平台开发中要求

Any request for feedback related to Intel’s competition is regarding their publicly released solutions and is not a request for their confidential information.

任何反馈信息，如有和英特尔友商讯息相关，需要的是他们已经发布的解决方案，而不需要他们的机密信息

## Package Carrier

| What are benefits/challenges of breaking the TIM bond when using an integrated TIM break lever?  Is this a useful feature compared to the use of a flathead screwdriver as on Purley 对于CPU固定框的TIM 分离杆去分离CPU，对您有什么收益和坏处？和Purely 时代用的扁平螺丝刀分离CPU相比，那一个结构比较好用？ | What are benefits/challenges of breaking the TIM bond when using an integrated TIM break lever?  Is this a useful feature compared to the use of a flathead screwdriver as on Purley 对于CPU固定框的TIM 分离杆去分离CPU，对您有什么收益和坏处？和Purely 时代用的扁平螺丝刀分离CPU相比，那一个结构比较好用？ |
| --- | --- |
|  |  |
| EagleStream - TIM 分离杆 | Purely - 扁平螺丝刀分离 |
| 答复： | 答复： |

| What logistical and inventory management impacts do carriers have on?   CPU 固定框进/出货的包装，对物流和零件管理有什么影响？ |
| --- |
| Factory / HVM integration?  对L6, L10, L12工厂/ 量产影响  答复： |

| Field service?  现场维护（指数据中心或其他系统维护场所）  答复： |
| --- |

| What might be improved on the carrier?  CPU固定框有什么需要改进的 ？ | What might be improved on the carrier?  CPU固定框有什么需要改进的 ？ |
| --- | --- |
|  |  |
| 答复： | 答复： |

## Processor Heatsink Module (PHM)

| Considering the hardware features and assembly/disassembly steps (alignment features, anti-mixing keys, anti-tilt wires, throughput time, etc.), what benefits, and challenges do you see with the PHM approach, including for:  关于那些heatsink 配件和组装/拆卸步骤（引导结构，防呆结构，防倾斜限位丝，组装时间等等），你认为PHM跟其他的 组装方式相比，有那些好处和难处？ |
| --- |
|  |

| Factory/HVM integration/Automation (Please consider both board and system assembly factories)  L6, L10, L12工厂/量产/自动化生产（请同时考虑PCBA和系统集成厂）  答复： |
| --- |

| Field service?  现场维护（指数据中心或其他系统维护场所）  答复： |
| --- |

| What are the benefits and challenges for automation with the PHM? What could be improved to better enable automation?  自动化安装PHM有什么好处和难处？那些改进可以帮我們更好的实行自动化？ |
| --- |
|  |
| 答复： |

| Considering overall benefits/challenges, is the PHM approach desired or valuable?  Why?  全面性来考虑PHM方式好处或难处，PHM可是您們需要的或是对您是有价值的吗？ 是什么原因呢？ |
| --- |
| 答复： |

| How does Intel's PHM solution compare to the related design and integration approach used by Intel's competition?  英特尔的PHM 解决方案和其他家使用的相关设计和集成方案相比您喜欢那样？ |
| --- |
|  |
| Things like Cycle Times of assembly, specific retention hardware (eg. backplate, bolster, carrier & etc), etc.   像比如组装次数， 具体组件等等  答复： |

## Manufacturing and Automation Discussion

| For the PnP cap removal tool, what benefits/challenges have been observed? Is the tool meeting your needs? What issues have been observed and what improvements can be made to ? 对于移除PnP盖子的治具，可有发现那些问题? 问题有那些？这个治具是否符合您的需求？需要做出什么改进 ？ |
| --- |
|  |
| 答复： |

| What automation processes/equipment have been implemented or are being planned for the board/system assembly and test processes?  有那些自动化工艺已经应用在生产线 ? 或在计划中 ？ |
| --- |
| 答复： |

## Thermal Solution Development

HSHW (Heatsink Hardware: PEEK nut, Rotating Wire, Nut Captivation)

散热器配件（PEEK 螺母，限位丝，螺母底座）

|  |
| --- |
| What are the tests you usually perform on these individual HSHW ?  你用什么测试标准来验证这些散热器配件？ |
| 答复： |

| What could be improved on the HSHW?  关于散热器配件（PEEK 螺母，限位丝，螺母底座）有那些需要改进的地方吗？ |
| --- |
| 答复： |

| Do the dimensional requirements for a thermal solution to support the HSHW create any design limitations or challenges?  散热器在设计中您是否有尺寸的要求/限制或困难？ |
| --- |
| Thermal solution dimensional requirements are specified in the ICD (Interface Control Drawing) published in a platform's Mechanical Drawings document. 散热器组件的尺寸需求都定义在 ICD（接口控制图）中，公开在机构2D文档中  答复： |

| what is your testing requirement for overall hardware stack?  what is the condition/setting ?  你们对整体散热器结构有那测试？是什么样的条件/设置？ |
| --- |
| 答复： |

| Are there any challenges in the overall enabled hardware stack to perform these tests （eg. Shock, Vibration, stiffness & etc） 这整个散热器应用还有什么困难？（例如冲击，振动和散热器坚固度） |
| --- |
| 答复： |

| How does mechanically designing a thermal solution for an Intel platform compare to Intel's competition?  (What works well, what is a challenge, etc.)  与友商相比，英特尔平台的散热方案机构设计如何？（那些做的好，那些需要改进） |
| --- |
| 答复： |

| Any other benefits/challenges or improvement of the HSHW?  这些散热器配件还有什么优点和需要改进的地方？ |
| --- |
| 答复： |

## TMSDG Thermal Solutions

| Considering the reference or proof of concept thermal solutions discussed in the TMSDG (1U/2U passive, 1U/2U EVAC, cold plates) 关于在 TMSDG中讨论的参考设计或概念验证的散热解决方案（1U/2U被动散热器，1U/2U EVAC, 冷板）的问题： |
| --- |
| What do you leverage from our published designs when developing your own solutions?   在您研发自己的散热解决方案中，沿用了我们发布的那些设计 ？ |
| 答复： |

| Do you purchase samples from suppliers listed in the TMSDG?  If so, which ones and what do you use them for?  你们是否向我们TMSDG里的供应商购买产品？如果是，你们买的是那款，用在什么地方？ |
| --- |
| 答复： |

| Are the thermal performance, drawings, and CAD and other details sufficient for your needs?  这些散热性能，2D，3D 和其他细节数据是否足够满足您们的需求？（比如：1U， 2U， EVAC?） |
| --- |
| 答复： |

| Any additional/other thermal solution feedback 是否还有其他和散热器相关的反馈？ | Any additional/other thermal solution feedback 是否还有其他和散热器相关的反馈？ |
| --- | --- |
| 答复： | 答复： |
|  |  |

## CNDA Mechanical Documents & Development Hardware:  TMSDG, MAS, Drawings, CAD, TTVs, ETBs, etc.

| Are there topics or details missing from collaterals that would help to have added?  If so what and why? 是否还有其他内容没有加入到以上文件？ 如果有，那是什么，又为何？ |
| --- |
| Hardware details  散热器配件细节  答复： |

| Design guidance / suggestions  设计指导/ 建议  答复： |
| --- |

| Test methodologies and related requirements clear    测试方法和相关要求是否明确  答复: |
| --- |

| Are the documents clear and easy to use?  Are there areas that could be improved?  以上这些文档是否清晰并容易使用？ 还有什么地方需要改进的 ？ |
| --- |
|  |
| 答复： |

| What are the benefits/challenges of the TTVs and ETBs?  What could be improved?  TTV和ETBs的对您有何好处和不足？有什么需要改良的？ |
| --- |
|  |
| 答复： |

| Is there any additional development hardware that would be helpful?  是否需要开发其他的有益的散热器测试硬件？ |
| --- |
| 答复： |

## Visual Markings & Plastic Colors

Considering the CPU and enabled CPU-stack hardware set, please comment on:

关于CPU和使用的散热器组件，请提出你的意见:

| Do the text and symbols on parts meet your needs?  (Part numbers, warnings, instructions, pin 1 indicators, etc.)   零件上的文字和符号是否达到您的需求？（产品料号，警告，介绍，第一Pin的标志） |
| --- |
| 答复： |

| Do all the heatsink hardware enabled colors meet your needs? Example below are some of the hardware & color used in Whitley platform.  散热器配件颜色是否符合你的需求？例如下面一些使用在Whitley平台的散热器配件的颜色 |
| --- |
|  |
| 答复： |

| Are there other families of colors that could be options on future hardware?  Or should be avoided? 这里是否需要选取一个颜色系列用在为未来的散热器配件上？或者要避免使用某种颜色？ |
| --- |
| 答复： |

| Any other related feedback?  是否还有其他相关散热器配件的反馈？ |
| --- |
| 答复： |

|  |  |
| --- | --- |

## Other Related Feedback

| Is there any other feedback you’d like to share?   你是否还有其他的反馈想分享？ |
| --- |
| 答复： |
