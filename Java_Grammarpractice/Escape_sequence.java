package practice01;

public class Escape_sequence {
    class EscapeSequences{
        public static void main(String[] args) {
            System.out.println("AB" + '\b' + 'c'); // AC
            System.out.println("AB" + '\t' + 'c'); // AB    C
            System.out.println("AB" + '\n' + 'c'); // AB
            // C
            System.out.println("AB" + '\r' + 'c'); // CB
        }
    }
}
