N, M = map(int, input().split())

L = []
for _ in range(N):
  S = input()
  L.append(S)

ans = []
for indexl, l in enumerate(L):
  cs = ""
  for indexs, s in enumerate(l):
    count = 0
    if indexl - 1 >= 0:
      if indexs - 1 >= 0:
        if L[indexl-1][indexs-1] == "#":
          count += 1
      if L[indexl-1][indexs] == "#":
        count += 1
      if indexs + 1 <= M-1:
        if L[indexl-1][indexs+1] == "#":
          count += 1

    if indexs - 1 >= 0:
      if L[indexl][indexs-1] == "#":
        count += 1
    if L[indexl][indexs] == "#":
      count += 1
    if indexs + 1 <= M-1:
      if L[indexl][indexs+1] == "#":
        count += 1
    if indexl + 1 <= N - 1:
      if indexs - 1 >= 0:
        if L[indexl+1][indexs-1] == "#":
          count += 1
      if L[indexl+1][indexs] == "#":
        count += 1
      if indexs + 1 <= M-1:
        if L[indexl+1][indexs+1] == "#":
          count += 1
    cs += str(count)
  ans.append(cs)
for a in ans:
  print(a)