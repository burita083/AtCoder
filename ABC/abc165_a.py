K = int(input())

A, B = map(int, input().split())

flag = False
for x in range(A, B+1):
  if x % K == 0:
    flag = True


if flag:
  print("OK")
else: 
  print("NG")
