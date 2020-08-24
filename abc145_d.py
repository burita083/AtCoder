mod = 7+10**9
def ncr(n,c,mod):
  x = 1
  y = 1
  for i in range(n-c+1,n+1):
    x = x*i%mod
  for j in range(1,c+1):
    y = y*j%mod
  return (x * pow(y, mod-2, mod)) % mod

X, Y = map(int, input().split())
if (X+Y) % 3 != 0:
  print(0)
  exit()

n = (2*Y-X) // 3
m = (2*X-Y) // 3
if n < 0 or m < 0:
  print(0)
  exit()

ans = ncr(n+m,n,mod)
print(ans)