
H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
sy,sx,gy,gx = Ch-1,Cw-1,Dh-1,Dw-1
S = [input() for i in range(H)]

from collections import deque
dxy = [(0,1),(1,0),(0,-1),(-1,0)]
dist = [[0]*H for i in range(W)]
visited = [[0]*H for i in range(W)]
visited[sy][sx] = 1
q = deque([(sx,sy)])
while q:
    x,y = q.popleft()
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if not 0 <= nx < H: continue
        if not 0 <= ny < W: continue
        if visited[ny][nx]: continue
        if S[ny][nx] == '#': continue
        visited[ny][nx] = 1
        dist[ny][nx] = dist[y][x] + 1
        q.append((nx,ny))
print(dist[3][0])

