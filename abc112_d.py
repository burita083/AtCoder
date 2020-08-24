
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass

N, M = map(int, input().split())

divisors = divisor(M)

ans = 1
divisors.sort()

for d in divisors:
  if N*d <= M:
    ans = d

print(ans)