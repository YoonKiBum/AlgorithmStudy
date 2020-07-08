#include <iostream>
#define MAX 51
using namespace std;

int main(void)
{ 
	// 입출력을 빠르게 하기 위한 코드
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	string A, B;
	cin >> A >> B;

	int minDiff = 99999999; // 두 문자열의 차이의 최소값을 구하기 위한 변수 일단 최대값으로 초기화를 한다
	int cnt = 0; // 두 문자열의 차이의 개수를 세기 위한 변수

	for (int i = 0; i < (signed)(B.length() - A.length())+1; i++) // 긴 문자열의 길이 - 짧은 문자열의 길이 + 1을 통해 슬라이딩
	{
		for (int j = 0; j < (signed)A.length(); j++) // 짧은 문자열의 길이만큼을 비교
		{
			if (A[j] != B[i+j]) // 두 문자열의 차이를 확인할때마다 cnt를 하나씩 증가시킴
			{
				cnt++;
			}
		} 
		if (minDiff > cnt) // minDiff가 cnr보다 크다면 minDiff를 cnr로 초기화 해줌.
		{
			minDiff = cnt;
		}
		cnt = 0;
	}


	cout << minDiff;
	return 0;
}
