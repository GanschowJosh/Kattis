from collections import defaultdict
def next_int(it, chart_string):
    """Read an integer from the string iterator."""
    x = 0
    while it < len(chart_string) and chart_string[it].isdigit():
        x = x * 10 + int(chart_string[it])
        it += 1
    return x, it

def parse_chart(chart_string):
    """Parse a chart string into a hierarchy."""
    it = 0
    org = defaultdict(set)
    roots = []
    
    head = next_int(it, chart_string)[0]
    roots.append(head)
    org[head] = set()

    it = next_int(it, chart_string)[1]

    while it < len(chart_string):
        char = chart_string[it]

        if char == ' ':
            it += 1
        elif char == '(':
            it += 1
        elif char == ')':
            it += 1
            roots.pop()
        else:  # The default case: a department number
            x, it = next_int(it, chart_string)
            org[roots[-1]].add(x)  # Add the child to the current root
            roots.append(x)  # Move to the new department

    return head, org

def main():
    a = input().strip()
    b = input().strip()

    r1, org1 = parse_chart(a)
    r2, org2 = parse_chart(b)

    if r1 != r2:
        print("No")
        return

    stk = [r1]

    while stk:
        r = stk.pop()

        if org1.get(r) != org2.get(r):
            print("No")
            return

        for child in org1[r]:
            stk.append(child)

    print("Yes")

main()
