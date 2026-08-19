---
title: 运维反馈与BAU断裂
type: concept
status: established
confidence: 0.6
sources:
  - "[[Team Topologies]]"
source_count: 1
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [运维反馈, bau, 反馈回路]
---

# 运维反馈与 BAU 断裂

## 一句话内核
运维是开发的**感官输入**;交付后另设维护/BAU 团队会切断 Ops→Dev 反馈回路——新技术好坏由感受不到痛苦的另一批人承担后果,复发由此生。

## 展开
- **禁止把维护外包给低价团队或另设 BAU 团队**:新服务团队与 BAU 团队分离 = 反馈回路断裂
- 正确做法:**同一(组)stream-aligned 团队同时负责新服务与老系统**;把新遥测回装老系统;服务台由最有经验的工程师(单人或带新人)值守,而非新手
- Amazon 2002 年 Bezos 令的极端版:每个团队对自己服务的开发与运营全责("you build it, you run it"),一切服务走 API——两披萨团队运行 17 年
- 支持模式:stream 对齐的支持团队 + 跨团队动态 swarm 处理重大事故("Service Experience Teams")——激励各 stream 运行时独立,并把发现的问题快速回流开发团队
- DevOps Handbook 三路径:系统思维 / 反馈回路 / 持续实验与学习

## 关联
- 直接解释 [[坑3-交付了但业务没变化]](交付后无人感受结果)与 [[坑5-问题修复后复发]](反馈回路被切断的结构版)
- FDE 复诊机制([[客服Agent全链路返审]])正是把 Ops 变 Dev 输入的实践;交付后不回访 = 人为制造 BAU 断裂
- 与 [[存量流量与反馈回路]] 同族:信息流决定系统行为
