line = input().split()

best = 1
best_word = line[0]

curr = 1
last = line[0]

for word in line[1:]:
  if word == last:
    curr += 1
    if curr > best:
      best = curr
      best_word = word
  else:
    curr = 1
  last = word

print(best_word)