K = int(input())
r = [[] for _ in range(10)]
r[0] = list(range(1,10))

for i in range(9):
  for a in r[i]:
    s = str(a)
    d = a%10
    for j in range(d-1, d+2):
      if not 0 <= j <= 9: continue
      r[i+1].append(int(s+str(j)))

for i in range(10):
  if K >= len(r[i]):
    K -= len(r[i])
  else:
    print(r[i][K-1])
    break