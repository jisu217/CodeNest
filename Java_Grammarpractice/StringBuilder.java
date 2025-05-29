package practice01;

public class StringBuilder {
    public static void main(String[] args) {
        // 문자열 "123"이 저장된 인스턴스의 생성
        StringBuilder stbuf = new StringBuilder("123");

        stbuf.append(45678);   // 문자열 덧붙이기 12345678
        System.out.println(stbuf.toString());

        stbuf.delete(0, 2);    // 문자열 일부 삭제 345678
        System.out.println(stbuf.toString());

        stbuf.replace(0, 3, "AB");    // 문자열 일부 교체 AB678
        System.out.println(stbuf.toString());

        stbuf.reverse();    // 문자열 내용 뒤집기 8765BA
        System.out.println(stbuf.toString());

        String sub = stbuf.substring(2, 4);  // 일부만 문자열로 반환 6B
        System.out.println(sub);
    }
}
