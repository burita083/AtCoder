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

// 各桁の和を計算する関数
int findSumOfDigits(int n) {
  int sum = 0;
  while (n > 0) { // n が 0 になるまで
    sum += n % 10;
    n /= 10;
  }
  return sum;
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

// 最短距離、頂点番号
using P = pair<int, int>;
int V;
struct edge {
    int to;
    int cost;
};
vector<vector<edge> > G;
vector<int> d;
vector<int> d1;
void dijkstra(int s) {
    priority_queue<P, vector<P>, greater<P> >que;
    d[s] = 0;
    que.push(P(0, s));
    while(!que.empty()) {
        P p = que.top();
        que.pop();
        int v = p.second;
        if (d[v] < p.first) continue;
        rep (i, 0, G[v].size()) {
            edge e = G[v][i];
            if (d[e.to] > d[v] + e.cost) {
                d[e.to] = d[v] + e.cost;
                que.push(P(d[e.to], e.to));
            }
        }
    }
}

void dijkstra2(int s, int t) {
    
}

//想定解答との絶対誤差または相対誤差が 10−6以下の場合+1以上だしておく。適当に15とかでもおｋ．
//cout << fixed << setprecision(15);

int main() {
    string s;
    int N, M, T;
    cin >> N >> M >> T;
    vi a(N);
    G.resize(N+1);
    d.resize(N);
    rep (i, 0, N) {
        cin >> a[i];
        d[i] = INF;
    }
    rep(i, 0, M) {
        int a, b, c;
        cin >> a >> b >> c;
        --a;
        --b;
        edge e = {b, c};
        G[a].push_back(e);
    }
    dijkstra(0);

    vector<int> from1(N);
    vector<int> to1(N);
    rep(i, 0, N) {
        from1[i] = d[i];
    }
    int ans = 0;
    rep(i, 1, N) {
        rep (i, 0, N) {
            d[i] = INF;
        }
        priority_queue<P, vector<P>, greater<P> >que;
        d[i] = 0;
        que.push(P(0, i));
        int remain = T;
        while(!que.empty()) {
            P p = que.top();
            que.pop();
            int v = p.second;
            if (d[v] < p.first) continue;
            if (v == 0) {
                to1[i] = from1[i] + p.first;
                remain -= to1[i];
                chmax(ans, remain*a[i]);
                break;
            }
            rep (i, 0, G[v].size()) {
                edge e = G[v][i];
                if (d[e.to] > d[v] + e.cost) {
                    d[e.to] = d[v] + e.cost;
                    que.push(P(d[e.to], e.to));
                }
            }
        }
    }
    chmax(ans, T*a[0]);
    cout << ans << endl;
    return 0;
}