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
int main() {
    string N;
    int K;
    cin >> N >> K;
    //vector<vector<int>> data(3, vector<int>(4));
    //初期値0
    //vector<int> data(i, 0);
    vi a(K);
    vi b;
    rep(i, 0, K) {
        cin >> a[i];
    }
    int j = 0;
    rep(i, 0, K) {
        if (a[j] != i) {
            if(find(b.begin(), b.end(), i) != b.end()) {
            } else {
                b.push_back(i);
            }
        } else {
            ++j;
        }
    }
    rep(i, 0, b.size()) {
        if (b[i] >= stoi(N)) {
            cout << b[i] << endl;
            return 0;
        }
    }
    int res = 0;
    rep(i, 0, b.size()) {
        if (b[i] >= int(N[0]) - 48) {
            cout << b[i];
            rep(j, 0, N.length()-1) {
                cout << b[0];
            }
            cout << endl;
            return 0;
        }
    }
    return 0;
}