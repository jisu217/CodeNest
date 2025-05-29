package practice01;

public class toString {
    class Box {
        private String conts;

        Box(String cont) {
            this.conts = cont;
        }
        public String toString() {
            return conts; // 문자열 반환
        }
    }

    public static void main(String[] args) {

        StringBuilder stb = new StringBuilder("12");
        stb.append(34);
        System.out.println(stb.toString()); //1234
        System.out.println(stb); //1234

        Box box = new Box("Camera");
        System.out.println(box.toString()); //Camera
        System.out.println(box); //Camera
    }
}
