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