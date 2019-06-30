t = int(input())
MOD = 10**9+7

def pay(MOD, n, k, votes):
    money = 0
    pre = 0 if votes[-1] == 'A' else 1
    
    if k == 0 and pre == 1:
        money += pow(2,n,MOD)
        pre = 0
    
    for i in range(n-2,-1,-1):
        if pre == k and votes[i] == 'B':
            pre -= 1
            money += pow(2,i+1,MOD)
        else:
            pre = pre+1 if votes[i] == 'B' else pre-1
        if pre < 0: pre = 0
            
    return money%MOD

for i in range(t):
    n, k = [int(s) for s in input().split(' ')]
    votes = input()
    print('Case #{}: {}'.format(i+1, pay(MOD, n, k, votes)))
