n = int(input())
heights = [int(input()) for _ in range(n)]
print(sum(int(b-a>c-b) for a,b,c in 
zip(heights[:-2],heights[1:-1],heights[2:])))