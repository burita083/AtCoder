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

int main() {
    ll n;
    cin >> n;
    n++;
    string N = to_string(n);
    int len = N.length();
    //cout << (N[0] -'0' + N[1]-'0') << endl;
    //cout << (N[0] -'0' + N[1]-'0' - 1) << endl;
    ll sum = N[0] - '0' - 1;
    sum += 9 * (N.length() - 1);
    cout << sum << endl;
    return 0;
}