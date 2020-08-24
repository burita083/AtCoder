N = int(input())


while N >= 0:
  N -= 1000
  if N == 0:
    break

print(abs(N))