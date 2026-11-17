#!/usr/bin/env python3
"""Read-only lookup of verified Writing 33 focus segments; standard library only."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--page', type=int, help='Part number: 4, 7, 8, 9, 10 or 11')
    parser.add_argument('--keyword', default='', help='Substring in segment summary/focus')
    parser.add_argument('--timeline', action='store_true', help='Search full timeline instead of selected clips')
    parser.add_argument('--json', action='store_true', help='Print structured JSON')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    data = json.loads((root / 'references' / 'catalog.json').read_text(encoding='utf-8'))
    episodes = data['episodes']
    known = [e['page'] for e in episodes]
    if args.page is not None and args.page not in known:
        result = {'status': 'outside_verified_scope', 'verified_pages': known,
                  'message': '该篇不在六篇精读索引内，不能据此提供分钟定位。',
                  'course_url': 'https://www.bilibili.com/video/BV1JPMi6REXC'}
        print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else result['message'])
        return 2
    mode = 'timeline' if args.timeline else 'clips'
    keyword = args.keyword.strip().casefold()
    rows = []
    for episode in episodes:
        if args.page is not None and args.page != episode['page']:
            continue
        for item in episode[mode]:
            haystack = ' '.join([item['summary'], item.get('focus', '')]).casefold()
            if keyword and keyword not in haystack:
                continue
            rows.append({'page': episode['page'], 'title': episode['title'], 'notes': episode['notes'], **item})
    result = {'status': 'ok' if rows else 'no_match', 'mode': mode,
              'verified_date': data['verified_date'], 'time_basis': data['time_basis'],
              'count': len(rows), 'total_interval_seconds': sum(r['end_seconds'] - r['start_seconds'] for r in rows),
              'results': rows}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif not rows:
        print('摘要索引未命中；可换关键词或阅读对应篇目。未命中不代表视频未涉及。')
    else:
        print('时间从各分集00:00起算；自动转写话题边界可能有数秒误差。')
        for row in rows:
            print(f"P{row['page']} {row['start']}—{row['end']} | {row['summary']}\n  {row['url']}")
        print(f"共{len(rows)}段；区间总长{result['total_interval_seconds']}秒。")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
