N = int(input())

A = list(map(int, input().split()))

AA = []
count = 1
for a in A:
  AA.append((a, count))
  count +=1

if len(AA) == 2:
    if AA[0][0] > AA[1][0]:
      print(AA[1][1])
      exit()
    else:
      print(AA[0][1])
      exit()

while len(AA) > 1:
  l = []
  for i in range(0, len(AA), 2):
    if AA[i][0] > AA[i+1][0]:
      l.append((AA[i][0], AA[i][1]))
    else:
      l.append((AA[i+1][0], AA[i+1][1]))

  if len(l) == 2:
    if l[0][0] > l[1][0]:
      print(l[1][1])
      exit()
    else:
      print(l[0][1])
      exit()

  AA = l[:]
  