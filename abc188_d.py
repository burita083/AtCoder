from itertools import accumulate
N, C = map(int, input().split())

data = [0] * 1000000001

for _ in range(N):
  a, b, c = map(int, input().split())
  data[a] += 1
  data[b+1] -= 1

cum = list(accumulate(data))
print(cum)

