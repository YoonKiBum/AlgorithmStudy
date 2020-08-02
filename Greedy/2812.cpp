#include <iostream>
#include <deque>
#include <string>
#define MAX 500001

using namespace std;
bool check = false;

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int N, K;
	cin >> N >> K;
	string s;
	cin >> s;

	deque<char> dq;
	for (unsigned int i = 0; i < s.length(); i++)
	{
		while (K && !dq.empty() && dq.back() < s[i])
		{
			dq.pop_back();
			K--;
		}
		dq.push_back(s[i]);
	}

	for (unsigned int i = 0; i < dq.size() - K; i++)
	{
		cout << dq[i];
	}
	cout << "\n";

	return 0;
}
