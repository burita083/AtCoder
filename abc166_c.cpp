#include <vector>
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <deque>
#include <map>

typedef long long ll;
#define rep(i, a, n) for(int i = a; i<n; i++)
#define ALL(a) begin(a), end(a)
#define mii map<int, int>
#define msi map<string, int>
#define vi vector<int>
#define vl vector<ll>
#define MOD 1000000007
#define INF 1e9
#define showVector(v) rep(i,0,v.size()){p(v[i]);p(" ")} pl("")
#define p(s) std::cout << s ;
#define pl(s)  std::cout << s << endl;
using namespace std;

// 素数判定 O(√n)
bool is_prime(int n){
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return false;
    }
    return true;
}

template<class T> inline bool chmin(T& a, T b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;

}
template<class T> inline bool chmax(T& a, T b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}
using Graph = vector<vector<int> >;//隣接リスト
 
vector<bool> seen;
void dfs(Graph &G, int v) {
    seen[v] = true;
    for (auto next_v: G[v]) {
        if (seen[next_v]) continue;
        dfs(G, next_v);
    }
}

int main() {
    ll N, M;
    cin >> N >> M;

    vl H(N+1);
    rep(i, 1, N+1) {
        cin >> H[i];
    }

    Graph G(N+1);

    for (int i = 0; i < M; ++i) {
        ll a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    ll ans = 0;
    rep(i, 1, N+1) {
        bool flag = true;
        rep(j, 0, G[i].size()) {
            if (H[i] > H[G[i][j]]) {
            } else {
                flag = false;
                break;
            }
        }
        if (flag) {
            ans++;
        }
    }
    cout << ans << endl;
}