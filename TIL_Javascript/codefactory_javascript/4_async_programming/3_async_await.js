/**
 * Async / Await
 */

const getPromise = (seconds) => new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('완료');
  }, seconds * 1000)
});

// promise를 만든 함수만 await 사용 가능
async function runner() {
  try{

    const result1 = await getPromise(1);
    console.log(result1);
    
    const result2 = await getPromise(2);
    console.log(result2);
    
    const result3 = await getPromise(1);
    console.log(result3);
  } catch {
    console.log('---catch e---');
    console.log(e);
  } finally {
    console.log('---finally---');
  }
  
}

runner();

console.log('실행 끝');