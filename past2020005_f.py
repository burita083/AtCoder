N = int(input())
S = ""
l = []
for _ in range(N):
  s = input()
  S += s

for x in S:
  l.append(x)

import collections

c = collections.Counter(l)
l = c.most_common(5000)

from collections import deque
d = deque()
s = ""
flag = True

if N % 2 == 0:
  for x in l:
    if x[1] % 2 == 0:
      for k in range(x[1]):
        if k % 2 == 0:
          d.appendleft(x[0])
        else:
          d.append(x[0])
          if len(d) == N:
            for x in d:
              s += x
            print(s)
            exit()
    else:
      if flag:
        for k in range(x[1]):
          d.insert(len(d)//2, x[0])
          if len(d) == N:
            for x in d:
              s += x
            print(s)
            exit()
        if len(s) % 2 != 0:
          s.lstrip()
          
        flag = False
else:
  for x in l:
    if x[1] % 2 == 0:
      for k in range(x[1]):
        if k % 2 == 0:
          d.appendleft(x[0])
          if flag:
            if len(d) == N:
              for x in d:
                s += x
              print(s)
              exit()

        else:
          d.append(x[0])
          if flag == False:
            if len(d) == N:
              for x in d:
                s += x
              print(s)
              exit()
    else:
      if flag:
        for k in range(x[1]):
          d.insert(len(d)//2, x[0])
          if len(d) == N:
            for x in d:
              s += x
            print(s)
            exit()
        flag = False

print(-1)