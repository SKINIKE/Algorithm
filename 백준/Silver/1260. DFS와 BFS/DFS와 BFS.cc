#include <algorithm>
#include <iostream>
#include <queue>
#include <string.h>
#include <vector>

using namespace std;

vector<int> graph[1001];
bool visited[1001];

void dfs(int v) {
  visited[v] = true;
  cout << v << " ";         //방문할때마다 출력
  for (int i = 0; i < graph[v].size(); i++) {
    if (visited[graph[v][i]] == false){     // next가 false라면
      int next = graph[v][i]; //지금 정점에서 방문할 노드를 next에 대입
      dfs(next);            //재귀
    }
  }
}

void bfs(int v) {
  queue<int> q;
  q.push(v);                 //방문할 정점을 큐에 삽입
  visited[v] = true;         //삽입 후 방문 처리
  while (!q.empty()) {       //큐가 빌때까지
    int current = q.front(); //현재 방문중인 정점 저장
    q.pop();                 //큐의 맨 앞 제거
    cout << current << " ";  // 방문처리하면서 출력
    for (int i = 0; i < graph[current].size(); i++) {
      if (!visited[graph[current][i]]) {   //방문된적 없으면
        visited[graph[current][i]] = true; //방문처리 후
        q.push(graph[current][i]);         //다음 방문지(cur)로 지정
      }
    }
  }
}

int main() {

  ios::sync_with_stdio(0);
  cin.tie(0);

  int n, m, v;
  int node1, node2;
  cin >> n >> m >> v;

  for (int i = 0; i < m; i++) {
    cin >> node1 >> node2;
    //양방향이기 때문에 각 인덱스마다 값을 넣어준다.
    graph[node1].push_back(node2);
    graph[node2].push_back(node1);
  }
  for (int i = 1; i <= n; i++) {
    //방문가능한 정점이 여러개면 작은것부터 방문해야하므로 정렬해줘야 한다.
    sort(graph[i].begin(), graph[i].end());
  }

  dfs(v);
  cout << '\n';
  memset(visited, false, sizeof(visited));
  bfs(v);

  return 0;
}