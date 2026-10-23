from autokattis import OpenKattis
from dataclasses import dataclass
import os
import datetime
import zoneinfo
import heapq

env_keys={}
with open(".env", "r") as f:
  lines=f.readlines()
  for line in lines:
    k,v=line.strip().split("=",1)
    env_keys[k]=v

kt = OpenKattis(username="joshua-ganschow", password=env_keys['kattis_password'])
print("logged in successfully")

problems_solved = kt.problems()
problems_unsolved = kt.problems(show_tried=True, show_solved=False)
stats=kt.stats()

print(f"pulled {len(problems_solved)+len(problems_unsolved)} problems succesfully")



files = [f for f in os.listdir("sol") if os.path.isfile(os.path.join("sol", f))]

@dataclass
class Problem:
  id:         str
  name:       str
  difficulty: float
  diff_cat:   str
  solved:     bool
  timestamp:  datetime.datetime
  language:   str

problems = {}

for pr in problems_solved:
  cp=Problem(pr['id'],pr['name'],pr['difficulty'],pr['category'],True,None,None)
  problems[pr['id']]=cp

for pr in problems_unsolved:
  cp=Problem(pr['id'],pr['name'],pr['difficulty'],pr['category'],False,None,None)
  problems[pr['id']]=cp


tz = zoneinfo.ZoneInfo('America/Chicago')

for problem in stats:
  id = problem['id']
  timestamp = problem['timestamp']

  try:
    if len(timestamp) == 8:
      t = datetime.datetime.strptime(timestamp, '%H:%M:%S').time()
      t = datetime.datetime.combine(datetime.datetime.now(tz).date(), t)
    else:
      t = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')

    t = t.replace(tzinfo=tz)

    if problem['test_case_passed'] == problem['test_case_full']:
      problems[id].timestamp = t
  except ValueError:
    print(f'Invalid timestamp: {timestamp}')

solved_problems = []
unsolved_problems = []
seen=set()
date_heap=[]
difficulty_heap=[]
for f in files:
  lang=f.split('.')[-1]
  if lang not in ["py","cpp","c"]: continue
  problem_id = f.split(".")[0].split("_")[0]
  if problem_id in seen:
    continue
  seen.add(problem_id)
  if problem_id not in problems: continue
  pr=problems[problem_id]
  pr.language=lang
  if pr.solved and pr.timestamp is not None:
    solved_problems.append(pr)
    heapq.heappush_max(date_heap, (pr.timestamp, pr.id, pr.difficulty))
    heapq.heappush_max(difficulty_heap, (pr.difficulty, pr.id))
  else: unsolved_problems.append(pr)


print("parsed all files")

sum_last_10=0
for i in range(10):
  c=heapq.heappop_max(date_heap)
  #print(c)
  sum_last_10+=c[2]


solution_base_link = 'https://github.com/GanschowJosh/Kattis/blob/main/sol/'

lines = []
lines.append("# open.kattis.com solutions")
lines.append("|Name|Id|Difficulty|Solved?|My Solution|")
lines.append("|----|--|----------|-------|-----------|")
num_solved = 0
num_unsolved = 0
diff_total = 0
for p in sorted(problems.values(), key=lambda x: x.name):
  if p.language is None:
    continue
  if p.solved:
    num_solved+=1
    diff_total += p.difficulty
  else: num_unsolved+=1
  lines.append(f"|[{p.name}](https://open.kattis.com/problems/{p.id})|{p.id}|{p.diff_cat}({p.difficulty})|{p.solved}|[source]({solution_base_link+p.id+'.'+p.language})|")

lines.extend(["\n","---"])
lines.append(f"Total solved: {num_solved}\n")
lines.append(f"Total unsolved: {num_unsolved}\n")
lines.append(f"Average difficulty solved: {diff_total/len(problems_solved)}\n")
lines.append(f'Average of last 10: {sum_last_10/10}\n')
highest_rated = heapq.heappop_max(difficulty_heap)
lines.append(f'Highest Difficulty: {highest_rated[0]} ({highest_rated[1]})')

print("created readme")

with open("out", "w") as out:
  out.write("\n".join(lines))