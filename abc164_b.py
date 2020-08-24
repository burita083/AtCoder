A, B, C, D = map(int, input().split())

for _ in range(10000):
  C -= B
  if C <= 0:
    print("Yes")
    exit()

  A -= D
  if A <= 0:
    print("No")
    exit()

