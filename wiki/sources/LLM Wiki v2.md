---
title: "LLM Wiki v2"
type: source
status: established
confidence: 0.9
author: rohitg00(扩展 Karpathy 原始想法)
format: md
path: 新建文件夹/LLM Wiki v2 — extending Karpathy's LLM Wiki pattern with lessons from building agentmemory.md
ingestion: full
sources:
  - 原文全文已读
source_count: 1
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [书目, 知识管理, 方法论]
---

# LLM Wiki v2

## 一句话内核
**停止重新推导,开始沉淀编译。** RAG 检索即遗忘,wiki 积累且复利;LLM 消灭的瓶颈是图书管理员式的簿记工作。

## 核心扩展(相对 Karpathy 原版)
1. **记忆生命周期**:置信度评分、supersession(新旧取代)、遗忘曲线、四级整合(工作/情景/语义/程序)
2. **知识图谱**:实体抽取 + 类型化关系,页面负责阅读,图谱负责导航
3. **检索规模化**:BM25 + 向量 + 图遍历的混合检索(>100 页后)
4. **自动化钩子**:摄取/会话开始结束/写入矛盾检测/定期 lint
5. **质量自愈**:内容打分、自动修孤儿页断链、矛盾自动裁决(新近性 > 权威 > 证据数)
6. **结晶(crystallization)**:探索过程本身即源,工作链路蒸馏成一等公民页面
7. **Schema 是真正的产品**:AGENTS.md/CLAUDE.md 把通用 LLM 变成守纪律的知识工作者

## 与本库的关系
本库按其实施光谱构建,当前达到 **L2(最小可用 + 生命周期 + 结构)**。落地映射见 [AGENTS.md](../../AGENTS.md) §10。
