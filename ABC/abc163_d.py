INF = 10 ** 9 + 7
N, K = map(int, input().split())

ans = 0
mx = 0
mn = 0

for i in range(N+1):
  mx += N-i
  mn += i
  if i + 1 >= K:
    ans += (mx - mn + 1) % INF

print(ans % INF)
