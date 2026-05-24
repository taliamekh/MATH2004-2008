#!/usr/bin/env python3
"""
build.py — Assemble MATH2004 course notes from modular fragment files.

Usage:
    python3 build.py

Reads shell-head.html, shell-foot.html, and all chapter fragments from chapters/
Outputs: MATH2004-notes.html (single viewable file)

Fragment loading order matches the sidebar:
  ch1-notes, ch1-prob, ch2-notes, ch2-prob, ch3-notes, ch3-prob,
  ch7-notes, ch7-prob, ch4-notes, ch4-prob, ch5-notes, ch5-prob,
  ch6-notes, ch6-prob, formulas, t1prep-t4prep, final,
  summary, progress
"""
import os, sys

DIR = os.path.dirname(os.path.abspath(__file__))
CHAPTERS = os.path.join(DIR, 'chapters')
OUTPUT = os.path.join(DIR, 'MATH2004-notes.html')

# Assembly order — matches sidebar navigation
FRAGMENTS = [
    'ch1-notes.html',  'ch1-prob.html',
    'ch2-notes.html',  'ch2-prob.html',
    'ch3-notes.html',  'ch3-prob.html',
    'ch7-notes.html',  'ch7-prob.html',
    'ch4-notes.html',  'ch4-prob.html',
    'ch5-notes.html',  'ch5-prob.html',
    'ch6-notes.html',  'ch6-prob.html',
    'formulas.html',
    'exam-formulas.html',
    't1prep.html', 't2prep.html', 't3prep.html', 't4prep.html', 'final.html',
    'final-w19.html', 'final-f14.html', 'final-f13.html', 'final-f17.html',
    'final-practice.html',
    'recommended.html',
    'summary.html',
    'progress.html',
]

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def build():
    # Read shell
    head = read(os.path.join(DIR, 'shell-head.html'))
    foot = read(os.path.join(DIR, 'shell-foot.html'))

    # Assemble content
    parts = []
    missing = []
    for fname in FRAGMENTS:
        fpath = os.path.join(CHAPTERS, fname)
        if os.path.exists(fpath):
            content = read(fpath).strip()
            parts.append(f'  <!-- ═══ {fname} ═══ -->')
            parts.append(f'  {content}')
            parts.append('')
        else:
            missing.append(fname)

    if missing:
        print(f"⚠ Missing fragments (skipped): {', '.join(missing)}")

    # Combine
    assembled = head + '\n'.join(parts) + '\n' + foot

    # Write output
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(assembled)

    # Stats
    total_frags = len(FRAGMENTS) - len(missing)
    print(f"✓ Built {OUTPUT}")
    print(f"  {total_frags}/{len(FRAGMENTS)} fragments assembled")
    print(f"  {len(assembled):,} bytes total")
    print(f"  Shell: {len(head)+len(foot):,} bytes")
    print(f"  Content: {sum(len(read(os.path.join(CHAPTERS,f))) for f in FRAGMENTS if os.path.exists(os.path.join(CHAPTERS,f))):,} bytes")

if __name__ == '__main__':
    build()

