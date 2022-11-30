package com.ssafy.modifier01;

public class CarTest {
    public static void main(String[] args) {
        // 자동차 하나 생성.
        Car c = new Car();
        // 이런 식으로 작성 가능.
        c.color = "Red";
//        c.speed = 100;

//        c.speed = 300; // 이렇게 작성한 것을 막을 수 있나? 없음.
//        System.out.println(c.speed);

        c.setSpeed(100);
        System.out.println(c.getSpeed());
    }
}
