N=int(input())
def divisor(M):
  res = set()
  i=1
  while(i*i<M):
    if M%i==0:
      res.add(i)
      res.add(M//i)
    i+=1
  return res
D=divisor(2*N)
ans=0
for n in D:
  m = (2*N)//n
  if (m-n)%2==1:
    ans+=1
print(ans)