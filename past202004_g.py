import collections
from collections import deque
from itertools import islice
Q = int(input())


S = ""
t = deque(S)
AnsL = []
for i in range(Q):
  L = []
  A = input().split()
  if int(A[0]) == 1:
    s = A[1]*int(A[2])
    t.append(s)
    result = ''.join(t)
  else:
    t  = deque(result)
    for _ in range(int(A[1])):
      if len(t) >= 1:
        p = t.popleft()
        L.append(p)

    c = collections.Counter(L)
    ans = 0
    for value in c.values():
      ans += value**2

    AnsL.append(ans)

for x in AnsL:
  print(x)
