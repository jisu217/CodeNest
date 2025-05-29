package practice01;

public class printin {
    class SystemOutPrintln { // SystemOutPrintln 클래스 이름
        public static void main(String[] args) { //main 메소드 이름
            System.out.println(7); //7
            System.out.println(3.15); //3.15
            System.out.println("3 + 5 = " + 8); // 3 + 5 = 8
            System.out.printin(3.15 +"는 실수입니다."); // 3.15는 실수입니다.
            System.out.printin("3 + 5"+"의 연산 결과는 8입니다."); 3 + 5의 연산 결과는 8입니다.
            System.out.println(3 + 5); //8
            System.out.println("3" + 5); //35
        }
    } // System.out.println 실행 이후 자동 개행
}
