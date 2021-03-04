#https://atcoder.jp/contests/abc012/submissions/me
N,M = map(int,input().split())
INF = float('inf')

dp = [[INF]*N for _ in range(N)]
for _ in range(M):
    a,b,t = map(int,input().split())
    dp[a-1][b-1] = t
    dp[b-1][a-1] = t

for i in range(N): #初期値0
    dp[i][i] = 0

for k in range(N): #中継点
    for i in range(N): #始点
        for j in range(N): #終点
          dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
longest = [0]*N
for i in range(N):
    for j in range(N):
        longest[i] = max(longest[i],dp[i][j])
print(min(longest))