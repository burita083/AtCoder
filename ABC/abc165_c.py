N, M, Q = map(int, input().split())
l = []
for x in range(Q):
  A = list(map(int, input().split()))
  l.append(A)

l.sort()
ll = sorted(l, key=lambda x:x[3], reverse= True)
a = []
for x in ll:
  
print(ll)
