H,W,K = map(int,input().split())
c = [input() for i in range(H)]

#for h in range(H):
#  for w in range(W):
#    if c[h][w] == '#':

h = len(c)
hl = []
for i in range(2 ** h):
 bit_set = []
 for j in range(h):
   if ((i >> j) & 1):
     bit_set.append(j)

 hl.append(bit_set)

wl = []
for i in range(2 ** W):
 bit_set = []
 for j in range(W):
   if ((i >> j) & 1):
     bit_set.append(j)
 wl.append(bit_set)


ans = 0
for w in wl:
  wll = []
  for ww in w:
    wll.append(ww)

  for h in hl:
    count = 0
    for i, cc in enumerate(c):
      if not i in h:
        for k, ccc in enumerate(cc):
          if not k in wll:
            if ccc == '#':
              count += 1

    if count == K:
      ans += 1


print(ans)

 