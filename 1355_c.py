from bisect import bisect_left
L = list(map(int, input().split()))
N = 4

ans = 0
for i in range(N-2):
  a = L[i]
  for j in range(N-2):
    b = L[j]
    c = bisect_left(L, a + b)
    ans += c - j - 1
    for x in range(L[c-j-1]):
      print(a, b, L[x])
    #if L[0] <= a <= L[1] and L[1] <= b <= L[2] and L[2] <= c <= L[3]:
     # print(a, b, c)

#print(ans)
