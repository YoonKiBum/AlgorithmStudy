#include <bits/stdc++.h>
#define MAX 20001
#define INF (int)1e9
using namespace std;
vector<pair<int, int> > graph[MAX];
int d[MAX];
int v, e;

void dijkstra(int start) {
	priority_queue<pair<int, int> > pq;
	pq.push({ 0, start });
	d[start] = 0;

	while (!pq.empty()) {
		int dist = -pq.top().first;
		int now = pq.top().second;
		pq.pop();
		if (d[now] < dist)
			continue;
		for (int i = 0; i < (signed)graph[now].size(); i++) {
			int cost = dist + graph[now][i].second;
			if (cost < d[graph[now][i].first]) {
				d[graph[now][i].first] = cost;
				pq.push({ -cost, graph[now][i].first });
			}
		}
	}
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> v >> e;
	int start;
	cin >> start;
	fill(d, d + MAX, INF);

	for (int i = 0; i < e; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		graph[a].push_back(make_pair(b, c));
	}

	dijkstra(start);

	for (int i = 1; i <= v; i++) {
		if (d[i] == INF) {
			cout << "INF" << "\n";
		}
		else {
			cout << d[i] << "\n";
		}
	}
	return 0;
}
