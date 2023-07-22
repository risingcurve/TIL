/**
 * Async Theory
 * 
 * Javascript는 single threaded다.
 * js는 어느 한 순간에 동시에 단 하나의 작업만 실행할 수 있다.
 * 
 */

function longWork() {
  const now = new Date();

  /**
   * milliseconds since epoch
   * 1970.1.1. 부터 지금 코드가 실행되는 순간까지의 시간을 밀리초로 변환한다.
   */

  const milliseconds = now.getTime();
  const afterTwoSeconds = milliseconds + 2 * 1000;

  while(new Date().getTime() < afterTwoSeconds) {

  }

  console.log('완료');
}

console.log('Hello');
longWork();
console.log('World');