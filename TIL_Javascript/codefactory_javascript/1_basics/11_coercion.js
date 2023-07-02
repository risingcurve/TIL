/**
 * 타입 변환
 * Type Conversion
 * 
 * 1) 명시적
 * 2) 암묵적
 */

let age = 32;

// 명시적
let stringAge = age.toString();
console.log(typeof stringAge, stringAge);


// 암묵적 : 코드 작성 시 암묵적 형변환은 절대 사용하지 않는다.
let test = age + '';
console.log(typeof test, test);

console.log('98' + 2);
console.log('98' * 2);
console.log('98' - 2);

/**
 * 명시적 변환 몇 가지 더 배우기
 */

console.log(typeof (99).toString(), (99).toString());
console.log(typeof (true).toString(), (true).toString());
console.log(typeof (Infinity).toString(), (Infinity).toString());

// 숫자 타입으로 변환
console.log(typeof parseInt('0'), parseInt('0'));
// parseInt는 정수까지만 변환
console.log(typeof parseFloat('0.99'), parseFloat('0.99'));
// parseFloat는 실수로 변환
console.log(typeof + '1', + '1');

console.log('--------------------')
/**
 * Boolean 타입으로의 변환
 * 
 * !''
 */
console.log(!'x');
// 앞에 !를 붙이면 반대 Boolean으로 타입 변경
// 앞에 !!를 붙이면 원래 Boolean으로 타입 변경
// String에 값이 있으면 true

console.log(!!'x');
// String에 값이 있으면 true

console.log(!!0);
console.log(!!'0');
console.log(!!'false');
console.log(!!false);
console.log(!!undefined);
// undefined을 Boolean으로 변경하면 false
console.log(!!null);
// null을 Boolean으로 변경하면 false

console.log(!!{});
// 객체는 Boolean으로 변경하면 무조건 true 반환
console.log(!![]);
// 배열은 Boolean으로 변경하면 무조건 true 반환

/**
 * 1) 아무 글자도 없는 String
 * 2) 값이 없는 경우
 * 3) 0
 * 
 * 모두 false를 반환한다.
 */



