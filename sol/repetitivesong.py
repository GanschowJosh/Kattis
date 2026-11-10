n=int(input())
seen={}
mx=0
for i in range(n):
  word=input()
  if word in seen:
    mx=max(n-(i-seen[word]),mx)
  seen[word]=i

print(mx)