N = int(input())

sm = float('inf')
mnA = float('inf')
mnB = float('inf')
l = []
for i in range(N):
  A, B = map(int, input().split())
  sm = min(sm, A+B)
  l.append((A, B))

idx = 0
for i in range(N):
  a, b = l[i]
  if a+b == sm:
    idx = i

flag = 0
for i in range(N):
  a, b = l[i]
  mnA = min(mnA, a)

Aidx = 0
for i in range(N):
  a, b = l[i]
  if mnA == a:
    Aidx = i

for i in range(N):
  a, b = l[i]
  if Aidx == i: continue
  mnB = min(mnB, b)

#for i in range(N):
  #if i == idx: continue
  #a, b = l[i]
  #mnA = min(mnA, a)
  #mnB = min(mnB, b)


mx = max(mnA, mnB)

ans = float('inf')

if sm < mx:
  print(sm)
else:
  print(mx)

