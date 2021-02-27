a, b, x, y = map(int, input().split())

roukaB = 2 * x 
kaidanB = y
time = 0
if a < b:
  kai = b-a
  time += x
  if roukaB >= kaidanB:
    time += kai * kaidanB
  else:
    time += kai * roukaB
elif a > b:
  kai = a - b
  if kai == 1:
    time = x
  else:
    time += x
    if roukaB >= kaidanB:
      time += (kai-1) * kaidanB
    else:
      time += (kai-1) * roukaB
else:
  time += x

print(time)
