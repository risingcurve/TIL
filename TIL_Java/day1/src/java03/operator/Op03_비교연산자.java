package java03.operator;

public class Op03_비교연산자 {
	public static void main(String[] args) {
		int a = 10;
		
		System.out.println(a > 10);
		System.out.println(a != 10);
		System.out.println(a >= 10);
		
		System.out.println(a == 10);
		System.out.println(a != 10);
		
		String c = "Hi";
		String d = "Hi";
		String e = new String("Hi");

		System.out.println(c == d);
		System.out.println(c == e);
		System.out.println(c.equals(e));
	}
}
