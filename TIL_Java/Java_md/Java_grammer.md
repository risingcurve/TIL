# Java 기본 문법

## 패키지, 클래스, 메소드

Java로 'Hello, World!'라는 문구를 출력하기 위해서는 아래와 같이 코드를 입력해야 한다.

```
package ch01.sec09;

public class Hello {
    public static void main(String args[]) {
        System.out.println("Hello, World!");
    }
}
```

그럼 이 코드를 뜯어보며 살펴보자.

다음과 같은 코드를 패키지 선언어라고 부르며, 이는 소스 파일이 scr/ch01/sec09 패키지에 있다는 뜻이다. 컴파일 후 생성되는 바이트코드 파일도 bin/ch01/sec09 패키지에 생성된다.

```
package ch01.sec09;
```

public class Hello를 클래스 선언이라 부르며, Hello를 클래스명이라고 한다. 클래스명은 숫자로 시작할 수 없고, 공백을 포함해서는 안 된다. 그리고 소스 파일명과 대소문자가 완전히 일치해야 한다. 그 다음으로 나오는 중괄호 { ... }를 클래스 블록이라고 하며 여기에는 클래스의 정의 내용이 작성된다.

```
public class Hello {
    // (클래스 블록)
}
```

public static void main(String\[\] args) {...}를 main() 메소드라고 부른다. 그리고 중괄호 {...}를 main() 메소드 블록이라고 한다. 바이트코드 파일을 실행하면 이 main() 메소드 블록이 실행된다. 그래서 main() 메소드를 프로그램 실행 진입점이라고 부른다. 참고로 이클립스 이 main() 메소드를 간편하게 입력할 수 있는 단축키가 있는데, `main`이라 입력한 뒤 `ctrl + space`를 누르고 `enter`를 누르면(자동적으로 맨 위의 항목이 선택) main 함수를 간편하게 입력할 수 있다.

```
public static void main(String[] args) {
     // (메소드 블록)
}
```

마지막 줄은 괄호 안에 있는 내용을 Console 뷰에 출력하는 코드이다.

```
System.out.println("Hello, World!");
```

이클립스에는 이러한 출력문을 쉽게 입력할 수 있는 단축키가 있는데, \`sysout\`이라 입력한 뒤 \`ctrl + space\`를 누르고 enter를 누르면(자동적으로 맨 위의 항목이 선택) main 함수를 간편하게 입력할 수 있다.



## 주석

주석은 프로그램 실행과는 상관없이 코드에 설명을 붙인 것이다. 복잡한 코드일수록 주석을 달면 전체 코드를 이해하기 쉽다. 주석은 컴파일 과정에서 무시되기 때문에 주석을 많이 작성한다고 해서 바이트코드 파일의 크기가 커지는 것은 아니다.

Java에서 주석을 다는 방법은 아래와 같다.

```
// 내용 : 해당 기호가 있는 위치부터 그 줄 끝까지 주석처리
/* 내용 */ : 해당 범위의 내용 주석처리
/** 내용 */ : Documentations API를 위한 주석 처리
```

주석 기호는 코드 내 어디든 작성이 가능하지만, 문자열(" ") 내부에서 작성하면 안 된다. 문자열 내부에서 주석 기호는 주석문이 아니라 문자열 데이터로 인식하기 때문이다.

```
System.out.println("Hello, /* 주석이 될 수 없음 */ World!");
```

참고로 대부분의 IDE에서는 `ctrl + /`로 한 줄이든 여러 줄이든 주석을 달 수 있다.


이제는 주석을 코드에 적용해 보자.

```
package ch01.sec09;
/**
 * 아무 내용이나 들어가도 상관 없습니다.
*/
/*
 역시 아무 내용이나 들어가도 상관 없습니다.
*/
public class Hello {
    // 프로그램 실행 진입점
    public static void main(String args[]) {
        // 콘솔에 출력하는 실행문
        System.out.println("Hello, World!");
    }
}
```



## 실행문과 세미콜론

main() 메소드 블록 내부에는 다양한 실행문이 작성된다. System.out.println("Hello.World");은 ()안의 내용을 출력하는 실행문이다. 실행문은 변수 선언, 변수값 저장, 메소드 호출에 해당하는 코드를 말한다. 아래는 앞으로 배울 실행문이다.

```
int a;                          // 변수 a 선언
a = 2;                          // 변수 a에 2 값을 저장
int b = 4;                      // 변수 b를 선언하고 2 값을 저장
int result = a + b;             // 변수 result를 선언하고 변수 a와 b를 더한 값을 저장
System.out.println(result);     // 콘솔에 변수의 값을 출력한느 println() 메소드 호출
```

실행문 끝에는 반드시 세미콜론(;)을 붙여야 한다. 그렇지 않으면 컴파일 에러가 발생한다. 실행문을 여러 줄에 걸쳐서 작성하고 맨 마지막에 세미콜론을 붙여도 된다.

```
int result =
a + b;
```

또한 여러가지 실행문을 세미콜론으로 구분해서 한 줄로 작성할 수도 있다.

```
int a = 2; int b = 4;
```

그럼 실행문에 세미콜론을 붙이는 실습을 해보자.

```
package ch01.sec10;

public class Calculator {
    public static void main(String[] args) {
        int a = 2;
        int b = 4;
        int result = a + b;
        System.out.println(result);
    }
}

// 실행 결과 : 3
```

