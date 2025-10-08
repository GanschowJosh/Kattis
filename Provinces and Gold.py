g, s, c = list(map(int, input().split()))

total = g*3 + s*2 + c*1
result = ""
if total >=8:
  result = "Province or "

elif total>=5:
  result = "Duchy or "

elif total >= 2:
  result = "Estate or "


if total >= 6:
  result += "Gold"
elif total >= 3:
  result += "Silver"
else:
  result += "Copper"

print(result)