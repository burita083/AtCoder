import collections
N = int(input())
A = list(map(int, input().split()))

l = []
r = []
al = []
for i, x in enumerate(A):
  if i % 2 == 0:
    l.append(x)
  else:
    r.append(x)
  al.append(x)

c = collections.Counter(l)
d = collections.Counter(r)
e = collections.Counter(al)

if len(e.keys()) <= 1:
  print(N//2)
  exit()
else:
  mx = -1
  ans = 0
  ck = max(c.items(), key=lambda x:x[1])[0]
  cmx = max(c.items(), key=lambda x:x[1])[1]

  dk = max(d.items(), key=lambda x:x[1])[0]
  dmx = max(d.items(), key=lambda x:x[1])[1]

  if ck == dk:
    if cmx > dmx:
      ans += N//2 - cmx
      ans += N//2 - d.most_common(2)[1][1]
    elif cmx < dmx:
      ans += N//2 - dmx
      ans += N//2 - c.most_common(2)[1][1]
    else:
      if c.most_common(2)[1][1] >= d.most_common(2)[1][1]:
        ans += N//2 - dmx
        ans += N//2 - c.most_common(2)[1][1]
      else:
        ans += N//2 - cmx
        ans += N//2 - d.most_common(2)[1][1]
  else:
      ans += N//2 - cmx
      ans += N//2 - dmx

print(ans)
