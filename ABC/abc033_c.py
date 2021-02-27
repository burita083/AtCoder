S = input()

count = 0
stack = []
flag = False
for s in S:
  if s == "*":
    stack.append("*")
  elif s == "+":
    if flag: 
      stack = []
      flag = False
      continue
    else:
      count += 1
  elif s == "0":
    flag = True
  else: continue
if flag:
  print(count)
else:
  print(count+1)
