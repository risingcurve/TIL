/**
 * Prototype
 */

const testObj = {};

// __proto__ 모든 객체에 존재하는 프로퍼티다.
// class 강의에서 배울 때 상속에서 부모 클래스에 해당되는 값이다.
console.log(testObj.__proto__);

function IdolModel(name, year) {
  this.name = name;
  this.year = year;
}

console.log(IdolModel.prototype);

console.dir(IdolModel.prototype, {
  showHidden: true,
});


/**
 * circular reference
 * 
 * 서로가 서로를 참조하는 형태.
 */
console.log(IdolModel.prototype.constructor === IdolModel);
// IdolModel 안의 prototype 안의 constructor key의 값은 실제로 IdolModel 함수다.
// 같은 메모리 주소를 참조하고 있다.

console.log(IdolModel.prototype.constructor.prototype === IdolModel.prototype);

const yuJin = new IdolModel('안유진', 2003);

console.log(yuJin.__proto__);
console.log(yuJin.__proto__ === IdolModel.prototype);

console.log(testObj.__proto__ === Object.prototype);

console.log(IdolModel.__proto__ == Function.prototype);
console.log(Function.prototype.__proto__ === Object.prototype);
console.log(IdolModel.prototype.__proto__ === Object.prototype);

console.log(yuJin.toString());
console.log(Object.prototype.toString());

function IdolModel2(name, year) {
  this.name = name;
  this.year = year;

  this.sayHello = function() {
    return `${this.name}이 인사를 합니다.`;
  }
}

const yuJin2 = new IdolModel2('안유진', 2003);
const wonYoung2 = new IdolModel2('장원영', 2004);

console.log(yuJin2.sayHello());
console.log(wonYoung2.sayHello());
console.log(yuJin2.sayHello === wonYoung2.sayHello);
// 다른 메모리 공간 참조

console.log(yuJin2.hasOwnProperty('sayHello'));
// true : yuJin2 객체 안에 선언된 함수

console.log('----------------');

function IdolModel3(name, year) {
  this.name = name;
  this.year = year;
}

IdolModel3.prototype.sayHello = function() {
  return `${this.name}이 인사를 합니다.`;
}

const yuJin3 = new IdolModel3('안유진', 2003);
const wonYoung3 = new IdolModel3('장원영', 2004);

console.log(yuJin3.sayHello());
console.log(wonYoung3.sayHello());

console.log(yuJin3.sayHello === wonYoung3.sayHello);
// 같은 메모리 공간 참조

console.log(yuJin3.hasOwnProperty('sayHello'));
// false : yuJin2 객체 안에 선언되지 않은 함수


IdolModel3.sayStaticHello = function() {
  return '안녕하세요 저는 static method입니다.'
}

console.log(IdolModel3.sayStaticHello());


/**
 * Overriding
 */

function IdolModel4(name, year) {
  this.name = name;
  this.year = year;

  // prototype 메서드를 인스턴스 메서드로 overriding하는 방법 : property shadowing(class에서 overriding과 마찬가지)
  this.sayHello = function() {
    return '안녕하세요 저는 인스턴스 메서드입니다.'
  }
}

IdolModel4.prototype.sayHello = function() {
  return '안녕하세요 저는 prototype 메서드입니다.';
}

const yuJin4 = new IdolModel4('안유진', 2003);
console.log(yuJin4.sayHello());


/**
 * getPrototypeOf, setPrototypeOf
 * 
 * 인스턴스의 __proto__ vs 함수의 prototype 변경
 */

function IdolModel(name, year) {
  this.name = name;
  this.year = year;

}

IdolModel.prototype.sayHello = function(){
  return `${this.name} 인사를 합니다.`;
}

function FemaleIdolModel(name, year) {
  this.name = name;
  this.year = year;

  this.dance = function() {
    return `${this.name}가 춤을 춥니다.`;
  }
}

const gaEul = new IdolModel('가을', 2002);
const ray = new FemaleIdolModel('레이', 2004);

console.log(gaEul.__proto__);
console.log(gaEul.__proto__ === IdolModel.prototype);
console.log(Object.getPrototypeOf(gaEul) === IdolModel.prototype);
// gaEul.__proto__ === IdolModel.prototype === Object.getPrototypeOf(gaEul)

console.log(gaEul.sayHello());
console.log(ray.dance());
console.log(Object.getPrototypeOf(ray) === FemaleIdolModel.prototype);
// console.log(ray.sayHello());
// 당연히 안 됨.

Object.setPrototypeOf(ray, IdolModel.prototype);
// 객체의 __proto__ 변경
console.log(ray.sayHello());

console.log(ray.constructor === FemaleIdolModel);

console.log(ray.constructor === IdolModel);
// ray의 constructor가 FemaleIdolModel에서 IdolModel로 변경된 것 확인

console.log(gaEul.constructor === IdolModel);
console.log(Object.getPrototypeOf(ray) === FemaleIdolModel.prototype);
// 변경했으므로 false
console.log(Object.getPrototypeOf(ray) === IdolModel.prototype);
console.log(FemaleIdolModel.prototype === IdolModel.prototype);

FemaleIdolModel.prototype = IdolModel.prototype;
// 함수의 prototype 변경

const eSeo = new FemaleIdolModel('이서', 2007);
console.log(Object.getPrototypeOf(eSeo) === FemaleIdolModel.prototype);
console.log(FemaleIdolModel.prototype === IdolModel.prototype);