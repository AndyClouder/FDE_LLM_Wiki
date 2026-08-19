---
title: Prompt工程八条最佳实践
type: practice
status: established
confidence: 0.6
sources:
  - "[[AI Engineering]]"
source_count: 1
last_confirmed: 2026-08-20
created: 2026-08-20
tags: [prompt工程, 实操手册, 版本化]
---

# Prompt 工程八条最佳实践

## 核心打法
Prompt 工程是人机沟通的系统实验,不是玄学——"The problem is not with prompt engineering… The problem is when prompt engineering is the only thing people know." 与 [[模型适配的优先级顺序]] 配套:这是"先穷尽 prompt"那一环的执行手册。

## 操作步骤(八条)
1. **清晰无歧义**:说明打分制、整数分、输出格式
2. **Persona**:视角改变输出(一年级老师视角把 2/5 分作文评为 4/5)
3. **例子**:few-shot 用省 token 格式("chickpea --> edible");末尾标记符防模型续写;强模型上 few-shot 增益递减,训练数据里罕见的领域 API 除外
4. **足够上下文**:缺信息必幻觉(接 [[RAG检索优化四招]])
5. **任务分解**:意图分类 + 按意图路由响应生成(GoDaddy 单 prompt 膨胀到 1500+ tokens,拆成十类意图后质量升 token 降);分解还带来监控/调试/并行/易写四好处
6. **CoT**:"think step by step";LinkedIn 发现 CoT 降幻觉
7. **Self-critique**:自评后修正(10+3=30 → 自检 → 13)
8. **迭代 + 版本化**:prompt catalog 带元数据;Instacart 内部 Prompt Marketplace 最热模板 "Fast Breakdown"(会议纪要提炼事实/开放问题/行动项并回写任务系统)

## 三个必知陷阱
- **Chat template 差异是静默失败源**:Llama 2 与 3 模板不同,多余换行即可显著劣化——发送前打印最终 prompt 检查
- **Lost in the middle**:模型对 prompt 开头与结尾处理最好,中间最差(needle-in-a-haystack/RULER 测试)
- **工具警惕**:prompt 工具隐藏 API 调用烧钱(10 变体 × 30 评测例 = 300+ 调用);工具自带模板也有 typo(LangChain 默认 prompt 曾被发现错字)——"Show Me the Prompt"(Hamel Husain),永远检查工具生成的实际 prompt

## 适用信号
- 客户现场积累的 prompt 是资产:进版本库而非散落个人电脑
- 系统提示按公开物标准写(保密信息永不进 prompt,见 [[提示词攻击面与三层防御]])
