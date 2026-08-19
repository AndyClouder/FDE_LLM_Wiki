---
title: 模型API依赖七轴权衡
type: practice
status: established
confidence: 0.6
sources:
  - "[[AI Engineering]]"
source_count: 1
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [build-vs-buy, 供应商, 选型]
---

# 模型 API 依赖七轴权衡

## 核心打法
选 API 还是自托管,按七轴打分而非只看 benchmark:**"You can't freeze a commercial model"**——商用模型会悄悄更新,是投产架构里必须预先消化的事实。

## 七轴
1. **data privacy**:Samsung 员工把源码贴给 ChatGPT 后全司禁用;StarCoder 记忆了 8% 训练集
2. **data lineage & copyright**:Gemini 报告对训练数据只字未提;开源模型侵权时,被诉的更可能是使用者
3. **performance**:最强模型永远闭源——"If you have the strongest model available, would you rather open source it for other people to capitalize on?"
4. **functionality**:logprobs 常不开放;能否微调受制于厂商
5. **API cost vs engineering cost**:"APIs are expensive, but engineering can be even more so"
6. **control**:模型悄悄更新使 prompt 失效且不可复现,受监管行业不可用;Voiceflow 因 GPT-3.5-turbo-0301→1106 意图分类掉 10%(同一变更却让 GoDaddy 客服 bot 变好);Convai 被迫微调开源模型解决拒绝问题
7. **on-device**:端侧部署的隐私与延迟

配套:模型选择先分 **hard attributes**(license/规模/隐私政策,过滤)与 **soft attributes**(准确率/毒性,优化)。

## 验证案例
- Voiceflow / GoDaddy:同一底层模型变更,不同应用方向相反 → 换 API 提供商 = 重新验收(不同服务商优化技术也会改变同一开源模型的行为)
- Convai:API 可控性不足时被迫走向自托管微调

## 适用信号
- 客户问"用 GPT 还是开源自建"时;签含 SLA/合规条款的 AI 项目前;模型供应商发版公告之后(巡检 drift 三源之一,见 [[渐进式AI应用架构五步法]])
