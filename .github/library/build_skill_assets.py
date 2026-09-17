#!/usr/bin/env python3
"""Keep the portable skill's template and worked example aligned with the book toolkit."""
import argparse
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def outputs():
    source=ROOT/'books/the-mom-test'
    package=ROOT/'skills/customer-interview-planner'
    plan=(source/'interview-plan.md').read_text().split('\n[Instructions]')[0].rstrip()+'\n'
    example=(source/'worked-example.md').read_text()
    example=example.replace('[Book guide](README.md) · [Blank interview plan](interview-plan.md) · [Playbook](../../playbooks/customer-interviews.md)', '[Blank interview plan](../assets/interview-plan.md) · [Evidence and decisions](evidence-and-decisions.md)')
    example=example.replace(' The dialogue for A appears in the [book guide](README.md#worked-example-the-calendar-was-not-the-starting-point).','')
    example=example.replace('(interview-plan.md)','(../assets/interview-plan.md)').replace('(../../skills/customer-interview-planner/assets/research-debrief.md)','(../assets/research-debrief.md)').replace('(../../skills/customer-interview-planner/assets/next-test.md)','(../assets/next-test.md)')
    result = {package/'assets/interview-plan.md':plan,package/'references/worked-example.md':example}
    for book in json.loads((ROOT/'.github/library/books.json').read_text()):
        if not book.get('toolkit'): continue
        source = ROOT/'books'/book['slug']; package=ROOT/'skills'/book['toolkit']['skill']
        for source_name, target_name in [('worksheet.md','assets/worksheet.md'),('worked-example.md','references/worked-example.md')]:
            text=(source/source_name).read_text().split('\n[Book guide]')[0].rstrip()+'\n\n'
            result[package/target_name]=text
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    for path,text in outputs().items():
        if args.check:
            if not path.exists() or path.read_text()!=text: raise SystemExit(f'Stale portable asset: {path.relative_to(ROOT)}')
        else: path.write_text(text)
    print('Portable book resources are current.' if args.check else 'Generated portable book resources.')
if __name__=='__main__': main()
