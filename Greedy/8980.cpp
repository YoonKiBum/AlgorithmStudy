#include <iostream>
#include <algorithm>
#define MAX 10001

using namespace std;

pair<pair<int, int>, int> bag[MAX];
int arr[MAX] = { 0 };

bool cmp(const pair<pair<int, int>, int>& a, const pair<pair<int, int>, int>& b)
{
	if (a.first.second < b.first.second)
	{
		return true;
	}

	else if (a.first.second == b.first.second)
	{
		if (a.first.first < b.first.first)
		{
			return true;
		}
	}

	return false;
}

int main(void)
{
	// 입력을 빠르게 해주는 코드
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, C, M;

	cin >> N >> C;
	cin >> M;

	for (int i = 0; i < M; i++)
	{
		cin >> bag[i].first.first >> bag[i].first.second >> bag[i].second;
	}

	sort(bag, bag + M, cmp); // second를 기준으로 정렬 대신 같은 경우 first를 기준으로 정렬
	
	int result = 0;
	int k = 0;
	for (int i = 0; i < M; i++)
	{
		int maxLoad = 0;
		for (int j = bag[i].first.first; j < bag[i].first.second; j++)
		{
			if (maxLoad < arr[j]) // 해당 루트에 있는 최대값 선택
			{
				maxLoad = arr[j];
			}
		}

		int volume = 0;
		if (maxLoad < C && C >= maxLoad + bag[i].second) // 최대 용량보다 해당 구간의 최대값 + 추가할 용량이 작은 경우
		{
			volume = bag[i].second;
			result += volume;
		}
		else if(maxLoad < C && C < maxLoad + bag[i].second)// 최대 용량이 해당 구간의 최대값 + 추가할 용량보다 작은 경우
		{
			volume = C - maxLoad;
			result += volume;
		}

		for (int j = bag[i].first.first; j < bag[i].first.second; j++) // 루트들을 조회하며 각 구간별로 volume을 더해준다.
		{
			arr[j] += volume;
		}
	}

	cout << result << endl;

	return 0;
}
