import collections
S = input()
N = len(S)

ans = 0
for i in range(1, 4):
  if i == 1:
    L = []
    for s in S:
      L.append(s)
      c = collections.Counter(L)
      ans += len(c.keys()) + 1
  elif i == 2:
    L = []
    for i in range(0, N-1):
      s = S[i:i+2]
      L.append(s)
      c = collections.Counter(L)

    for x in c.keys():
      for k in x:
        for l in k:
          temp = l
          l += '.'
          "." += temp
          L.append(l)
          L.append(temp)
          L.append("..")

    c = collections.Counter(L)
    print(c)
  else:
    print(3)