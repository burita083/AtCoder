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

//想定解答との絶対誤差または相対誤差が 10−6以下の場合+1以上だしておく。適当に15とかでもおｋ．
//cout << fixed << setprecision(15);

int main() {
    int N;
    cin >> N;
    //vector<vector<int>> data(3, vector<int>(4));
    //初期値0
    //vector<int> data(i, 0);
    vl a(N);
    rep(i, 0, N) {
        int a, b, c;
        int res = 0;
    bool flag3 = false;
    bool flag2A = false;
    bool flag2B = false;
    bool flag2C = false;
    bool flag1A = false;
    bool flag1B = false;
    bool flag1C = false;
        cin >> a >> b >> c;
        while(true) {
            int temp = res;
            if(a>=1 && flag1A == false) {
                a--;
                flag1A = true;
                //cout << "1A ";
                ++res;
            } else if(b>=1 && flag1B == false) {
                b--;
                flag1B = true;
                //cout << "1B ";
                ++res;
            } else if(c>=1 && flag1C == false) {
                c--;
                flag1C = true;
                //cout << "1C ";
                ++res;
            } else {
                int mx = -1;
                mx = max(a, b);
                if (chmax(mx, c)) {
                    if (flag2C) {
                        if(a>=1 && b>=1 && flag2A == false) {
                            a--;
                            b--;
                            flag2A = true;
                            //cout << "2A ";
                            ++res;
                        } 
                    }
                } else {
                    if(a>=1 && b>=1 && flag2A == false) {
                        a--;
                        b--;
                        flag2A = true;
                        //cout << "2A ";
                        ++res;
                    } 
                }

                mx = -1;
                mx = max(a, c);
                if (chmax(mx, b)) {
                    if (flag2B) {
                        if(a>=1 && c>=1 && flag2C == false) {
                            a--;
                            c--;
                            flag2C = true;
                            //cout << "2C ";
                            ++res;
                        } 
                    }
                } else {
                        if(a>=1 && c>=1 && flag2C == false) {
                            a--;
                            c--;
                            flag2C = true;
                            //cout << "2C ";
                            ++res;
                        } 
                }
           
                mx = -1;
                mx = max(b, c);
                if (chmax(mx, a)) {
                    if (flag2A) {
                        if(b>=1 && c>=1 && flag2B == false) {
                            b--;
                            c--;
                            flag2B = true;
                            //cout << "2B ";
                            ++res;
                        }
                    }
                } else {
                    if(b>=1 && c>=1 && flag2B == false) {
                        b--;
                        c--;
                        flag2B = true;
                        //cout << "2B ";
                        ++res;
                    }
                }
            
                if(a>=1 && b >= 1 && c>=1 && flag3 == false) {
                    a--;
                    b--;
                    c--;
                    flag3 = true;
                    //cout << "3 ";
                    ++res;
                }
            }
            
            if (temp == res) break;
        }
        cout << res << endl;
    }
    return 0;
}