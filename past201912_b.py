N = int(input())

for i in range(N):
  A = int(input())
  if i == 0:
    temp = A
    continue
  else:
    if A == temp:
      print("stay")
    elif A > temp:
      print("up " + str((A-temp)))
    else:
      print("down " + str(abs((A-temp))))
    temp = A
