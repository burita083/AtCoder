N, K = map(int, input().split())

"1 2 3 4 5を配列に"
p = list(map(int, input().split()))

p.sort()

count = 0
for i in range(K):
  count += p[i]

print(count)
