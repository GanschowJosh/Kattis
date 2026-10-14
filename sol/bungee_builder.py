n=int(input())
h=list(map(int, input().split()))
l,r=0,n-1

mxl=0
mxr=0
mx=0
while l < r :
  hl=h[l]
  hr=h[r]
  mxl=max(mxl,hl)
  mxr=max(mxr,hr)
  mx=max(mx,mxr-hr,mxl-hl)
  if hl > hr:
    r -= 1
  else:
    l += 1

print(mx)
