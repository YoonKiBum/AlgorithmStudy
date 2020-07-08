#include <iostream>
#include <string> 
#define MAX 2501
using namespace std;

int main(void)
{
	// 입출력을 빠르게 하기 위한 코드
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string A, B;
	getline(cin, A); // 공백문자까지 입력받기 위하여 getline함수 사용
	getline(cin, B); // 공백문자까지 입력받기 위하여 getline함수 사용

	int cnt = 0; // 같은 경우를 샐 변수 cnt
	bool flag = false; // 다른 경우를 판별할 bool형 변수 flag flase로 초기화 함
	int j = 0;

	for (int i = 0; i < (signed)(A.length()-B.length())+1; i++) // 긴 문자열의 길이 - 짧은 문자열의 길이 +1 만큼 for loop반복
	{
		for (j = 0; j < (signed)B.length(); j++) // 짧은 문자열의 길이만큼 for loop를 반복하며 조회
		{
			if (A[i + j] != B[j]) // 하나라도 다른 문자가 존재한다면
			{
				flag = true; // flag를 true로 재정의 
				break;
			}
		}
		if (flag == false) // 만약 flag 가 false라면 즉 다른 문자가 하나라도 없다면
		{
			cnt++; // cnt를 하나 증가시킴
			i = i + j-1; // i를 i + j - 1로 재정의 하여 찾은 경우 해당하는 칸 만큼을 띄어넘는것을 구현
		}
		flag = false; // flag를 초기화 해줌
	}

	cout << cnt;
	return 0;
}
