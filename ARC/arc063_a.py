S = input()

count = 0

prev = S[0]
for s in S:
  if s != prev:
    count += 1
  prev = s
print(count)
