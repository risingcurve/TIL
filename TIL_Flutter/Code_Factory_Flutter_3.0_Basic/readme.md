- 출력
  
  ```dart
  void main() {
    print('Hello, world!');
  }
  
  void main() {
    // variable
    var name = '코드팩토리';
    print(name);
  
    var name2 = '레드벨벳';
    print(name2);
  
    // 동일한 스코프 내에서 변수 중복 선언 불가
    // var name = '코드팩토리2';
    // print(name);
  }
  ```

- 정수
  
  ```dart
  void main() {
    // 정수
    // integer
    int number1 = 10;
    print(number1);
  
    int number2 = 15;
    print(number2);
  
    int number3 = -20;
    print(number3);
  
  }
  
  void main() {
    // 정수
    // integer
    int number1 = 2;
    int number2 = 4;
  
    print(number1 + number2);
    print(number1 - number2);
    print(number1 / number2);
    print(number1 * number2);
  }
  
  void main() {
    // 실수
    // double
    double number1 = 2.5;
    double number2 = 0.5;
  
    print(number1 + number2);
    print(number1 - number2);
    print(number1 / number2);
    print(number1 * number2);
  
  }
  ```

- Boolean
  
  ```dart
  void main() {
    // 맞다 / 틀리다
    // Boolean
    bool isTrue = true;
    bool isFalse = false;
  
    print(isTrue);
    print(isFalse);
  
  }
  ```

- String
  
  ```dart
  void main() {
    // 글자 타입
    // String
    String name = '레드벨벳';
    String name2 = '코드팩토리';
  
    print(name);
    print(name2);
  
    // var String
    // var는 타입을 할당된 값을 기반으로 추측
    var name3 = '블랙핑크';
    var number = 20;
  
    print(name3.runtimeType);
  
    Map<String, Map<int, List<double>>> testType = {};
    var testType = {};
  }
  ```

- String2
  
  ```
  void main() {
    // 글자 타입
    // String
  
    String name = '레드벨벳';
    String name2 = '슬기';
  
    print(name + name2);
    print(name + ' ' + name2);
  
    print('${name} ${name2}');
  
    print('$name $name2');
  
    print('$name.runtimeType $name2');
  
    print('${name.runtimeType} ${name2}');
  }
  ```

- dynamic
  
  ```dart
  void main() {
    dynamic name = '코드팩토리';
  ```

    print(name);
    
    dynamic number = 1;
    
    print(number);
    
    var name2 = '블랙핑크';
    
    
    print(name2);
    
    print(name.runtimeType);
    print(name2.runtimeType);
    
    name = 2;
    // dynamic은 변수 선언 이후 타입 변경 가능
    
    // name2 = 5;
    // var는 변수 선언 이후 타입 변경 불가

  }

```
- nullable

```dart
void main() {
  // nullable = null이 될 수 있다.
  // non-nullable = null이 될 수 없다.
  // null = 아무런 값도 있지 않다.

  String name = '코드팩토리';

  print(name);

  // name = null;
  // null이 들어갈 수 없는 스트링 타입

  String? name2 = '블랙핑크';
  // ?가 있으면 null 가능

  name2 = null;

  print(name2);
  // print(name2!);
  // null이 들어갈 수 있는 타입에 !가 붙으면 현재 이 값은 null이 아니다.


}
```

- final / const
  
  ```dart
  void main() {
  
    final String name = '코드팩토리';
  
    print(name);
  
    // name = '블랙핑크';
    // final로 변수 선언하면 변경 불가
  
    const String name2 = '블랙핑크';
  
    print(name2);
  
    // name2 = '코드팩토리';
    // const로 변수 선언하면 변경 불가
  
    // final,const는 var 기능 -> 타입 생략
  
  }
  ```

- Datetime
  
  ```dart
  void main() {
  
    final DateTime now = DateTime.now();
    // 버튼을 누르는 순간이 아니고 코드가 실행되는 순간을 보여줌.
    // 빌드 타임의 값을 알고 있지 않아도 됨.
  
    print(now);
  
    const DateTime now2 = DateTime.now();
    // 빌드타임의 값을 알고 있어야 함.
  }
  ```

- d
  
  ```dart
  void main() {
  
    int number = 2;
  
    print(number);
    print(number + 2);
    print(number - 2);
    print(number * 2);
    print(number / 2);
    print('---------------');
    print(number % 2);
    print(number);
  
    print('---------------');
  
    number ++;
    print(number);
  
    number --;
    print(number);
  }
  ```

- d
  
  ```dart
  void main() {
  
    double number = 4.0;
  
    print(number);
  
    number += 1;
  
    print(number);
  
    number -= 1;
  
    print(number);
  
    number *= 2;
  
    print(number);
  
    number /= 2;
  
    print(number);
  }
  ```

- operator
  
  ```dart
  void main() {
    // null
    double? number = 4.0;
  
    print(number);
  
    number = 2.0;
  
    print(number);
  
    number = null;
  
    print(number);
  
    number ??= 3.0;
    // number가 null이면 값을 할당해라.
  
    print(number);
  }
  ```

- operator 2
  
  ```dart
  void main() {
    int number1 = 1;
    int number2 = 2;
  
    print(number1 > number2);
    print(number1 < number2);
    print(number1 >= number2);
    print(number1 <= number2);
    print(number1 == number2);
    print(number1 != number2);
  }
  ```

- dd
  
  ```dart
  void main() {
    int number1 = 1;
  
    print(number1 is int);
    print(number1 is String);
  
    print(number1 is! int);
    print(number1 is! String);
  }
  ```

- dd
  
  ```dart
  void main() {
    // && - and 조건
    // || - or 조건
  
    bool result = 12 > 10 && 1 > 0;
  
    print(result);
  
    bool result2 = 12 > 10 && 0 > 1;
  
    print(result2);
  
    bool result3 = 12 > 10 || 1 > 0;
  
    print(result3);
  
    bool result4 = 12 > 10 || 0 > 1;
  
    print(result4);
  
    bool result5 = 12 < 10 || 0 > 1;
  
    print(result5);
  }
  ```

- dd
  
  ```dart
  void main() {
    // List
    // 리스트
  
    List<String> blackPink = ['제니', '지수', '로제', '리사'];
    List<int> numbers = [1, 2, 3, 4, 5];
  
    print(blackPink);
    print(numbers);
  
    // index
    // 순서
    // 0부터 시작
    print(blackPink[0]);
    print(blackPink[1]);
    print(blackPink[2]);
    print(blackPink[3]);
    print(blackPink[4]);
  }
  ```

- dd
  
  ```dart
  void main() {
    // List
    // 리스트
  
    List<String> blackPink = ['제니', '지수', '로제', '리사'];
  
    print(blackPink.length);
  
    blackPink.add('코드팩토리');
  
    print(blackPink);
  
    blackPink.remove('코드팩토리');
  
    print(blackPink);
  
    print(blackPink.indexOf('로제'));
  ```

  }

```
- map

```dart
void main() {
  // Map
  // Key / Value

  Map<String, String> dictionary = {
    'Harry Potter': '해리포터',
    'Ron Weasley': '론 위즐리',
    'Hermione Granger': '헤르미온느 그레인저',
  };

  print(dictionary);

  Map<String, bool> isHarryPotter = {
    'Harry Potter': true,
    'Ron Weasley': true,
    'Ironman': false,
  };

  print(isHarryPotter);

  isHarryPotter.addAll({
    'Spiderman': false,
  });

  print(isHarryPotter);

  print(isHarryPotter['Ironman']);

  isHarryPotter['Hulk'] = false;

  print(isHarryPotter);

  isHarryPotter['Spiderman'] = true;

  print(isHarryPotter);
}

void main() {
  // Map
  // Key / Value


  Map<String, bool> isHarryPotter = {
    'Harry Potter': true,
    'Ron Weasley': true,
    'Ironman': false,
  };

  print(isHarryPotter);

  isHarryPotter.remove('Harry Potter');

  print(isHarryPotter);

  print(isHarryPotter.keys);
  print(isHarryPotter.values);
}
```

- set
  
  ```dart
  void main() {
    // Set
    // List와 달리 중복 불가 -> 자동 중복 처리
  
    final Set<String> names = {
      'Code Factory',
      'Flutter',
      'Black Pink',
  
    };
  
    print(names);
  
    names.add('Jenny');
  
    print(names);
  
    names.remove('Jenny');
  
    print(names);
  
    print(names.contains('Flutter'));
  }
  ```

- if
  
  ```dart
  void main() {
    // if 문
    // 조건이 false가 되면 실행이 안 됨.
  
    int number = 2;
  
    if(number % 2 == 0){
      print('값이 짝수입니다.');
    }
  
    int number1 = 3;
  
    if(number1 % 2 == 0){
      print('값이 짝수입니다.');
    } else {
      print('값이 홀수입니다.');
    }
  
    int number2 = 5;
  
    if(number2 % 3 == 0){
      print('나머지가 0입니다.');
    } else if(number2 % 3 == 1) {
      print('나머지가 1입니다.');
    } else {
      print('나머지가 2입니다.');
    }
    // 조건에 맞으면 아래 조건 계산은 생략
  }
  ```

- switch
  
  ```dart
  void main() {
    // switch 문
  
    int number = 3;
  
    switch(number % 3){
      case 0:
        print('나머지가 0입니다.');
        break;
  
      case 1:
        print('나머지가 1입니다.');
        break;
  
      default:
        print('나머지가 2입니다.');
        break;
    }
  }
  ```

- for loop
  
  ```dart
  void main() {
    // for loop
  
    for(int i = 0; i < 10; i++){
      print(i);
    }
  
    int total = 0;
  
    List<int> numbers = [1, 2, 3, 4, 5, 6];
  
    for(int i = 0; i < numbers.length; i++) {
      total += numbers[i];
    }
  
    print(total);
  
    total = 0;
  
    for(int number in numbers){
      total += number;
    }
  
    print(total);
  
  }
  ```

- while loop
  
  ```dart
  void main() {
    // while loop
  
    int total = 0;
  
    while(total < -1) {
      total += 1;
    }
  
    print(total);
  
    do {
      total += 1;
    } while(total < 10);
  
    print(total);
  }
  
  void main() {
    // while loop
  
    int total = 0;
  
    while(total < 10){
      total += 1;
  
      if(total == 5){
        break;
      }
    }
  
    print(total);
  
    for(int i = 0; i < 10; i++){
      total += 1;
      if(total == 5){
        break;
      }
    }
  
    print(total);
  }
  
  void main() {
    // while loop
  
    for(int i = 0; i < 10; i++){
      if(i == 5){
        continue;
      }  
      print(i);
    }
  }
  ```
