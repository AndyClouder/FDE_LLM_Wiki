import os, re, sys

# FDE 知识库全库审计脚本(lint)
# 用法:python tools/lint.py
# 检查:frontmatter 完整性 / wikilink 断链 / 孤儿页 / 源卡摄取状态 / index 统计一致性 / 待办清单

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
issues = []

all_md = []
for root, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in ('.obsidian', '.zcode-tmp', '新建文件夹', '.agents')]
    for f in files:
        if f.endswith('.md'):
            all_md.append(os.path.join(root, f))

names = {}
for p in all_md:
    names.setdefault(os.path.splitext(os.path.basename(p))[0], []).append(p)

wiki_pages = [p for p in all_md if os.sep + 'wiki' + os.sep in p]
episodic_pages = [p for p in all_md if os.sep + 'episodic' + os.sep in p]
REQUIRED = ['title', 'type', 'status', 'confidence', 'sources', 'source_count', 'last_confirmed', 'created', 'tags']
VALID_TYPE = {'source', 'concept', 'pitfall', 'practice', 'digest'}
VALID_STATUS = {'working', 'established', 'superseded'}

stats = {'source': 0, 'concept': 0, 'pitfall': 0, 'practice': 0}
link_ref = {}

def strip_code(t):
    t = re.sub(r'```.*?```', '', t, flags=re.S)
    t = re.sub(r'`[^`\n]*`', '', t)
    return t

for p in sorted(wiki_pages):
    rel = os.path.relpath(p, ROOT)
    with open(p, encoding='utf-8') as f:
        text = f.read()
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        issues.append(f"[frontmatter] {rel}: 缺少 frontmatter")
        continue
    fm = m.group(1)
    missing = [k for k in REQUIRED if not re.search(rf'^{k}:', fm, re.M)]
    if missing:
        issues.append(f"[frontmatter] {rel}: 缺字段 {missing}")
    tm = re.search(r'^type:\s*(\S+)', fm, re.M)
    sm = re.search(r'^status:\s*(\S+)', fm, re.M)
    if tm and tm.group(1) not in VALID_TYPE:
        issues.append(f"[type] {rel}: 非法 type {tm.group(1)}")
    if sm and sm.group(1) not in VALID_STATUS:
        issues.append(f"[status] {rel}: 非法 status {sm.group(1)}")
    if tm and tm.group(1) in stats:
        stats[tm.group(1)] += 1
    if tm and tm.group(1) == 'source':
        im = re.search(r'^ingestion:\s*(\S+)', fm, re.M)
        if not im or im.group(1) != 'full':
            issues.append(f"[ingestion] {rel}: ingestion={im.group(1) if im else '缺失'} != full")

for p in sorted(all_md):
    rel = os.path.relpath(p, ROOT)
    with open(p, encoding='utf-8') as f:
        text = strip_code(f.read())
    self_name = os.path.splitext(os.path.basename(p))[0]
    for link in re.findall(r'\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]', text):
        link = link.strip()
        if link not in names:
            issues.append(f"[断链] {rel}: [[{link}]] 无对应文件")
        elif link != self_name:
            link_ref.setdefault(link, set()).add(rel)

for p in sorted(wiki_pages):
    name = os.path.splitext(os.path.basename(p))[0]
    if not link_ref.get(name):
        issues.append(f"[孤儿页] {name}: 无任何入链")

with open(os.path.join(ROOT, 'index.md'), encoding='utf-8') as f:
    idx = f.read()
sm = re.search(r'源卡 (\d+) · 坑位 (\d+) · 概念 (\d+) · 打法 (\d+) · 结晶 (\d+)', idx)
if sm:
    declared = tuple(int(x) for x in sm.groups())
    actual = (stats['source'], stats['pitfall'], stats['concept'], stats['practice'], len(episodic_pages))
    if declared != actual:
        issues.append(f"[统计] index.md 声明 {declared} vs 实际 {actual}")
else:
    issues.append("[统计] index.md 统计行未找到")

pending = re.findall(r'^- \[ \](.+)$', idx, re.M)
if pending:
    issues.append(f"[待办] index.md 仍有未勾选项: {pending}")

print(f"wiki 页面: {len(wiki_pages)}(源{stats['source']} 坑{stats['pitfall']} 概念{stats['concept']} 打法{stats['practice']}) | episodic: {len(episodic_pages)} | 被引用实体: {len(link_ref)}")
if issues:
    print(f"\n发现 {len(issues)} 个问题:")
    for i in issues:
        print("  -", i)
    sys.exit(1)
print("\n✅ LINT 全部通过:frontmatter 完整、无断链、无孤儿页、源卡摄取状态正常、统计一致、无未完成待办")
print("   人工检查项(脚本不覆盖,按 AGENTS.md LINT 清单执行):置信度衰减重算、矛盾检测、inbox 无源卡资料补卡")
