import math
N, M = map(int, input().split())

"1 2 3 4 5を配列に"
A = list(map(int, input().split()))
sA = sorted(A)
l = 0
r = N+1
ans = 0
temp = 0
count = 100000
last = 0
for index, k in enumerate(sA):
  if index == 0:
    ans = k - index-1
    temp = k
    if ans == 0:
      continue
    count = min(ans, count)
  else:
    last = index
    ans = k - temp - 1
    temp = k
    if ans == 0:
      continue
    count = min(ans, count)
  

if last == len(sA) - 1:
    ans = N+1 - temp - 1
    if ans != 0:
      count = min(ans, count)

a = 0
t = 0


if M == 0:
  print(N)
  exit()

if count == 0:
  print(0)
  exit()

for index, k in enumerate(sA):
  if index == 0 and k == 1:
    t = k
    continue

  if index == 0:
    now = k - 0 - 1
    t = k
    if now % count == 0:
      a += now//count
  else:
    now = k - t - 1
    t = k
    if now % count == 0:
      a += now//count
    else:
      a += math.ceil(now/count)
    
  if index == len(sA) - 1:
    now = N+1 - t - 1
    if now % count == 0:
      a += now//count
    else:
      a += math.ceil(now/count)

  

print(a)
