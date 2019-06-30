t = int(input())

def calc(lst):
    n1,sign,n2 = lst
    
    if sign == '|': return n1|n2
    if sign == '&': return n1&n2
    if sign == '^': return n1^n2

def evaluate(s,x):
    stack = []
    n = len(s)
    
    for i in range(n):
        if s[i] == '(':
            stack += [[]]
        elif s[i] == ')':
            num = calc(stack.pop())
            if stack:
                stack[-1] += [num]
            else:
                return num
        elif s[i] == 'x':
            stack[-1] += [x]
        elif s[i] == 'X':
            stack[-1] += [1-x]
        elif s[i].isdigit():
            stack[-1] += [int(s[i])]
        else:
            stack[-1] += [s[i]]
           
for i in range(t):
    s = input()
    
    if len(s)<=1:
        if s == 'X' or s == 'x': change = 1
        else: change = 0
    elif evaluate(s,1) == evaluate(s,0): change = 0
    else: change = 1
    
    print("Case #{}: {}".format(i+1,change))

    
