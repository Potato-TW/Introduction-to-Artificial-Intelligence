from bfs import bfs
from dfs_stack import dfs
from ucs import ucs
from astar import astar
from astar_time import astar_time

start = [2270143902, 426882161, 1718165260, 1]
end = [1079387396, 1737223506, 8513026827, 5]

# start = 2270143902
# end = 1079387396

# start = 426882161
# end = 1737223506

# start = 1718165260
# end = 8513026827

# start = 1
# end = 5
for i in range(3):
    # a,b,c = bfs(start[i], end[i])
    # print(f'bfs: {len(a)} {b}, {c}')
    # a,b,c= dfs(start[i], end[i])
    # print(f'dfs: {len(a)} {b}, {c}')
    # a,b,c = ucs(start[i], end[i])
    # print(f'uscs: {len(a)} {b}, {c}')
    # a, b, c = astar(start[i], end[i])
    # print(f'astar: {len(a)} {b}, {c}\n')
    astar_time(start[i], end[i])
    # print(f'astar_time: {len(a)} {b}, {c}\n')

