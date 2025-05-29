package practice01;

public class super {
    class Cake {
        public void yummy() {
            System.out.println("Yummy Cake");
        }
    }

    class CheeseCake extends Cake {
        public void yummy() {
            super.yummy(); // 부모 클래스(Cake)의 yummy() 메서드를 호출
            System.out.println("Yummy Cheese Cake");
        }

        public void tasty() {
            super.yummy(); // 부모 클래스(Cake)의 yummy() 메서드를 호출
            System.out.println("Yummy Tasty Cake");
        }
    }

    public class Main {
        public static void main(String[] args) {
            CheeseCake cheesecake = new CheeseCake();
            cheesecake.yummy(); // CheeseCake 클래스의 yummy() 메서드를 호출
            cheesecake.tasty(); // CheeseCake 클래스의 tasty() 메서드를 호출
        }
    }
}

// Yummy Cake
// Yummy Cheese Cake
// Yummy Cake
// Yummy Tasty Cake
