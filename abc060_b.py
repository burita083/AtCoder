A, B, C = map(int, input().split())

while True:
  for i in range(1, 101):
    ans = B*i+C
    if ans % A == 0:
      print("YES")
      exit()
  print("NO")
  exit()


