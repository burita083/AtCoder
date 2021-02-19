S = input()

count = 0
ln = len(S)
for s in S:
    if s == "o":
        count += 1
remain = 15-ln
if count + remain >= 8:
    print("YES")
else:
    print("NO")

