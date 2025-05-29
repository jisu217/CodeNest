package practice01;

public class Overloading_keyword_this {
    class Person {
        private int regiNum;    // 주민등록 번호
        private int passNum;    // 여권 번호

        Person(int rnum, int pnum) {
            regiNum = rnum;
            passNum = pnum;
        }

        Person(int rnum) {
            regiNum = rnum;
            passNum = 0;
        }

        void showPersonalInfo() {...}
    }

    public static void main(String[] args) {
        // 여권 있는 사람의 정보를 담은 인스턴스 생성
        Person jung = new Person(335577, 112233);

        // 여권 없는 사람의 정보를 담은 인스턴스 생성
        Person hong = new Person(775544);

        jung.showPersonalInfo();
        hong.showPersonalInfo();
    }

    class Person {
        private int regiNum;    // 주민등록 번호
        private int passNum;    // 여권 번호

        Person(int rnum, int pnum) {
            regiNum = rnum;
            passNum = pnum;
        }

        // Person(int rnum) {
        //    regiNum = rnum;
        //    passNum = 0;
        //  } 키워드 this를 이용한 다른 생성자의 호출 / rnum과 0을 인자로 받는 오버로딩 된 다른 생성자 호출, 중복된 코드를 줄이는 효과

        Person(int rnum) {
            this(rnum, 0);
        }

        void showPersonalInfo() {...}
    }

    Person(int rnum) {
        this(rnum, 0);
    }
}
