package practice01;

public class SCE_motion {
    class Aritop {
        public static void main(String[] args) {
            int num1 = 7;
            int num2 = 3;
            boolean result;

            result = ((num1 += 10) < 0) && ((num2 += 10) > 0);
            System.out.println("result = " + result);
            System.out.println("num1 = " + num1);
            System.out.println("num2 = " + num2 + '\n');

            result = ((num1 += 10) > 0) || ((num2 += 10) > 0);
            System.out.println("result = " + result);
            System.out.println("num1 = " + num1);
            System.out.println("num2 = " + num2);
        }
    }
}
