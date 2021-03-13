N = int(input())

if N == 1:
  print(-1)
  exit()
if N%2!=0:
  print(1)
else:
  a = 2
  b = N//2
  if a-b==0:
    print(-1)
  else:
    if b%2 == 0:
      print(1)
    else:
      print(-1)