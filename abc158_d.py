from collections import deque
S = input()
Q = int(input())

queue = deque(S)
reverse = 0
l = []
for _ in range(Q):
  q = input().split()
  l.append(q)
  if q[0] == "1":
    reverse += 1

direction = 1
count = 0
temp = reverse
for ll in l:
  if ll[0] == "1":
    reverse -= 1
    direction *= -1
    count += 1
  else:
    if direction == 1:
     if ll[1] == "1":
       queue.appendleft(ll[2])
     else:
       queue.append(ll[2])
    else:
     if ll[1] == "2":
       queue.appendleft(ll[2])
     else:
       queue.append(ll[2])



ans = ""
if count% 2 != 0:
  queue.reverse()
for q in queue:
  ans += q
print(ans)