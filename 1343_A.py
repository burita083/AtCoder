t = int(input())

l = []
for x in range(t):
  n = int(input())
  x = -1
  total = 1
  k = 2
  while x == -1:
    total += 2**(k-1)
    if n % total == 0:
      x = n//total
      l.append(x)
    k += 1


for x in l:
  print(x)
