N, K = map(int, input().split())
A = list(map(int, input().split()))

cums = [0]
for a in A:
  cums.append(cums[-1] + a)

st = set()
for i in range(1, N+1):
  for j in range(0, N+1-i):
    st.add(cums[j+i]-cums[j])

ans = 0
l = sorted(st)
L = []
for i in range(K):
  L.append(l.pop())
ans = 0
for i in range(len(L)-1):
  ans = L[i] & L[i+1]
print(ans)