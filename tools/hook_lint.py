# -*- coding: utf-8 -*-
"""SessionStart 钩子包装(L4):自动跑 lint 并把结果注入会话上下文。

输出严格 JSON(ZCode 钩子 schema):{"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "..."}}
任何内部错误都吞掉并以 exit 0 退出——体检失败不应阻塞会话启动。
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LINT = os.path.join(HERE, 'lint.py')

try:
    r = subprocess.run([sys.executable, LINT], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=120, cwd=os.path.join(HERE, '..'))
    out = (r.stdout or '').strip()
    ok = (r.returncode == 0)
    # 控制长度:additionalContext 只保留头部与问题清单
    ctx = out[:1800] + ('\n…(截断,可手动跑 python tools/lint.py 看全量)' if len(out) > 1800 else '')
    prefix = '[知识库自动体检 SessionStart]\n' if ok else '[知识库自动体检 SessionStart·发现问题]\n'
    payload = prefix + ctx + ('\n提示:能自动修的直接修并记 changelog,拿不准的只标记(见 AGENTS.md LINT)。' if not ok else '')
except Exception as e:  # noqa: BLE001
    payload = f'[知识库自动体检 SessionStart] 钩子运行失败:{e}(可手动跑 python tools/lint.py)'

print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": payload}},
                 ensure_ascii=True))
sys.exit(0)
