---
title: Agent复合错误率
type: pitfall
status: established
confidence: 0.6
sources:
  - "[[AI Engineering]]"
source_count: 1
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [agent, 可靠性, 复合错误]
---

# Agent 复合错误率

## 症状(怎么死)
演示里单链跑得通的 Agent,投产后续错误频发:每步 95% 准确率,10 步只剩 60%,100 步只剩 0.6%——"The more automated the agent becomes, the more catastrophic its failures can be"。

## 成因
Agent = 感知环境并作用于环境,由环境 + 工具集刻画。失败四类:
1. **规划失败**:调用不存在的工具 / 有效工具配无效参数 / 参数值错误 / 目标偏离(去了错误城市、超预算)/**反思错误——50 人分 30 间房只分了 40 人,却坚称已完成**(最阴险)/ 时间约束(grant 截止后才交稿)
2. **工具失败**:工具输出本身错;缺工具——某领域常败可能是缺该领域工具,要观察人类专家用什么工具
3. **效率失败**:平均步数 / 成本 / 时长劣于人类基线(注意人机结构不同:人一次看一页,AI 可并发百页)
4. **传递放大**:复合错误率使每个小缺陷在多步链路上指数放大

## 解释概念
[[Demo与生产系统的鸿沟]] 的数学表达:Demo 只验证单链,生产要看复合可靠度。规划-执行解耦(计划先经启发式 + AI 裁判验证再执行,防 1000 步空跑烧钱)、ReAct、Reflexion 是结构性缓解。

## 怎么堵
- 按失败四类**逐类建评测基准**,不混在一个"准确率"里
- **每次工具调用及输出全部留痕**("Always print out each tool call and its output")——事后可归因
- 工具集做减法:消融实验(去掉无性能损失的工具就删)、换掉模型总用错的工具、统计 tool call 分布与 tool transition(常连用的两个工具可合并)
- 验收必须 functional correctness(可执行验证),不能信 Agent 自述完成
- 高风险写操作(删库/发邮件/转账)强制人工审批:"Just as you shouldn't give an intern the authority to delete your production database, you shouldn't allow an unreliable AI to initiate bank transfers."——落地见 [[三层写回权限与回滚]]
