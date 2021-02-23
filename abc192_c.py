N, K = map(int, input().split())

def g2(x):
  s = sorted(str(x))
  S = "".join(s)
  return int(S)

def g1(x):
  s = sorted(str(x), reverse=True)
  S = "".join(s)
  return int(S)
  

n = N
for k in range(K):
  G1 = g1(n)
  G2 = g2(n)
  n = G1 - G2
print(n)