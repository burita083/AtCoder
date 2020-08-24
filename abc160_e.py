X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort()
p.reverse()
q.sort()
q.reverse()
r.sort()

l = X+Y
lst = []
for i in range(X):
  lst.append(p[i])

for i in range(Y):
  lst.append(q[i])

for i in r:
  lst.append(i)

lst.sort()
lst.reverse()

ans = 0
for i in range(l):
  ans += lst[i]

print(ans)
  