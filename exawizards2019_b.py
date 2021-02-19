N = int(input())
s = input()

r = 0
b = 0
for s in S:
    if s == "R":
        r += 1
    else:
        b += 1
if r > b:
    print("Yes")
else:
    print("No")