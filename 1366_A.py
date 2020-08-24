t = int(input())

for _ in range(t):
  a, b = map(int, input().split())
  if a <= 0 or b <= 0:
    print(0)
    continue

  if a + b <= 2:
    print(0)
    continue
  
  count = 0
  flag = False
  while a != b:
    if a + b <= 2:
      flag = True
      break

    if a <= 0 or b <= 0:
      flag = True
      break

    if a >= b:
      a -= 2
      b -= 1
    else:
      a -= 1
      b -= 2
    count += 1
    print(a,b)
  
  if flag == False and a + b >= 3:
    count += (a+b)//3

  print(count)
  
  
