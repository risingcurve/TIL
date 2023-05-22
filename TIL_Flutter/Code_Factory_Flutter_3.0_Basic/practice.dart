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

