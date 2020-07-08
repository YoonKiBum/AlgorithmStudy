#include <iostream>
#include <algorithm>

#define MAX 1001
using namespace std;

int main(void)
{
	// 입출력 속도를 빠르게 하기 위한 코드
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, L;
	int pos[MAX]; // 위치를 담는 배열 
	int cnt = 0;  // 테이프의 개수를 담을 배열
	cin >> N >> L;

	for (int i = 0; i < N; i++) // 물이 새는 곳의 개수 만큼 위치를 배열에 넣음
	{
		cin >> pos[i];
	}

	sort(pos,pos+N); // 입력받은 위치들을 정렬해줌 stl 사용

	int i = 0;
	for (int j = 0; j < N; j++) // 위치들의 개수만큼 반복을 함 
	{
		if(pos[j+1]- pos[j] < L) // 현재 위치와 다음 위치의 거리 차이가 한 테이프로 커버 가능한 경우
		{
			cnt += 1; // 테이프의 개수를 하나 증가
			i = j+1;  // i를 j+1로 초기화
			while (pos[i] - pos[j]<L) // 현재 위치와 i번쨰 위치 사이의 거리가 한 테이프로 커버 가능한 동안 반복
			{
				i++; // 다음 위치를 조회하기 위하여 i를 하나 증가시킴
			}
			j = i-1; // 한 테이프로 커버 불가능 한 경우 j를 하나 줄인 i로 초기화 한다.
		}
		else // 현재 위치와 다음 위치의 거리 차이가 한 테이프로 커버 불가능 한 경우  
		{
			cnt++; // 테이프의 개수를 하나 증가시킴
		}
	}

	cout << cnt;

	return 0;
}
