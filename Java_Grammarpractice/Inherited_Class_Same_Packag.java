package practice01;

public class Inherited_Class_Same_Packag {
    public class AAA {
        int num;
    } // AAA.java - 디폴트 패키지

    // extends AAA는 AAA 클래스의 상속을 의미함
    public class ZZZ extends AAA {
        public void init(int n) {
            num = n;    // 상속된 변수 num의 접근!
        }
    } // ZZZ.java - 디폴트 패키지: 패키지 선언이 되어 있지 않은 클래스들을 하나의 패키지로 묶기 위한 개념

package zoo; -> or animal

    class Duck {
        // 빈 클래스
    }

    public class Cat {
        public void makeCat() {
            Duck quack = new Duck();
        }
    } // Cat.java

package animal; // -> or zoo

    public class Dog {
        public void makeCat() {
            zoo.Cat yaong = new zoo.Cat();
        }

        public void makeDuck() {
            zoo.Duck quack = new zoo.Duck();
        }
    } // Dog.java
}
