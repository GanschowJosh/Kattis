from autokattis import OpenKattis
from dataclasses import dataclass
import os

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

print(f"pulled {len(problems_solved)+len(problems_unsolved)} problems succesfully")

files = [f for f in os.listdir("sol") if os.path.isfile(os.path.join("sol", f))]

@dataclass
class problem:
  name: str
  pid: str
  difficulty: float
  diff_cat: str
  solved: bool

problems = []
failed = []
seen=set()
for f in files:
  if f.split(".")[-1] not in ["py","cpp","c"]: continue
  problem_id = f.split(".")[0].split("_")[0]
  if problem_id in seen:
    continue
  seen.add(problem_id)
  print(problem_id)
  for prob in problems_solved:
    if prob['id']==problem_id:
      pr=problem(prob['name'], problem_id, prob['difficulty'], prob['category'], True)
      break
  else:
    for prob in problems_unsolved:
      if prob['id']==problem_id:
        pr=problem(prob['name'], problem_id, prob['difficulty'], prob['category'], False)

  if pr:
    problems.append(pr)
  else:
    failed.append(problem_id)


print("parsed all files")
 
lines = []
lines.append("# open.kattis.com solutions")
lines.append("|Name|Id|Difficulty|Solved?|")
lines.append("|----|--|----------|-------|")
num_solved = 0
num_unsolved = 0
diff_total = 0
for p in sorted(problems, key=lambda x: x.name):
  if p.solved:
    num_solved+=1
    diff_total += p.difficulty
  else: num_unsolved+=1
  lines.append(f"|[{p.name}](https://open.kattis.com/problems/{p.pid})|{p.pid}|{p.diff_cat}({p.difficulty})|{p.solved}|")

lines.extend(["\n","---"])
lines.append(f"Total solved: {num_solved}\n")
lines.append(f"Total unsolved: {num_unsolved}\n")
lines.append(f"Average difficulty solved: {diff_total/len(problems_solved)}\n")

print("created readme")

with open("out", "w") as out:
  out.write("\n".join(lines))
  