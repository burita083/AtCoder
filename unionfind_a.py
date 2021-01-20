class UnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self._size = [1] * N
        self.count = 0

    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self,a,b):
        return self.root(a) == self.root(b)

    def unite(self,a,b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self._size[ra] < self._size[rb]: ra,rb = rb,ra
        self._size[ra] += self._size[rb]
        self.parent[rb] = ra
        self.count += 1

    def size(self,a):
        return self._size[self.root(a)]


N, Q = map(int, input().split())
PAB = [tuple(map(int,input().split())) for i in range(Q)]
uf = UnionFind(N)
for pab in PAB:
    if pab[0] == 0:
        uf.unite(pab[1],pab[2])
    else:
        if uf.is_same(pab[1],pab[2]): 
            print("Yes")
        else: 
            print("No")

