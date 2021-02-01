"nの素因数分解"
def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass

N, P = map(int, input().split())

from collections import Counter
primes = prime_factor(P)
C = Counter(primes)

ans = 1
for k, v in C.items():
  if v >= N:
    count = v//N
    ans *= (k ** (v//N))
print(ans)


