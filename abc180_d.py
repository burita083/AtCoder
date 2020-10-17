X, Y, A, B = map(int, input().split())

ans = 0
now = X
flag = False
y = Y
while now < Y:
  temp = now
  if now*A >= now+B:
    temp += B
  else:
    temp *= A
  if temp >= Y:
    print(ans)
    exit()

  if now*A >= now+B:
    now += B
    y -= now
    flag = True
  else:
    now *= A
    y -= now
  ans += 1
  if flag:
    break

temp = ans
if y%B == 0:
  ans += y//B-1
else:
  ans += (y//B)

bCount = ans-temp
v = bCount*B+now
for _ in range(0, 10):
  v += B
  if v < Y:
    ans += 1
  else:
    break
print(ans)