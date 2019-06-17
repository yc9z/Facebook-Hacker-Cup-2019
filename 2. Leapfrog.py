t = int(input())

def reach(s):
    b = s.count('B')
    sp = s.count('.')
    if not sp: return 'Y' if not b else 'N'
    if not b or (b == 1 and sp>1): return 'N'
    return 'Y'

for i in range(t):
    s = input()
    print("Case #{}: {}".format(i+1,reach(s)))
