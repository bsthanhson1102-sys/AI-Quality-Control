#!/usr/bin/env python3
"""Deterministic preflight for Vietnamese aesthetic-service posts.
Screening aid only: NOT a substitute for CORE or human/domain review.
"""
import argparse, json, re, sys
GENERIC_HOOKS=[r'nâng mũi đẹp không chỉ là',r'sống mũi cao hơn chưa chắc',r'không có một dáng mũi.*phù hợp với tất cả']
GENERIC_CTA=[r'nhắn tin.*để được tư vấn nhé',r'nhắn tin.*để được hướng dẫn đặt lịch tư vấn']
DETAILS=['bán cấu trúc','cấu trúc','sụn','da mũi','đầu mũi','trụ mũi','tiền sử','thăm khám','hồi phục','tái khám','giới hạn','biến chứng']
def assess(text):
 t=' '.join(text.lower().split()); issues=[]
 def add(code,severity,evidence):issues.append({'id':code,'severity':severity,'evidence':evidence})
 if len(text.strip())<450:add('DEPTH_SHORT','MAJOR','Fewer than 450 characters; requires editorial depth review')
 if any(re.search(p,t) for p in GENERIC_HOOKS):add('HOOK_TEMPLATE','MAJOR','Repeated generic hook from failed T10 fixtures')
 found=[d for d in DETAILS if d in t]
 if len(found)<2:add('LOW_SERVICE_DETAIL','MAJOR',f'Only {len(found)} concrete terms found: {found}')
 if t.count('?')>=3 and len(found)<2:add('QUESTIONNAIRE_WITHOUT_PAYOFF','MAJOR','Three or more questions but fewer than two concrete service/clinical details; editorial review required')
 if any(re.search(p,t) for p in GENERIC_CTA):add('GENERIC_CTA','MINOR','Generic consultation CTA')
 if re.search(r'cam kết.*(đẹp|an toàn|100%)|đảm bảo.*(đẹp|an toàn)|không.*(rủi ro|biến chứng)',t):add('UNSUPPORTED_PROMISE','CRITICAL','Potential guarantee; requires claim review')
 return {'screen':'BLOCK' if any(x['severity'] in ('MAJOR','CRITICAL') for x in issues) else 'REVIEW_REQUIRED','issues':issues,'detail_terms':found,'note':'REVIEW_REQUIRED is not PASS; CORE domain/technical acceptance and evidence are still required.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('file');a=ap.parse_args()
 r=assess(open(a.file,encoding='utf-8').read());print(json.dumps(r,ensure_ascii=False,indent=2))
 return 2 if r['screen']=='BLOCK' else 0
if __name__=='__main__':sys.exit(main())
