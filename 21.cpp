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

 ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (NULL == l1) return l2;
        if (NULL == l2) return l1;
        
        ListNode* head = NULL;
        
        if (l1->val < l2->val) {
            head = l1;
            l1 = l1->next; 
        } else {
            head = l2;
            l2 = l2->next;
        }
        
        ListNode* p = head;
        
        while (l1 && l2) {
            if (l1->val < l2->val) {
                p->next = l1;
                l1 = l1->next;
            } else {
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        
        if (l1) {
            p->next = l1;
        } else {
            p->next = l2;
        }
        
        return head;
}

int main() {
    string s;
    int N;
    cin >> N;
    //vector<vector<int>> data(3, vector<int>(4));
    //初期値0
    //vector<int> data(i, 0);
    vl a(N);
    rep(i, 0, N) {
        cin >> a[i];
    }
    cout << N << endl;
    return 0;
}