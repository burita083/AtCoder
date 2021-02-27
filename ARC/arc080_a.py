N = int(input())

from collections import Counter
A = list(map(int, input().split()))
C = Counter(A)

count = 0
two = 0
for k, v in C.items():
  if k % 4 != 0 and k % 2 == 0:
    two += v
  if k % 4 == 0:
    count += v

if count == 0 and two == 0:
  print("No")
  exit()

if N%2 == 0:
  if count >= N//2:
    print("Yes")
    exit()
  else:
    remain = N-(2*count)
    if two >= remain:
      print("Yes")
      exit()
else:
  if count >= N//2:
    print("Yes")
    exit()
  else:
    remain = N-(2*count)
    if two >= remain:
      print("Yes")
      exit()


print("No")

