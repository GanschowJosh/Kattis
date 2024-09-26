import sys
vardict = {}
for line in sys.stdin:
    line = line.split()
    if line[0] == "def":
        if line[1] in vardict:
            oldVal = vardict[line[1]]
            del vardict[int(oldVal)]
        vardict[line[1]] = line[2]
        vardict[int(line[2])] = line[1]
    if line[0] == "calc":
        try:
            a = eval("".join([vardict.get(item, item) for item in line[1:-1]]))
            print(" ".join(line[1:]) + " " + vardict[a])
        except:
            print(" ".join(line[1:]) + " unknown")
    if line[0] == "clear":
        vardict = {}