from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())

#二次元の表をこれで作れる
L = [list(input()) for i in range(N)]
print(L)

d = 0
for i in range(N):
    for j in range(M):
        if L[i][j] == '.':
            d += 1

ans = 0
for i in range(N):
    for j in range(M):
        seen = [[0]*M for _ in range(N)]#Visitedを毎回初期化
        D = L[:] #毎回初期化
        if D[i][j] == '#':#"#"を探し、・に変更し、・の数と一致するかを調べる
            D[i][j] == '.'
            c = 0
            que = deque()
            que.append((i, j))#.にしたところをスタートにする
            seen[i][j] = 1
            while que:
                p = que.pop()
                x = p[0]
                y = p[1]
                for k in range(4):#いつもの4方向
                    nx = dx[k] + x
                    ny = dy[k] + y
                    if 0 <= nx < N and 0 <= ny < M and D[nx][ny] != '#' and seen[nx][ny] != 1:
                        seen[nx][ny] = 1
                        que.append((nx, ny))
                        c+=1
            if c == d:
                ans +=1
print(ans)
