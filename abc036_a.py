 
A, B = map(int, input().split())
 
if (A >= B) : 
  print(1)
else :
  if (B % A == 0) :
    print(B//A)
  else :
    print(B//A+1)
 