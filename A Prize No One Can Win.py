n, x = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
score = 0
idx = 0
while idx < n-1 and nums[idx] + nums[idx+1] <= x:
  score += 1
  idx+=1
print(score+1)