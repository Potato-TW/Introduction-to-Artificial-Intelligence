import csv
edgeFile = 'edges.csv'
# edgeFile = 'test.csv'


def ucs(start, end):
    # Begin your code (Part 3)
    '''
    First, I handled the data from "edges.csv" just like bfs and dfs.

    Then, just like dijkstra, I made "dis" record node and its distance from start point,
    and kept finding the closest node to start point which was not visited, and updated 
    its distance if it was closer than the previous path. And also I recorded how many
    nodes I visited.

    Final, just like bfs and dfs, I found path from end to start point, reversed it, and 
    calculated the distance from start to end point.
    '''

    file = open(edgeFile, 'r')

    rows = csv.reader(file)
    
    graph = {}
    for i in rows:
        if graph.__contains__(i[0]):
            tmp = graph[i[0]]
            tmp.append([i[1], i[2]])
            graph[i[0]] = tmp
        else:
            tmp = []
            tmp.append([i[1], i[2]])
            graph[i[0]] = tmp

    file.close()

    first = str(start)
    last = str(end)

    dis = {}
    for i in graph:
        dis[i]=['none', 10000000000]
        for j in graph[i]:
            dis[j[0]]=['none', 10000000000]
            
    dis[first]=[first,0]

    queue = []
    queue.append([first,0])
    vis = []
    num=0
    while(len(queue)>0):
        queue = sorted(queue, key=lambda q:q[1])
        curv = queue.pop(0)
        num+=1

        if curv[0] in vis:
            continue

        vis.append(curv[0])

        if graph.__contains__(curv[0]) == 0:
            continue

        for i in graph[curv[0]]:
            if i[0] not in vis:
                if dis[i[0]][1]>float(i[1])+dis[curv[0]][1]:                      
                    dis[i[0]]=[curv[0],float(i[1])+dis[curv[0]][1]]
                queue.append([i[0],dis[i[0]][1]])

    cur = last
    result = []
    result.append(cur)
    while(cur != first):
        cur = dis[cur][0]
        result.append(cur)

    result.reverse()

    dist = 0
    for i in range(0, len(result)-1):
        for j in graph[result[i]]:
            if j[0]==result[i+1]:
                dist+=float(j[1])
    
    tmp = []
    for i in result:
        tmp.append(int(i))
    result = tmp

    return result, dist, num
    # raise NotImplementedError("To be implemented")
    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
