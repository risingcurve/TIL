/**
 * Using function to create objects
 */

function IdolModel(name, year) {
  if(!new.target) {
    return new IdolModel(name, year);
  }

  this.name = name;
  this.year = year;

  // return {};
  // {}만 반환함.
  // return 123;
  // primitive data는 반환하지 않음.

  this.dance = function(){
    return `${this.name}이 춤을 춥니다.`;
  }
}

const yuJin = new IdolModel('안유진', 2003);
console.log(yuJin);
// console.log(yuJin.dance());

const yuJin2 = IdolModel('안유진', 2003);
console.log(yuJin2);
// new 안 쓰면 undefined 출력

// console.log(global.name);
// 생성자 키워드(new)를 사용하지 않으면 global로 this.name, this.year 이동



const IdolModelArrow = (name, year) => {
  this.name = name;
  this.year = year;
};

// const yuJin3 = new IdolModelArrow('안유진', 2003);
// new 키워드는 일반 함수에서만 사용 가능하고 Arrow Function에서는 사용 불가능하다.
// console.log(yuJin3);