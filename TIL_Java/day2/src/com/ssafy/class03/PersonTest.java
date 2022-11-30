package com.ssafy.class03;

public class PersonTest {
	public static void main(String[] args) {
		Person p1 = new Person();

		p1.name = "Yang";
		p1.age = 45;
		p1.hobby = "Youtube";

		Person p2 = new Person();

		p2.name = "Hong";
		p2.age = 25;
		p2.hobby = "Golf";
		
		// 클래스 변수인 personCount를 한 번 보고 싶어
		System.out.println(Person.personCount);
		System.out.println(p1.personCount++ );

		System.out.println(p2.personCount);
		System.out.println(Person.personCount);

		Person p = new Person();
		p.study((byte) 10);			// O
		p.study((short) 10);		// O	
		p.study(10);				// O
		p.study(10L);				// O (메소드 오버라이딩 해서 가능함)
		// p.study(10.0f);			// X
		// p.study(10.0);			// X
		// p.study(10, 10);			// X 정의한 것 이이에 쓸 수 없음
		// 위의 것들을 가능하게 하려면 메소드 오버라이딩 필요.

	}



	void test() {

	}

}