n = int(input())


l = 0
r = n+2

while r-l>1:
    m = (l+r)//2
    print(m, "l", l, "r", r)
    if m*(m+1)//2 <= n+1:
        l = m
    else:
        r = m
print(n-l+1)