n,lph=map(int, input().split())
nums = []
for _ in range(n):
  nums.append(int(input()))

nums.sort()
curr = 0
point = 0
while point < len(nums) and curr+nums[point] <= lph*5:
  curr += nums[point]
  point += 1

print(point)