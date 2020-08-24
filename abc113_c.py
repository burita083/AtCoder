N,M = map(int,input().split())
PY = [tuple(map(int,input().split())) for i in range(M)]

#こういう書き方ができると暗記する
ypi = sorted((y,p,i) for i,(p,y) in enumerate(PY))
 
from collections import defaultdict
d = defaultdict(lambda: 0)

#list初期化
ans = [None] * M

for y,p,i in ypi:
    d[p] += 1

    #lenがMのansのlistに添字ではなくて、意図的に、iでインデックス指定で入れる。
    #こうすることで、わざわざ探す処理なく、順番も入れ替えることなく処理が可能
    ans[i] = str(p).zfill(6) + str(d[p]).zfill(6)
print(*ans, sep='\n')