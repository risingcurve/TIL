/**
 * Variable 선언하기
 * 
 * 1) var - 더 이상 쓰지 않는다.
 * 2) let
 * 3) const
 */

var name = '코드팩토리';
console.log(name);

var age = 32;
console.log(age);

let ive = '아이브';
console.log(ive);

/**
 * let과 var로 선언하면
 * 값을 추후 변경할 수 있다.
 */

ive = '안유진';
console.log(ive);

const newJeans = '뉴진스';
console.log(newJeans);

// newJeans = '코드팩토리'


/**
 * 선언과 할당
 * 
 * 1) 변수를 선언하는 것.
 * 
 */

var name = '코드팩토리';
console.log(name);

// let은 할당을 하지 않아도 사용은 가능하나, 콘솔로그로 찍어보면 undefined로 찍힘.
let girlFriend;
console.log(girlFriend);

// const는 할당을 하지 않으면 사용 불가
// const girlFriend2;