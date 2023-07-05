/**
 * Getter and Setter
 */

class IdolModel {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }

  /**
   * getter의 역할
   * 
   * 1) 데이터를 가공해서 새로운 데이터를 반환할 때
   * 2) private한 값을 반환할 때
   */

  get nameAndYear() {
    return `${this.name}-${this.year}`;
  }

  set setName(name){
    this.name = name;
    // this.name이 가리키는 것 : 클래스의 name
  }
}

const yuJin = new IdolModel('안유진', 2003);
console.log(yuJin);
console.log(yuJin.nameAndYear);
// getter는 함수처럼 정의했지만 함수는 아니다. 그러므로 yuJin.nameAndYear()라고 하면 안 된다.

yuJin.name = '장원영';
// setter를 사용하지 않아도 객체의 프로퍼티의 밸류를 바꿀 수도 있지만 private으로 만들었을 때는 setter를 이용해야만 접근이 가능하다.
yuJin.setName = '장원영_setter';
console.log(yuJin);


// private
class IdolModel2 {
  #name;
  // ES7 이후 지원
  year;

  constructor(name, year) {
    this.#name = name;
    this.year = year;
  }

  get name() {
    return this.#name;
  }
  // get은 그나마 가끔 사용.

  set name(name) {
    this.#name = name;
  }
  // set은 잘 안 씀.
}

const yuJin2 = new IdolModel2('안유진', 2003);
console.log(yuJin2);
console.log(yuJin2.name);
// getter를 이용해서 private한 값을 가져올 수 있다.

yuJin2.name = '코드팩토리';
console.log(yuJin2.name);
// setter를 이용해서 private한 프로퍼티의 값을 변경할 수 있다.