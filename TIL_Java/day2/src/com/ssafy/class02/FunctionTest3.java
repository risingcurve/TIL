package com.ssafy.class02;

public class FunctionTest3 {
	public static void main(String[] args) {
		System.out.println("아침에 일어난다.");
		move("교육장", "대중교통");
		education();
		move("집", "대중교통");

		
		System.out.println("과제를 해결한다.");
		System.out.println("잔다.");
		
		System.out.println("============================");
		
		System.out.println("아침에 일어난다.");
		System.out.println("아침밥을 먹는다.");
		
		move("교육장", "대중교통");
		education();
		move("집", "대중교통");
		
		System.out.println("과제를 해결한다.");
		System.out.println("잔다.");

	}
	
	public static void education() {
		System.out.println("오전 수업을 듣는다.");
		System.out.println("점심을 먹는다.");
		System.out.println("오후 수업을 듣는다.");	}
	
	public static void move() {
		System.out.println(place+"(으)로" + transportation +"을(를) 이용하여 이동한다.");
	}
}
