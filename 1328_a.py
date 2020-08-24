t = int(input())
for _ in range(t):
  a, b = map(int, input().split())
  amari = a % b
  if amari == 0:
    print(0)
  else:
    print(b-amari)

