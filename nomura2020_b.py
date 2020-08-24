T = input()

s = list(T)
for i, x in enumerate(T):
  if x == "?":
    s[i] = "D"


print("".join(s))