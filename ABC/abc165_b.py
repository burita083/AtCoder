X = int(input())

A = 100
r = 0.01

i = 0
while A < X:
  A += (A*1)//100
  i = i + 1

print(i)
