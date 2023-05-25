## 비동기 프로그래밍의 이해

```dart
void main() {
  addNumbers(1, 1);
  addNumbers(2, 2);
}

// 계산중, 계산 완료의 순서가 뒤바뀔 일은 없음.

void addNumbers(int number1, int number2) {
  print('계산중: $number1 + $number2');

  print('계산 완료: ${number1 + number2}');
}
```

## Future

```dart
void main() {
  // Future - 미래
  // 미래에 받아올 값

  Future<String> name = Future.value('코드팩토리');
  Future<int> number = Future.value(1);
  Future<bool> isTrue = Future.value(true);

  addNumbers(1, 1);
  addNumbers(2, 2);

  // print('함수 시작');

  // 2개의 파라미터
  // delayed - 지연되다.
  // 1번 파라미터 - 지연할 기간(얼마나 지연할 건지) Duration
  // 2번 파라미터 - 지연 시간이 지난 후 실행할 함수.
//   Future.delayed(Duration(seconds: 2), (){
//     print('Delay 끝');
//   });
}

void addNumbers(int number1 , int number2) {
  print('계산 시작 : $number1 + $number2');

  // 서버 시뮬레이션
  Future.delayed(Duration(seconds: 2), (){
    print('계산 완료: $number1 + $number2 = ${number2}');
  });

  print('함수 완료 : $number1 + $number2');
}
```

## Future 2

```dart
void main() async {
  // Future - 미래
  // 미래에 받아올 값

  Future<String> name = Future.value('코드팩토리');
  Future<int> number = Future.value(1);
  Future<bool> isTrue = Future.value(true);

  await addNumbers(1, 1);
  await addNumbers(2, 2);


}
// await를 쓰려면 async를 써야 함
// await로 기다리는 동안 다른 작업을 할 수 있음.
// await는 Future를 리턴하는 함수만 가능.
Future<void> addNumbers(int number1 , int number2) async {
  print('계산 시작 : $number1 + $number2');

  // 서버 시뮬레이션
  await Future.delayed(Duration(seconds: 2), (){
    print('계산 완료: $number1 + $number2 = ${number2}');
  });

  print('함수 완료 : $number1 + $number2');
}
```

## Future 3

```dart
void main() async {
  // Future - 미래
  // 미래에 받아올 값

  Future<String> name = Future.value('코드팩토리');
  Future<int> number = Future.value(1);
  Future<bool> isTrue = Future.value(true);

  final result1 = await addNumbers(1, 1);
  final result2 = await addNumbers(2, 2);

  print('result1: $result1');
  print('result2: $result2');
  print('result1 + result2 = ${result1 + result2}');

}
// await를 쓰려면 async를 써야 함
// await로 기다리는 동안 다른 작업을 할 수 있음.
// await는 Future를 리턴하는 함수만 가능.
Future<int> addNumbers(int number1 , int number2) async {
  print('계산 시작 : $number1 + $number2');

  // 서버 시뮬레이션
  await Future.delayed(Duration(seconds: 2), (){
    print('계산 완료: $number1 + $number2 = ${number2}');
  });

  print('함수 완료 : $number1 + $number2');

  return number1 + number2;
}
```

## Stream

```dart
import 'dart:async';

void main() {
  final controller = StreamController();
  final stream = controller.stream.asBroadcastStream();

  final streamListener1 = stream.listen((val){
    print('Listener 1 : $val');
  });

  final streamListener2 = stream.listen((val){
    print('Listener 2 : $val');
  });

  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);
  controller.sink.add(4);
  controller.sink.add(5);
}
```

## Stream 2

```dart
import 'dart:async';

void main() {
  final controller = StreamController();
  // 여러번 리스닝하려면 asBroadcastStream
  final stream = controller.stream.asBroadcastStream();


  final streamListener1 = stream.where((val) => val % 2 == 0).listen((val){
    print('Listener 1 : $val');
  });

  final streamListener2 = stream.where((val) => val % 2 == 1).listen((val){
    print('Listener 1 : $val');
  });



  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);
  controller.sink.add(4);
  controller.sink.add(5);
}
```

## Stream 3(함수로 Stream 제공)

```dart
import 'dart:async';

void main() {
  calculate(2).listen((val){
    print('calculate(2) : $val');
  });
  calculate(4).listen((val){
    print('calculate(4) : $val');
  });
}

Stream<int> calculate(int number) async* {
  for(int i = 0; i < 5; i++) {
    yield i * number;

    await Future.delayed(Duration(seconds: 1));
  }

}
```

## Stream 4

```dart
import 'dart:async';

void main() {
  playAllStream().listen((val){
    print(val);
  });
}

Stream<int> playAllStream() async* {
  yield* calculate(1);
  yield* calculate(1000);
}

Stream<int> calculate(int number) async* {
  for(int i = 0; i < 5; i++) {
    yield i * number;

    await Future.delayed(Duration(seconds: 1));
  }

}
```
