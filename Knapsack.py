"""
Verdict: TLE
"""
from sys import stdin, stdout
def knapsack(c, n, values, weights):
    dp = [0] * (c+1)
    chosen = [[] for _ in range(c+1)]

    for i in range(n):
        for w in range(c, weights[i]-1, -1):
            if dp[w] < dp[w-weights[i]] + values[i]:
                dp[w] = dp[w-weights[i]] + values[i]
                chosen[w] = chosen[w-weights[i]] + [i]

    maxvalue = max(dp)
    maxidx = dp.index(maxvalue)

    return len(chosen[maxidx]), chosen[maxidx]

input = stdin.readline
print = stdout.write
while True:
    try:
        c, n = list(map(int, input().split()))
        values = []
        weights = []
        for _ in range(n):
            v, w = list(map(int, input().split()))
            values.append(v)
            weights.append(w)

        numChosen, chosen = knapsack(c, n, values, weights)
        print(f"{numChosen}\n")
        print(' '.join(map(str, chosen)) + '\n')
    
    except EOFError:
        break

