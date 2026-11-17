s=input()
n=len(s)
m=int(input())
amt=0
a=0
for i in range(n):
  if s[i]!='A': amt+=a
  else: a+=1

end=n
while end > 0 and s[end-1] =='A':
  end-=1

count=0
i=end-1
while end > 0 and count < m and i >= 0:
  if s[i]=='A':
    mm=min(m-count,end-i-1)
    # print(end,i,mm,count)
    count+=mm
    amt-=mm
    end-=1
  i-=1

print(amt)