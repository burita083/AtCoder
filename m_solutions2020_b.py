r, g, b = map(int, input().split())

K = int(input())

while K > 0:
  if g <= r:
    g *= 2
    K -= 1
  elif b <= g:
    b *= 2
    K -= 1
  else:
    break
    




if g > r and b > g:
  print("Yes")
else:
  print("No")

