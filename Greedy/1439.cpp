#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
bool flag = false; // 0과 1을 판별할 bool형 flag

int main(void)
{
	// 입출력을 빠르게 하기 위한 코드
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string s;
	int numOfZero = 0, numOfOne = 0;
	int ans = 0;

	cin >> s;
	s.append("!"); // 문자열의 끝에 다른 문자를 넣어서 끝임을 표시함

	for (int i = 0; i < (signed)s.length()-1; i++) // 문자열 끝 바로 전 까지 조회
	{
		// 0 이면 flag를 flase로 세팅, 1 이면 flag를 true로 세팅
		if (s[i]=='0')
		{
			flag = false;
		}
		else if (s[i] == '1')
		{
			flag = true;
		}

		if (flag == false && s[i + 1] != s[i]) // flag가 false이면서 다음 원소와 다르면 numOfZero증가
		{
			numOfZero++;
		}
		else if (flag == true && s[i + 1] != s[i]) // flag가 true이면서 다음 원소와 다르면 numOfOne증가
		{
			numOfOne++;
		}
	}

	cout << min(numOfOne, numOfZero); // 둘 중 최소값을 출력
	return 0;
}
