N = int(input())

A = list(map(int, input().split()))

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
    while n > 1:
      if prev != sieve[n]:
        prev = sieve[n]
        if sieve[n] in s:
          return False
        else:
          s.add(sieve[n])
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
isPairwise = True
isNext = False
for a in A:
  isPairwise = prime_factor(a)
  if isPairwise:
    continue
  else:
    isNext = True
    break
if isNext == False:
  print("pairwise coprime")
  exit()
   
gd = gcd(A[0], A[1])
if gd == 1:
  print("setwise coprime")
  exit()
for i in range(2, N):
  gd = gcd(gd, A[i])
  if gd == 1:
    print("setwise coprime")
    exit()
print("not coprime")
