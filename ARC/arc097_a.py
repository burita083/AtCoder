s = input()
N = len(s)
K = int(input())

subs = set()
for i in range(N):
  for j in range(K):
    subs.add(s[i:i+1+j])
  
print(sorted(subs)[K-1])

