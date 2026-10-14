n=int(input())
heights = list(map(int, input().split()))

l,r=0,n-1
mxl=0
mxr=0
mx=0
while l < r:
  hl=heights[l]
  hr=heights[r]
  mxl=max(mxl,hl)
  mxr=max(mxr,hr)
  mx=max(mx,mxl-hl,mxr-hr)
  if hl > hr:
    r-=1
  else:
    l+=1

print(mx)
