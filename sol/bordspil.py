from math import floor
a,u=map(int, input().split())

if floor(2*a/3)+2 > u: print("Arnar")
else: print("Unnar")