n1 = int(input())
n2 = int(input())
diff = n2-n1

if diff > 180:
    diff -= 360
elif diff < -180:
    diff += 360


if diff == -180:
    diff = 180

print(diff)