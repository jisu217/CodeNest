package practice01;

public class break {
    public class Main {
        public static void main(String[] args) {
            int num = 1;
            boolean search = false;  // 변수를 명시적으로 초기화하여 조건을 만족하는 숫자를 찾지 못했음을 명확히 나타내기 위함

            while(num < 100) {
                if(((num % 5) == 0) && ((num % 7) == 0)) {
                    search = true;  // 조건을 만족하는 숫자를 찾으면 search를 true로 설정
                    break;  // 루프 종료이자 while문 탈출
                } 
                
            num++;    
            }
            
            if(search)
                System.out.println("찾는 정수: " + num);
            else
                System.out.println("조건을 만족하는 숫자를 찾지 못했습니다.");
        }
    }
}
