from itertools import combinations
from collections import Counter

n, k = map(int, input().split())
probs = []
def isValid(probs, k):
    counter = Counter()
    for problem in probs:
        counter.update(problem)
    print(counter)
    
    return all(count <= k//2 for count in counter.values())

def countValid(n, k, probs):
    valid = 0
    for contest in combinations(probs, k):
        if isValid(contest, k):
            valid+=1
    return valid

for _ in range(n):
    inp = input().split()
    t = int(inp[0])
    topics = tuple(inp[1:])
    probs.append(topics)

print(probs)
print(countValid(n, k, probs))