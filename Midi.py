"""n = int(input())
text = ""
for _ in range(n):
  text = input()[::-1] + text
print(text)"""
n = int(input())
parts = []
for _ in range(n):
  parts.append(input()[::-1])

print(''.join(parts[::-1]))