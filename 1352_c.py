t = int(input())

for _ in range(t):
  x = int(input())
  l = []
  amari = x
  while True:
    x = amari
    ln = len(str(amari))
    div = int(str(amari)[0])*(10**(ln-1))
    if div == 0:
      print(len(l))
      print(' '.join(map(str, l)))
      break
    else:
      amari = x % div
      x -= amari
      l.append(x)
