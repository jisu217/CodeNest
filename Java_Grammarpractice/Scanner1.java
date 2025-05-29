package practice01;

public class Scanner1 {
    import java.util.Scanner; //scanner 사용하기 위함

    public class Main {
        public static void main(String[] args) {
            Scanner inputReader = new Scanner(System.in);
            String strInput = inputReader.nextLine(); // nextLine_한 줄을 읽어서 strInput이라는 변수에 한줄의 내용 저장
            System.out.println(strInput);
        }
    }
}
