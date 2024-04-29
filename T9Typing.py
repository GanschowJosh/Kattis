import sys
numDict = {'a': 2, 'b': 22, 'c': 222, 
           'd': 3, 'e': 33, 'f': 333, 
            'g': 4, 'h': 44, 'i': 444, 
            'j': 5, 'k': 55, 'l': 555,
            'm': 6, 'n': 66, 'o': 666, 
            'p':7, 'q': 77, 'r': 777, 's': 7777,
            't': 8, 'u': 88, 'v': 888,
            'w': 9, 'x': 99, 'y': 999, 'z': 9999,
            ' ': 0}
def lettersToT9():
    lines = input()
    inputs = []
    try:
        for _ in range(int(lines)):
            inputs.append(input())
    except:
        print("Wrong")
        sys.exit()
    lastPrint = 0
    for phrase in inputs:
        print(f"Case #{inputs.index(phrase) + 1}:", end=" ")
        for letter in phrase:
            if lastPrint == str(numDict[letter])[0]:
                print(" ", end="")
            print(numDict[letter], end="")
            lastPrint = str(numDict[letter])[0]
        print(" ")
        
def t9ToLetters():
    nums = input().split()
    numbers = (int(num) for num in nums)
    letterDict = {v:k for k, v in numDict.items()}
    for number in numbers:
        print(letterDict[number], end="")
        
while(True):
    choice = input("Letters to T9 (L)? Or Reverse (R)?\t")
    if choice == 'L':
        lettersToT9()
        break
    elif choice == 'R':
        t9ToLetters()
        break
    else:
        print("Invalid Choice")
