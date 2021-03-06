A, B = map(int, input().split())

sm = A+B
ans = 0
if sm >= 15 and B >=8:
  ans = 1
elif sm >= 10 and B >=3:
  ans = 2
elif sm >=3:
  ans = 3
else:
  ans = 4
print(ans)
