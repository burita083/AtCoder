S = input()
a = 0
b = 0
c = 0
for x in S:
  if x == "a":
    a += 1
  elif x == "b":
    b += 1
  else:
    c += 1

mx = max(a, b, c)

if mx == a:
  print("a")
elif mx == b:
  print("b")
else:
  print("c")