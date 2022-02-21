#include <bits/stdc++.h>
#define MAX 21	
using namespace std;

int n;
int graph[MAX][MAX];
int ans;

void moveGraph(int dir) { // N, E, S, W
	if (dir == 0) {
		for (int j = 0; j < n; j++) {
			int idx = 0;
			for (int i = 1; i < n; i++) {
				if (graph[i][j] != 0) {
					int temp = graph[i][j];
					graph[i][j] = 0;
					if (graph[idx][j] == temp) {
						graph[idx][j] *= 2;
						idx += 1;
					}
					else if (graph[idx][j] == 0)
						graph[idx][j] = temp;
					else {
						idx += 1;
						graph[idx][j] = temp;
					}
				}
			}
		}
	}

	else if (dir == 1) {
		for (int i = 0; i < n; i++) {
			int idx = n-1;
			for (int j = n-2; j > -1; j--) {
				if (graph[i][j] != 0) {
					int temp = graph[i][j];
					graph[i][j] = 0;
					if (graph[i][idx] == temp) {
						graph[i][idx] *= 2;
						idx -= 1;
					}
					else if (graph[i][idx] == 0)
						graph[i][idx] = temp;
					else {
						idx -= 1;
						graph[i][idx] = temp;
					}
				}
			}
		}
	}

	else if (dir == 2) {
		for (int j = 0; j < n; j++) {
			int idx = n-1;
			for (int i = n-2; i > -1; i--) {
				if (graph[i][j] != 0) {
					int temp = graph[i][j];
					graph[i][j] = 0;
					if (graph[idx][j] == temp) {
						graph[idx][j] *= 2;
						idx -= 1;
					}
					else if (graph[idx][j] == 0)
						graph[idx][j] = temp;
					else {
						idx -= 1;
						graph[idx][j] = temp;
					}
				}
			}
		}
	}

	else {
		for (int i = 0; i < n; i++) {
			int idx = 0;
			for (int j = 1; j < n; j++) {
				if (graph[i][j] != 0) {
					int temp = graph[i][j];
					graph[i][j] = 0;
					if (graph[i][idx] == temp) {
						graph[i][idx] *= 2;
						idx += 1;
					}
					else if (graph[i][idx] == 0)
						graph[i][idx] = temp;
					else {
						idx += 1;
						graph[i][idx] = temp;
					}
				}
			}
		}
	}
}

void dfs(int count) {
	if (count == 5) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				ans = max(ans, graph[i][j]);
			}
		}
		return;
	}

	int copyGraph[MAX][MAX] = { 0, };
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			copyGraph[i][j] = graph[i][j];
		}
	}

	for (int k = 0; k < 4; k++) {
		moveGraph(k);
		dfs(count + 1);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				graph[i][j] = copyGraph[i][j];
			}
		}
	}
}

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> graph[i][j];
		}
	}
	dfs(0);
	cout << ans;
	return 0;
}
