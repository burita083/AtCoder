mod = 7+10**9
def ncr(n,c,mod):
  x = 1
  y = 1
  for i in range(n-c+1,n+1):
    x = x*i%mod
  for j in range(1,c+1):
    y = y*j%mod
  return (x * pow(y, mod-2, mod)) % mod

n, a, b = map(int, input().split())
al = pow(2, n, mod) -1
acr = ncr(n, a, mod)
bcr = ncr(n, b, mod)
print( (al-(acr+bcr))%mod )