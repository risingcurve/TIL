/**
 * Array Functions
 */

let iveMembers = [
  '안유진',
  '가을',
  '레이',
  '장원영',
  '리즈',
  '이서',
]

console.log(iveMembers);

// push() : 아규먼트를 맨 뒤에 삽입하지만 길이를 반환
console.log(iveMembers.push('코드팩토리'));
console.log(iveMembers);

console.log('---------------');


// pop() : 마지막 엘리먼트를 삭제하지만 삭제한 값을 반환
console.log(iveMembers.pop());
console.log(iveMembers);

console.log('---------------');


// shift() : 첫번째 값을 삭제하지만 삭제한 값을 반환
console.log(iveMembers.shift());
console.log(iveMembers);

// unshift() : 아규먼트를 맨 앞에 삽입하지만 길이를 반환
console.log(iveMembers.unshift('안유진'));
console.log(iveMembers);


// splice() : n번 인덱스부터 m개 삭제하지만 삭제한 엘리먼트 반환
console.log(iveMembers.splice(0, 3))
console.log(iveMembers);

console.log('--------------------------------')


iveMembers = [
  '안유진',
  '가을',
  '레이',
  '장원영',
  '리즈',
  '이서',
]


// concat() : push와 비슷하지만 원래 Array를 변경하지 않고 새로운 Array를 만들어서 반환(아예 다른 메모리 공간)
console.log(iveMembers.concat('코드팩토리'));
console.log(iveMembers);

// slice() : splice와 비슷하지만 원래 Array를 변경하지 않고 새로운 Array를 만들어서 반환(아예 다른 메모리 공간)
console.log(iveMembers.slice(0, 3));
console.log(iveMembers)


console.log('--------------------------------')


// spread operator
let iveMembers2 = [
  ...iveMembers,
];

console.log(iveMembers2)

let iveMembers3 = [
  iveMembers,
];

console.log(iveMembers3)

let iveMembers4 = iveMembers;
console.log(iveMembers4);
console.log(iveMembers4 === iveMembers);

console.log([
  ...iveMembers,
] === iveMembers);
// 완전히 새로운 Array 탄생



// join() 
console.log(iveMembers.join());
console.log(iveMembers.join('/'));
console.log(iveMembers.join(', '));

// sort()
// 오름차순
iveMembers.sort();
console.log(iveMembers);

console.log(iveMembers.reverse());

let numbers = [
  1,
  9,
  7,
  5,
  3,
];
console.log(numbers);

// a, b를 비교했을 때
// 1) a를 b보다 나중에 정렬하려면 (뒤에 두려면) 0보다 큰 숫자를 반환
// 2) a를 b보다 먼저 정렬하려면 (앞에 두려면) 0보다 작은 숫자를 반환
// 3) 원래 순서를 그대로 두려면 0을 반환
numbers.sort((a, b)=>{
  return a > b ? 1 : -1;
});

console.log(numbers);

numbers.sort((a, b) => a > b ? -1 : 1);
console.log(numbers);

// map()
console.log(iveMembers.map((x) => x));
console.log(iveMembers.map((x) => `아이브: ${x}`));

console.log(iveMembers.map((x) => {
  if(x === '안유진'){
    return `아이브: ${x}`;
  } else {
    return x;
  }
}));
console.log(iveMembers);
// map()도 원래 Array를 바꾸지 않고 새로운 Array를 반환한다.


// filter()
numbers = [1, 8, 7, 6, 3];

console.log(numbers.filter((x) => true));
console.log(numbers.filter((x) => x % 2 === 0));


// find() : 조건에 해당하는 값 발견 시 즉시 반환(조건에 부합하는 다른 값이 있어도 안 봄)
console.log(numbers.find((x) => x % 2 === 0));

// findIndex() : 조건에 해당하는 값 발견 시 즉시 인덱스 반환(조건에 부합하는 다른 값이 있어도 안 봄)
console.log(numbers.findIndex((x) => x % 2 === 0));

// reduce()
console.log(numbers.reduce((p, n) => p + n,0));


/**
 * reduce()
 * 
 *  
 */