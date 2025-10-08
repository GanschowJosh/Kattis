numFac = int(input())
opusNums = list(map(int, input().split()))

currentFac = [i + 1 for i in range(numFac)]
current_idx = 0

while len(currentFac) > 1:
  k = opusNums[currentFac[current_idx] - 1]  # Get the opus number of the current professor
  current_idx = (current_idx + k - 1) % len(currentFac)  # Calculate the next elimination index
  currentFac.pop(current_idx)  # Remove the selected professor
  
  if current_idx == len(currentFac):  
    current_idx = 0

print(currentFac[0])