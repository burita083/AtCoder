t = int(input())

for _ in range(t):
  n = int(input())
  if n % 2  == 0:
    k = n//2 + 1
    print(n-k)
  else:
    k = -(-n//2)
    print(n-k)