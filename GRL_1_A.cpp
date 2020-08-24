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

using Graph = vector<vector<int> >;//隣接リスト
vector<bool> seen;
void dfs(Graph &G, int v) {
    seen[v] = true;
    for (auto next_v: G[v]) {
        if (seen[next_v]) continue;
        dfs(G, next_v);
    }
}
struct edge{int to,cost;};

// O(ElogE)
 
// pq<pair> はfirstが大きい順に出てくるのですか？
// s:= 開始ノード  v:= 頂点数  adjlist:= 隣接リスト (first:= コスト   second:= 行先)
vector<int> dijk(int s, int v, vector<vector<pair<int, int> > > adjlist){
     
    priority_queue <pair<int, int> > wait;
    vector<int> result(v, INF);
 
    //スタート地点を追加
    result[s] = 0;
    wait.push(make_pair(0, s));
 
    //ダイクストラ本体
    while(!wait.empty()){    //waitが空になるまで
 
        int nowpoint = wait.top().second;
        int nowcost = -wait.top().first;
        wait.pop();
 
        if(result[nowpoint] < nowcost) continue;
 
 
        //今いる頂点と隣接しているすべての頂点をなめる
        for(int i = 0; i < adjlist[nowpoint].size(); i++){
 
            int nextpoint = adjlist[nowpoint][i].second;
            int nextcost = nowcost + adjlist[nowpoint][i].first;
            //現時点より安く到達できそうであれば、結果を更新して優先度付きキューに格納
            if(result[nextpoint] > nextcost){
                result[nextpoint] = nextcost;
                wait.push(make_pair(-nextcost, nextpoint));
            }
        }
    }
     
    return result;         //結果列を返す
}
 
int main(){
 
    int V, E, S; cin >> V >> E >> S;     // V:= 頂点の数    E:= 辺の数    S:= スタートノード
    vector<vector<pair<int, int> > > adjlist(V);      //first := コスト　second := 行先
 
    //入力
    for(int i = 0; i < E; i++){
        int a, b, c; cin >> a >> b >> c;           // a ,b 間に コスト c の辺がある
        adjlist[a].push_back(make_pair(c, b));
        //adjlist[b].push_back(make_pair(c, a));      
    }
 
    vector<int> result(V);
    result = dijk(S, V, adjlist);
    //cout << result[G] << endl;
 
    for(int i = 0; i < V; i++){
        if(result[i] == INF) cout << "INF" << endl;
        else cout << result[i] << endl;
    }
    return 0;
}
