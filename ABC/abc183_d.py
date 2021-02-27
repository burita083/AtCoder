
N, W = map(int, input().split())

"dictonary初期化"
d = {}
 
for n in range(N):
  S, T, P = map(int, input().split())
  for i in range(S, T):
    if i in d:
      d[i] += P
      if d[i] > W:
        print("No")
        exit()
    else:
      d[i] = P


print("Yes")