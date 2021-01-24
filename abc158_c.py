A, B = map(int, input().split())

for i in range(1, 10001):
  a = int(i*8/100)
  b = int(i*10/100)
  if a == A and b == B:
    print(i)
    exit()

print(-1)