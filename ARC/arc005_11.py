N = int(input())
W = input()
w = W[:-1].split()
count = 0
for e in w:
  if e == "TAKAHASHIKUN" or e == "Takahashikun" or e == "takahashikun":
    count += 1


print(count)