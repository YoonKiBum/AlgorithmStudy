#include <iostream>
#include <algorithm> // sort 함수 이용
#include <vector>
#include <queue>
#define MAX  300001

using namespace std;

bool check[MAX]; // 보석을 가방에 담은 여부를 판단하기 위한 bool형 배열 check

vector<pair<int, int>> vec; // 보석의 무게와 가격을 vector의 pair형으로 구현
vector<int> bag; // 가방에 담을 수 있는 무게의 정보를 저장할 vector bag
priority_queue<int> pq; // 우선 순위 큐 pq

void steal(vector<pair<int,int>> a, vector<int> b) 
{
	long long int total = 0;
	int j = 0;
	for (int i = 0; i < (signed)b.size(); i++) // 가방의 개수만큼 조회하면서 가방에 담을 보석을 정함
	{
		while (j < (signed)a.size()&& a[j].first <= b[i]) // 보석들을 조회하면서 가방의 무게보다 작은 것들을 가방에 넣음
		{
			pq.push(a[j].second);
			j++;
		}
		if (pq.empty() == false) // pq가 비어있지 않다면 가장 무거운 무게가 맨 위에 있으므로 해당하는 것을 더함
		{
			total += pq.top();
			pq.pop();
		}
	}
	cout << total << endl;
}

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, K; // 보석의 개수 가방의 개수	
	cin >> N >> K;

	for (int i = 0; i < N; i++)
	{
		int M, V;
		cin >> M >> V;
		vec.push_back(make_pair(M, V));
	}
	sort(vec.begin(), vec.end()); // 보석을 무게를 기준으로 내림차순 정렬

	for (int j = 0; j < K; j++)
	{
		int C;
		cin >> C;
		bag.push_back(C);
	}
	sort(bag.begin(), bag.end()); // 가방의 수용 무게를 기준으로 내림차순 정렬
	
	steal(vec,bag);

	return 0;
}
