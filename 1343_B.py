t = int(input())
for _ in range(t):
  n = int(input())
  if ((n//2)%2!=0):
    print("NO")
  else:
    half = n//2
    mx = 2*half
    l = []
    esum = 0
    for x in range(2, mx+1, 2):
      esum += x
      l.append(x)

    count = 1
    osum = 0
    for x in range(half-1):
      l.append(count)
      osum += count
      count += 2
    
    l.append(esum-osum)
    print("YES")
    print(*l)
