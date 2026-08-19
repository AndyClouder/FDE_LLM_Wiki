---
title: AI裁判与比较评测
type: concept
status: established
confidence: 0.6
sources:
  - "[[AI Engineering]]"
source_count: 1
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [评测, ai裁判, 偏差]
---

# AI 裁判与比较评测

## 一句话内核
用 AI 评 AI 可行(GPT-4 与人类一致率 85%,高于人类之间的 81%),但**看不见裁判的模型与 prompt 就不可信**,胜率也换算不出业务价值。

## 展开
- **可行性证据**:MT-Bench 上 GPT-4 裁判与人类一致率 85% > 人类互相一致率 81%;AlpacaEval 的 AI 裁判与人类 Chat Arena 排名相关 0.98。弱模型可以评强模型——"judging is easier than generation"(人人都能评价一首歌,但不是人人能写歌)。
- **打分制设计**:分类 > 离散数值 > 连续数值;范围越宽越差,典型用 1-5 分;裁判 prompt 必须含任务 + 标准 + 打分制 + 带理由的示例。
- **裁判四限制**:
  1. 不一致——同一裁判跑两次分数不同;加示例一致性 65%→77.5% 但成本 ×4;
  2. 标准歧义——MLflow、Ragas、LlamaIndex 对 faithfulness 分别用 1-5 分、0/1、YES/NO,分数互不可比。"Do not trust any AI judge if you can't see the model and the prompt used for the judge";
  3. 成本延迟——生成 + 评估双倍调用,三条标准 = 四倍调用;
  4. 偏差——self-bias(GPT-4 偏爱自己 10%、Claude-v1 25%)、first-position bias(与人类的 recency bias 相反)、verbosity bias(偏好含事实错误的长答案)。
- **比较评测(pointwise vs comparative)**:LMSYS Chat Arena 匿名双模型对答 + 群众投票;rating 算法从 Elo 改为 Bradley-Terry。三大挑战:规模瓶颈(57 模型 = 1596 对,平方增长)、质控缺失(3.3 万条 prompt 中 180 条是 "hello",简单题刷分)、**胜率 ≠ 绝对性能**——B 比 A 赢 51% 无法换算成"多自动化多少工单",做不了成本收益分析。
- **适用边界**:偏好投票不适用于有客观对错的问题(数学题二选一是灾难);适用于"AI 当助手、用户懂行"的场景。

## 关联
- 是 [[评测驱动开发]] 中"方法与数据"环节的裁判选型理论
- 验收场景的推论:验收方与交付方必须用**同一裁判**(同模型 + 同 prompt + 同打分制),否则分数不可比——见 [[专利评审三道门]] 的评审前移思想
- FDE 主题:结果、责任
