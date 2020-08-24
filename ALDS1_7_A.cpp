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
#define NIL -1
struct Node {
    int parent;
    int left;
    int right;
};

Node T[100001];
int D[100001];
void print(int i) {
    cout << "node " << i << ": ";
    cout << "parent = " << T[i].parent;
    cout << ", depth = " << D[i];
    cout << ", ";

    if (T[i].parent == NIL) cout << "root";
    else if (T[i].left == NIL) cout << "leaf";
    else cout << "internal node";
    cout << ", [";

    // left, rightの巡回の仕方を理解する
    // NILチェックを忘れない。そうしないとループが終わらない。
    if (T[i].left != NIL) {
        int current = T[i].left;
        cout << current;

        while (T[current].right != NIL) {
            current = T[current].right;
            cout << ", " << current;
        }
    }
    cout << "]" << endl;
}
void depth(int n, int d) {
    D[n] = d;
    if (T[n].right != NIL) depth(T[n].right, d);
    // 左で深さを1増やす
    if (T[n].left != NIL) depth(T[n].left, d+1);
}
int main() {
    int n, id, k, c, root;
    cin >> n;

    // 初期設定
    rep(i, 0, n) T[i].parent = T[i].left = T[i].right = NIL;

    rep(i, 0, n)  {
        cin >> id >> k;
        int left;
        // 次数の数だけループ
        rep(j, 0, k) {

            //ループの中で値取得。此のやり方は覚えておく。
            cin >> c;
            if (j == 0){ 
                T[id].left = c;
            } else {
                T[left].right = c;
            }
            // 添字が木の値
            T[c].parent = id;
            // left -> right -> right ... -> nil
            left = c;
        }
    }

    // rootはparentが設定されていない
    rep(i, 0, n) {
        if (T[i].parent == NIL) {
            root = i;
            break;
        }
    }

    depth(root, 0);
    rep(i, 0, n) print(i);
    

    return 0;
}