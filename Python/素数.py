def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())

if is_prime(n):
    print("Yes")
else:
    print("No")

"nの約数列挙"
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass

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

#n以下の素数列挙(O(n log(n))
def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass

"a以上b未満の素数列挙"
def segment_sieve(a,b):
    ass = []
    is_prime_small = [True] * (int(b**0.5)+1)
    is_prime = [True] * (b-a)
    for i in range(2,int(b**0.5)):
        if is_prime_small[i]:
            j = 2*i
            while j**2 < b:
                is_prime_small[j] = False
                j += i
            j = max(2*i,((a+i-1)//i)*i)
            while j < b:
                is_prime[j-a] = False
                j += i
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(a+i)
    if ass[0] == 1:
        del ass[0]
    return ass


def furui() {
    d = []
    temp = 2
    d[temp] = 2
    for i in range(temp*2, 10**7+1, temp):
        d[i] = d[i-temp]+1
}

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def gcd_r(x, y):
    if b == 0:
        return x
    else:
        gcd_r(y, x % y)