t = int(input())

def reach(s):
    b = s.count('B')
    sp = s.count('.')
    if not sp: return 'Y' if not b else 'N'
    return 'Y' if b>=sp else 'N'

for i in range(t):
    s = input()
    print("Case #{}: {}".format(i+1,reach(s)))
