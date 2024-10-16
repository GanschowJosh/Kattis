n, m = map(int, input().split())
currRankings = [f"T{i+1}" for i in range(n)]
for _ in range(m):
    winner, loser = list(input().split())
    winneridx = currRankings.index(winner)
    loseridx = currRankings.index(loser)
    if winneridx < loseridx:
        continue
    currRankings = currRankings[:loseridx] + currRankings[loseridx+1:winneridx+1] + [loser] + currRankings[winneridx+1:]

print(" ".join(currRankings))
