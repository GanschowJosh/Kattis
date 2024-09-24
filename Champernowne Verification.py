def generate(s):
    result = ""
    number = 1
    while(len(result) < s):
        result += str(number)
        number+=1
    return result
    

def isC(s):
    a = generate(len(s))
    if s == a:
        return a[-1]
    else:
        return -1
    
inp = input()
print(isC(inp))
