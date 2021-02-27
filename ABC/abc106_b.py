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

count = 0
for i in range(1, N+1):
  if i % 2 != 0 and len(divisor(i)) == 8:
    count += 1

print(count)

