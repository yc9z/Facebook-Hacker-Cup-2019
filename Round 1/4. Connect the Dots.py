import heapq
import collections


def draw(points):
    to_draw = collections.defaultdict(list)
    max_x, max_y = 0,0
    occured_x, occured_y = set(), set()
    
    for x,y in points:
        to_draw[y] += [x]
        if y>max_y: max_y = y
        if x>max_x: max_x = x
        occured_x.add(x)
        occured_y.add(y)
        
    for y in range(max_y+1,-1,-1):
        if y in to_draw:
            for x in range(0,max_x+1):
                if x not in to_draw[y]:
                    if x in occured_x:
                        print('     ', end = ' ')
                else:
                    print((x,y), end = ' ')
        if y in occured_y:
            print(' ')



"""
def connect_ver(n,h,v,points):
    points = [(y,x) for x,y in points]
    h,v = v,h
    print(connect_hoz(n,h,v,points))
    return connect_hoz(n,h,v,points)
"""


def find_points(n,x1,x2,ax,bx,cx,dx,y1,y2,ay,by,cy,dy):
    points = [(x1,y1),(x2,y2)]
    
    for i in range(2,n):
        x1, y1 = points[i-2]
        x2, y2 = points[i-1]
        x = (ax*x1+bx*x2+cx) % dx + 1
        y = (ay*y1+by*y2+cy) % dy + 1
        points.append((x,y))

    return points


def connect_hoz(n,h,v,points):
    if h+v < n: return -1
    
    # hoz_points is a max heap
    _, _, hoz_points, ver_cost = find_most_hoz_points(n,h,points)
    #print(hoz_points,ver_cost)
    cost = float('inf')
    ver_num = n-len(hoz_points)

    while hoz_points and ver_num <= v:
        x, y = hoz_points.pop()
        if cost > ver_cost + x:
            cost = ver_cost + x
            #print(cost, hoz_points, ver_cost)
        ver_cost = max(ver_cost, y)
        ver_num += 1

    if ver_num <= v: cost = min(cost,ver_cost)
    

    hoz_points = [(y,x) for x,y in points[:h]]
    heapq.heapify(hoz_points)
    extra_ver_cost = 0
    ver_costs = [0]*n
    ver_costs[-1] = points[-1][1]
    
    for i in range(n-2,-1,-1):
        ver_costs[i] = max(ver_costs[i+1],points[i][1])

    
    for i in range(h,n):
        if hoz_points:
            y,x = heapq.heappop(hoz_points)
            extra_ver_cost = max(extra_ver_cost,y)
            if i+1<n:
                ver_cost = max(ver_costs[i+1], extra_ver_cost)
            else:
                ver_cost = extra_ver_cost
            x1,y1 = points[i]
            heapq.heappush(hoz_points,(y1,x1))
        
            if cost > ver_cost + x1:
                cost = ver_cost + x1
                #print(cost, hoz_points, ver_cost)
        else:
            break

    return cost


def find_most_hoz_points(n,h,points):
    height = 0
    reduced_points = []
    """
    
    for i in range(n-1,-1,-1):
        x, y = points[i]
        if height < y:
            height = y
            reduced_points = [(x,y)] + reduced_points
    n = len(reduced_points)
    """
    ver_cost = 0
    

    hoz_points = points[:h]
    
    ver_cost = max([y for _,y in points[h:]]+[0])

    return n, reduced_points, hoz_points, ver_cost


t = int(input())
for i in range(t):
    n, h, v = [int(s) for s in input().split(' ')]
    x1, x2, ax, bx, cx, dx = [int(s) for s in input().split(' ')]
    y1, y2, ay, by, cy, dy = [int(s) for s in input().split(' ')]
    points = find_points(n,x1,x2,ax,bx,cx,dx,y1,y2,ay,by,cy,dy)
    #print(points)
    points = sorted(points)
    #draw(points)
    ans = connect_hoz(n,h,v,points)
    print('Case #{}: {}'.format(i+1, ans))
