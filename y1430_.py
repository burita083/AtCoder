N, C = map(int, input().split())
P = []
for i in range(N):
  p = int(input())
  P.append(p)

TX = [tuple(map(int,input().split())) for i in range(C)]

ans = 0
items = set()
qupons = set()
l = []
for idx, p in enumerate(P):
  for i, (t, x) in enumerate(TX):
    if t == 1:
      l.append((idx, i,  min(x, p)))
    else:
      l.append((idx, i, p-p*(100-x)//100))


buys = []
l.sort(key=lambda x:(-x[2]))
for itemsId, couponId, v in l:
  if itemsId in items:
    continue
  if couponId in qupons:
    continue
  items.add(itemsId)
  qupons.add(couponId)
  buys.append((itemsId, couponId))
print(len(buys))
print(len(P))
for i, p in enumerate(P):
  flag = False
  for itemsId, couponId in buys:
    if itemsId == i:
      flag = True
      if TX[couponId][0] == 1:
        ans += max(p-TX[couponId][1], 0)
        break
      else:
        rate = (100-TX[couponId][1])/100
        ans += p*rate
        break
  if flag == False:
    ans += p
print(int(ans))

