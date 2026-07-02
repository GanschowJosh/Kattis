s = input().strip()

cnt={'A':0,'B':0,'C':0}

ans=0
for ch in s:
  cnt[ch]+=1
  ans=max(ans, max(cnt.values())-min(cnt.values()))

print(ans)