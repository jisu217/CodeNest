package practice01;

class SuperCLS {
    public SuperCLS() {
        System.out.println("I'm Super Class");
    }
}

class SubCLS extends SuperCLS {
    public SubCLS() {
        System.out.println("I'm Sub Class");
    }
}

class SuperSubCon {
    public static void main(String[] args) {
        new SubCLS();
    }
}

// I'm Super Class
// I'm Sub Class

