n = int(input())
n -= 1

v = []

nums = input().split()
for num in nums:
    v.append(int(num))

totalCost = 0
needed = 1
enough = False

longEdge = pow(2, -3/4)
shortEdge = pow(2, -5/4)

for i in range(len(v)):
    #calculate cost
    totalCost += needed*longEdge #calculates total length of tape needed for the current step,
                                    #taking into account how many sheets are being joined together (needed)
    shortEdge, longEdge = longEdge, shortEdge #accounts for folding the paper in half
    shortEdge/=2

    #calculate paper needed now
    needed *=2 #needed doubled, accounts for smaller paper
    needed -= v[i] #represents using some of the available sheets to create the larger paper

    #check if we have enough paper
    if needed <= 0:
        enough = True
        break

if enough:
    print(totalCost)
else:
    print("Impossible")