N = int(input())

ten = N
eight = '{:o}'.format(ten)

d = {}
for i in range(N+1):
  ten = i
  eight = '{:o}'.format(ten)
  sTen = str(ten)
  sEight = str(eight)
  if "7" in sTen:
    if sTen in d:
      continue
    else:
      d[sTen] = 1

  if "7" in sEight:
    if sTen in d:
      continue
    else:
      d[sTen] = 1




print(N-len(d))