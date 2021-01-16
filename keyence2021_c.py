
H,W, K = map(int,input().split())
sy,sx = (1, 1)
gy,gx = (H, W)
sy,sx,gy,gx = sy-1,sx-1,gy-1,gx-1
S = [[0]*W for i in range(H)]
d = {}
for i in range(K):
  A = list(input().split())
  h, w = int(A[0])-1, int(A[1])-1
  S[h][w] = A[2]
  if A[2] in d:
    d[A[2]] += 1
  else:
    d[A[2]] = 1

count = H*W-K
print(count)
#from collections import deque
#dxy = [(0,1),(1,0),(0,-1),(-1,0)]
#dist = [[0]*C for i in range(R)]
#visited = [[0]*C for i in range(R)]
#visited[sy][sx] = 1
#q = deque([(sx,sy)])
#while q:
    #x,y = q.popleft()
    #for dx,dy in dxy:
        #nx,ny = x+dx,y+dy
        #if visited[ny][nx]: continue
        #if S[ny][nx] == '#': continue
        #visited[ny][nx] = 1
        #dist[ny][nx] = dist[y][x] + 1
        #q.append((nx,ny))
        #if ny==gy and nx==gx:
            #print(dist[ny][nx])
            #exit()
MOD = 998244353
 
MAXN = 2*10**5+5
fac = [1,1] + [0]*MAXN
finv = [1,1] + [0]*MAXN
inv = [0,1] + [0]*MAXN
for i in range(2,MAXN+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD
 
def comb(n,r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD
 
R = comb(H+W-2, H-1) * (count - d["R"]) % MOD
D = comb(H+W-2, H-1) * (count - d["D"]) % MOD
X = comb(H+W-2, H-1) * (count - d["X"]) % MOD
print(R+D+X)