import itertools
S = int(input())



ans = 0
rng = S//3
amari = 1000000007
for i in range(1, rng+1):
  mn = 3*i
  if S < mn:
    continue

  diff = S-mn
  l = []
  for k in range(0, diff+1):
    l.append(k)

  Ls = list(itertools.product(l, repeat=i))
  for L in Ls:
    if sum(L) == diff:
      print(L)
      ans += 1
      ans %= amari

print(ans%amari)



