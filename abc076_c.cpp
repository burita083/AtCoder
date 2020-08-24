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
    string S, T;
    bool flag = false;
    cin >> S >> T;
    rep(i, 0, T.length()) {
        rep(j, 0, S.length()) {
            if (T[i] == S[j] || S[j] == '?') {
                S[j] = T[i];
                int temp = i;
                rep(k, j+1, S.length()) {
                    if (S[k] == T[temp+1] || S[k] == '?') {
                        S[k] = T[temp+1];
                        ++temp;
                        if (temp == T.length()-1) {
                            flag = true;
                        }
                    } else {
                        S[j] = '?';
                        break;
                    }
                }
                temp = i;
                int tempj = j-1;
                for (int i = temp-1; temp >= 0; --temp) {
                    if (S[tempj] == '?') {
                        S[tempj] = T[i];
                        --tempj;
                    } else {
                        break;
                    }
                }
            }
        }
    }
    rep(i, 0, S.length()) {
        if (S[i] == '?') {
            S[i] = 'a';
        }
    }
    if (flag) {
        cout << S << endl;
    } else {
        cout << "UNRESTORABLE" << endl;
    }
    return 0;
}