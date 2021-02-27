N, X = map(int, input().split())

"1 2 3 4 5を配列に"
A = list(map(int, input().split()))


ans = []
for a in A:
  if a == X: continue
  ans.append(a)

print(' '.join(map(str, ans)))