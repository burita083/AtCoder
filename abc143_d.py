N = int(input())
L = list(map(int, input().split()))

L.sort()

ans = 0
print(L)
for i in range(N - 2):
  a = L[i]
  for j in range(i + 1, N - 1):
    b = L[j]
    c = bisect_left(L, a + b)
    ans += c - j - 1
    print(a, b, c-j-1)

print(ans)