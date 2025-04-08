c = float(input())
l = int(input())
running = 0
for _ in range(l):
    width, length = map(float, input().split())
    running += (width*length)*c
print(running)