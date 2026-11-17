from collections import defaultdict

N = int(input())
prices = list(map(int,input().split()))
dprices = defaultdict(int)
for p in prices:
  dprices[p%5] += 1

save=0
amt=(min(dprices[4],dprices[3]))
save += 2*amt
dprices[4]-=amt
dprices[3]-=amt

amt=dprices[4]//3
save+=2*amt
dprices[4]-=(3*amt)

amt=dprices[3]//2
save+=amt
dprices[3]-=(2*amt)

for i,num in dprices.items():
  if i in [1,2]:
    save+=i*(num)
  if i == 3:
    save-=2*num
  if i == 4:
    save-=num

print(save)