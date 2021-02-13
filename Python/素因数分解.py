MAXN = 10**6+10
sieve = [i for i in range(MAXN+1)]
p = 2
while p*p <= MAXN:
    if sieve[p] == p:
        for q in range(2*p,MAXN+1,p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1
 
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
 
"nの素因数分解"
def prime_factor(n):
    prev = -1
    ss=set()
    while n > 1:
      if not sieve[n] in ss:
        prev = sieve[n]
        if sieve[n] in s:
          return False
        else:
          s.add(sieve[n])
          ss.add(sieve[n])
        n //= sieve[n]
      else:
        prev = sieve[n]
        n //= sieve[n]
    if n != 1:
      if sieve[n] in s:
        return False
      else:
        s.add(sieve[n])
    return True
 
s = set()

def eratosthenes(N):
    sieve = [True]*(N+1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(N**.5)+1):
        if not sieve[i]:
            continue
        for j in range(2*i, N+1, i):
            sieve[j] = False
    return [i for i in range(N+1) if sieve[i]]
 
E = eratosthenes(10**6)