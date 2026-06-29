n=int(input())
nums=list(map(int, input().split()))

lb=[0]*n
ls=[0]*n

for i in range(n):
  if i > 0 and nums[i-1]<=nums[i]:
    lb[i]=lb[i-1]
    ls[i]=ls[i-1]
  else:
    lb[i]=nums[i]
    ls[i]=i


rb=[0]*n
rs=[0]*n

for i in range(n-1,-1,-1):
  if i+1 < n and nums[i] >= nums[i+1]:
    rb[i]=rb[i+1]
    rs[i]=rs[i+1]
  else:
    rb[i]=nums[i]
    rs[i]=i

mx = 0

for j in range(n):
  if ls[j] < j and rs[j]>j:
    mx=max(mx, min(nums[j]-lb[j], nums[j]-rb[j]))

print(mx)