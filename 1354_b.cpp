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
  
const int MAX_CHARS = 256; 
  
// Function to find smallest window containing 
// all distinct characters 
string findSubString(string str) 
{ 
    int n = str.length(); 
  
    // Count all distinct characters. 
    int dist_count = 0; 
    unordered_map<int, int> hash_map; 
    for (int i = 0; i < n; i++) { 
        hash_map[str[i]]++; 
    } 
  
    dist_count = hash_map.size(); 
    int size = INT_MAX; 
    string res; 
    // Now follow the algorithm discussed in below 
    for (int i = 0; i < n; i++) { 
        int count = 0; 
        int visited[256] = { 0 }; 
        string sub_str = ""; 
        for (int j = i; j < n; j++) { 
            if (visited[str[j]] == 0) { 
                count++; 
                visited[str[j]] = 1; 
            } 
            sub_str += str[j]; 
            if (count == dist_count) 
                break; 
        } 
        if (sub_str.length() < size && count == dist_count) 
            res = sub_str; 
    } 
    return res; 
} 
  

int main() {
    int t;
    cin >> t;
    //vector<vector<int>> data(3, vector<int>(4));
    //初期値0
    //vector<int> data(i, 0);
    rep(i, 0, t) {
        string s;
        cin >> s;
        int len = findSubString(s);
        if (len == 1 || len == 2) {
            cout << 0 << endl;
        } else {
            cout << len << endl;
        }
    }
    return 0;
}