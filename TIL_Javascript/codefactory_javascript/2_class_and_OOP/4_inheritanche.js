/**
 * Inheritance
 * 
 * 상속은 객체들 간의 관계를 구축하는 방법이다. 수퍼클래스 또는 부모 클래스 등의 기존의 클래스로부터 속성과 동작을 상속 받을 수 있다.
 */

class IdolModel {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
}

class FemaleIdolModel extends IdolModel {
  dance() {
    return `여자아이돌이 춤을 춘다.`;
  }
}

class maleIdolModel extends IdolModel {
  sing() {
    return `남자아이돌이 노래를 부른다.`;
  }
}

const yuJin = new FemaleIdolModel('안유진', 2003);
console.log(yuJin);

const jiMin = new maleIdolModel('박지민', 1995);
console.log(jiMin);

console.log(yuJin.dance());
console.log(yuJin.name)

console.log(jiMin.sing());
console.log(jiMin.year);

// console.log(yuJin.sing());
// femaleIdolModel에 정의되어 있지 않기 때문에 실행 불가.

const cf = new IdolModel('코드팩토리', 1992);
console.log(cf);

console.log(cf.name);
// console.log(cf.dance());
// cf에 정의되어 있지 않기 때문에 실행 불가.

console.log('-------------');
console.log(yuJin instanceof IdolModel);
console.log(yuJin instanceof FemaleIdolModel);
console.log(yuJin instanceof maleIdolModel);


console.log('-------------');
console.log(jiMin instanceof IdolModel);
console.log(jiMin instanceof FemaleIdolModel);
console.log(jiMin instanceof maleIdolModel);

console.log('-------------');
console.log(cf instanceof IdolModel);
console.log(cf instanceof FemaleIdolModel);
console.log(cf instanceof maleIdolModel);