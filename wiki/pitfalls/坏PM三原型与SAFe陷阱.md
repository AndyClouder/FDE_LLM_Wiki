---
title: 坏PM三原型与SAFe陷阱
type: pitfall
status: established
confidence: 0.6
sources:
  - "[[Escaping the Build Trap]]"
source_count: 1
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [pm角色, safe, 组织设计]
---

# 坏 PM 三原型与 SAFe 陷阱

## 症状(怎么死)
PM 被用错角色:90% 的招聘启事把 PM 写成 "Mini-CEO",实际招进去的人要么独断全队厌恶,要么沦为接单员和排期机器——产品无人守住 why。

## 成因(三个原型 + 一个组织陷阱)
1. **Mini-CEO**:自认下一个乔布斯、指定方案、无人事权却靠职位压人(Marquetly 的 Nick 案例;作者自述在 OpenSky 犯过同病,靠倾听团队、爱上问题、用数据代替意见一个月翻盘)
2. **Waiter(服务员)**:接单员——问客户"你想要什么"并照做,直接进入 Product Death Cycle(见 [[坑2-假需求]])
3. **Former Project Manager**:PM 答 why,项目经理答 when;转岗的 PM 常变成"挥着日历的服务员"——只对进度负责,不对结果负责
4. **SAFe 陷阱(组织层)**:SAFe 把 PM/PO 分层是全书认为最弱的设计——PO 与用户隔绝、PM 向下 Waterfall 式下发需求、**无人做验证**;作者:"trained dozens of SAFe teams, never seen it work well"(国内大客户常见,值得警觉)

## 怎么堵
- **好 PM 的定义**:拥有 why,团队集体拥有 what;连接点者而非独狼;"product owner is a role you play on a Scrum team. Product manager is a career."
- **Meghan 案例**(银行房贷,全书最佳正面样本):愿景"让房贷申请随处可得"→ 业务目标(首次申请完成率,60% 流失给竞品)→ 拉漏斗数据找流失者 → 带开发与 UX 一起听用户 → 发现"到网点核验证件约不到号" → **concierge 手动实验完成率相对 +90%** → 第一版产品减半线下核验。前提:管理层给了目标与空间、允许接触用户
- 晋升阶梯参考:tactical(建功能)/ strategic(定位取胜)/ operational(roadmap 接回战术)三级构成,层级越高 tactical 越少;APM→PM→Senior→Director→VP→CPO(CPO 进董事会语言:财务影响)
- FDE 同型死法:被当 mini-CEO(指定方案)、被当 waiter(客户要什么做什么)、被当项目经理(只对进度负责)——把对话拉回 why 与问题本身

## 关联
- [[坑2-假需求]](Waiter 机制)· [[方案实验三型]](Meghan 的 concierge)· [[三大战略鸿沟]](SAFe 是 Effects Gap 错误填法的商品化)
