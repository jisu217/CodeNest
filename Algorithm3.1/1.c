# 자기주도적 과제_선형 검색에서 중복 원소 모두 찾기

#include <stdio.h>
#include <stdlib.h>

int search_all(const int a[], int n, int key) {
    int count = 0; // 검색된 요소의 개수를 저장할 변수 초기화

    for (int i = 0; i < n; i++) {
        if (a[i] == key) {
            printf("%d(은)는 x[%d]에 있습니다.\n", key, i);
            count++;
        }
    }
    return count;
}

int main(void) {
    int nx, ky; // nx: 요소 개수, ky: 검색할 값
    puts("선형 검색 (중복 원소 모두 찾기)");

    printf("요소 개수 : ");
    scanf("%d", &nx);

    int *x = calloc(nx, sizeof(int));

    for (int i = 0; i < nx; i++) {
        printf("x[%d] : ", i);
        scanf("%d", &x[i]);
    }

    printf("검색값 : ");
    scanf("%d", &ky);

    int count = search_all(x, nx, ky);

    if (count == 0) {
        puts("검색에 실패했습니다.");
    }

    free(x);
    return 0;
}