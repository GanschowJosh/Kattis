l_f, log_f, head_f = map(float, input().split())
L = int(round(l_f * 10))
A = int(round(log_f * 10))
B = int(round(head_f * 10))

best_i = 0
best_j = 0
best_sum = -1

for i in range(L // A, -1, -1):
  remaining = L - i * A
  j = remaining // B
  total = i * A + j * B
  if total > best_sum:
    best_sum = total
    best_i, best_j = i, j

print(f"{best_i} {best_j}")
