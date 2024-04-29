ops = ['+', '-', '*', '/']
evals = {}

def ev(a, b, op):
    if op == '/':
        result = eval(str(a) + str(op) + str(b))
        return str(int(result)) if result.is_integer() else "{:.6f}".format(result).lstrip('0') or '0'
    else:
        return str(eval(str(a) + str(op) + str(b)))

for i in range(4):
    for j in range(4):
        for k in range(4):
            expression = '4' + ops[i] + '4' + ops[j] + '4' + ops[k] + '4'
            print(expression)
            # Process * and / from left to right
            x = 1
            while x < len(expression):
                if expression[x] == '*' or expression[x] == '/':
                    expression = expression[:x-1] + ev(expression[x-1], expression[x+1], expression[x]) + expression[x+2:]
                else:
                    x += 2

            # Process + and - from left to right
            y = 1
            while y < len(expression):
                if expression[y] == '+' or expression[y] == '-':
                    expression = expression[:y-1] + ev(expression[y-1], expression[y+1], expression[y]) + expression[y+2:]
                else:
                    y += 2
            
            evals[expression] = eval(expression)

print(evals)
