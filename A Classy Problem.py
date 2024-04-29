classDict = {"upper": 3, "middle": 2, "lower": 1}

numCases = int(input())
for _ in range(numCases):
    numinCase = int(input())
    peopleClasses = []
    nameDict = {}
    scoreDict = {}
    nameLookup = {}
    maxLen = 0
    inputData = []
    for i in range(numinCase):
        inputData.append(input().split())
    for i in range(numinCase):
        name, classes, x = inputData[i]
        name = name[:-1]
        scoreDict[name] = 0
        nameLookup[i] = name
        cl = classes.split("-")
        maxLen = max(maxLen, len(cl))
        peopleClasses.append(cl)
    for i in range(len(peopleClasses)):
        while len(peopleClasses[i]) < maxLen:
            peopleClasses[i].append("middle")
        for j in range(len(peopleClasses[i])-1, -1, -1):
            scoreDict[nameLookup[i]] += classDict[peopleClasses[i][j]]*(10**(len(peopleClasses[i])-j-1))
    scoreList = sorted([(v, k) for k, v in scoreDict.items()], reverse=True)
    for value, name in scoreList:
        print(name)
    print("=" * 30)
