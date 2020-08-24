N, X, T = map(int, input().split())

time = 0

while 0 < N:
  N -= X
  time += T


print(time)