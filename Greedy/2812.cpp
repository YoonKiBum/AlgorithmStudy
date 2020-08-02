#include <iostream>
#include <stack>

using namespace std;

stack<int> S;

int main(void)
{
	// 입출력을 빠르게 하기 위한 코드
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, K;
	string st; // 입력 받는 문자열
	string ans;// 답을 출력해줄 ans
	int count = 0;

	cin >> N >> K;
	cin >> st;

	for (int i = 0; i < (signed)st.length(); i++)
	{
		while ((count < K) && !S.empty() && S.top() < st[i]) 
		{
			S.pop();
			count++;
		}
		S.push(st[i]);
	}

	while (!S.empty())
	{
		ans += S.top();
		S.pop();
	}

	for (int i = (signed)ans.length() - 1; i >= (K-count); i--)
	{
		cout << ans[i];
	}

	return 0;
} 
