A, B, C, D = map(int, input().split())

ans = 0
dict = {}
for c in range(C, B+1, C):
  if c >= A and c <= B:
    dict[c] = 1

for d in range(D, B+1, D):
  if d >= A and d <= B:
    dict[d] = 1
print(B-A+1-len(dict))

