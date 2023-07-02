/**
 * Hoisting
 */
console.log('Hello');
console.log('World');
console.log('--------------');

// console.log(name);
// var name = '코드팩토리';
// console.log(name);


/**
 * Hoisting은 무엇인가?
 * 
 * 모든 변수 선언문이 코드의 최상단으로 이동되는 것처럼 느껴지는 현상을 이야기한다.
 * var, let, const 모두 호이스팅 현상이 일어남.
 * var는 호이스팅 현상을 못 막음.
 * let, const는 호이스팅 현상을 막아 줌.
 */
// var name;
// console.log(name);
// name = '코드팩토리';
// console.log(name);

console.log(wonYoung);
var wonYoung = '리즈';
// undefined로 출력됨
console.log(yuJin);
let yuJin = '안유진';
// 에러 발생 : Cannot access 'yuJin' before initialization
console.log(leez);
const leez = '리즈';
// 에러 발생 : Cannot access 'leez' before initialization