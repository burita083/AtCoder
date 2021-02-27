N, M, T = map(int, input().split())
time = 0
temp = N
for x in range(M):
  A, B = map(int, input().split())
  temp -= A-time
  time = A
  if temp <= 0:
    print("No")
    exit()

  temp += B-time
  if temp >= N:
    temp = N
  time = B
temp -= T-time
if temp <= 0:
  print("No")
  exit()
print("Yes")
