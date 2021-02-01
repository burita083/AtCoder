N = int(input())

mn = 0
P = list(map(int, input().split()))
ans = []
st = set()
for p in P:
  st.add(p)
  if p > mn:
    ans.append(mn)
  else:
    p = mn
    while p in st: 
      p += 1
    ans.append(p)
    mn = p

for a in ans:
  print(a)