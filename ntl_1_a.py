def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass

n = int(input())
primes = prime_factor(n)
primes.sort()
ans = str(n) + ":"
for p in primes:
  ans += " " + str(p)
print(ans)