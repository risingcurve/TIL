# Java 기본 문법

## 패키지, 클래스, 메소드

Java로 'Hello, World!'라는 문구를 출력하기 위해서는 아래와 같이 코드를 입력해야 한다.

```java
package ch01.sec09;

public class Hello {
    public static void main(String args[]) {
        System.out.println("Hello, World!");
    }
}
```

그럼 이 코드를 뜯어보며 살펴보자.

다음과 같은 코드를 패키지 선언어라고 부르며, 이는 소스 파일이 scr/ch01/sec09 패키지에 있다는 뜻이다. 컴파일 후 생성되는 바이트코드 파일도 bin/ch01/sec09 패키지에 생성된다.

```java
package ch01.sec09;
```

public class Hello를 클래스 선언이라 부르며, Hello를 클래스명이라고 한다. 클래스명은 숫자로 시작할 수 없고, 공백을 포함해서는 안 된다. 그리고 소스 파일명과 대소문자가 완전히 일치해야 한다. 그 다음으로 나오는 중괄호 { ... }를 클래스 블록이라고 하며 여기에는 클래스의 정의 내용이 작성된다.

```java
public class Hello {
    // (클래스 블록)
}
```

public static void main(String\[\] args) {...}를 main() 메소드라고 부른다. 그리고 중괄호 {...}를 main() 메소드 블록이라고 한다. 바이트코드 파일을 실행하면 이 main() 메소드 블록이 실행된다. 그래서 main() 메소드를 프로그램 실행 진입점이라고 부른다. 참고로 이클립스 이 main() 메소드를 간편하게 입력할 수 있는 단축키가 있는데, `main`이라 입력한 뒤 `ctrl + space`를 누르고 `enter`를 누르면(자동적으로 맨 위의 항목이 선택) main 함수를 간편하게 입력할 수 있다.

```java
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

```java
// 내용 : 해당 기호가 있는 위치부터 그 줄 끝까지 주석처리
/* 내용 */ : 해당 범위의 내용 주석처리
/** 내용 */ : Documentations API를 위한 주석 처리
```

주석 기호는 코드 내 어디든 작성이 가능하지만, 문자열(" ") 내부에서 작성하면 안 된다. 문자열 내부에서 주석 기호는 주석문이 아니라 문자열 데이터로 인식하기 때문이다.

```java
System.out.println("Hello, /* 주석이 될 수 없음 */ World!");
```

참고로 대부분의 IDE에서는 `ctrl + /`로 한 줄이든 여러 줄이든 주석을 달 수 있다.

이제는 주석을 코드에 적용해 보자.

```java
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

```java
int a;                          // 변수 a 선언
a = 2;                          // 변수 a에 2 값을 저장
int b = 4;                      // 변수 b를 선언하고 2 값을 저장
int result = a + b;             // 변수 result를 선언하고 변수 a와 b를 더한 값을 저장
System.out.println(result);     // 콘솔에 변수의 값을 출력한느 println() 메소드 호출
```

실행문 끝에는 반드시 세미콜론(;)을 붙여야 한다. 그렇지 않으면 컴파일 에러가 발생한다. 실행문을 여러 줄에 걸쳐서 작성하고 맨 마지막에 세미콜론을 붙여도 된다.

```java
int result =
a + b;
```

또한 여러가지 실행문을 세미콜론으로 구분해서 한 줄로 작성할 수도 있다.

```java
int a = 2; int b = 4;
```

그럼 실행문에 세미콜론을 붙이는 실습을 해보자.

```java
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

### 

### 변수

---

컴퓨터 메모리(RAM)는 수많은 번지들로 구성된 데이터 저장 공간이다. 프로그램은 데이터를 메모리에 저장하고 읽는 작업을 지속적으로 수행한다. 이때 데이터를 어디에, 어떤 방식으로 저장할지 정해져 있지 않다면 메모리 관리가 매우 어려워질 것이다. Java는 이러한 문제를 해결하기 위해 변수를 사용한다.

변수는 데이터를 저장할 메모리의 위치를 나타내는 이름이다. 즉 하나의 값을 저장할 수 있는 메모리 번지에 붙여진 이름이다. 변수를 통해 프로그램은 메모리 번지에 값을 저장하고 읽을 수 있다. 메모리 상에 데이터를 보관할 수 있는 공간을 확보해야 하는데, 적절한 공간을 확보하기 위해서 변수의 타입이 등장한다.

자바는 정수와 실수만 변수로 저장할 수 있다. 이는 정수형 변수에 정수값을 저장하고, 실수형 변수에 실수값을 저장하는 양상으로 나타난다.

변수를 사용하려면 변수 선언이 필요한데, 변수 선언은 어떤 타입의 데이터를 어떻게 저정할 것인지 그리고 변수 이름이 무엇인지를 결정하는 것이다.

```java
int age;            // 정수(int) 값을 저장할 수 있는 age 변수 선언
double value;       // 실수(double) 값을 저장할 수 있는 value 변수 선언
```

변수 이름은 첫 번째 글자가 문자여야 하고, 중간부터는 문자, 숫자, $, _를 포함할 수 있다. 다만 변수가 합성어일 경우 camelCase(ex. computerScore)로 작성하는 것이 좋다. 한글을 이용한 변수도 작명이 가능하나, 권장하는 바는 아니다.

변수가 선언되었다면 값을 저장할 수 있는데, 대입연산자인 `=`를 사용한다. 우측 값을 좌측 변수에 대입한다고 이해하면 될 것이다.

```java
int score;      // 변수 선언
score = 90;     // 값 대입
```

변수 선언은 저장되는 값의 타입과 이름만 결정한 것이지, 아직 메모리에 할당된 것은 아니다. 변수에 최초로 값이 대입될 때 메모리에 할당되고, 해당 메모리에 값이 저장된다.

변수에 최초로 대입하는 행위를 변수 초기화라고 하고, 이때의 값을 초기값이라고 한다. 초기값은 다음과 같이 변수를 선언함과 동시에 대입할 수도 있다.

초기화되지 않은 변수는 아직 메모리에 할당되지 않았기 때문에 변수를 통해 메모리 값을 읽을 수 없다. 초기화되지 않은 변수를 연산식에 사용할 경우 컴파일 에러가 발생한다. 따라서 다음은 잘못된 코딩이다.

```java
int value;
int result = value + 20;
```

`int value`에서 변수가 선언되었지만, 초기화되지 않았기 때문에 `value + 10`에서 value 변수값은 읽어올 수 없다. 따라서 위 코드는 다음과 같이 변경해야 한다.

```java
int value = 40;
int result = value + 20;
```

변수는 출력문이나 연산식에 사용되어 변수값을 활용한다. 다음 코드는 변수를 문자열과 결합 후 출력하거나 연산식에서 활용하는 모습을 보여준다.

```java
package ch02.sec01;

public class VariableUseExample {
    public static void main(String[] args) {
        int hour = 3;
        int minute = 5;
        System.out.println(hour + "시간" + minute + "분");

        int totalMinute = (hour*60) + minute;
        System.out.println("총" + totalMinute + "분");
    }
}

// 실행 결과
// 3시간 5분
// 총 185분
```

그리고 변수는 또 다른 변수에 대입되어 메모리 간에 값을 복사할 수 있다. 다음 코드를 보자.

```java
int x = 30;     // 변수 x에 30을 대입
int y = x;      // 변수 y에 변수 x 값을 대입
```

다음 코드는 두 변수의 값을 교환하는 방법을 보여준다. 두 변수의 값을 교환하기 위해서 새로운 변수를 선언하였다.

```java
package ch02.sec01;

public class VariableExchangeExample {
    public static void main(String[] args) {
        int x = 3;
        int y = 5;
        System.out.println("x:" + x + ", y:" + y);

        int z = x;
        x = y;
        y = z;
        System.out.println("x:" + x + ", y:" + y);
    }
}

// 실행 결과
// x:3, y:5
// x:5, y:3
```

### 자료형 : 숫자 타입

변수는 선언될 때의 타입에 따라 저장할 수 있는 값의 종류와 허용 범위가 달라진다. 자바는 정수, 실수, 논리값을 저장할 수 있는 기본 타입 8개를 다음과 같이 제공한다.

| 타입  | 세부타입 | 데이터형    | 크기    |
| --- | ---- | ------- | ----- |
| 논리형 |      | boolean |       |
| 문자형 |      | char    | 2byte |
| 숫자형 | 정수형  | byte    | 1byte |
| 숫자형 | 정수형  | short   | 2byte |
| 숫자형 | 정수형  | int     | 4byte |
| 숫자형 | 정수형  | long    | 8byte |
| 숫자형 | 실수형  | float   | 4byte |
| 숫자형 | 실수형  | double  | 8byte |

자료형의 크기를 비교하면 다음과 같다.

```
byte < short < int < long < float < double
 char < int < long < float < double
```

코드에서 프로그래머가 직접 입력한 값을 리터럴이라고 하는데, 변수에 대입할 정수 리터럴은 진수에 따라 작성하는 방법이 다르다.

- 2진수 : 0b 또는 0B로 시작하고 0과 1로 작성
  
  ```java
  int a = 0b1011;
  int b = 0B10110;
  ```

- 8진수 : 0으로 시작하고 0~7 숫자로 작성
  
  ```java
  int a = 013;
  int b = 0206;
  ```

- 10진수 : 소수점이 없는 0~9 숫자로 작성
  
  ```java
  int a = 13;
  int b = 589;
  ```

- 16진수 : 0x 또는 0X로 시작하고 0~9 숫자나 A, B, C, D, E, F 또는 a, b, c, d, e, f로 작성
  
  ```java
  int a = 0xB3;
  int b = 0x2A0F;
  ```

다음 코드는 다양한 정수 리터럴을 int 타입 변수에 대입하고 10진수로 출력한다.

```java
package ch02.sec02

public class IntegerLiteralExample {
    public static void main(String[] args) {
        int var1 = 0b1011;
        int var2 = 0206;
        int var3 = 365;
        int var4 = 0xB3;

        System.out.println("var1: " + var1);
        System.out.println("var2: " + var2);
        System.out.println("var3: " + var3);
        System.out.println("var4: " + var4);
    }
}


// 실행 결과
// var1: 11
// var2: 134
// var3: 365
// var4: 179
```

### 자료형 : 숫자 타입

### 

### 자동 타입 변환

자동 타입 변환은 말 그대로 자동으로 타입 변환이 일어나는 것을 말한다. 자동 타입 변환은 값의 허용 범위가 작은 타입이 허용 범위가 큰 타입으로 대입될 때 발생한다.
