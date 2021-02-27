X, Y = map(int, input().split())


if X > Y:
  y = Y + 3
  if y > X:
    print("Yes")
  else:
    print("No")
else:
  x = X + 3
  if x > Y:
    print("Yes")
  else:
    print("No")
