import pickle
import json
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

N = int(input())

#A+B=N-C
ans = 0
for a in range(1, N):
  b = (N-1)//a
  ans += b
print(ans)