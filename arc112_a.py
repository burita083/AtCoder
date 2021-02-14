T = int(input())
for t in range(T):
  L, R = map(int, input().split())
  count = 0
  m = R-2*L+1
  if 2*L <= R:
    print(m*(m+1)//2)
  else:
    print("0")
