N = int(input())

A = list(map(int, input().split()))

B = A[:]
B.sort()
l = []
for i, a in enumerate(A):
  flag = False
  for k, b in enumerate(B):
    if a == b:
      if k == len(B)-1 and flag==False:
        l.append(i+1)
      continue

    if a >= b:
      if a % b == 0:
        flag = True
        break
    else:
      if flag==False:
        l.append(i+1)
      break
    
    if k == len(B)-1 and flag==False:
      l.append(i+1)
 

print(len(l))