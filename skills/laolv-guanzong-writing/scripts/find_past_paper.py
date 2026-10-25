#!/usr/bin/env python3
"""Read the bundled verified index; never infer answers or unseen timestamps."""
import argparse, json
from pathlib import Path

def lookup(catalog, year, exam, question=None, text_no=None, kind=None, restricted=False):
    found=[]
    for r in catalog['records']:
        if year not in r['years'] or r['exam'] != exam: continue
        if r['restricted'] and not restricted: continue
        if text_no is not None and r.get('text') != text_no: continue
        if kind and kind not in (r.get('scope','')+' '+r['title']): continue
        row=dict(r)
        qr=r.get('question_range')
        if question is not None:
            if question in r.get('excluded_questions',[]): continue
            if qr and not (qr[0] <= question <= qr[-1]): continue
            row['match_level']='question_title' if qr and qr[0]==qr[-1] else 'question_range_title' if qr else 'year_only_question_unlocated'
        else: row['match_level']='year_or_text_title'
        found.append(row)
    order={'question_title':0,'question_range_title':1,'year_or_text_title':2,'year_only_question_unlocated':3}
    found.sort(key=lambda x:(x['restricted'],order[x['match_level']],x.get('page') or 0))
    return found

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--year',type=int,required=True)
    ap.add_argument('--exam',default=DEFAULT_EXAM,choices=['199','204','396','october_joint','199_candidate'])
    ap.add_argument('--question',type=int)
    ap.add_argument('--text',type=int)
    ap.add_argument('--type',dest='kind')
    ap.add_argument('--include-restricted',action='store_true')
    a=ap.parse_args()
    c=json.loads((Path(__file__).resolve().parents[1]/'references/past-papers/catalog.json').read_text())
    result=lookup(c,a.year,a.exam,a.question,a.text,a.kind,a.include_restricted)
    print(json.dumps({'verified_at':c['verified_at'],'count':len(result),'warning':'目录定位不等于已读取课堂内容；无结果不等于不存在视频；受限课默认不返回。','matches':result},ensure_ascii=False,indent=2))

DEFAULT_EXAM='199'
if __name__=='__main__':main()
