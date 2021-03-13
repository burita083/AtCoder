A, B, W = map(int, input().split())

W = 1000*W

for a in range(A, B+1):
  K = W//a
  for i in range(1, K):
    remain = W
    remain -= a*i
    for b in range(A, B+1):
      if a == b:continue

