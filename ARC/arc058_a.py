N, K = map(int, input().split())
D = list(map(int, input().split()))

i = N
while True:
  flg = True
  for j in str(i):
    if int(j) in D:
      flg = False
      break

  if flg == True:
    print(i)
    exit()

  i += 1