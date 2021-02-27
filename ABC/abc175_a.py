S = input()

count = 0
ans = 0
ansR = 0
for s in S:
  if s == "R":
    count += 1
    ansR = count
  else:
    ans = count
    count = 0


print(max(ans, ansR))

