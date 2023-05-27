# 형변환

```dart
void main() {
  List<String> blackPink = ['로제', '지수', '리사', '제니', '제니'];

  print(blackPink);
  print(blackPink.asMap());
  print(blackPink.toSet());

  Map blackPinkMap = blackPink.asMap();

  print(blackPinkMap.keys.toList());
  print(blackPinkMap.values.toList());

  Set blackPinkSet = Set.from(blackPink);

  print(blackPinkSet.toList());
}
```

# Map

```dart
void main() {
  Map<String, String> harryPotter = {
    'Harry Potter': '해리 포터',
    'Ron Weasley': '론 위즐리',
    'Hermione Granger': '헤르미온느 그레인저',
  };

  final result = harryPotter.map(
    (key, value) => MapEntry(
      'Harry Potter Character $key',
      '해리포터 캐릭터 $value',
    ),
  );

  print(harryPotter);
  print(result);

  final keys = harryPotter.keys.map((x) => 'HPC $x').toList();
  final values = harryPotter.values.map((x) => '해리포터 $x').toList();



  print(keys);
  print(values);
}
```

# Set

```dart
void main() {
  Set blackPinkSet = {
    '로제',
    '지수',
    '제니',
    '리사',
  };

  final newSet = blackPinkSet.map((x) => '블랙핑크 $x').toSet();

  print(newSet);
}
```

# Where

```dart
void main() {
  List<Map<String, String>> people = [
    {
      'name' : '로제',
      'group' : '블랙핑크',
    },
    {
      'name' : '지수',
      'group' : '블랙핑크',
    },
    {
      'name' : 'RM',
      'group' : 'BTS',
    },
    {
      'name' : '뷔',
      'group' : 'BTs',
    },
  ];

  print(people);

  final blackPink = people.where((x) => x['group'] == '블랙핑크');
  final bts = people.where((x) => x['group'] == 'BTS').toList();

  print(blackPink);
  print(bts);
}
```

# reduce

```dart
void main() {
  List<int> numbers = [
    1,
    3,
    5,
    7,
    9
  ];


  final result = numbers.reduce((prev, next) => prev + next);

//   final result = numbers.reduce((prev, next) {
//     print('---------------');
//     print('previous : $prev');
//     print('next : $next');
//     print('total : ${prev + next}');

//     return prev + next;
//   });

  print(result);

  List<String> words = [
    '안녕하세요',
    '저는',
    '코드팩토리입니다.',
  ];

  final sentence = words.reduce((prev, next) => prev + next);

  print(sentence);

  // reduce를 실행하는 멤버들과 같은 타입으로 리턴해 줘야 함.
  // words.reduce((prev, next) => prev.length + next.length);
}
```

# fold

```dart
void main() {
  List<int> numbers = [1, 3, 5, 7, 9];

  final sum = numbers.fold<int>(0, (prev, next) => prev + next);

  print(sum);

  List<String> words = [
    '안녕하세요 ',
    '저는 ',
    '코드팩토리입니다.',
  ];

  final sentence = words.fold<String>('', (prev, next) => prev + next);

  print(sentence);

  final count = words.fold<int>(0, (prev, next) => prev + next.length);

  print(count);

}
```

# Cascading Operator

```dart
void main() {
  List<int> even = [
    2, 4, 6, 8,
  ];

  List<int> odd = [
    1, 3, 4, 7,
  ];

  // cascading operator
  // ...
  // list 안에 값을 풀어넣는 역할

  // print([even, odd]);는 리스트 안에 리스트가 들어감
  print([...even, ...odd]);
  print(even);
  print([...even]);
  print(even == [...even]);
  // 완전히 새로운 list에 값을 풀어 넣을 수 있다.
}
```

# Funtional Programming

```dart
void main() {
    // functional programming
  // 실행하는 대상 리스트, 셋, 맵과 완전히 다른 새로운 값 생성
  // 함수들 체이닝해서 새로운 값 생성 가능

  final List<Map<String, String>> people = [
    {
      'name' : '로제',
      'group' : '블랙핑크',
    },
    {
      'name' : '지수',
      'group' : '블랙핑크',
    },
    {
      'name' : 'RM',
      'group' : 'BTS',
    },
    {
      'name' : '뷔',
      'group' : 'BTS',
    },
  ];

  print(people);

  final parsedPeople = people.map(
    (x) => Person(
      name: x['name']!,
      group: x['group']!,
    ),
  ).toList();

  print(parsedPeople);

  for(Person person in parsedPeople){
    print(person.name);
    print(person.group);
  }

  final bts = parsedPeople.where(
    (x) => x.group == 'BTS',
  );

  print(bts);

  final result = people.map(
    (x) => Person(
      name: x['name']!,
      group: x['group']!,
    ),
  ).where((x) => x.group == 'BTS')
    .fold<int>(0, (prev, next) => prev + next.name.length); 

  print(result);
}

class Person {
  final String name;
  final String group;

  Person({
    required this.name,
    required this.group,
  });

  @override
  String toString(){
    return 'Person(name:$name, group:$group)';
  }
}
```
