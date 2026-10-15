t=int(input())
for _ in range(t):
    n=int(input())
    for _ in range(n-2):
        print("."*n)
    print("."*(n-1)+"C")
    print("."*(n-2)+"C.")