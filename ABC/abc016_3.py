N, M = map(int, input().split())
AB = [tuple(map(int,input().split())) for i in range(M)]

G = [[] for i in range(N)]
for a,b in AB:
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)

L = []
for index, g in enumerate(G):
    st = set()
    for gg in g:
        for to in G[gg]:
            if not to in g and to != index:
                st.add(to)
    L.append(st)

for l in L:
    print(len(l))
