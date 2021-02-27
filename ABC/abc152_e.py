MAXN = 10**6+1
E = [i for i in range(MAXN+1)]
p = 2
while p*p <= MAXN:
    if E[p] == p:
        for q in range(2*p,MAXN+1,p):
            if E[q] == q:
                E[q] = p
    p += 1

dic = {}
N = int(input())
A = list(map(int, input().split()))
for a in A:
  x = a
  c = 0
  prev = E[a]
  while x > 1:
    if x%E[x] == 0:
      if prev != E[x]: 
        c = 0
      c += 1
      if E[x] in dic:
        dic[E[x]] = max(dic[E[x]], c)
      else:
        dic[E[x]] = c
      prev = E[x]
      x //= E[x]

P = 1
for k, v in dic.items():
  for i in range(v):
    P *= k

p = 10**9+7
ans = 0
for a in A:
  ans += P*pow(a, -1, p)
  ans %= p

print(ans)