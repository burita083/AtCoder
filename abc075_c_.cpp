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
#define rep(i, a, n) for(ll i = a; i<n; i++)
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

class UnionFind {
public:
    vector<ll> par;
    void init(ll n) {
        rep(i, 0, n) {
            //par[i] == iのとき、iの親はiとなるから初期化では全て根であるとする。
            par.push_back(i);
        }
    }
    void clear() {
        rep(i, 0, par.size()) {
            par[i] = i;
        }
    }

    ll root(ll x) {
        if (par[x] == x) {
            return x;
        } else {
            return par[x] = root(par[x]);
        }
    }

    // これは併合するために使う
    bool unite(ll x, ll y) {
        x = root(x);
        y = root(y);
        // 併合済ならばfalse
        if (x == y) return false;

        par[y] = x;
        return true;
    }

    bool isSame(ll x, ll y) {
        return root(x) == root(y);
    }
};

int main() {
    ll N, M;;
    cin >> N >> M;
    vector<pair<ll, ll> > e(M);
    ll u, v;
    rep(i, 0, M) {
        cin >> u >> v;
        --u; --v;
        e[i] = make_pair(u, v);
    }

    UnionFind T;
    T.init(N);
    int count = 0;
    rep(i, 0, M) {
        T.clear();
        int ans = 0;
        bool flag = true;
        rep(j, 0, M) {
            if (j <= count) continue;
            T.unite(e[j].first, e[j].second);
        }

            rep(j, 0, N) {
                if (!T.isSame(j, i)) {
                    ++ans;
                }
            }
        ++count;
        cout << ans/2 << endl;
    }
    return 0;
}