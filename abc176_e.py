H,W,M = map(int,input().split())
S = [["."]*W for i in range(H)]
for i in range(M):
  h, w = map(int,input().split())
  S[h-1][w-1] = "#"

print(S)

rs = [[0]*W for i in range(H)]
ls = [[0]*W for i in range(H)]
ds = [[0]*W for i in range(H)]
us = [[0]*W for i in range(H)]

for i in range(H):
    tmp = 0
    for j in range(W):
        if S[i][j] == '#':
            tmp += 1
            rs[i][j] = tmp
        else:
            tmp += 0
    tmp = 0

for j in range(W):
    tmp = 0
    for i in range(H):
        if S[i][j] == '#':
            tmp += 1
            ds[i][j] = tmp
        else:
            tmp += 0
    tmp = 0

ans = 0
for i in range(H):
    for j in range(W):
        tmp = rs[i][j] + ls[i][j] + ds[i][j] + us[i][j] - 3
        ans = max(ans, tmp)
print(ans)
