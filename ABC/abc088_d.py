H, W = map(int,input().split())
S = [input() for i in range(H)]
count = 0

for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            count += 1

sy,sx = (1, 1)
gy,gx = (H, W)
sy,sx,gy,gx = sy-1,sx-1,gy-1,gx-1
dyx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
from collections import deque
dist = [[0]*W for i in range(H)]
visited = [[0]*W for i in range(H)]
visited[sy][sx] = 1
q = deque([(sy, sx)])
while q:
    y, x = q.popleft()
    for dy, dx in dyx:
        newY = y+dy
        newX = x+dx
        if not 0 <= newY < H: continue
        if not 0 <= newX < W: continue
        if S[newY][newX] == "#": continue
        if visited[newY][newX] == 1: continue

        dist[newY][newX] = dist[y][x] + 1
        visited[newY][newX] = 1
        if newY == gy and newX == gx:
            print(count-dist[newY][newX]-1)
            exit()
        q.append((newY, newX))
print("-1")




        
