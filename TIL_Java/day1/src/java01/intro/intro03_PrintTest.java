package java01.intro;

public class intro03_PrintTest {
	public static void main(String[] args) {
		// 한 줄 출력을 해보자.
		System.out.println("Hello world\n");
		// \n을 사용하면 줄이 바뀐다.
		// println을 써보자.
		System.out.println("Hello world!!!");
		System.out.println("Hello world!!!");
		
		System.out.println("\\");
		System.out.println("\"");
		
		System.out.printf("%d \n", 10); // 정수(10진수)
		System.out.printf("%o \n", 10); // 정수 (8진수)
		System.out.printf("%X \n", 10); // 정수 (16진수)
		System.out.printf("%x \n", 10); // 정수 (16진수)

		System.out.printf("%4d\n", 10); // 4칸을 확보한 뒤 오른쪽부터 차지
		System.out.printf("%-4d\n", 10); // 4칸을 확보한 뒤 왼쪽부터 차지
		System.out.printf("%04d\n", 10); // 4칸을 확보한 뒤 오른쪽부터 차지(빈칸에 0을 채운다.)
		
		System.out.printf("%f\n", 10.1); // 실수
		System.out.printf("%.2f\n", 10.1); // 실수(소수점 둘째자리까지)
		
		System.out.printf("%s\n", "양명균"); // 실수(소수점 둘째자리까지)
		System.out.printf("%c\n", 'o'); // 실수(소수점 둘째자리까지)
		
		System.out.printf("안녕하세요. 저는 %s입니다. 제 혈액형은 %c 일걸요?","양명균", 'O');
		
	}
}
