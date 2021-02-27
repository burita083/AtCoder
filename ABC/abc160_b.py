X = int(input())
if X >= 500:
  q = X // 500 
  mod = X % 500 
  f = mod // 5
  print(q*1000+f*5)
else:
  f = X // 5
  print(f*5)