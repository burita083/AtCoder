S = input()
T = input()

found = []

#区間大事。 len(T)がの仕切りを何箇所入れれるか
for i in range(len(S) - len(T) + 1):
  for cs, ct in zip(S[i:], T):
    if cs != '?' and cs != ct:
      break
  else:
    found.append(i)

if not found:
  print("UNRESTORABLE")
  exit()

ans = 'z'  * 51

for i in found:
  tmp = S[:i] + T + S[i+len(T):]
  ans = min(ans, tmp.replace("?", "a"))
print(ans)
