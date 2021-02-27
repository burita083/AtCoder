N = int(input())
XY = [tuple(map(int,input().split())) for i in range(N)]

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            x1,y1 = XY[i]
            x2,y2 = XY[j]
            x3,y3 = XY[k]
            a = x2-x1
            b = y2-y1
            c = x3-x1
            d = y3-y1
            if a*d == b*c:
                print('Yes')
                exit()
print('No')
 