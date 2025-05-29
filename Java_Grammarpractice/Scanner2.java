package practice01;

public class Scanner2 {
    import java.util.Scanner;

    public class HelloWorld {
        public static void main(String[] args) {
            System.out.println("계산할 값을 입력하고 Enter키를 치세요.");
            Scanner s = new Scanner(System.in);
            int i = s.nextInt();
            char c = s.next().charAt(0); // next()는 한 문자를 입력 받는 기능이 아닌 여러 문자 입력 받는 기능으로
            // 문자형 변수인 char이 아닌 문자열(문자의 집합)인 String 변수로 값을 입력 받게 됨 -> String에 조작을 가한 것
            // s.next()로 입력 받은 문자열 중에 첫번쨰 문자 charAt(0)를 가져다가 문자형 char 변수 c에다가 저장하라는 명령
            int j = s.nextInt();

            int z = 0;
            if ( c == '+') {
                z = i + j;
            }
            else if ( c == '-') {
                z = i - j;
            }
            else if ( c == '*') {
                z = i * j;
            }
            else if ( c == '/') {
                z = i / j;
            }
            System.out.println(z);
        }
    }
}
