import sys
counter = 1
for line in sys.stdin:
    line = list(map(int, line.split()))
    num = line[0]
    line = line[1:]
    print(f"Case {counter}: {min(line)} {max(line)} {max(line)-min(line)}")
    counter+=1