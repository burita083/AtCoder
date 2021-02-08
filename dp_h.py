H, W = map(int,input().split())
S = [input() for i in range(H)]

#sy,sx = map(int,input().split())
#gy,gx = map(int,input().split())
#sy,sx,gy,gx = sy-1,sx-1,gy-1,gx-1
#dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#from collections import deque
#dist = [[0]*W for i in range(H)]
#visited = [[0]*W for i in range(H)]
#visited[sy][sx] = 1
#q = deque([(sx, sy)])

dp = [[1]*W for _ in range(H)]
for y in range(H):
    if y-1 >= 0:
        if S[y][0] == "#" or dp[y-1][0] == 0:
            dp[y][0] = 0


for x in range(W):
    if x-1 >= 0:
        if S[0][x] == "#" or dp[0][x-1] == 0:
            dp[0][x] = 0

for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            dp[y][x] = 0
        else:
            if y-1 >= 0 and x-1 >= 0:
                dp[y][x] = dp[y-1][x] + dp[y][x-1]

MOD = 10**9+7
print(dp[H-1][W-1]%MOD)