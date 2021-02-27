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
N = int(input())
ans = sorted(divisor(N))
for x in ans:
  print(x)


