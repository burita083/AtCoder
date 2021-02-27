H, W = map(int,input().split())
S = [input() for i in range(H)]
black = 0
Hs = []
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            break
    else:
        Hs.append(h)

Ws = []
for w in range(W):
    for h in range(H):
        if S[h][w] == "#":
            break
    else:
        Ws.append(w)
new = []
for index, s in enumerate(S):
    if index in Hs: continue
    new.append(s)
new2 = []
for n in new:
    temp = ""
    for index, s in enumerate(n):
        if index in Ws: continue
        temp += s
    new2.append(temp)
for n in new2:
    print(n)
#sy,sx = map(int,input().split())
#gy,gx = map(int,input().split())
#sy,sx,gy,gx = sy-1,sx-1,gy-1,gx-1
#dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#from collections import deque
#dist = [[0]*W for i in range(H)]
#visited = [[0]*W for i in range(H)]
#visited[sy][sx] = 1
#q = deque([(sx, sy)])