inp = input()
abbr = inp[0]
prev = ''
for letter in inp:
    if prev == '-':
        abbr += letter
    prev = letter

print(abbr)