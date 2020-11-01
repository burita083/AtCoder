N = int(input())


d = {}
e = {}
f = {}
g = {}
flag1 = False
flag2 = False
for _ in range(N):
  x, y = map(int, input().split())
  if x in d:
    if d[x] == y:
      continue
    else:
      e[x] += 1
      if e[x] >= 3:
        flag1 = True
        print("Yes")
        exit()
  else:
    d[x] = y
    e[x] = 1

  if y in f:
    if f[y] == x:
      continue
    else:
      g[y] += 1
      if g[y] >= 3:
        flag2 = True
        print("Yes")
        exit()
  else:
    f[y] = x
    g[y] = 1

print(e)
print(g)
print("No")
