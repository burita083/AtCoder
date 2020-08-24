from collections import deque

t = int(input())

for x in range(t):
  n = int(input())
  A = list(map(int, input().split()))
  d = deque()
  for x in A:
    d.append(x)
  
  turn = 0
  count = 0
  previous_a = 0
  previous_b = 0
  sum_a = 0
  sum_b = 0
  while True:
    alice = 0
    bob = 0
    if turn == 0:
        if len(d) > 0:
          while alice <= previous_b:
            if len(d) > 0:
              alice += d.popleft()
            else: 
              break
        
          sum_a += alice 
          previous_a = alice
          if alice == 0:
            break
          count += 1
          turn = 1
        else:
            break
    if turn == 1:
        if len(d) > 0:
          while bob <= previous_a:
            if len(d) > 0:
              bob += d.pop()
            else:
              break

          sum_b += bob 
          previous_b = bob
          if bob == 0:
            break
          count += 1
          turn = 0
        else:
            break
  
  print(count, sum_a, sum_b)

