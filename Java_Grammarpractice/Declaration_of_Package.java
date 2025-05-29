package practice01;

public class Declaration_of_Package {
    package com.wxfx.smart;
    public class Circle {
        double rad;
        final double PI;

        public Circle(double r) { . . . }
        public double getArea() { . . . }
    } www.wxfx.com의 Circle.java

package com.fxmx.simple;
    public class Circle {
        double rad;
        final double PI;

        public Circle(double r) { . . . }
        public double getPerimeter() { . . . }
    } www.fxmx.com의 Circle.java

    com.wxfx.smart.Circle c1 = new com.wxfx.smart.Circle(3.5);
    com.fxmx.simple.Circle c2 = new com.fxmx.simple.Circle(5.5);
}

// 패키지 이름은 모두 소문자로 구성
// 인터넷 도메인 이름의 역순으로 이름 구성
// 이름 끝에 클래스를 정의한 주체 또는 팀의 이름 추가
