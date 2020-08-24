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
  int N;
    cin >> N;
    vector<int> P(N);
    vector<int> Q(N);
    rep(i, 0, N) {
        cin >> P[i];
        Q[i] = P[i];
    }
    sort(P.begin(), P.end());

    int count = 0;
    int c = 0;
    do{
         for(int i=0; i<N-1; i++){
             c = 0;
             rep(j, 0, N) {
                 if (P[j] == Q[j]) {
                     ++c;
                 }
             }
             if (c == N) {
                 break;
             }
            if (P[i+1] != Q[i]) {
                ++count;
            }
         }
         if (count == N-1) {
             rep(i, 0, N) {
                 cout << P[i];
                 cout << " ";
             }
             return 0;
         }
    }while(next_permutation(P.begin(),P.end()));
    cout << -1 << endl;

    return 0;
}