---
title: RAG检索优化四招
type: practice
status: established
confidence: 0.6
sources:
  - "[[AI Engineering]]"
source_count: 1
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [rag, 检索, 上下文]
---

# RAG 检索优化四招

## 核心打法
任务完成 = 指令 + 信息,RAG 补信息;**起步用 BM25 而非向量库,把预算留给评测**——有些公司向量库支出达模型 API 的 1/5 到 1/2。**长上下文不会杀死 RAG**:数据只增不减("an application's context expands to fill the context limit supported by the model");能装下 ≠ 用得好;每个 token 都有成本(Anthropic:知识库 <200K tokens 可整库塞 prompt)。

## 操作步骤(检索优化四招)
1. **Chunking 策略**:小 chunk 多样性好 vs 大 chunk 保完整;**overlap 防边界信息丢失**;无万能值,按语料试
2. **Reranking**:初筛召回 + 精确重排;时间敏感场景按时间加权
3. **Query rewriting**:"How about Emily Doe?" 必须改写成独立成句的查询;**改写不出来该承认不可解,而非幻觉一个名字**
4. **Contextual retrieval**(Anthropic):为每个 chunk 生成 50-100 token 的定位说明前置,大幅提升可检索性
- 配套:hybrid search(term 召回 + 语义重排,RRF 融合);检索评测用 context precision / context recall,排序用 NDCG/MAP/MRR;term-based(BM25,开箱即用、难再提升)vs embedding(语义检索、可微调持续提升但贵,且会抹掉错误码/产品名等关键词)
- **Memory 三层管理**(并入):internal knowledge(训练所得)/ short-term(上下文:FIFO 可能致命——开头常是任务目的;用摘要 + 实体追踪、reflection 式合并 insert/merge/replace)/ long-term(外部检索);按使用频率分配:全部任务都要的进模型、罕用的进长期记忆

## 适用信号
- 知识型 AI 应用(客服/知识库/分析)投产;检索质量差先查 chunking 与 query rewriting,再谈换模型
- 与 [[模型适配的优先级顺序]] 衔接:接数据源时先 term-based RAG
