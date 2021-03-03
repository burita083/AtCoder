N = int(input())

A = list(map(int, input().split()))
st = set()

ans = 0
r = 0
for l in range(N):
  while r < N and A[r] not in st:
    st.add(A[r])
    r += 1
  st.remove(A[l])
  ans = max(ans, r-l)
print(ans)
