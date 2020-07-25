#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 1001

using namespace std;

bool comp(pair<int, int> a, pair<int, int> b)
{
	if (a.second < b.second) // b의 second가 a의 second보다 큰 경우
	{
		return true;
	}
	else // a의 second와 b의 second가 같거나 작은 경우
	{
		if (a.second == b.second) 
		{
			if (a.first < b.first)
			{
				return true;
			}
		}
		return false;
	}
}

int main(void)
{
	// 입출력을 빠르게 하기 위한 코드
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int numOfTest = 0;
	int N, M, num1, num2;
	cin >> numOfTest; // 사용자로 부터 입력받음

	for (int i = 0; i < numOfTest; i++)
	{
		cin >> N >> M;
		vector<pair<int, int >> pa;

		for (int k = 0; k < M; k++)
		{
			cin >> num1 >> num2;
			pa.push_back(make_pair(num1, num2)); // num1, num2를 입력받음
		}

		sort(pa.begin(), pa.end(), comp); // 두 번째 원소를 기준으로 내림차순

		int count = 0;
		bool c[MAX] = { false };
		for (int k = 0; k < M; k++)
		{ 	
			for (int j = pa[k].first; j <= pa[k].second; j++)
			{
				if (c[j] == false)
				{
					c[j] = true;
					count++;
					break;
				}
			}
		}
		cout << count << endl;
	}
	return 0;
}
