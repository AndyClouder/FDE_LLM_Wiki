---
title: "Product-Kata六问"
type: practice
status: established
confidence: 0.85
sources:
  - "[[Escaping the Build Trap]]"
source_count: 1
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [打法, 产品流程, 实验思维]
---

# Product Kata 六问

## 核心打法
像武术形(kata)一样反复演练同一组问题,把"解决问题"而不是"执行需求"变成肌肉记忆。**所有设计和开发工作都服务于到达目标——很多尝试不应该被 shipping,杀掉坏主意就是业绩。**

## 操作步骤
设定目标后,循环走六问:
1. **目标是什么?**(对齐 [[战略阶梯从愿景到团队目标]] 的层级)
2. **我们现在离目标多远?**(评估现状)
3. **挡在路上的最大问题/障碍是什么?**(一次只攻一个)
4. **怎么尝试解决它?**(选工具/方案)
5. **预期发生什么?**(写下假设)
6. **实际发生了什么?我们学到了什么?**(回到第 1 问,进入下一轮)

配套四阶段,先判断自己在哪个阶段再选工具:**理解方向 → 问题探索 → 方案探索 → 方案优化**。
- 最常见错误:问题还没弄清就跳去做 A/B 测试;方案已经很确定还在"探索"
- 非核心价值环节直接抄最佳实践(Brian Kalma:"别为不属于你价值主张的东西设计独特方案");核心价值环节才值得多方案实验

## 验证案例
书中 Marquetly 团队用 Product Kata 从"建更多功能"转向:先研究得出两个产品倡议(增加内容量、更健壮的测评),每个倡议下探索多个选项,用团队目标逐版验证——而非直接执行第一个想法。

**全书精读补充(2026-08-20)**:
- **Kata 台账格式**(Table 18-1):现状 / 要学什么 / 下一步 / 预期 / 实学——支撑 build-partner-buy 决策(收购布达佩斯剪辑软件前,让 40 名教师真用:30 人当月发布,远超基线 25%)
- **首发不达标继续 Kata**:Marquetly 收购后首发采用率 60%(目标 75%),团队没有宣布失败而是继续用 Kata 诊断非采用者—— Kata 不止用于探索,也用于优化阶段
- "The best thing you can do… is kill the bad ideas!"——功能越少越好,防 feature fatigue;作者自评入行第一课是谦逊:"my role was not that of the big idea generator but that of the bad idea terminator… Data beats any opinion every time."

**V1 优先级与反例**(Ch19,2026-08-20 第二轮补入):
- V1 优先级用 **Cost of Delay**(Reinertsen 称"the one thing" 该量化的东西;Arnold & Yuce 的 urgency×value 定性矩阵)——Marquetly 砍掉第三方集成拼出首版
- 配套 **North Star 文档**(问题/方案/成功要素/产出结果,全公司可视化、随学习演化)+ **Story Mapping**(Jeff Patton)
- OKR 反例警示:key result 写成 "Deliver by June 2018"(纯 output)等于把 Build Trap 写进目标体系——key result 应是 outcome

## 适用信号
- 团队直接从需求跳到方案,没人说得清目标
- 实验做了很多,但不知道在验证什么假设
- 功能越堆越多,客户价值没涨

## 关联
- 堵的坑:[[坑3-交付了但业务没变化]]
- 理论依据:[[业务结果导向]] · 派生自 [[Escaping the Build Trap]] Part IV
- 与 [[评测驱动开发]] 同构:先写假设与度量,再动手——一个用于产品探索,一个用于 AI 工程
