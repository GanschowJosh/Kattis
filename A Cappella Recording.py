n, d = list(map(int, input().split()))

notes = [int(input()) for _ in range(n)]

notes = sorted(notes)
buckets = 1
startNote = notes[0]
for note in notes[1:]:
  if note - startNote > d:
    buckets+=1
    startNote = note
    
  
print(buckets)