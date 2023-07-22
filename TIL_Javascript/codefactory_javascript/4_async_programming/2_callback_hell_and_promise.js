/**
 * Callback
 */

function waitAndRun() {
  // 여기가 콜백함수
  setTimeout(() => {
    console.log('끝');
    }, 2000);
}

// waitAndRun();

// 이런 함수는 가독성이 매우 떨어짐. 콜백 지옥.
function waitAndRun2() {
  setTimeout(
    () => {
      console.log('1번 콜백 끝');

      setTimeout(() => {
        console.log('2번 콜백 끝');
        setTimeout(() => {
          console.log('3번 콜백 끝');
        }, 2000);
      }, 2000);
    }, 2000);
}

// waitAndRun2();


/**
 * Promise
 */

// const timeoutPromise = new Promise((resolve, reject) => {
//   setTimeout(() => {
//     resolve('완료');
//   }, 2000);
// });

// timeoutPromise.then((res) => {
//   console.log('---then---');
//   console.log(res);
// });

// const getPromise = (seconds) => new Promise((resolve, reject) => {
//   setTimeout(() => {
//     resolve('완료');
//   }, seconds * 1000);
// });

// callback 함수로 작성한 코드보다 클린함.
// getPromise(3)
//   .then((res) => {
//     console.log('---first then---');
//     console.log(res);

//     return getPromise(3);
//   }).then((res) => {
//     console.log('--- second then ---');
//     console.log(res);

//     return getPromise(4);
//   }).then((res) => {
//     console.log('--- third then ---');
//     console.log(res);

//     return getPromise(4);
//   });

const getPromise = (seconds) => new Promise((resolve, reject) => {
  setTimeout(() => {
  // if(xxx) {
  //   resolve('성공');
  // } else {
    //   reject('에러');
    // }
    
    resolve('성공');
    // reject('에러');
  }, seconds * 1000);
});

//   getPromise(3)
//   .then((res) => {
//     console.log('---first then---');
//     console.log(res);

//     return getPromise(3);
//   })
//   .catch((res) => {
//     console.log('---first catch---');
//     console.log(res);
//   })
//   // finally는 resolve, reject 가리지 않고 무조건 실행
//   .finally(() => {
//     console.log('---finally---');
//   });


Promise.all([
  getPromise(1),
  getPromise(4),
  getPromise(1),
  // 가장 느린 함수를 기준으로 동시에 then 실행
]).then((res) => {
  console.log(res);
});