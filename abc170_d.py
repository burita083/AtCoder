N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(len(A)):
  flag = True
  for j in range(len(A)):
    if i == j: continue
    if A[i] % A[j] == 0:
      flag = False
      break
  if flag:
    count+=1
print(count)