package practice01;

public class GCD {
    class Solution {
        public int GCD(int num1, int num2) {
            if (num1 % num2 == 0)
                return num2;
            return GCD(num2, num1 % num2);
        }

        public int[] solution(int denum1, int num1, int denum2, int num2) {
            int[] answer;

            denum1 *= num2;
            denum2 *= num1;

            answer = new int[]{denum1 + denum2, num1 * num2};

            int greatest_common_divisor = GCD(answer[0], answer[1]); // answer[0]: 두 분수의 합산된 분자, answer[1]: 두 분수의 분모
            answer[0] /= greatest_common_divisor;
            answer[1] /= greatest_common_divisor;

            return answer;
        }
    }
    }

// 최대공약수(GCD)를 구하는 유클리드 호제법
// public int GCD(int num1, int num2) {
//    if (num1 % num2 == 0)
//    return num2;
// return GCD(num2, num1 % num2);
// }

// 첫 번째 호출: GCD(7, 4)

// 7 % 4 = 3 (나머지 3)
// num1 % num2가 0이 아니므로 return GCD(4, 3)를 호출
// 두 번째 호출: GCD(4, 3)

// 4 % 3 = 1 (나머지 1)
// num1 % num2가 0이 아니므로 return GCD(3, 1)를 호출
// 세 번째 호출: GCD(3, 1)

// 3 % 1 = 0 (나머지 0)
// num1 % num2가 0이므로 return 1을 반환
// 따라서, GCD(7, 4)의 결과는 1. 즉, 7과 4의 최대공약수는 1
