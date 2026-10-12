#!/usr/bin/env python3
"""Sanity-check cross-references and numerical scenario controls. No external dependencies."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT/'projects'/'01-student-enrolment-implementation'
REG=PROJECT/'registers'
def load(name):
 with (REG/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
assert sum(int(x['Baseline_CAD']) for x in load('budget.csv'))==240000
assert sum(int(x['Illustrative_EAC_W16_CAD']) for x in load('budget.csv'))==236000
assert sum(int(x['Baseline_CAD']) for x in load('budget.csv') if x['Workstream']!='Contingency')==228000
assert len(load('milestones.csv'))==8
m={r['ID']:r for r in load('milestones.csv')}
assert [int(m[k]['Baseline_Week']) for k in ('M-02','M-04','M-05','M-06','M-07','M-08')]==[5,17,18,20,21,24]
requirements={x['Requirement_ID'] for x in load('requirements_traceability.csv')}
tests={x['Test_ID'] for x in load('uat_cases.csv')}
assert all(x['Requirement_ID'] in requirements for x in load('uat_cases.csv'))
assert all(x['Test_Ref'] in tests for x in load('requirements_traceability.csv'))
assert any(x['ID']=='CHG-01' for x in load('changes_and_decisions.csv'))
assert any(x['Record_ID']=='I-01' for x in load('raid.csv'))
for md in ROOT.rglob('*.md'):
 txt=md.read_text(encoding='utf-8')
 for link in __import__('re').findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',txt):
  if not link or link.startswith(('http://','https://','#','mailto:')):continue
  assert (md.parent/link.split('#')[0]).exists(),f'Missing link {link!r} in {md}'
for slug,cap,eac in [('02-pension-administration-modernization',480000,468000),('03-network-management-application-design',120000,116000)]:
 project=ROOT/'projects'/slug
 def rows(name):
  with (project/'registers'/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
 budget=rows('budget.csv')
 assert sum(int(float(x['Baseline CAD'])) for x in budget)==cap
 assert sum(int(float(x['Forecast CAD'])) for x in budget)==eac
 assert all(int(float(x['Forecast CAD']))==int(float(x['Actual CAD']))+int(float(x['Remaining CAD'])) for x in budget)
 schedule=rows('schedule.csv')
 prior={x['ID']:x for x in schedule}
 for x in schedule:
  dep=x['Dependency']
  assert not dep or dep in prior, f'Unknown schedule predecessor {dep}'
  assert not dep or float(prior[dep]['Forecast week'])<=float(x['Forecast week'])
  seen={x['ID']}; cursor=dep
  while cursor:
   assert cursor not in seen, f'Schedule dependency cycle at {cursor}'
   seen.add(cursor); cursor=prior[cursor]['Dependency']
 gates=rows('gates.csv')
 latest='W26 status' if slug.startswith('02') else 'W16 status'
 assert all(x[latest]=='Pass' for x in gates)
 assert all(x['Evidence'].strip() and x['Reviewer'].strip() and x['Owner'].strip() for x in gates)
 if slug.startswith('03'):
  for x in rows('research.csv'):
   expected=float(x['Final success'])/float(x['Final sample'])
   assert abs(float(x['Final rate'])-expected)<1e-10
   assert x['Gate']=='Meets' and expected>=float(x['Target'])
  assert rows('backlog.csv')[-1]['Final status']=='Deferred'
 else:
  assert any(x['W24 result']=='Fail' and x['W26 result']=='Pass' for x in rows('traceability.csv'))
assert 12000==11988+12
for md in ROOT.rglob('*.md'):
 text=md.read_text()
 for forbidden in ('Blessing Nnabugwu','Blessing Ezinne','Equitable, Waterloo','Sidmach Technologies','Grange School','Ministry of Interior','Military Pension Board'):
  assert forbidden not in text,f'Excluded identity in {md}'
print('PASS: all 3 case budgets, forecast arithmetic, schedule dependencies, research rates, gate evidence, local links and excluded identities.')
