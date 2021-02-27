import itertools
N = int(input())

l = []
for i in range(N):
  x, y = map(int, input().split())
  l.append((x,y))

ll = []
for num in itertools.combinations(l, 2):
    ll.append(num)

count = 0
for l in ll:
  y = l[1][1] - l[0][1]
  x = l[1][0] - l[0][0]
  a = y/x
  if a >= -1 and a <= 1:
    count += 1
print(count)