N,M,Q = map(int,input().split())
WV = [tuple(map(int,input().split())) for i in range(N)]
X = list(map(int,input().split()))
LR = [tuple(map(int,input().split())) for i in range(Q)]
 
l = [(1, 2, 3), (3, 2, 4), (3, 4, 9)]
print(l)


l.sort(key=lambda x:(-x[1]))
print(l)

l = [(1, 2, 3), (3, 2, 4), (3, 4, 9)]
l.sort(key=lambda x:(-x[2]))
print(l)
for l, r in LR:
    xs = X[:l-1] + X[r:]
    xs.sort()
    ans = 0
    for w, v in WV:
        idx = -1
        if not xs: break
        if w > xs[-1]: continue
        ans += v
        for i, x in enumerate(xs):
          if w <= x:
            idx =  i
            break
        if idx == -1: continue
        del xs[idx]
    print(ans)