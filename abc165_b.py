X = int(input())

A = 100
r = 0.01

i = 0
while A < X:
  A = int(A*(1+r))
  i = i + 1

print(i)
