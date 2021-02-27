N = int(input())

A = list(map(int, input().split()))


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

ans = -1
b = 0
for i in range(2, 1001):
  count = 0
  for a in A:
    if a % i == 0:
      count += 1
  if count >= ans:
    b = i
    ans = count

print(b)

