from collections import Counter
input("")
inp = input().split()
diceArr = []
for i in range(6):
    for j in range(6):
        diceArr.append((i+1)+(j+1))
countedDice = Counter(diceArr)
total = len(diceArr)
numOccur = 0
for i in inp:
    numOccur += countedDice[int(i)]
print(numOccur/total)
