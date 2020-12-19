H, W = map(int, input().split())
ans = 0
mn = 1000000
array = []
for x in range(H):
  A = list(map(int, input().split()))
  array.append(A)
  mn = min(min(A),mn)

for a in array:
  count = 0
  for aa in a:
    count += aa - mn
  ans += count

print(ans)
