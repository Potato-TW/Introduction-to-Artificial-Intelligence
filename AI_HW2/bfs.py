import csv
edgeFile = 'edges.csv'


def bfs(start, end):
    # Begin your code (Part 1)
    '''
    First, I opened the file "edges.csv" and turned it into a dictionary "graph" of
    "key : value" in "start point : [end point, distance]".

    Then, "queue" was used to collect all the neighbors, which I visited children's 
    neighbors after visiting parent's neighbors. "Par" was used to record who was the
    node's parent, and also "vis" was used to record which node was visited
    and avoided visiting it again, and "num" recorded how many nodes I visited.

    Final, after bfs, since "par" recorded child to parent, thus I built path from 
    end to start, and made it reverse, and added the distance between start,end points
    one by one.
    '''
    with open(edgeFile, newline='') as file:
        rows = csv.reader(file)

        first = str(start)
        last = str(end)

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
        
        par = {}
        q = []
        q.append(first)
        vis = []
        vis.append(first)
        num=0
        while(len(q)>0):
            curv = q.pop(0)
            num+=1

            if graph.__contains__(curv)==0:
                continue

            for neighbor in graph[curv]:
                if neighbor[0] not in vis:
                    q.append(neighbor[0])
                    vis.append(neighbor[0])
                    if par.__contains__(neighbor[0]):
                        graph[neighbor[0]].append(curv)
                    else:
                        tmp=[]
                        tmp.append(curv)
                        par[neighbor[0]] = tmp

        cur = last
        result = []
        result.append(cur)
        while(cur != first):
            cur = par[cur][0]
            result.append(cur)

        result.reverse()

        dis = 0
        for i in range(0, len(result)-1):
            for j in graph[result[i]]:
                if j[0]==result[i+1]:
                    dis+=float(j[1])
    
    tmp = []
    for i in result:
        tmp.append(int(i))
    result = tmp
    
    return result, dis, num

    # raise NotImplementedError("To be implemented")
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
