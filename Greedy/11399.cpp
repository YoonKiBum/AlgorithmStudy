#include <iostream>
#include <algorithm> 
#define MAX 1001

using namespace std;
int a[MAX];
int n, sum;

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	sort(a, a + n); // C++ stl을 활용하여 오름차순으로 정렬해줌

	for (int i = 0; i < n; i++) // 각 사람들의 소요시간의 총합을 구하는 for문
	{
		for (int j = 0; j <= i; j++)
		{
			sum += a[j];
		}
	}

	cout << sum;

	return 0;
}

