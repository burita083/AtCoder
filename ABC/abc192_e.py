import heapq
N, M, X, Y = map(int, input().split())

edge = [list() for _ in range(N)]
cost = {}
for e in range(M):
  s, to, cost, time = map(int, input().split())
  s, to = s-1, to-1
  edge[s].append((to, cost, time))
  edge[to].append((s, cost, time))


heap = []
heapq.heappush(heap, (0, X-1))
visited = [False] * N
times = [float('inf')] * N
times[X-1] = 0
mn = float('inf')

while heap:
  d, current = heapq.heappop(heap)
  if times[current] < d:
    continue

  temp = ""
  if current == Y-1:
      print(d)
      exit()

  for to, cost, time in edge[current]:
      temp += str(to+1)
      temp += " "
  for to, cost, time in edge[current]:
    if times[current] % time == 0:
        temp = times[current] + cost
    else:
        temp = times[current]//time * time + time + cost
    if times[to] > temp:
        if current == X-1:
            times[to] = cost
        else:
            if times[current] % time == 0:
                times[to] = times[current] + cost
            else:
                times[to] = times[current]//time * time + time + cost
        heapq.heappush(heap, (times[to], to))
    
print("-1")
