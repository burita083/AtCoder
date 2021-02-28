import itertools
N = input()
K = int(input())
L = len(N)
ans = 0
#for i in range(1, L):
  #S = str(i)
  #count = 0
  #for s in S:
    #if int(s) != 0:
      #count += 1
  #if count == K:
    #print(S)
    #ans += 1
#print(ans)


ans = 0
if K == 1:
  for i in range(1, L+1):
    if i == 1:
      if len(N) == 1:
        ans += int(N[0])
      else:
        ans += 9
    elif i == 2:
      if len(N) == 2:
        ans += int(N[1])
      else:
        ans += 9
    else:
      ans += int(N[0])
elif K == 2:
  for i in range(1, L+1):
    if i == 1:
      continue
    elif i == 2:
      if len(N) == 2:
        ans += (int(N[0])-1)*9
        ans += int(N[1])
      else:
        ans += 9*9
    else:
      if i == L:
        if len(N) == 3:
          ans += 8*9*2
          ans += int(N[1])
          ans += int(N[2])
        else:
          ans += (int(N[0])-1)*9*(i-1)
          ans += int(N[1])
          ans += 9*(i-2)
      else:
        ans += 9*9*(i-1)
else:
  for i in range(1, L+1):
    if i == 1:
      continue
    elif i == 2:
      continue
    else:
      #組合せ・重複なし
      if i == L:
        all = itertools.combinations(N[1:i], 2)
        for x in all:
          ans += int(N[0])*(int(x[0])*int(x[1]))
      else:
        temp = ((i-1)*(i-2))//2
        ans += 9*(9*9*temp)

print(ans)

