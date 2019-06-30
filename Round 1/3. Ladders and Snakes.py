import collections
import heapq

t = int(input())


def construct_graph(n,h,ladders):
    graph = collections.defaultdict(collections.Counter)
    
    for i in range(n):
        lads = [tuple(ladders[i][1:])]
        
        for j in range(i+1,n):
            lad2 = ladders[j][1:]
            new = []

            for lad in lads:
                hi = min(lad[1], lad2[1])
                lo = max(lad[0], lad2[0])
                
                if lo < hi:
                    
                    graph[i][j] += hi-lo
                    graph[j][i] += hi-lo
                    
                    if hi < lad[1]:
                        new.append((hi, lad[1]))
                    if lo > lad[0]:
                        new.append((lad[0],lo))
                else:
                    new.append(lad)

            lads = new
                
    return graph


def find_starts(n,ladders):
    starts = set()
    
    for i in range(n):
        _,a,_ = ladders[i]
        if not a: starts.add(i)

    return starts


def find_ends(n,ladders,h):
    ends = set()
    
    for i in range(n):
        _,_,b = ladders[i]
        if b == h:
            ends.add(i)

    return ends


def find_path(graph, n, starts, ends):
    queue = collections.deque([(s,(s,)) for s in starts])
    visited = set(starts)
    ends = set(ends)
    
    while queue:
        now,path = queue.popleft()
        
        for i in graph[now]:
            if i not in visited:
                if i in ends:
                    return path+(i,)
                queue.append((i,path+(i,)))
                visited.add(i)

    return False


def find_cut_edges(cutted, graph, n, starts, ends):
    new_graph = collections.defaultdict(dict)
    
    for i in graph:
        for j in graph[i]:
            if (i,j) not in cutted and (j,i) not in cutted:
                new_graph[i][j] = graph[i][j]
                new_graph[j][i] = graph[j][i]

    path = find_path(new_graph, n, starts, ends)
    if not path: return False
    
    can_cut_edges = []

    for i in range(len(path)-1):
        a, b = path[i], path[i+1]
        l = graph[a][b]
        can_cut_edges += [(l,a,b)]

    return can_cut_edges


def min_cut(graph, n, starts, ends):
    heap = [(0,set())]
    heapq.heapify(heap)
    m = float('inf')
    good = set([(5, 4), (16, 4), (18, 4), (1, 4), (23, 20), (7, 4), (23, 21), (18, 11), (18, 20)])

    while heap:
        
        cut, cutted = heapq.heappop(heap)
        can_cut_edges = find_cut_edges(cutted, graph, n, starts, ends)
        
        if can_cut_edges:
            for l, i, j in can_cut_edges:
                if (i,j) in good or (j,i) in good:
                    if (i,j) in good:
                        good.remove((i,j))
                    if (j,i) in good:
                        good.remove((j,i))
                new_cutted = set(cutted)
                new_cutted.update([(i,j)])
                
                if new_cutted:
                    heapq.heappush(heap,(l+cut, new_cutted))
        else:
            return cut
        
    return -1

    
def min_snake(n,h,ladders):
    graph = construct_graph(n,h,ladders)
    starts = find_starts(n,ladders)
    ends = find_ends(n,ladders,h)
    
    if len(starts) > len(starts-ends): return -1
    
    return min_cut(graph, n, starts, ends)


def draw_ladders(ladders):
    end_points = set()
    
    for x,a,b in ladders:
       end_points.update([a,b])

for i in range(t):
    n,h = [int(s) for s in input().split(' ')]
    ladders = []

    for j in range(n):
        X_i, A_i, B_i = [int(s) for s in input().split(' ')]
        ladders.append((X_i, A_i, B_i))

    # draw_ladders(ladders)

    ladders = sorted(ladders)

    print('Case #{}: {}'.format(i+1,min_snake(n,h,ladders)))
