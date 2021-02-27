N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(M)]
K = int(input())
CD = [tuple(map(int,input().split())) for i in range(K)]

ans = 0
for bit in range(1<<K):
  st = set()
  for i in range(K):
    if bit & (1<<i):
      c = CD[i][0]
      st.add(c)
    else:
      d = CD[i][1]
      st.add(d)
  cnt = 0
  for a,b in AB:
      if a in st and b in st:
          cnt += 1
  ans = max(ans, cnt)
print(ans)