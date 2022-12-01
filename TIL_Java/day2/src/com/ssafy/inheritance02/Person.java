package com.ssafy.inheritance02;

public final class Person {
    String name;
    int age;

    public Person() {
//        System.out.println("나는 Person의 기본 생성자야.");
    }

    public Person(String name, int age) {
        super();
        this.name = name;
        this.age = age;
    }

    public final void eat() {
        System.out.println("음식을 먹는다.");
    }

    private void eat(String food) {
        System.out.println(food+"냠냠");
    }

    @Override
    public String toString() {
        return "Person [name=" + name + "";
    }
}
