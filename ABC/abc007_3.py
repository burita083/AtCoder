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

while q:
  x, y = q.popleft()
  for dx, dy in dxy:
    nx, ny = x+dx, y+dy
    if not 0 <= nx < C: continue
    if not 0 <= ny < R: continue
    if visited[ny][nx] == "#": continue
    if S[ny][nx] == '#': continue
    visited[ny][nx] = "#"
    dist[ny][nx] = dist[y][x] + 1
    q.append((nx, ny))

print(visited)