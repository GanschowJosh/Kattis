inp1 = input("")
inp = input("").split(" ")
total = 0
for i in inp:
    if int(i) < 0:
        total +=1
print (total)