/**
 * 클래스
 * 
 * 클래스는 객체지향 프로그래밍에서 특정 객체(인스턴스)를 생성하기 위한 변수와 메소드(함수)를 정의하는 일종의 틀이다.
 * 즉 정보를 일반화해서 정리하는 방법이다.
 * 
 */

class IdolModel{
  name;
  year;
  // 프로퍼티를 정의하는 것은 필수적이지 않다(프로퍼티를 정의하지 않아도 실행은 가능하지만 정의하는 것이 좋다).

  constructor(name, year) {
    // this는 인스턴스
    this.name = name;
    this.year = year;
  }
}

// constructor : 생성자

const yuJin = new IdolModel('안유진', 2003);
console.log(yuJin);
const gaEul = new IdolModel('가을', 2002);
console.log(gaEul);
const ray = new IdolModel('레이', 2004);
console.log(ray);
const wonYoung = new IdolModel('장원영', 2004);
console.log(wonYoung);
const liz = new IdolModel('리즈', 2004);
console.log(liz);
const eSeo = new IdolModel('이서', 2007);
console.log(eSeo);

console.log(yuJin.name);
console.log(yuJin.year);


class IdolModel2 {
  constructor(name, year) {
    // this는 인스턴스
    this.name = name;
    this.year = year;
  }

  // 클래스 내에서 메소드를 정의할 때는 function을 적지 않고 함수 이름만 적는다.
  sayName() {
    return `안녕하세요. 저는 ${this.name}입니다.`
  }
}

const yuJin2 = new IdolModel2('안유진', 2003);
// console.log(yuJin2);

console.log(yuJin2.sayName());


console.log(typeof IdolModel);
console.log(typeof yuJin);