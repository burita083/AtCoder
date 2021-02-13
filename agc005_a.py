X = input()
ans = ""
temp = ""
stack = []
for x in X:
    if x == "S":
        stack.append(x)
    else:
        if len(stack) >= 1:
            stack.pop()
        else:
            ans += x
    
for x in stack:
    ans += x
print(len(ans))
