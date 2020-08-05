#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<pair<long long, int>> vec;
long long ans, num1, num2, num3;

// num2를 찾는 과정 주사위의 자신에 해당하는 면과 맞은편 면을 제외한 4면중 최소 값을 찾음
long long minNum(int num)
{
	for (int j = 0; j < 6; j++)
	{
		if (vec[j].second != num && (vec[j].second + num) != 5)
		{
			return vec[j].first;
		}
	}
}

// num3를 찾는 과정 주사위의 자신에 해당하는 면과 맞으편 면을 제외한 4면중 이웃하는 두 면의 합의 최소를 구함
long long minNum2(int num)
{
	long long arr2[4] = { 0 };
	long long arr3[4] = { 0 };
	vector<pair<long long, int>> a;

	int j = 0;

	for (int i = 0; i < 6; i++)
	{
		if (vec[i].second != num && (vec[i].second + num) != 5)
		{
			a.push_back(make_pair(vec[i].first, vec[i].second));
			j++;
		}
	}

	int m = 0;
	for (int k = 0; k < 4; k++)
	{
		for (int l = k; l < 4; l++)
		{
			if (a[k].second != a[l].second && a[k].second + a[l].second != 5)
			{
				arr3[m] = a[k].first + a[l].first;
				m++;
			}
		}
	}

	sort(arr3, arr3 + 4);

	return arr3[0];
}

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	long long n, m, p;
	
	cin >> n;

	for (int i = 0; i < 6; i++)
	{
		cin >> m;
		vec.push_back(make_pair(m, i));
	}

	sort(vec.begin(),vec.end());
	num1 = vec[0].first;
	p = vec[0].second;

	switch (p)
	{
		case 0:
			num2 = minNum(0);
			num3 = minNum2(0);
			break;
		case 1:
			num2 = minNum(1);
			num3 = minNum2(1);
			break;
		case 2:
			num2 = minNum(2);
			num3 = minNum2(2);
			break;
		case 3:
			num2 = minNum(3);
			num3 = minNum2(3);
			break;
		case 4:
			num2 = minNum(4);
			num3 = minNum2(4);
			break;
		case 5:
			num2 = minNum(5);
			num3 = minNum2(5);
			break;
	}


	if (n == 1)
	{
		for (int i = 0; i < 5; i++)
		{
			ans += vec[i].first;
		}
		cout << ans;
	}
	else if(n >= 2)
	{
		ans = num1 * (5 * n - 6) * (n - 2) + (8 * n - 12) * (num1 + num2) + 4 * (num1 + num3);
		cout << ans;
	}

	return 0;
}
