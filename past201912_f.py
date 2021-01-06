S = input()

d = {}
flag = False
ans = ""
for s in S:
    if s.isupper() and flag == False:
        flag = True
        ans += s
        continue

    if s.isupper() and flag:
        flag = False
        ans += s
        if ans in d:
            d[ans] += ans
        else:
            d[ans] = ans
        ans = ""
        continue
    ans += s
    
dic2 = sorted(d.keys(), key=str.lower)
print(dic2)
ans = ""
for v in dic2:
    ans += d[v]

print(ans)

