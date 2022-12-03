package com.sssafy.abstractclass4;

public class ChefTest {
	// 추상 메서드를 활용하면 좋은 점은?
	// 부모가 구현하고 싶은 내용이 없다고 해서, 구현 자체를 빼버리면
	// 동적 바인팅에 의해 자식이 오버라이딩 된 함수가 실행되는 기회를 없애개 된다.
	// 빈 깡통만 만들어 놓으면 자식이 구현하든 말든 신경 안 씀.
	// abstract로 만들어 놓으면 자식 클래스는 해당 클래스를 무조건 구현해야 하는 의무를 가진다.
	
	
	
	public static void main(String[] args) {
		Chef c = new KFoodChef();
		c.cook();
		
		
		// 추상클래스는 미온성이 설계도이니까, 인스턴스를 생성할 수 없음.
		// 미완성되노 부분을 만들어주면 된다.
		// 익명클래스 문법으로 1회 한정으로 구현하고 인스턴스를 만들 수 있게 해 준다.
		Chef c2 = new Chef() {
			@Override
			public void cook() {
				System.out.println("오리한다.");
			}
		};
		
		c2.cook();
	}
}
