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

for _ in range(N):
  A, B = map(int, input().split())
  a = prime_factor(A)
  b = prime_factor(B)
  l1 = []
  l2 = []
  for x in a:
    if x != 2:
      l1.append(x)
    else:
      l2.append(x)

  m1 = []
  m2 = []
  for x in b:
    if x != 2:
      m1.append(x)
    else:
      m2.append(x)

  l = l2 + m2
  if sum(l1) == sum(m1):

print(l)