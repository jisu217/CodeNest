package practice01;

public class Reference_variable {
    class Cake {
        public void sweet() {...}
    }

    class CheeseCake extends Cake {
        public void milky() {...}
    }

    CheeseCake ca1 = new CheeseCake();
    Cake ca2 = ca1;    // 가능!

    Cake ca3 = new CheeseCake();
    CheeseCake ca4 = ca3;     // 불가능!
                              // 이 시점에 컴파일러 및 가상머신은 ca3가 참조하는 대상을 Cake 인스턴스로 판단, ca3가 참조하는 인스턴스의 정확한 클래스 정보는 유지 X

}
