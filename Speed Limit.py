while True:
    n = int(input())
    if n==-1:
        break
    totaldist = 0
    currhrs = 0
    a,b = list(map(int, input().split()))
    totaldist += a*b
    currhrs = b
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        totaldist += a*(b - currhrs)
        currhrs = b
    print(f"{totaldist} miles")
