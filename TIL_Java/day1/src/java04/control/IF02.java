package java04.control;

public class IF02 {
	public static void main(String[] args) {
		// if(조건식) {} else {} 조건식이 참일 경우 if 블록 내부 수행 / 거짓이면 else 블록 수행
	
		int age = 17;
		
		if(age < 20) {
			System.out.println("You have to drink beverage.");
		} else {
			System.out.println("You can drink beer.");
		}
		
		int num;
		if(age < 20) {
			num = 10;
		} else {
			num = 20;
		}
		
		System.out.println(num);
	}
}
