def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
            if i in d:
              d[i] += 1
            else:
              d[i] = 1
    if n != 1:
        ass.append(n)
        if n in d:
          d[n] += 1
        else:
          d[n] = 1
    return ass
N = int(input())

d = {}
for i in reversed(range(2, N+1)):
  prime_factor(i)

MOD = 10**9+7
ans = 1
for v in d.values():
  ans *= (v+1)
  ans %= MOD
print(ans%MOD)