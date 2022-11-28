package java03.operator;

public class Op05_삼항연산자 {
	public static void main(String[] args) {
		int num = (int)(Math.random()*10)+1;
		
		System.out.println("내가 뭐라고 했더라???");
		System.out.println(num % 2 == 0 ? "짝" : "홀");
	}
}
