package practice01;

public class Method_Overriding {
    class Cake {
        public void yummy() {
            System.out.println("Yummy Cake");
        }
    }

    class CheeseCake extends Cake {
        public void yummy() { // Cake의 yummy를 오버라이딩
            System.out.println("Yummy Cheese Cake");
        }
    }

    class StrawberryCheeseCake extends CheeseCake {
        public void yummy() { // 그리고 CheeseCake의 yummy를 오버라이딩
            System.out.println("Yummy Strawberry Cheese Cake");
        }
    }

    public static void main(String[] args) {
        Cake c1 = new StrawberryCheeseCake();
        CheeseCake c2 = new StrawberryCheeseCake();
        StrawberryCheeseCake c3 = new StrawberryCheeseCake();

        c1.yummy(); // Yummy Strawberry Cheese Cake
        c2.yummy(); // Yummy Strawberry Cheese Cake
        c3.yummy(); // Yummy Strawberry Cheese Cake
    }
}
