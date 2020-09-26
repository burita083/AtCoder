N, K = map(int, input().split())

ans = []
#A = int(input())
#prev = A
#if N == 1: 
  #if A <= K:
    #print(1)
    #exit()
  #else:
    #print(0)
    #exit()

a = []
for i in range(N):
  A = int(input())
  a.append(A)

count = -1
for i in range(N):
  ans = []
  for j, k in enumerate(range(i, N)):
    #print(j, k)
    print(i, k, j)
    if j == 0:
      prev = a[k]
      continue

    if abs(prev-a[k]) <= K:
      print("prev", prev, a[k])
      ans.append(prev)
      prev = a[k]
      #print(k)
      if k == N-1:
        #print(k)
        ans.append(a[k])
  count = max(count,len(ans))
  print(ans)
    #Jprint(ans)

print(count)