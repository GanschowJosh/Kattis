ops = ["*","+","-","//"]*4
#print(ops)

from collections import defaultdict
from itertools import combinations
eval_map = defaultdict(list)

def find_all_evals():
  for comb in combinations(ops, 3):
    opa, opb, opc = comb
    curr = "4 " + opa + " 4 " + opb + " 4 " + opc + " 4"
    e = eval(curr)
    if opa == "//":
      opa = "/"
    if opb == "//":
      opb = "/"
    if opc == "//":
      opc = "/"
    curr = "4 " + opa + " 4 " + opb + " 4 " + opc + " 4"
    eval_map[e].append(curr)

find_all_evals()
#print(eval_map)

m = int(input())

for _ in range(m):
  n = int(input())
  if eval_map[n]:
    print(f"{eval_map[n][0]} = {n}")
  else:
    print("no solution")