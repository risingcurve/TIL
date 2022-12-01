package com.ssafy.inheritance02;

public class Student extends Person {
    String major;

    public Student() {
        super("양", 45); // 부모의 기본 생성자를 호출할 거야.
//        System.out.println("나는 Student의 기본 생성자야.");
    }

    public void study() {
        super.eat();
        System.out.println("공부를 한다.");

    }

    // 메서드 오버라이딩
    public void eat(String food) {
        System.out.println("지식을 먹는다.");
    }

    @Override
    public String toString() {
//        return super.name + "이고, " + major + "전공입니다.";
        return super.toString() + "이고, " + major + "전공입니다.";
    }

    @Override
    public boolean equals(Object obj) {
        // TODO Auto-generated method stub
        return super.equals(obj);
    }
}
