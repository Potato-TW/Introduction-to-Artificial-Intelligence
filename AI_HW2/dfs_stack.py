import csv
edgeFile = 'edges.csv'


def dfs(start, end):
    # Begin your code (Part 2)
    '''
    First, I handled the data from "edges.csv" just like bfs. 

    Then, most variables I used in dfs were similar to that in bfs. The most different
    things were I used "stack" to record the next node ready to implement. And also the
    algorithm was a little different with bfs that dfs kept finding the child of a node
    and child's of a child of a node until find the goal.

    Final, after bfs, since "par" recorded child to parent, thus I built path from 
    end to start, and made it reverse, and added the distance between start,end points
    one by one.
    '''

    with open(edgeFile) as file:
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
        stack = []
        stack.append(first)
        vis = []
        vis.append(first)
        num=0
        while(len(stack)>0):
            curv = stack.pop()
            num+=1

            if graph.__contains__(curv)==0:
                continue

            for neighbor in graph[curv]:
                if neighbor[0] not in vis:
                    stack.append(neighbor[0])
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
    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
