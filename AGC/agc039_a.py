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
  
top = S[0]
ans = 0
flag = False
for s in reversed(S):
  if s == S[0]:
    ans += 1
  else:
    flag = True
    break

print(len(S), "aa")
if len(S) == 1:
  if K == 1:
    print(1)
    exit()
  else:
    print((K+1)//2)
    exit()
if len(S) % 2 == 0:
  if flag and ans % 2 != 0 and S[0] == S[-1]:
    print(count*K+(K-1))
  else:
    print(count*K)
else:
    print(count*K+(K-1))