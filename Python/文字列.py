
#数字を受け取って、数字を並べ変える方法。
#数値は桁数なので、Nの値が多くても、、桁数という意味では小さいことを感覚的に覚える
N,K = map(int,input().split())
 
for k in range(K):
    l = list(str(N))
    a = ''.join(sorted(l, reverse=True))
    b = ''.join(sorted(l))