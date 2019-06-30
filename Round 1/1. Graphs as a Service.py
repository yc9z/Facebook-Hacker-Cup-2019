import collections

def check_dist(graph,n):
    for n1 in graph:
        distances = min_dist(n1,graph,n)
        for n2 in graph[n1]:
            if distances[n2]<graph[n1][n2]:
                return False

    return True

def min_dist(start,graph,n):
    queue = collections.deque([(start,0)])
    distances = collections.defaultdict(lambda: float('inf'))

    while queue:
        now, d = queue.popleft()
        for nextt in graph[now]:
            d1 = graph[now][nextt]
            if d+d1 < distances[nextt]:
                queue.append((nextt, d+d1))
                distances[nextt] = d+d1

    return distances


def make_graph(m):
    graph = collections.defaultdict(dict)
    edges = []

    for i in range(m):
        n1,n2,d = [int(s) for s in input().split(' ')]
        if n1 == n2 and d>0: return False, False
        graph[n1][n2] = d
        graph[n2][n1] = d
        edges += [(n1,n2,d)]

    return graph, edges


def print_graph(i, edges, m):
    if not edges:
        print('Case #{}: Impossible'.format(i+1))
    
    else:
        print('Case #{}: {}'.format(i+1, m))
        
        for edge in edges:
            a,b,c = edge
            print('{} {} {}'.format(a,b,c))
        

t = int(input())

for i in range(t):
    n,m = [int(s) for s in input().split(' ')]
    graph, edges = make_graph(m)
    if graph and not check_dist(graph, n): edges = False
    print_graph(i, edges, m)
