S = input()
T = input()
d = {}

for s, t in zip(S, T):
  if s in d:
    #含まれている場合で、tと異なるならば、変換ができないということ
    if d[s] != t:
      print("No")
      exit()
  else:
    d[s] = t

#keyの数に対し、valuesが重複していて、数が合わなければ、変換ができない
print(d.keys())
print(len(d.values()))
print(set(d.values()))
if len(d) != len(set(d.values())):
  print("No")
else:
  print("Yes")

