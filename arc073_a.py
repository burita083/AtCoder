N, T = map(int, input().split())

t = list(map(int, input().split()))

flag = False
ans = 0
st = t[0]
prev = 0
for index, i in enumerate(t):
  if flag == False:
    start = st
  if i - st - T > 0:
    #if index == len(t)-1:
    #  ans += i - st + T
    #else:
    ans += prev - st + T
    flag = False
    st = i
    prev = i
    if index == len(t) - 1:
      ans += prev-st+T
  else:
    flag = True
    prev = i
    if index == len(t) - 1:
      ans += prev-st+T

print(ans)
