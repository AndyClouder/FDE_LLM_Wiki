# -*- coding: utf-8 -*-
"""FDE 知识库轻量检索(L5,BM25 零依赖)

用法:
    python tools/search.py 客户说好但没人用
    python tools/search.py 康威
    python tools/search.py demo 翻车 -n 5

分词:ASCII 词 + 中文二元组(bigram);标题/文件名命中加权。
输出:按 BM25 得分排序的候选页 + 前三名反向链接(图谱导航的轻量替代)。
向量语义层待"关键词检索不够用"的痛感明确后再评估(AGENTS.md §10 不跳级原则)。
"""
import math
import os
import re
import sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
K1, B = 1.2, 0.75

# ---------- 语料 ----------
def load_corpus():
    docs = []
    for sub in ('wiki', 'episodic'):
        base = os.path.join(ROOT, sub)
        for root, dirs, files in os.walk(base):
            for f in sorted(files):
                if f.endswith('.md'):
                    p = os.path.join(root, f)
                    with open(p, encoding='utf-8') as fh:
                        docs.append((os.path.splitext(f)[0], os.path.relpath(p, ROOT), fh.read()))
    return docs

# ---------- 分词 ----------
ASCII_WORD = re.compile(r'[a-z0-9]+')

def tokenize(text):
    text = text.lower()
    toks = ASCII_WORD.findall(text)
    # 中文按连续段切二元组;单字段落一元
    for seg in re.findall(r'[\u4e00-\u9fff]+', text):
        if len(seg) == 1:
            toks.append(seg)
        else:
            toks.extend(seg[i:i+2] for i in range(len(seg) - 1))
    return toks

# ---------- BM25 ----------
def main():
    args = sys.argv[1:]
    n = 10
    if '-n' in args:
        i = args.index('-n')
        n = int(args[i + 1])
        args = args[:i] + args[i+2:]
    query = ' '.join(args).strip()
    if not query:
        print(__doc__)
        sys.exit(0)

    docs = load_corpus()
    tf, dl, title_toks = [], [], []
    for name, rel, text in docs:
        t = tokenize(text)
        tf.append(Counter(t))
        dl.append(len(t))
        title_toks.append(set(tokenize(name)))
    N = len(docs)
    avgdl = sum(dl) / max(N, 1)
    df = Counter()
    for c in tf:
        for tok in c:
            df[tok] += 1

    qtoks = tokenize(query)
    scores = []
    for i in range(N):
        s = 0.0
        for q in qtoks:
            if q not in tf[i]:
                continue
            idf = math.log(1 + (N - df[q] + 0.5) / (df[q] + 0.5))
            s += idf * tf[i][q] * (K1 + 1) / (tf[i][q] + K1 * (1 - B + B * dl[i] / avgdl))
        if s <= 0:
            continue
        # 标题/文件名命中加权:检索词全部出现在页名里 → 强信号
        if all(q in ' '.join(title_toks[i]) for q in qtoks):
            s += 10.0
        scores.append((s, i))
    scores.sort(reverse=True)
    if not scores:
        print(f"未命中:{query}(可换同义词再试,或读 index.md 目录)")
        sys.exit(0)

    # 反向链接表(供 top 结果导航)
    back = {}
    for name, rel, text in docs:
        for link in re.findall(r'\[\[([^\]\|#]+)', text):
            back.setdefault(link.strip(), set()).add(name)

    print(f"检索:{query}  |  语料 {N} 页  |  top {min(n, len(scores))}")
    for rank, (s, i) in enumerate(scores[:n], 1):
        name, rel, _ = docs[i]
        bl = '、'.join(sorted(back.get(name, []))[:4]) or '—'
        print(f"{rank:>2}. [{s:6.2f}] {name}  ({rel})")
        print(f"     被引:{bl}")

if __name__ == '__main__':
    main()
