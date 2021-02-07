import sys
sys.setrecursionlimit(1000000)
N, M = map(int, input().split())

graph = [[] for _ in range(N)]
memo = [False] * N

for _ in range(M):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)

dp = [0] * N
def dfs(n):
  if memo[n]: 
    return dp[n]
  for to in graph[n]:
    dp[n] = max(dfs(to) + 1, dp[n])
  memo[n] = True
  return dp[n]

for i in range(N):
  dfs(i)

print(max(dp))