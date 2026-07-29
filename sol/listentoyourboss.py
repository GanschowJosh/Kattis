import sys
sys.setrecursionlimit(1000000)

n,m=map(int, input().split())

graph=dict()

for i in range(n-1):
  man=int(input())
  if man not in graph: graph[man]=[]
  graph[man].append(i+2)

start=[0]*(n+1)
end=[0]*(n+1)
vorder=0

def dfs(i):
  global vorder
  start[i]=vorder
  vorder+=1
  for child in graph.get(i, []):
    dfs(child)
  end[i]=vorder

dfs(1)

for _ in range(m):
  a,b=map(int, input().split())
  if start[b] <= start[a] < end[b]:
    print("No")
  else:
    print("Yes")