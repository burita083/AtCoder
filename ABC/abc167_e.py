N, M, K = map(int, input().split())

MOD = 998244353

ans = 0

for k in range(K + 1):
  ans += M * nCr(N-1)