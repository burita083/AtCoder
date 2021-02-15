N, K = map(int, input().split())

def count(n):
    if n < 2 or n > 2*N: return 0
    if n <= N+1:
        return n-1
    else:
        return 2*N+1-n

ans = 0
for x in range(2, 2*N+1):
    Y = x-K
    ans += count(x) * count(Y)
print(ans)

