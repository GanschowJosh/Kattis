t=int(input())
for _ in range(t):
    n,p=map(int, input().split())
    bks=list(map(int, input().split()))
    su=sum(bks)
    npu=p/su
    s=0
    for i in bks:
        s+=(((npu*i)**2)/i)
    print(s)