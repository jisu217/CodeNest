package practice01;

public class descending_order {
    public class Helloworld {
        public static void main(String[] args) {
            int [] englishScores = {80, 90, 30, 40, 70, 95, 76, 98, 100, 77};
            int temp = 0; // 순서 변경 시 임의로 값을 저장할 때 사용하는 임시 변수

            for (int i = 0; i < englishScores.length; i++) {
                for (int j = i + 1; j < englishScores.length; j++) {

                    // i = 0일 때, j는 1부터 시작 - englishScores[0]과 englishScores[1], englishScores[2], ..., englishScores[9]를 비교
                    // i = 1일 때, j는 2부터 시작 - englishScores[1]과 englishScores[2], englishScores[3], ..., englishScores[9]를 비교
                    // englishScores[0]과 englishScores[1]을 다시 비교하는 것을 피하기 위하여 작성

                    if (englishScores[i] < englishScores[j]) {
                        temp = englishScores[i];
                        englishScores[i] = englishScores[j];
                        englishScores[j] = temp;
                    }
                }
                system.out.print(englishScores[i] + " ");
            }
        }
    }
}
