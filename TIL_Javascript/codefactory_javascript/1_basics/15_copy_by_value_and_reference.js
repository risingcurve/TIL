/**
 * copy by value : 값에 의한 전달
 * copy by reference : 참조에 의한 전달
 * 
 * 1) 기본적으로 모든 primitive 값은 copy by value다.
 * 2) 객체는 copy by reference다.
 */

let original = '안녕하세요';
let clone = original;

console.log(original);
console.log(clone);

clone += '안유진입니다.';
console.log(original);
console.log(clone);

let originalObj = {
  name: '안유진',
  group: '아이브',
};

let cloneObj = originalObj;

console.log(originalObj);
console.log(cloneObj);

originalObj['group'] = '코드팩토리';
console.log(originalObj);
console.log(cloneObj);

console.log(originalObj === cloneObj);

originalObj = {
  name: '최지호',
  group: '코드팩토리',
};

cloneObj = {
  name: '최지호',
  group: '코드팩토리',
};

console.log(originalObj === cloneObj);

console.log('----------------')

const yuJin1 = {
  name : '안유진',
  group : '아이브',
}

const yuJin2 = yuJin1;

const yuJin3 = {
  name : '안유진',
  group: '아이브',
}

console.log(yuJin1 === yuJin2);
// true

console.log(yuJin1 === yuJin3);
// false

console.log(yuJin2 === yuJin3);
// false

/**
 * Spread Operator : copy by value
 * 나중에 쓴 게 덮어쓰기 때문에 위치가 중요하다.
 */

const yuJin4 = {
  ... yuJin3,
};
console.log(yuJin4);
console.log(yuJin4 === yuJin3);
// false

const yuJin5 = {
  year: 2003,
  ...yuJin3,
};
console.log(yuJin5);

const yuJin6 = {
  name: '코드팩토리',
  ...yuJin3,
};
console.log(yuJin6);
// yuJin3로 덮어씀

const yuJin7 = {
  ...yuJin3,
  name: '코드팩토리',
};
console.log(yuJin6);
// '코드팩토리'로 덮어씀

const numbers = [1, 3, 5];
const numbers2 = [
  ... numbers,
  10,
];
const numbers3 = [
  10,
  ... numbers,
];
console.log(numbers2);
console.log(numbers3);
// numbers2와 numbers3이 10이 들어간 위치가 다름.