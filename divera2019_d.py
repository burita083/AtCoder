N = int(input())


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
l = divisor(N)

ans = 0
for n in l:
    m = N//n-1
    if m != 0:
        if N%m == N//m:
            ans += m
print(ans)