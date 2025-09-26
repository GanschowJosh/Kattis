arr = list(map(int, input().split()))
arr = arr[1:]
num_nums = len(arr)
right_min = [float('inf')]*num_nums
left_max = [float('-inf')]*num_nums

for i in range(1, num_nums):
    left_max[i] = max(left_max[i-1], arr[i-1])

for i in range(num_nums-2, -1, -1):
    right_min[i] = min(right_min[i+1], arr[i+1])

num_pivs = 0
pivs = []
for i in range(num_nums):
    if left_max[i] <= arr[i] <= right_min[i]:
        num_pivs +=1
        pivs.append(arr[i])

print(f"{num_pivs}", end=' ')
end = num_pivs
if num_pivs > 100:
    end = 100
for i in range(end):
    print(pivs[i], end=' ')

