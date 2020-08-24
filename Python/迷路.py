R,C = map(int,input().split())

sy,sx = map(int,input().split())

gy,gx = map(int,input().split())

sy,sx,gy,gx = sy-1,sx-1,gy-1,gx-1

S = [input() for i in range(R)]

from collections import deque
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dist = [[0]*C for i in range(R)]
visited = [[0]*C for i in range(R)]
visited[sy][sx] = 1
q = deque([(sx, sy)])

print(visited)
print(q)