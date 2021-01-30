
A, B, C = map(int, input().split())

if C == 0:
  for i in range(301):
    if A == 0:
      print("Aoki")
      exit()
    A -= 1
    if B == 0:
      print("Takahashi")
      exit()
    B -= 1
else:
  for i in range(201):
    if B == 0:
      print("Takahashi")
      exit()
    B -= 1
    if A == 0:
      print("Aoki")
      exit()
    A -= 1
