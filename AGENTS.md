# AGENTS.md — FDE 认知知识库 · 运作规范(Schema)

> 本文件是知识库的"宪法"。**任何在本目录工作的 LLM 会话,动手前必须先读本文件并严格遵守。**
> 依据:[[LLM Wiki v2]](扩展自 Karpathy 的 LLM Wiki 模式)。核心原则:**停止重新推导,开始沉淀编译**——RAG 检索即遗忘,wiki 积累且复利。

## 1. 定位

Forward Deployed Engineer(FDE)的个人认知库。领域主题:**投产、需求、结果、责任、系统、协作**。
本库的知识主线是「坑位 → 概念 → 打法」三轴:每个坑(必踩的失败模式)由一个概念(理论解释)理解,由一个打法(可操作程序)堵住。

## 2. 目录结构(三层架构 + 四级记忆)

| 位置 | 角色 | 说明 |
|---|---|---|
| `inbox/` | **原始层 + 工作记忆(投喂口)** | 所有原始资料(书 / 报告 / 剪藏 / 笔记)与未加工观察都放这里。资料文件**永不修改、永不删除、不移动**;是否已摄取由源卡的 `ingestion` 字段跟踪 |
| `新建文件夹/` | 原始层(剪藏) | 只读 |
| `wiki/sources/` | 语义记忆 · 源卡片 | 每份资料一页,登记书目信息与摄取状态 |
| `wiki/pitfalls/` | 语义记忆 · 坑位 | FDE 必踩的失败模式:症状 / 成因 / 怎么堵 |
| `wiki/concepts/` | 语义记忆 · 概念 | 解释坑位的理论内核 |
| `wiki/practices/` | 程序性记忆 · 打法 | 可操作的工作程序,含验证案例 |
| `episodic/` | **情景记忆** | 会话结晶摘要(YYYY-MM-DD-主题.md) |
| `graph.md` | 知识图谱 | 实体表 + 类型化关系表,用于导航与影响分析 |
| `index.md` | 人类可读目录 | 总目录 + 统计 + 待摄取清单 |
| `changelog.md` | 审计日志 | 每次 ingest / lint / 合并 / 删除都记一行 |
| `.agents/skills/` | 标准技能 | 三个固化操作:知识库摄取 / 知识库体检 / 知识库结晶(含完整步骤与踩坑点) |
| `.zcode/config.json` | 钩子配置(L4) | SessionStart 自动跑 lint 并把结果注入上下文(`tools/hook_lint.py`);每周五 11:30 定时体检+衰减重算(持久定时任务,绑定工作区) |
| `tools/` | 工具 | `lint.py` 全库机器审计(含 inbox 源卡覆盖)· `search.py` BM25 轻量检索(L5)· `hook_lint.py` 钩子包装 |

四级记忆的晋升方向:inbox(工作)→ episodic(情景)→ wiki/concepts(语义)→ wiki/practices(程序)。越往上越压缩、置信度越高、生命越长。

## 3. 页面类型与模板

所有 wiki 页面必须带 frontmatter:

```yaml
---
title: 页面标题
type: source | concept | pitfall | practice | digest
status: working | established | superseded
confidence: 0.0 ~ 0.95
sources:            # 本页声明的来源,[[wikilink]] 或"个人实践:xxx"
  - "[[书名或来源]]"
source_count: N
last_confirmed: YYYY-MM-DD
created: YYYY-MM-DD
tags: [少量小写标签]
superseded_by: "[[新页面]]"   # 仅 status=superseded 时存在
---
```

正文约定:
- 源卡片:`ingestion: card-only | pending | full` 标注摄取深度
- 坑位页:症状(怎么死)/ 成因 / 解释概念 / 怎么堵
- 概念页:一句话内核 / 展开 / 关联
- 打法页:核心打法 / 操作步骤 / 验证案例 / 适用信号
- 任何页面中"待深度摄取后补充"的内容,显式用 `> 待补:` 标注,不得冒充已确认事实

## 4. 生命周期规则

**置信度初始值**:单源 0.6;双源 0.8;三源及以上 0.9;有个人实践验证再 +0.1;上限 0.95。

**衰减(半衰期按页面类型)**:概念/架构类 12 个月;打法类 6 个月;瞬态事实(bug、版本号、价格)1 个月。lint 时检查 `last_confirmed`,超过一个半衰期未强化 → confidence −0.1 并更新页面。

**强化**:任何新源确认本页 → `last_confirmed` 更新为当天,confidence +0.05,`source_count` +1。

**Supersession(取代)**:新信息与旧页冲突且判定新方更可信时——旧页**不删除**:status → superseded,frontmatter 加 `superseded_by`;新页列出 `supersedes`;两页互链并保留时间戳。这是知识的版本控制。

## 5. 实体与关系(graph.md 规范)

实体类型:`book / concept / pitfall / practice / project / artifact / tool / person`
关系类型(每条边记录:起点、类型、终点、依据、置信度):

| 关系 | 含义 | 典型方向 |
|---|---|---|
| explains | 解释 | concept → pitfall |
| fixes | 堵住 | practice → pitfall |
| derives-from | 派生自 | concept/practice → source |
| applied-in | 应用于 | practice → project |
| produces | 产出 | practice → artifact |
| contradicts | 矛盾 | 任意,必须触发处理流程 |
| supersedes | 取代 | 新页 → 旧页 |
| relates-to | 弱关联 | 兜底,能不用就不用 |

图谱不替代页面:**页面负责阅读,图谱负责导航与发现**。回答"影响/波及"类问题时,从实体出发沿 fixes / applied-in / derives-from 边遍历,不做关键词匹配。

## 6. 四个标准操作(只允许这四种方式改动知识库)

> INGEST / LINT / CRYSTALLIZE 已固化为标准技能(`.agents/skills/`),**详细步骤与踩坑点以技能文件为单一事实源**,调用方式:说"摄取/体检/结晶"或对应斜杠命令。本节只保留规则要点。QUERY 属始终生效的对话模式,不做成技能(《图解Skill》:始终生效的规则放配置)。

**INGEST 摄取**(有新资料时)→ 技能:[知识库摄取](.agents/skills/知识库摄取/SKILL.md)
流程要点:扫描 inbox → 建源卡 → **脱敏(强制,先于一切内容处理)** → 提取声明(已有页面走强化 / 没有则新建)→ 更新 graph / index → 记 changelog。声明落页规则见 §3/§4。

**QUERY 查询**(始终生效的对话模式)
1. 先定位候选页:读 `index.md`,或跑 `python tools/search.py <关键词>`(L5 BM25 检索,输出附反向链接;向量语义层待"关键词不够用"的痛感明确后再评估)
2. 读页面正文;影响/波及类问题走 `graph.md` 遍历
3. 回答必须标注置信度与来源;confidence < 0.6 要明说"不太确定"
4. 若推导出高质量回答(用户认可、推理链完整),按 CRYSTALLIZE 归档

**LINT 体检**(L4 已自动化:SessionStart 钩子自动跑并注入结果;每周五 11:30 定时体检+衰减重算)→ 技能:[知识库体检](.agents/skills/知识库体检/SKILL.md)
工具:`python tools/lint.py`(frontmatter / 断链 / 孤儿页 / 摄取状态 / 统计一致性 / 待办清单 / inbox 源卡覆盖)+ 人工项(置信度衰减、矛盾检测)。能自动修的直接修并记 changelog,拿不准的只标记不动手。

**CRYSTALLIZE 结晶**(有价值的会话结束时)→ 技能:[知识库结晶](.agents/skills/知识库结晶/SKILL.md)
流程要点:写 `episodic/YYYY-MM-DD-主题.md`(问题/做了什么/关键发现/教训/待办)→ 够格教训晋升 wiki(克制:wiki 页面数不是 KPI)→ 更新 graph / index / changelog。

## 7. 矛盾处理

新旧声明冲突时,按 **源新近性 > 源权威性 > 支持证据数** 提议保留方,执行 §4 的 supersession,并在 changelog 记录判断理由。人类可随时否决——被否决的裁决回滚并注明。

## 8. 安全与审计

- 一切写操作(摄取、修改、合并、删除、批量清理)必须记 `changelog.md`:日期 / 操作 / 对象 / 理由
- 批量操作(批量删除过期内容、合并重复实体)必须可回滚:先在 changelog 登记清单,再动手
- 敏感信息在摄取入口过滤, wiki 内出现即视为事故,发现立即清除并记录

## 9. 约定

- 中文文件名;页面间用 `[[wikilink]]` 互链,链接名与文件名(不含扩展名)严格一致
- 一个概念一页;引用必带源;不复制原文大段,只留提炼后的声明
- **永不移动/修改/删除 `inbox/` 与 `新建文件夹/` 中的原始资料文件**(用户投喂即入库,位置不再变动)

## 10. 成熟度路线图(对应 LLM Wiki v2 实施光谱)

| 级别 | 能力 | 状态 |
|---|---|---|
| L1 最小可用 | 源 + wiki 页 + index + schema | ✅ 2026-08-20 |
| L2 生命周期 | 置信度、supersession、衰减 | ✅ 2026-08-20 |
| L3 结构 | 实体抽取、类型化关系、图谱 | ✅ 2026-08-20 |
| L4 自动化 | 钩子:自动摄取/自动 lint/上下文注入 | ✅ 2026-08-20:SessionStart 钩子自动 lint+注入(`.zcode/config.json` + `tools/hook_lint.py`);每周五 11:30 定时体检+衰减重算;自动摄取 = lint 的 inbox 覆盖检查自动提醒建卡 |
| L5 规模化 | 混合检索(页面 >100 后再考虑) | ✅ 轻量版 2026-08-20:`tools/search.py` BM25(关键词+反向链接导航);向量语义层按"不跳级"原则待痛感明确后再评估 |
| L6 多人协作 | mesh 同步、共享/私有作用域 | ⬜ |

不要跳级。每级跑顺了再上下一级。
