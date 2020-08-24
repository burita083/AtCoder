#include <bits/stdc++.h>
#include <algorithm>
#include <string>
using namespace std;
using Graph = vector<vector<int>>;//隣接リスト
 
vector<bool> seen;
void dfs(Graph &G, int v) {
    seen[v] = true;
    for (auto next_v: G[v]) {
        if (seen[next_v]) continue;
        dfs(G, next_v);
    }
}

void dfs(Graph &G, int v) {
    seen[v] = true;
    for (auto next_v: G[v]) {
        if (seen[next_v]) continue;
        dfs(G, next_v);
    }
}
void bfs(Graph &G, int v) {
    seen[v] = true;
    while (!que.empty()) {
        for (auto next_v: G[v]) {
            if (seen[next_v]) continue;
            que.push(next_v);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M, s, t;
    cin >> N >> M >> s >> t;
    Graph G(N);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin a >> b;
        G[a].push_back(b);
        //無向グラフ
        //G[b].push_back(a);
    }

    seen.assign(N, false);
    dfs(G, s);
    if (seen[t]) cout << "Yes" <<endl;
    else cout << "No" <<endl;
    return 0;
}