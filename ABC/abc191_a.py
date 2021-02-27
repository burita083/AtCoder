V, T, S, D = map(int, input().split())

if D < V*T:
  print("Yes")
  exit()

if D == V*T:
  print("No")
  exit()

if D > V*T:
  if D <= V*S:
    print("No")
    exit()
  else:
    print("Yes")
