import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'

def astar_time(start, end):
    # Begin your code (Part 6)
    '''
    Most code is equal to astar.py. But some containers are changed a little that 
    "edg" is enhanced and becomes "dictionary:[dictionary]" and adds speed limit to it,
    and "heu" is also added speed limit. However, I replace values in heuristic function
    with time instead of distance, which I just divides distance by average of every
    speed limit from endpoint's neighbors to the endpoint. And use astar algorithm 
    but use time as comparing value instead of distance.
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
        if edg.__contains__(int(i[0])):
            speed = float(i[3])*1000/3600
            edg[int(i[0])].append({int(i[1]): [float(i[2])/speed, speed]})
        else:
            speed = float(i[3])*1000/3600
            edg[int(i[0])] = [{int(i[1]): [float(i[2])/speed, speed]}]

    tmp = csv.reader(b)
    htmp = []
    for i in tmp:
        htmp.append(i)

    a.close()
    b.close()

    index = htmp[0].index(str(end))
    heu = {}
    for i in htmp:
        if i == htmp[0]:
            continue
        heu[int(i[0])] = [float(i[index])]

    cnt=0
    avg=0
    for i in edg:
        for j in edg[i]:
            for k in j:
                if k==end:
                    cnt+=1
                    avg+=j[k][1]
    
    # print(cnt)
    avg/=cnt
    # print(avg)
    

    for i in heu:
        # avg = 0
        # if edg.__contains__(i)==0:
        #     continue
        # for j in edg[i]:
        #     for k in j:
        #         if avg<j[k][1]:
        #             avg = j[k][1]
        # avg /= len(edg[i])    
        heu[i].append(avg)
    # print(heu)
    for i in heu:
        if len(heu[i])<2:
            heu[i].append(1)
        heu[i][0]/=heu[i][1]

    g = {}
    f = {}
    for i in edg:
        for j in edg[i]:
            for k in j:
                g[k] = 10000000000
    for i in edg:
        for j in edg[i]:
            for k in j:
                f[k] = 10000000000
    g[start] = 0
    f[start] = heu[start]

    par = {}
    queue = []
    queue.append([start, f[start]])
    vis = []
    num=0
    while (len(queue) > 0):
        queue = sorted(queue, key=lambda x: x[1])
        curv = queue.pop(0)
        num += 1

        if curv[0] == end:
            break
        
        if edg.__contains__(curv[0])==0:
            continue

        for neighbor in edg[curv[0]]:
            for k in neighbor:
                endpoint = k
                cal = g[curv[0]] + neighbor[k][0]

            flag = 0
            if endpoint not in vis:
                flag = 1
                
            if cal < g[endpoint]:
                flag = 1
            
            if flag:
                vis.append(endpoint)
                par[endpoint] = curv[0]
                g[endpoint] = cal
                f[endpoint] = g[endpoint]+heu[endpoint][0]
                queue.append([endpoint, f[endpoint]])

    cur = end
    result = []
    result.append(cur)
    while (cur != start):
        cur = par[cur]
        result.append(cur)

    result.reverse()

    time = 0
    for i in range(0, len(result)-1):
        for j in edg[result[i]]:
            for k in j:
                if k==result[i+1]:
                    time+=j[k][0]
                    break
    # print(edg)
    # print(len(result))
    # print(time)
    # print(num)

    return result, time, num
    # raise NotImplementedError("To be implemented")
    # End your code (Part 6)


if __name__ == '__main__':
    path, time, num_visited = astar_time(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total second of path: {time}')
    print(f'The number of visited nodes: {num_visited}')
