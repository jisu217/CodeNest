// Quiz1. 키의 최대값/합계/평균를 구하는 문제
#include <stdio.h>
#include <stdlib.h>

int maxof(const int a[], int n) { // 최댓값 함수
   int max = a[0];
   for (int i = 1; i < n; i++) {
     if (a[i] > max) max = a[i];
     } return max;
}

int sumof(const int a[], int n) { // 합계 함수
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += a[i];
    } return sum;
}

double aveof(const int a[], int n) { // 평균 함수
    return (double)sumof(a, n) / n;
}

// 키의 최대값/합계/평균
int main(void) {
  int number;

  printf("사람 수: ");
  scanf("%d", &number);

  int* height = calloc(number, sizeof(int));

  printf("%d명의 키를 입력하세요.\n", number);
  for (int i = 0; i < number; i++) {
    printf("height[%d] : ", i);
    scanf("%d", &height[i]);
  }

  printf("최댓값은 %d입니다.\n", maxof(height, number));
  printf("합계는 %d입니다.\n", sumof(height, number));
  printf("평균은 %.2f입니다.\n", aveof(height, number));

  free(height); // 메모리 해제
  return 0;
}
