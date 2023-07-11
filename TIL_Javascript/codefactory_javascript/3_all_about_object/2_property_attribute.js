/**
 * Property Attribute
 * 
 * 1) 데이터 프로퍼티 - 키와 값으로 형성된 실질적 값을 갖고 있는 프로퍼티
 * 2) 액세서 프로퍼티 - 자체적으로 값을 갖고 있지 않지만 다른 값을 가져오거나 설정할 때 호출되는 함수로 구성된 프로퍼티
 * 예를 들면 getter와 setter
 */

const yuJin = {
  name: '안유진',
  year: 2003,
};

console.log(Object.getOwnPropertyDescriptor(yuJin, 'year'));


/**
 * 1) value - 실제 프로퍼티의 값
 * 2) writable - 값을 수정할 수 있는지 여부. false로 설정하면 프로퍼티 값을 수정할 수 없다.
 * 3) enumerable - 열거가 가능한지 여부이다. for ... in 등을 사용할 수 있으면 true를 반환한다.
 * 4) configurable - 프로퍼티 어트리뷰트의 재정의가 가능한지 여부를 판단한다.
 * false일 경우 프로퍼티 삭제나 어트리뷰트 변경이 금지된다. 단 writable이 true인 경우 값 변경과 writable을 변경하는 건 가능하다.
 */

console.log(Object.getOwnPropertyDescriptor(yuJin, 'name'));
console.log(Object.getOwnPropertyDescriptors(yuJin));

const yuJin2 = {
  name: '안유진',
  year: 2003,

  get age(){
    return new Date().getFullYear() - this.year;
  },

  set age(age){
    this.year = new Date().getFullYear() - age;
  }
}

console.log(yuJin2);
console.log(yuJin2.age);

yuJin2.age = 32;
console.log(yuJin2.age);
console.log(yuJin2.year);

console.log(Object.getOwnPropertyDescriptor(yuJin2, 'age'));
// 데이터 프로퍼티와 액세스 프로퍼티를 구분하는 방법은 getOwnPropertyDescriptor()를 실행하여
// value라는 프로퍼티가 존재하지 않고 get, set 프로퍼티 어트리뷰트가 존재하면 액세스 프로퍼티

// yuJin2.height = 172; 
// 또는
yuJin2['height'] = 172;
console.log(Object.getOwnPropertyDescriptor(yuJin2, 'height'));

Object.defineProperty(yuJin2, 'height', {
  value: 172,
  writable: true,
  enumerable: true,
  configurable: true,
  // 여기서 writable, enumerable, configurable을 추가하지 않으면 false가 디폴트임.
})
console.log(yuJin2);
console.log(Object.getOwnPropertyDescriptor(yuJin2, 'height'));

yuJin2.height = 180;

Object.defineProperty(yuJin2, 'height', {
  writable: false,
})
console.log(Object.getOwnPropertyDescriptor(yuJin2, 'height'));
// 기존에 존재하는 객체의 프로퍼티 어트리뷰트를 수정하면 수정한 값만 바뀜.

console.log('--------------------');
yuJin2.height = 172;
console.log(yuJin2);

/**
 * Enumerable
 */

console.log(Object.keys(yuJin2));
for(let key in yuJin2){
  console.log(key);
}

Object.defineProperty(yuJin2, 'name', {
  enumerable:false,
});

console.log(Object.getOwnPropertyDescriptor(yuJin2, 'name'));
console.log('------------------');
console.log(Object.keys(yuJin2));
for(let key in yuJin2){
  console.log(key);
}
console.log(yuJin2);
console.log(yuJin2.name);


/**
 * Configurable
 */
Object.defineProperty(yuJin2,'height', {
  configurable: false,
});
console.log(Object.getOwnPropertyDescriptor(yuJin2, 'height'));

// Object.defineProperty(yuJin2, 'height', {
//   enumerable: false,
// });

Object.defineProperty(yuJin2, 'height', {
  value: 172,
});
console.log(Object.getOwnPropertyDescriptor(yuJin2, 'height'));

Object.defineProperty(yuJin2, 'height', {
  writable: false,
});

Object.defineProperty(yuJin2, 'height', {
  writable: true,
});
// configurable을 한 번 false로 바꾸면 그 이후에는 변경 불가.