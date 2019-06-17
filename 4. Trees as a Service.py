import collections

t = int(input())

def divide(root, nodes, rels):
    same_side = collections.defaultdict(list)
    other_side = collections.defaultdict(list)
    
    for x,y,z in rels:
        if z != root:
            same_side[x] += [y,z]
            same_side[y] += [x,z]
        else:
            other_side[x] += [y]
            other_side[y] += [x]

    parts = []
    
    while nodes:
        part = set()
        subrel = []
        stack = [nodes.pop()]
        while stack:
            now = stack.pop()
            part.add(now)
            for n in same_side[now]:
                if n in nodes:
                    stack.append(n)
                    nodes.remove(n)
        for p in part:
            for node in other_side[p]:
                if node in part:
                    return False
        for x,y,z in rels:
            if z in part:
                subrel += [(x,y,z)]

        parts += [(part,subrel)]
    
    return parts

    
def plant(nodes,rels):
    if not rels:
        done.update(nodes)
        return True
    
    roots = set(nodes)
    
    for x,y,z in rels:
        if x in roots and x!=z: roots.remove(x)
        if y in roots and y!=z: roots.remove(y)

    if not roots: return False

    root = roots.pop()
    done.add(root)

    nodes.remove(root)

    for n in nodes:
        if n not in done:
            tree[n-1] = root
            
    nextt = divide(root, nodes, rels)
    
    if not nextt: return False
    
    for nodes,rels in nextt:
        if not plant(nodes, rels): return False

    return True

    
for i in range(t):
    n,m = [int(s) for s in input().split(' ')]
    rels = []
    done = set()
    
    for j in range(m):
        x,y,z = [int(s) for s in input().split(' ')]
        rels += [(x,y,z)]

    tree = [0]*n
        
    if not plant(set([i for i in range(1,n+1)]),rels):
        print("Case #{}: {}".format(i+1, 'Impossible'))
    else:
        print("Case #{}:".format(i+1),*tree)
    
    
