a = int(input())

for i in range(a):
  N, K = map(int, input().split())
  if N<=K:
    if K%N==0:
      print(K//N)
    else:
      print(K//N+1)
  else:
    if N%K==0:
      print(1)
    else:
      temp = N//K
      K = K*(temp+1)
      if K%N==0:
        print(K//N)
      else:
        print(K//N+1)

