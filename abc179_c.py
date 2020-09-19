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

count = 0
#for a in range(1, 10**3):
  #for b in range(1, 10**3):
    #c = N-(a*b)
    #if c >= 1 and c <= N-1:
      #print(a, b, c)
      #count += 1


d = {}
for x in range(1, N+1):
  count = 0
  for c in range(1, x):
    temp = x-c
    for a in range(1, (temp+1)//2):
      if temp % a == 0:
        count += 1
        if temp / a != a:
          count += 1

  d[x] = count

  with open('file.txt', 'w') as file:
    file.write(json.dumps(d))

  print(d[x])
