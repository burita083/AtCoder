#include <algorithm>
#include <string>
using namespace std;
 
long long memo[100000];

long long fib(int n) {
    if (n <= 1) return n;
    if (memo[n] != 0) return memo[n];
    return memo[n] = fib(n - 1) + fib(n - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int a;
    cin >> a;
    int n = fib(a);
    cout << n << endl;
    return 0;
}

