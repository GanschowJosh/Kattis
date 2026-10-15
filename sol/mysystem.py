from random import choice

t = int(input())
for _ in range(t):
  for q in range(100):
    print(choice(["F","T"]))
    a = input()
    print({"T":"F","F":"T"}[a])
    input()