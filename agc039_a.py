S = input()
K = int(input())

count = 0
prev = ""  
for s in S:
  if s == prev:
    count += 1
    prev = ""
  else:
    prev = s

if len(S) == 1:
  if K == 1:
    print(1)
    exit()
  else:
    print((K+1)//2)
    exit()
if len(S) % 2 == 0:
  print(count*K)
else:
  if S[0] == S[-1]:
    print(count*K+K//2)
  else:
    print(count*K)