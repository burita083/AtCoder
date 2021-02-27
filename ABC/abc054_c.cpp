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
bool check = true;
int ans = 0;
void dfs(Graph &G, int v) {
    seen[v] = true;
    cout << v;
    cout << "を訪問済みにしたよ" << endl;
    rep(i, 1, seen.size()) {
        if (seen[i] == false) {
            check = false;
            break;
        }
    }
    if (check) {
        ++ans;
       cout << "全部訪問したよ" << endl;
    } else {
        rep(i, 1, seen.size()) {
            if (seen[i] == false) {
                cout << i;
                cout << ", ";
            }
        }
        cout << "が未訪問だね" << endl;
    }
    check = true;
    for (auto next_v: G[v]) {
        cout << v;
        cout << "のループ開始だよ" << endl;
        if (seen[next_v]) {
        cout << "今は";
        cout << v;
        cout << "だね。";
        cout << next_v;
        cout << "につながってはいるけど訪問済みだよ。次にいこうね。" << endl;
            continue;
        }
        cout << next_v;
        cout << "にいくね。" << endl;
        dfs(G, next_v);
        //cout << v << endl;
        //cout << next_v << endl;
    }
    cout << v;
    cout << "のループ終わったよ。" << endl;
    seen[v] = false;
    cout << v;
    cout << "を未訪問にしたよ" << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M, s, t;
    cin >> N >> M;
    Graph G(N+1);
    cout << endl;
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        //無向グラフ
        G[b].push_back(a);
    }

    seen.assign(N+1, false);
    dfs(G, 1);
    cout << ans << endl;
    return 0;
}