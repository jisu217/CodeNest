import java.util.ArrayList;
import java.util.Iterator;

public class Iterator_Sample {
    public static void main(String[] args) {
        ArrayList<String> myStringArrays = new ArrayList<String>();

        myStringArrays.add("안녕0"); // 배열 0번째 입력
        myStringArrays.add("안녕1"); // 배열 1번째 입력
        myStringArrays.add("안녕2"); // 배열 2번째 입력

        Iterator<String> myIterator = myStringArrays.iterator();
        while (myIterator.hasNext()) {
            System myString = myIterator.next(); // 다음 항목이 있는가?
            System.out.println(myString); // 다음 항목을 읽어온다.
        }
    }
}
