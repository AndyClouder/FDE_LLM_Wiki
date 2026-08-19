---
title: "客服Agent全链路返审"
type: practice
status: established
confidence: 0.85
sources:
  - "[[Thinking in Systems]]"
  - 个人实践:客服Agent项目
  - "[[AI Engineering]]"
source_count: 3
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [打法, 系统思维, agent运维]
---

# 客服 Agent 全链路返审

## 核心打法
修 Agent 规则时,不只修那一条答案——同步返审**旧训练样本、评测集、工具权限**,给旧的判断补上返回路径,问题才不会绕一圈回来。

## 操作步骤
1. 定位问题答案/规则,先修当前症状
2. 沿系统链路排查同类"存量":
   - 旧训练样本里含过时判断的,返审并标注
   - 评测集覆盖不到该场景的,补用例
   - 工具权限允许旧逻辑继续生效的,收紧
3. 确认修复改变了回路结构(旧判断有纠错出口),而非只改了一个输出
4. 回归评测通过才算修完

## 理论补强(2026-08 深度摄取)
[[AI Engineering]] Ch6 系统化了 Agent 失败模式,与本打法的返审清单对应:**规划失败**(无效工具/无效参数/错误参数值/目标偏离/超时/**反思错误**——Agent 坚信已完成实则未完成)、**工具失败**(工具本身输出错/缺工具)、**效率失败**(步数/成本/时长)。排查前提是可观测性:"Always print out each tool call and its output"。"The more automated the agent becomes, the more catastrophic its failures can be" ——自动化程度越高,返审越不能省。

## 验证案例
客服 Agent 项目:改规则 + 返审训练样本/评测集/工具权限三件套,复发被止住。

## 适用信号
- 同类问题修完又复发
- 修复只动了一个输出点,没动数据与权限存量
- "打地鼠"感明显

## 关联
- 堵的坑:[[坑5-问题修复后复发]]
- 理论依据:[[存量流量与反馈回路]] · 派生自 [[Thinking in Systems]]
