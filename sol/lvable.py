n = int(input().strip())
s = input().strip()

if "lv" in s:
  print(0)
elif 'l' in s or 'v' in s:
  print(1)
else:
  print(2)