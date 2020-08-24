t = int(input())

for _ in range(t):
  n, k = map(int, input().split())
  j = n-1
  if k % j == 0:
    near = k // j #97//6
    ans = near*n-1
    print(ans)
  else:
    near = k // j #97//6
    amari = k%j
    ans = near*n-1
    ans += amari + 1
    print(ans)
