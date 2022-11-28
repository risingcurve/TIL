package java03.operator;

public class Op04_논리연산자 {
	public static void main(String[] args) {
		int a = 10;
		int b = 20;
		
		System.out.println(a > 5 && b > 5); // 참
		System.out.println(a > 5 && b < 5); // 거짓
		System.out.println(a < 5 && b > 5); // 거짓
		System.out.println(a < 5 && b < 5); // 거짓
		
		System.out.println(a > 5 || b > 5); // 참
		System.out.println(a > 5 || b < 5); // 참
		System.out.println(a < 5 || b > 5); // 참
		System.out.println(a < 5 || b < 5); // 거짓
		
		System.out.println(!(a > 5 || b > 5)); // 뒤집기
	}
}
