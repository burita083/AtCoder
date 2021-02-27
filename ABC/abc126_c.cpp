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
# define p(s) std::cout << s ;
# define pl(s)  std::cout << s << endl;
using namespace std;

int main() {
    double N, K;
    cin >> N >> K;
    double ans = 0;
    for (ll i = 1; i <= N; ++i) {
        long double res = 1.0 / N;
        ll num = i;
        while (num < K) {
            num *= 2;
            res *= 0.5;
        }
        ans += res;
    }
    cout<<fixed;
    cout<<setprecision(10);
    cout << ans << endl;
    return 0;
}