import java.util.ArrayList;

public class Wrapper {
    public static void main(String[] args) {
        ArrayList<Integer> myIntArrays = new ArrayList<Integer>();
        for(int i = 0; i < 10; i++) {
            myIntArrays.add(i);
        }
        System.out.println(myIntArrays.get(3)); // 인덱스 3에 해당하는 값인 3 출력

        ArrayList<Double> myDoubleArrays = new ArrayList<Double>();
        for(double j = 0.0; j <= 10.0; j = j + 2.0) {
            myDoubleArrays.add(j);
        }
        System.out.println(myDoubleArrays.get(3)); // 인덱스 3에 해당하는 값인 6.0 출력
    }
}
