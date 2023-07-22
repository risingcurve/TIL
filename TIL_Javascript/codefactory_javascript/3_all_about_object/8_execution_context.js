/**
 * Execution Context
 * 
 * Execution Context는 실행하려는 js 코드와 코드를 실행할 때 필요한 정보를 담고 있는 특수한 환경이다.
 * 코드 실행에 필요한 모든 데이터를 들고 있는 환경이라고 생각하면 된다.
 * 
 * Execution Context는 크게 두 개로 나뉜다.
 * - Global Context : 최상위 Execution Context다. 코드를 실행하면 무조건 생성되는 context로 웹에서의 window 객체나 nodejs에서의 global 객체를 생성하고 들고 있다.
 * - Function Context : 함수가 실행될 때마다 함수별로 실행되는 context다. 함수 실행에 대한 모든 정보를 갖고 있는다.
 */

/**
 * Execution Context Stack
 * 
 * - Creation Phase
 *  - Global Object를 생성한다. window 또는 global 객체가 생성되고 함수에서는 arguments 객체가 생성된다.
 *  - this를 window 또는 global에 바인딩한다.
 *  - 변수와 함수를 Memory Heap에 배정하고 기본 값을 undefined로 저장한다.
 *    -> 호이스팅이 발생하는 이유 : Creations Phase가 먼저 일어나고 Execution Phase가 일어나기 때문.
 * 
 * - Execution Phase
 *  - 코드를 실행한다.
 *  - 필요하다면 새로운 Execution Context를 생성한다.
 */