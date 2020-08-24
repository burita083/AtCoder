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

int H, W;
int s_y, s_x, g_y, g_x;
vector<string> vec;
vector<vector<bool> > reached;
void search(int y, int x) {
    if (y < 0 || H <= y || x < 0 || W <= x || vec[y][x] == '#') {
        return;
    }

    if (reached[y][x]) {
        return;
    }

    reached[y][x] = true;
    search(y+1, x);
    search(y-1, x);
    search(y, x+1);
    search(y, x-1);
}
int main() {
    cin >> H >> W;
    vec.resize(H);
    rep(i, 0, H) {
        cin >> vec[i];
    }

    reached.resize(H, vector<bool>(W));

    rep(i, 0, H) {
        rep(j, 0, W) {
            if (vec[i][j] == 's') {
                s_y = i;
                s_x = j;
            }

            if (vec[i][j] == 'g') {
                g_y = i;
                g_x = j;
            }
        }
    }

    search(s_y, s_x);
    reached[g_y][g_x] ? cout << "Yes" : cout << "No";
    cout << endl;
    return 0;
}