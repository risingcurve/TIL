/**
 * try...catch
 * 
 * 1) 발생시킬때 -> 던진다고 한다.(throw)
 * 2) 명시적으로 인지할 때 -> 잡는다고 한다.(catch)
 */

function runner() {
  try{
    console.log('Hello');
  
    throw new Error('큰 문제가 생겼습니다.');
  
    console.log('Code Factory');
    
  } catch(e) {
    console.log('---catch---');
    console.log(e);
  } finally {
    // 에러 여부와 관계 없이 finally는 무조건 출력(써도 되고 안 써도 됨)
    console.log('---finally---');
  }
};

runner();