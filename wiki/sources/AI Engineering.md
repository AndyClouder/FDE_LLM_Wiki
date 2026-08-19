---
title: "AI Engineering"
type: source
status: established
confidence: 0.9
author: Chip Huyen(O'Reilly,2024-12)
format: pdf
path: inbox/AI Engineering.pdf
ingestion: full
sources:
  - 全书已精读(Ch1-Ch10 + Epilogue,2026-08-20 第二轮全书通读)
source_count: 1
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [书目, ai工程化, 生产部署]
---

# AI Engineering(Chip Huyen)

## 一句话内核
**Demo 能跑,不等于能投产。**"It's easy to build a cool demo with foundation models. It's hard to create a profitable product." AI 工程 = 基于现成基础模型的**模型适配 + 评测**,而非从零建模;方法论 = start-simple、按失败模式逐级加码、评测贯穿每一步。

## 全书逐章摘要(2026-08-20 全书精读)
- **Ch1 规划 AI 应用**:演化链 LM→LLM(自监督解标注瓶颈)→foundation model(多模态通用)→AI engineering(model as a service)。八类用例;企业偏好低风险(内部先于外部)。用例评估三档风险(生存>利润>FOMO)。AI 角色三轴(critical/complementary、reactive/proactive、dynamic/static)。Crawl-Walk-Run 渐进自动化。三护城河(技术/数据/分发)。期望设定先业务指标再 usefulness threshold(质量/延迟/成本)。**最后一公里规律**(LinkedIn:1 个月 80%,再花 4 个月才超 95%)。维护承诺:"riding this bullet train"(API 降价/供应商倒闭/GDPR/IP)。案例:GitHub Copilot 两年 $100M ARR;Chegg $28→$2;MIT 实验(ChatGPT 写作 -40% 时间 +18% 质量,主要拉高低能力者)
- **Ch2 理解基础模型**:训练数据(Common Crawl 英语 45.88% → 低资源语言系统性劣势:同题英文可解 Burmese 全错、Burmese 贵 10 倍慢 10 倍;中文 7/7 产假信息 vs 英文 6/7 拒绝)。Chinchilla scaling law(token≈参数×20;GPT-3 训练成本约 $4M)。scaling 两瓶颈:数据枯竭(C4 45% 受限)+ 电力(数据中心占全球耗电 1-2%)。post-training 两步(SFT→偏好微调;比较比打分容易:人工比较一对 3-5 分钟)。sampling(temperature/top-k/top-p)。**test time compute**:加 verifier ≈ 模型扩大 30 倍;采样增益有上限(400 outputs 后反降)。结构化输出五层(prompting→后处理→test-time compute→约束采样→微调)。概率本性;**幻觉两假说**(self-delusion/snowballing;知识错配、RLHF 加重 InstructGPT 幻觉)
- **Ch3 评测方法论**:四大难点(越强越难评/开放式无 ground truth/黑盒/基准快速饱和)。PPL 三规律三用途。exact evaluation(functional correctness 终极指标;BLEU 缺陷:HumanEval 对错代码分接近;embedding 语义相似度)。**AI as a judge**(GPT-4 与人类一致 85%>人类间 81%;打分制分类>离散>连续;裁判四限制:不一致/标准歧义/成本/四偏差——self-bias 10-25%、first-position、verbosity;专用裁判 reward/reference/preference model;"judging is easier than generation")。**比较评测**(Chatbot Arena;Elo→Bradley-Terry;规模平方瓶颈/质控缺失/**胜率≠绝对性能**——51% 胜率换算不出自动化率)
- **Ch4 评测 AI 系统**:evaluation-driven development(类比 TDD);"部署了但没人知道有没有用"比没部署更糟。可评测才被部署的偏置("路灯下找钥匙"错过 game-changing 应用)。评测标准四桶(领域能力/生成能力——factual consistency 分 local/global,检测用 GPT-judge 90-96%、SelfCheckGQ、SAFE、textual entailment;TruthfulQA;safety 六类;instruction-following——IFEval 25 类;成本延迟 Pareto)。模型选择 hard/soft attributes 四步。**build vs buy 七轴**(Samsung 泄密/"最强模型永远闭源"/"You can't freeze a commercial model"——Voiceflow 掉 10%、GoDaddy 反而变好/API 贵工程更贵)。**公共基准导航**(HF 6 个 vs HELM 10 个仅 2 重叠;Schaeffer 讽刺论文;GPT-3 有 13 个基准 ≥40% 入训练集;"A benchmark stops being useful as soon as it becomes public")。评测管线三步 + 指标映射业务指标 + OpenAI 样本量规则
- **Ch5 Prompt 工程**:人机沟通而非玄学("The problem is when prompt engineering is the only thing people know")。chat template 差异是静默失败源(Llama 2/3 模板不同,多余换行即显著劣化)。few-shot 增益在强模型上递减。**lost in the middle**(开头结尾最好,中间最差)。八条最佳实践(清晰/persona/例子/上下文/**任务分解**——GoDaddy 单 prompt 膨胀 1500+ tokens,十类意图分解后质量升 token 降/CoT 降幻觉/self-critique/迭代 + **prompt 版本化**——Instacart Prompt Marketplace)。工具警惕(隐藏 API 调用烧钱;"Show Me the Prompt")。**防御性 prompt 工程**:三类攻击(prompt extraction/jailbreak——PAIR <20 次查询破防/**间接注入**——攻击载荷埋在检索工具里:邮件助手、RAG 用户名投毒/divergence attack 记忆率约 1%);防御三层(模型层 instruction hierarchy 鲁棒 +63%/prompt 层/system 层——高危命令强制人工审批);**violation rate + false refusal rate 双指标**。"Write your system prompt assuming that it will one day become public."
- **Ch6 RAG 与 Agent**:任务完成 = 指令 + 信息;RAG 补信息、agent 补行动。**长上下文不会杀死 RAG**(数据只增不减;Anthropic:<200K tokens 可整库塞 prompt)。两类检索(term-based BM25 开箱即用 vs embedding 向量库贵——有公司向量库支出达 API 的 1/5-1/2;hybrid search + reranking)。检索优化四招(chunking/reranking/query rewriting/contextual retrieval——Anthropic 每 chunk 生成 50-100 token 定位说明)。工具三类(knowledge/capability/write actions——"Just as you shouldn't give an intern the authority to delete your production database...")。**Agent 需要更强模型两原因:复合错误率(95%^10=60%)+ 高风险**。任务流程四步(plan→reflect→execute→reflect;规划执行解耦防空跑烧钱;ReAct/Reflexion)。工具选择(消融/换错工具/tool transition 合并/Vogager skill library)。Agent 失败模式四类(规划——含反思错误:50 人分 40 却称完成/工具/效率/时间约束)。**Memory 三层**(internal/short-term/long-term;短期管理 FIFO 致命、摘要+实体追踪、reflection 合并)
- **Ch7 微调**:何时微调(输出格式/蒸馏 Grammarly/私有化/偏见矫正)、何时不(四重前置投入/alignment tax/**BloombergGPT 教训**)。**RAG vs Finetuning 诊断框架**:"finetuning is for form, and RAG is for facts"(Ovadia:base+RAG 胜过 finetuned+RAG 57% 的情况)。**适配五步顺序**。内存数学(训练=权重+激活+梯度+优化器;Adam 每参数额外 3 值)。数值格式(BF16 vs FP16 陷阱)。**PEFT**(LoRA:0.0027% 参数追平全量;r=4-64 通常够;multi-LoRA serving:100 客户 1 底座+100 对小矩阵;QLoRA 65B 单卡 48GB;intrinsic dimension 解释)。模型合并(task vectors:微调模型−底座=可加减的能力向量;TIES 保留 top 20% 参数;frankenmerging/sparse upcycling)。战术(OpenAI progression path vs distillation path;超参经验)
- **Ch8 数据工程**:quality/coverage/quantity 三金标准。质量六特征;少而精(LIMA 1000 条 43% 追平 GPT-4 但鲁棒性不达产品级)。Llama 3 三阶段配比(偏好微调 82% 通用)。数量三因素 + **50-100 条小数据试验先行**。获取(最优源=自己的应用数据 data flywheel;标注指南比标注难)。**合成数据**(五动机;reverse instruction;Llama 3 代码合成管线 2.7M 样本;**四限制**——表面模仿教幻觉/model collapse 全合成必崩混真实可免/lineage)。"People only synthesize data they can verify"。蒸馏(DistilBERT 小 40% 保 97%)。处理四步(inspect——"盯数据 15 分钟价值最高"/dedupe——0.1% 重复 100 次使 800M 退化到 400M/clean——标注 session 后半程质量下降/format——推理与训练格式严格一致)
- **Ch9 推理优化**:"No matter how good your model is, if it's too slow... its predictions might become useless"。online API vs **batch API 约 5 折**(合成数据/定期报告/批处理场景)。延迟 = TTFT + TPOT×token 数(TPOT≈120ms 达阅读速度);p50/p90/p99;agent 用 time to publish;**goodput = 满足 SLO 的吞吐**(100 RPM 只 30 条达标则 goodput=30)。**nvidia-smi GPU utilization 是假指标**(真指标 MFU/MBU)。内存三级(DRAM 25-50GB/s → HBM 256GB/s-1.5TB/s → SRAM >10TB/s)。推理占已部署 ML 成本最高 90%。模型级(speculative decoding 延迟减半/inference with reference 2×/**KV cache**——500B 模型 batch 512 时 KV cache 达 3TB;Character.AI 组合三招降 20 倍/FlashAttention)。服务级(**continuous batching**/prefill-decode 分离/**prompt caching** 最长省 90% 成本/最有效四件套:量化+tensor 并行+replica+attention 优化)。**同一开源模型不同服务商优化后质量有差异**——换供应商要重测
- **Ch10 架构与用户反馈**:渐进式架构五步(见打法页)。护栏细节/Router(小模型意图分类)/Gateway/缓存(exact vs semantic;**缓存泄密案例**)/可观测性(**log everything**/MTTD/MTTR/CFR/**drift 三源**)。编排器起步不用。**用户反馈**:双属性(评估产品+训练数据=护城河);自然语言反馈信号(early termination/**error correction 最强偏好信号**/complaints FITS 八类/sentiment);行为反馈;收集时机三刻(出坏事时必须给降级出路);收集方式(Midjourney 四图三选项/Copilot Tab;别问用户答不了的问题;私密反馈比公开真实);**偏差五类**(leniency——Uber 4.8 通胀/randomness/position/preference/degenerate loop);**sycophancy**(RLHF 模型说用户想听的话)
- **Epilogue**:"Many AI challenges are, at their core, system problems"——退一步看整个系统,才是解决真实问题、解锁新可能、保障安全的正途

## 堵哪个坑
[[坑1-Demo到生产翻车]](主)· 关联 [[坑2-假需求]](FOMO 三档风险)

## 已沉淀页面
- 概念:[[Demo与生产系统的鸿沟]] · [[评测驱动开发]] · [[模型适配的优先级顺序]] · [[AI裁判与比较评测]] · [[幻觉两假说]] · [[采样参数与结构化输出五层]]
- 打法:[[三层写回权限与回滚]] · [[渐进式AI应用架构五步法]] · [[模型API依赖七轴权衡]] · [[数据三金标准与合成数据边界]] · [[对话式反馈信号与反馈设计]] · [[Prompt工程八条最佳实践]] · [[推理经济学与省钱四件套]] · [[RAG检索优化四招]]
- 坑位:[[公域基准污染]] · [[Agent复合错误率]] · [[提示词攻击面与三层防御]]

**第二轮查缺补漏(2026-08-20)**:新建 5 页(攻击面/推理经济学/RAG 四招/采样五层/Prompt 八条);并入强化 3 页(数据三金·蒸馏边界、幻觉两假说·检测四法、模型适配·语言不平等)。

## 与库内其他源的关系
- [[80-95-99规律]]([[FDE模式行业观察与实践]])获得本书"0→60 易 / 60→100 难"的独立印证
- Agent 失败模式与 [[客服Agent全链路返审]] 的返审清单互补
- degenerate feedback loop / sycophancy 为 [[存量流量与反馈回路]] 提供 AI 实证
- 全书精读原始摘要已随会话临时文件清理;需复核时从 inbox/ 原书重新提取
