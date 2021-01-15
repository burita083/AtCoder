def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False

    return True
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

N = int(input())

d = {}
for i in range(1, N+1):
    if is_prime(i):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    else:
        l = prime_factor(i)
        for ll in l:
            if ll in d:
                d[ll] += 1
            else:
                d[ll] = 1

ans = 1
MOD = 10**9+7
for e in d.values():
    ans *= (e+1)
    ans %= MOD
print(ans)


