/**
 * Static Keyword
 */

// class IdolModel{
//   name;
//   year;
//   static groupName = '아이브';

//   constructor(name, year) {
//     this.name = name;
//     this.year = year;
//   }

//   static returnGroupName() {
//     return '아이브';
//   }
// }

// const yuJin = new IdolModel('안유진', 2003);
// console.log(yuJin);

// console.log(IdolModel.groupName);
// // static을 사용하면 인스턴스에 귀속되는 것이 아니라 클래스 자체에 귀속됨.
// console.log(IdolModel.returnGroupName());




/**
 * factory constructor
 * 
 * 어떤 데이터를 입력받아서 데이터를 만들지 템플릿화해서 데이터를 만들 수 있다.
 */

class IdolModel {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }

  // static을 사용한 함수일 뿐.
  static fromObject(object) {
    return new IdolModel(
      object.name,
      object.year,
    );
  }

  static fromList(list) {
    return new IdolModel(
      list[0],
      list[1],
    );
  }
}

// const yuJin2 = new IdolModel('안유진', 2003);
const yuJin2 = IdolModel.fromObject({
  name: '안유진',
  year: 2003,
});
console.log(yuJin2);


const wonYoung = IdolModel.fromList(
  [
    '장원영',
    2003,
  ]
);
console.log(wonYoung);