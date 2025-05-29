public class Ex07_ShortCircuitEvaluation
{
    public static void main(String[] args)
    {
        int x = 0;
        int y = 0;
        boolean result;

        result = ((x = x + 1) < 0) && ((y = y + 1) > 0);

        System.out.println("result = " + result); // result = false
        System.out.println("x = " + x); // x = 1
        System.out.println("y = " + y + '\n'); // y = 0, && (AND) 연산자는 첫 번째 조건이 false이면 두 번째 조건을 평가하지 않으므로

        result = ((x = x + 1) > 0) || ((y = y + 1) > 0);

        System.out.println("result = " + result); // result = true
        System.out.println("x = " + x); // x = 2
        System.out.println("y = " + y); // y = 0, || (OR) 연산자는 첫 번째 조건이 true이면 두 번째 조건을 평가하지 않으므로
    }
}
