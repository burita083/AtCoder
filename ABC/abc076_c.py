s,t=input(),input()
n,k=len(s),len(t)
a=[]
for i in range(n-k+1):
  for j in range(k):
    if s[i+j]!='?' and s[i+j]!=t[j]: 
      break
  else: 
    print(i, j)
    a+=[(s[:i]+t+s[i+k:]).replace('?','a')]
print(a)
print(min(a) if a else 'UNRESTORABLE')