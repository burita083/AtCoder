N = int(input())
d = {}
l = []
for n in range(N):
  S = input()
  l.append(S)
  if S in d:
    d[S] += 1
  else:
    d[S] = 1


for ll in l:
  if "!" in ll:
    if ll.lstrip("!") in d:
      print(ll.lstrip("!"))
      exit()
  else:
    temp = "!" + ll
    if temp in d:
      print(ll)
      exit()

print("satisfiable")


