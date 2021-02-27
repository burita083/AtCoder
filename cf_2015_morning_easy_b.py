N = int(input())

S = input()

if N % 2 != 0:
  print(-1)
  exit()

left = S[:len(S)//2]
right = S[len(S)//2:]


count = 0
for (l, r) in zip(left, right):
  if l != r:
    count += 1
print(count)