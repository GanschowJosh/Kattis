n=int(input())
e=int(input())

new_songs=[]

for _ in range(e):
  line=list(map(int, input().split()))
  num, at=line[0],set(line[1:])
  if 1 in at:
    new_songs.append(at)
  else:
    for song in new_songs:
      if song & at:
        for i in at:
          song.add(i)

a=set(range(n+1))
for s in new_songs:
  a&=s

for i in sorted(a):
  print(i)