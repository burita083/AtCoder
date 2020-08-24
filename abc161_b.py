N, M = map(int, input().split())

"1 2 3 4 5を配列に"
A = list(map(int, input().split()))
s = sum(A)
ok = s * (1/(4*M))
count = 0

for a in A:
  if a >= ok:
    count += 1

if count >= M:
  print("Yes")
else:
  print("No")