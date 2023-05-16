import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar(start, end):
    # Begin your code (Part 4)
    '''
    First, collect the data from "edges.csv" just like the 3 other cases. But this time
    I built dictionary for "heuristic.csv" that via choosing the end point from the first
    line in "heuristic.csv", I inserted that column into "heu", and built dictionary "g"
    and "f" to record distance from start point and sum of that and distance to end point 
    from "heu" respectively.

    Then, according to the value in "f" of the node, I found the smallest one's neighbors.
    Check if visited and if distance from start point to previous node added by previous 
    node to its is smaller than distance from start point to it that recorded. If so, add
    it to "queue" and wait for handle. And also update "vis" (visited node), "par" (parent
    node), "g', "f".

    Final, just like other 3 cases, find path from end to start point, and reverse it.
    Calculated the distance from start to end point.
    '''

    a = open(edgeFile, 'r')
    b = open(heuristicFile, 'r')

    edg = {}
    heu = {}
    tmp = csv.reader(a)
    cnt = 0
    for i in tmp:
        if cnt == 0:
            cnt += 1
            continue
        if edg.__contains__(i[0]):
            edg[i[0]].append([i[1], float(i[2])])
        else:
            edg[i[0]] = [[i[1], float(i[2])]]

    tmp = csv.reader(b)
    htmp = []
    for i in tmp:
        htmp.append(i)

    a.close()
    b.close()

    first = str(start)
    last = str(end)

    index = htmp[0].index(last)
    heu = {}
    for i in htmp:
        if i == htmp[0]:
            continue
        heu[i[0]] = float(i[index])

    g = {}
    f = {}
    for i in edg:
        for j in edg[i]:
            g[j[0]] = 10000000000
    for i in edg:
        for j in edg[i]:
            f[j[0]] = 10000000000
    g[first] = 0
    f[first] = heu[first]

    par = {}
    queue = []
    queue.append([first, f[first]])
    vis = []
    num=0
    while (len(queue) > 0):
        queue = sorted(queue, key=lambda x: x[1])
        curv = queue.pop(0)
        num += 1

        if curv[0] == last:
            break
        
        if edg.__contains__(curv[0])==0:
            continue

        for neighbor in edg[curv[0]]:
            cal = g[curv[0]] + neighbor[1]

            flag = 0
            if neighbor[0] not in vis:
                flag = 1
                
            if cal < g[neighbor[0]]:
                flag = 1
            
            if flag:
                vis.append(neighbor[0])
                par[neighbor[0]] = curv[0]
                g[neighbor[0]] = cal
                f[neighbor[0]] = g[neighbor[0]]+heu[neighbor[0]]
                queue.append([neighbor[0], f[neighbor[0]]])

    cur = last
    result = []
    result.append(cur)
    while (cur != first):
        cur = par[cur]
        result.append(cur)

    result.reverse()

    dis = 0
    for i in range(0, len(result)-1):
        for j in edg[result[i]]:
            if j[0] == result[i+1]:
                dis += float(j[1])

    tmp = []
    for i in result:
        tmp.append(int(i))
    result = tmp

    return result, dis, num
    # raise NotImplementedError("To be implemented")
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
