N = int(input())

"1 2 3 4 5を配列に"
A = list(map(int, input().split()))
B = list(map(int, input().split()))

l = []
d = []
prev = -1
mx = -1
ans = []
prevlist = []
maxprev = -1
for i, (a, b) in enumerate(zip(A, B)):
  if prev == -1:
    prev = a
    maxprev = max(prev, maxprev)
    mx = max(a*b, mx)
    ans.append(mx)
  else:
    if i == N-1: 
      mx = max(a*b, mx)
      ans.append(mx)
      break
    mx = max(a*b, mx, maxprev*b)
    ans.append(mx)
    prev = a
    maxprev = max(prev, maxprev)

for a in ans:
  print(a)
