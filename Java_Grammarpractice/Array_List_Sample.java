import java.util.ArrayList; // java.util의 ArrayList를 사용

public class Array_List_Sample {
    public static void main(String[] args) {
        ArrayList<String> myStringArrays = new ArrayList<String>();

        myStringArrays.add("안녕0"); // 배열 0번째 입력
        myStringArrays.add("안녕1"); // 배열 1번째 입력
        myStringArrays.add("안녕2"); // 배열 2번째 입력

        String myString1 = myStringArrays.get(1); // 배열 1번째 읽기
        System.out.println(myString1); // 안녕1
        System.out.println();

        myStringArrays.add(1, "Java1"); // 배열 1번째 내용 수정
        for( String myStringVar : myStringArrays) { //  myStringArrays에 있는 모든 문자열 요소를 하나씩 꺼내어 myStringVar에 대입하고 출력
            System.out.println(myStringVar);
        }
        System.out.println(); // 안녕0
                              // Java1
                              // 안녕1
                              // 안녕2

        myStringArrays.remove(0); // 배열 0번째 삭제
        for (String myStringVar : myStringArrays) {
            System.out.println(myStringVar); // Java1
                                             // 안녕1
                                             // 안녕2
        }
    }
}
