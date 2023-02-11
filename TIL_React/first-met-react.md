# 섹션 0. 준비하기

---

## 1. HTML과 CSS

### HTML

- 정의 : 웹사이트의 뼈대를 구성하기 위해 사용하는 마크업 언어

### 태그

- 태그를 사용해 구조를 형성하고 내용을 채움(ex. <html></html>

- 태그는 열었으면 꼭 닫아줘야 함.

- 웹사이트의 뼈대를 구성하는 태그들
  
  ```html
  <html>
      <head>
      </head>
      <body>
      </body>
  </html>
  
  head : 웹사이트의 설명 등을 담고 있음. 메타데이터
  body : 실제로 웹사이트에서 보이는 컨텐츠가 들어감
  ```

### SPA(Single Page Application)

- 하나의 페이지만 존재하는 웹 사이트 또는 웹 애플리케이션
  
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1f000b58-8917-477b-9b3f-9524754be0db/Untitled.png)

### CSS(Cascading Style Sheets)

- 웹사이트의 레이아웃과 글꼴 등 디자인을 입히는 것.

## 2. JavaScript 소개 및 자료형

### Javascript = ECMAScript

- html은 웹사이트의 뼈대, 자바스크립트는 웹사이트에 생명을 불어넣어 주는 역할
- 스크립트 언어 : 프로그램이 실행되는 런타임에 코드가 해석됨.
  - 컴파일 언어 : 컴파일이라는 과정에서 코드가 해석되고 실행가능하도록 변환.
- ES6(ECMAScript 2015, ES2015) ← 자바스크립트의 표준화

### Javascript의 문법

- 자료형
  
  - 프로그램에서 자료를 자루기 위해 미리 정해놓은 유형
  
  - 일반적으로는 변수를 선언하는 시점에 자료형이 결정되지만 자바스크립트에서는 변수에 데이터가 대입될 때 자료형이 결정 ← 동적 타이핑(Dynamic Typing)
    
    ```jsx
    // Number type
    let n1 = 1234;
    let n2 = 5.678;
    
    // Stirng type
    let s1 = "hello";
    let s2 = 'world';
    
    // Boolean type
    let b1 = true;
    let b2 = false;
    
    // Null type
    let n = null;
    
    // Undefined type
    let u1;
    let u2 = undefined;
    
    // Array type
    let arr = [1, 2, 3, 4];
    
    // Object type
    let obj = { a: "apple", b: "banana", c:"carrot" };
    ```
    
    ```jsx
    // Number type
    let n1 = 1234;
    let n2 = 5.678;
    
    // String type
    let s1 = "hello";
    let s2 = 'world';
    
    // Boolean type
    let b1 = true;
    let b2 = false;
    
    // Null type
    let n = null;
    
    // Undefined type
    let u1;
    let u2 = undefined;
    
    // Array type
    let arr = [1, 2, 3, 4];
    
    // Object type
    let obj = { a: "apple", b:"banana", c: "carrot" };
    ```
    
    ```jsx
    // Number 타입으로만 이루어진 배열
    let arr1 = [1, 2, 3, 4, 5];
    
    // String 타입으로만 이루어진 배열
    let arr2 = ["h", "e", "l"];
    
    // Number 타입과 String 타입을 함께 사용한 배열
    let arr3 = [1, "h", 4, "i"];
    
    // 다양한 자료형을 함께 사용한 배열
    let arr4 = [true, 1, undefined, false, "h", 2, null, "i"];
    
    console.log(arr1[0]);
    // 출력 결과 : 1
    
    console.log(arr2[1]);
    // 출력 결과 : e
    
    console.log(arr3[2]);
    // 출력 결과 : 2
    
    console.log(arr4[3]);
    // 출력 결과 : false
    ```
    
    ```jsx
    // 값으로 String 타입만을 사용한 객체
    let obj1 = { a: "apple", b: "banana", c: "carrot" };
    
    // 값으로 Number 타입만을 사용한 객체
    let obj2 = { a: 1, b: 2, c: 3 };
    
    // 값으로 다양한 자료형들을 함께 사용한 객체
    let obj3 = { a: "hello", b: 100, c: [1, 2, 3, 4] };
    
    // 값으로 객체를 사용한 객체
    let obj4 = {
      a: { a1: 1, a2: 2},
      b: { b1: 3, b2: 4},
      c: { c1: 5, c2: 6},
    };
    
    console.log(obj1['a']);
    // 출력 결과 : apple
    
    console.log(obj2.a);
    // 출력 결과 : 1
    
    console.log(obj3.a);
    // 출력 결과 : [1, 2, 3, 4]
    
    console.log(obj4.c.c2);
    // 출력 결과 : 6
    ```

- 참고 : [자바스크립트 공식문서](https://developer.mozilla.org/ko/docs/Web/JavaScript)

## 3. Javascript의 연산자

### 연산자

- 대입 연산자(Assignment operator) : ‘=’의 오른쪽에서 왼쪽으로 대입.
  
  ```jsx
  let a = 10;
  let b = 20;
  
  console.log(a);
  // 출력 결과 : 10
  
  console.log(b);
  // 출력 결과 : 20
  ```

### 사칙 연산자

- 사칙 연산자
  
  - +, -, *, /

- 산술 연산자
  
  - 사칙 연산자
  
  - % : 나머지 구하기
  
  - ** : 지수 구하기
    
    ```jsx
    let a = 2;
    let b = 4;
    
    console.log(a + b);
    // 출력 결과 : 6
    
    console.log(a - b);
    // 출력 결과 : -2
    
    console.log(a * b);
    // 출력 결과 : 8
    
    console.log(a / b);
    // 출력 결과 : 0.5
    
    console.log(a % b);
    // 출력 결과 : 2
    
    console.log(a ** b);
    // 출력 결과 : 16
    ```
    
    ```jsx
    let a = 2;
    let b = 4;
    
    a += b; // a = a + b
    console.log(a);
    // 출력 결과 : 6
    
    a -= b; // a = a - b
    console.log(a);
    // 출력 결과 : 2
    
    a *= b; // a = a * b
    console.log(a);
    // 출력 결과 : 8
    
    a /= b; // a = a / b
    console.log(a);
    // 출력 결과 : 2
    ```

- 증가 연산자(++) : a++, ++a

- 감소 연산자(—) : a—, —a
  
  ```jsx
  let a = 1;
  let b = a++;
  
  console.log(a, b);
  // 출력 결과 : 2, 1
  
  let c = 1;
  let d = ++c;
  
  console.log(c, d);
  // 출력 결과 : 2, 2
  ```

- 관계 연산자 = 비교 연산자
  
  - <, >, ≤, ≥
    
    ```jsx
    let a = 1;
    let b = 2;
    
    console.log(a < b);
    // 출력 결과 : true
    
    console.log(a > b);
    // 출력 결과 : false
    
    console.log(a <= b);
    // 출력 결과 : true
    
    console.log(a >= b);
    // 출력 결과 : false
    ```

- 동등 연산자
  - a == b : a와 b가 같다.
  - a ≠ b : a와 b가 같지 않다.

- 일치연산자
  
  - a === b : a가 b와 값과 자료형이 모두 같다.
  
  - a !== b : a가 b와 값과 자료형이 같지 않다.
    
    ```jsx
    let a = 1;
    let b = '1';
    
    console.log(a == b);
    // 출력 결과 : true
    
    console.log(a != b);
    // 출력 결과 : false
    
    console.log(a === b);
    // 출력 결과 : false
    
    console.log(a !== b);
    // 출력 결과 : true
    ```

- 이진 논리 연산자
  
  - a && b : a와 b가 모두 true일 경우에만 true
  
  - a || b : a 또는 b가 true일 경우에는 true
    
    ```jsx
    let a = true;
    let b = false;
    
    console.log(a && b);
    // 출력 결과 : false
    
    console.log(a || b);
    // 출력 결과 : true
    ```

- 조건부 연산자 = 삼항 연산자
  
  - 조건식 ? true일 경우 : false일 경우
    
    ```jsx
    let a = true;
    let b = false;
    
    console.log(a ? 1 : 2);
    // 출력 결과 : 1
    
    console.log(b ? 1 : 2);
    // 출력 결과 : 2
    ```

## Javascript의 함수

### 함수

- 함수란 입력을 받아서 정해진 출력을 하는 것

- 입력 : 파라미터, 인자
  
  ```jsx
  // function statement를 사용
  function sum(a, b) {
      return a + b;
  }
  
  console.log(sum(10, 20));
  // 출력 결과 : 30
  
  // arrow function expression 사용
  const multiply = (a, b) => {
      return a * b;
  }
  
  console.log(multiply(10, 20));
  // 출력 결과 : 200
  ```

# 섹션 1. 리액트 소개

## 리액트는 무엇인가?

### 라이브러리

- 자주 사용되는 기능들을 정리해 모아 놓은 것
- 리액트는 자바스크립트 UI 라이브러리

### 프레임워크 vs 라이브러리

- 프레임워크 프로그램의 흐름의 제한을 개발자가 아닌 프레임워크가 가지고 있음.
- 라이브러리는 프로그램의 흐름을 개발자가 제어함.

## 리액트의 장점과 단점

### 리액트의 장점

- 빠른 업데이트와 렌더링 속도
  
  - Virtual DOM(Document Object Model)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4fa52c3e-e8fa-4867-95d8-4d87a9e3af57/Untitled.png)

- Component-Based
  
  - 레고 블록 조립하듯 컴포넌트들을 모아서 개발
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8dccd83d-b81a-4fd7-a955-44e42dc2aa16/Untitled.png)

- 재사용성
  
  - 계속해서 사용이 가능한 성질
    
      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d43dc702-a73c-421d-b51f-8f6e88ba5735/Untitled.png)
  
  - 모듈의 의존성을 낮추고 호환성을 높임. ⇒ 재사용성을 높임
  
  - 효과
    
    - 개발 기간 단축
    - 유지 보수 용이
    - Meta라는 든든한 지원군
    - 커뮤니티의 활성화 정도
    - React Native로 모바일 개발도 가능

### 리액트의 단점

- 방대한 학습량
- 계속 뭔가 바뀜
- 높은 상태관리 복잡도
- 상태 관리의 기본 개념을 제대로 이해하자

# 섹션 2. 리액트 시작하기

- index.html
  
  ```html
  <!-- index.html -->
  
  <html>
      <head>
          <title>잡식성 개발자</title>
          <link rel="stylesheet" href="styles.css" />
      </head>
      <body>
          <h1>잡식성 개발자 블로그에 오신 여러분을 환영합니다.</h1>
  
          <!-- DOM Conatiner(Root DOM Node) -->
          <div id="root"></div>
      </body>
  </html>
  ```
  
  ```html
  <!-- index.html -->
  
  <html>
      <head>
          <title>잡식성 개발자</title>
          <link rel="stylesheet" href="styles.css" />
      </head>
      <body>
          <h1>잡식성 개발자 블로그에 오신 여러분을 환영합니다.</h1>
  
          {/* DOM Conatiner(Root DOM Node) */}
          <div id="root"></div>
  
          <!-- 리액트 가져오기 -->
          <script src="https://unpkg.com/react@17/umd/react.development.js" crossorigin></script>
          <script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js" crossorigin></script>
  
          <!-- 리액트 컴포넌트 가져오기 -->
          <script src="MyButton.js"></script>
      </body>
  </html>
  ```

- MyButton.js
  
  ```jsx
  // MyButton.js
  
  function MyButton(props) {
      const [isClicked, setIsClicked] = React.useState(false);
  
      return React.createElement(
          'button',
          { onclick: () => setIsClicked(true) },
          isClicked ? 'Clicked!' : 'Click here!'
      )
  }
  
  const domContainer = document.querySelector('#root');
  ReactDOM.render(React.createElement(MyButton), domContainer);
  ```

## 실습. create-react-app

### create-react-app

- 리액트로 개발을 하기 위한 모든 설정이 되어있는 상태로 프로젝트를 생성

- 조건
  
  - Node.js v14.0.0 이상
  - npm v6.14.0 이상
  - VS Code

- 명령어
  
  ```jsx
  # 사용법
  $ npx create-react-app <your-project-name>
  
  # 실제 사용 예제
  $ npx create-react-app my-app
  ```
  
  ```jsx
  # 경로 변경 (change directory)
  $ cd my-app
  
  # 애플리케이션 실행
  $ npm start
  ```

- 실행 화면
  
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0b2bcc4d-f649-4b30-a353-1d7f1adf3a2d/Untitled.png)

- [리액트 공식 문서](https://reactjs.org/docs/getting-started.html)

# 섹션 3. JSX

---

## JSX의 정의와 역할

- JSX의 정의
  
  - A syntax extension to Javascript
  - 즉 자바스크립트의 확장 문법
  - 자바스크립트 + XML/HTML
  - `1 const element = <h1>Hello, world!</h1>;`

- 역할
  
  - JSX는 내부적으로 XML 코드를 자스로 변환하는 과정을 거침
    
    ```jsx
    React.createElement(
          type,
          [props],
          [...children]
    )
    ```
  
  - JSX를 사용한 코드
    
    ```html
    class Hello extends React.Component {
          render() {
                  return <div>Hello {this.props.toWhat}</div>;
          }
    }
    
    ReactDOM.render(
          <Hello woWhat="World" />,
          document.getElementById('root')
    );
    ```
  
  - JSX를 사용하지 않은 코드
    
    ```jsx
    class Hello extends React.component {
      render() {
          return React.createElement('div', null, `Hello ${this.props.toWhat}`);
    
      }
    }
    
    ReactDOM.render(
      React.createElement(Hello, { toWhat: 'World' }, null),
      document.getElementById('root')
    );
    ```
    
    ```jsx
    // JSX를 사용한 코드
    const element = (
      <h1 className="greeting">
          Hello, World!
      </h1>
    )
    
    // JSX를 사용하지 않은 코드
    const element = React.createElement(
      'h1',
      { className: 'greeting' },
      'Hello, world!'
    )
    ```

- React.createElement()의 결과로 아래와 같은 객체가 생성됨
  
  ```jsx
  const elemnet = {
      type: 'h1',
      props: {
          className: 'greeting',
          children: 'Hello, world!'
      }
  }
  ```
  
  ```jsx
  React.createElement(
      type,
      [props],
      [...children]
  )
  ```
  
  - type : element의 유형
  - props : 속성
  - children : 현재 element가 포함하고 있는 자식 element
  - 리액트에서 JSX를 사용하는 것이 필수는 아니지만 훨씬 편리함

## JSX의 장점 및 사용법

### JSX의 장점

- 편리함
  
  ```jsx
  // JSX 사용함
  <div>Hello, {name}</div>
  
  // JSX 사용 안 함
  React.createElement('div', null, `Hello, ${name}`);
  ```

- 가독성 향상
  
  - 버그를 발견하기 쉬움

- injection Attacks 방어
  
  - 보안성 향상
    
    ```jsx
    const title = response.potentiallyMaliciousInput;
    
    // 이 코드는 안전합니다.
    const element = <h1>{title}</h1>;
    ```

### JSX 사용법

- Javascript 코드 + XML / HTML
  
  ```jsx
  const name = '소플';
  const element = <h1>안녕, {name}</h1>;
  
  ReactDOM.render(
          element,
          document.getElementById('root')
  );
  ```
  
  ```jsx
  ... XML / HTML
  {Javascript 코드}
  ... XML / HTML
  ```
  
  ```jsx
  function formatName(user) {
          return user.firstName + ' ' + user.lastName;
  }
  
  const user = {
          firstName: 'Inje',
          lastName: 'Lee'
  };
  
  const element = {
          <h1>
                  Hello, {formatUser(user)}
          </h1>
  );
  
  ReactDOM.render(
          element,
          document.getElementById('root')
  );
  ```
  
  ```jsx
  function getGreeting(user) {
          if (user) {
                  return <h1>Hello, {formatName(user)}!</h1>;
          }
          return <h1>Hello, Stranger.</h1>
  }
  ```

- 태그의 속성에 값을 넣는 방법
  
  ```jsx
  // 큰따옴표 사이에 문자열을 넣기너
  const element = <div tabIndex="0"></div>;
  
  // 중괄호 사이에 자바스크립트 코드를 넣으면 됨!
  const element = <img src={user.avatarUrl}</img>;
  ```

- 자식을 정의하는 방법
  
  ```jsx
  const element = {
          <div>
                  <h1>안녕하세요</h1>
                  <h2>열심히 리액트를 공부해 봅시다!</h2>
          </div>
  );
  ```

## 실습. JSX 코드 작성해 보기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/00c13875-6e98-4e22-a94a-991733899bbd/Untitled.png)

```jsx
// src/chapter_03/Book.jsx

import react from "react";

function Book(props) {
    return (
        <div>
            <h1>{`이 책의 이름은 ${props.name}입니다.`}</h1>
            <h2>{`이 책의 이름은 ${props.numOfPage}페이지로 이뤄져 있습니다.`}</h2>
        </div>
    );
}

export default Book;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/131af3b5-82e0-4467-8866-7f4932ce77d5/Untitled.png)

```jsx
// src/chapter_03/Library.jsx

import React from "react";
import Book from "./Book";

function Library(props) {
    return (
        <div>
            <Book name="처음 만난 파이썬" numOfpage={300} /> 
            <Book name="처음 만난 AWS" numOfpage={400} /> 
            <Book name="처음 만난 리액트" numOfpage={500} /> 
        </div>
    )
}

export default Library;
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7f48a522-95f6-4b80-8e23-18e884f36b83/Untitled.png)



# 섹션 4. Rendering Elements

---

## Element의 정의와 생김새

### Element란?

- 리액트 앱을 구성하는 요소
  
  - Elements are the smallest building blocks of React apps.
  - 리액트 앱을 구성하는 가장 작은 블록들
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/af63b3da-6490-48a5-9abd-941949abe4f4/Untitled.png)

- 화면에 나타나는 내용을 기술하는 자바스크립트 객체(Descriptor → Element)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/795bea3b-9097-4136-a990-3e9fb7d62f76/Untitled.png)

- Elements는 화면에서 보이는 내용을 기술

```jsx
const elemnet = <h1>Hello, world</h1>;
```

### Elements의 생김새

- 리액트 엘리먼트는 자바스크립트 객체 형태로 존재

- 불변성

- 버튼을 나타내는 객체
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/20794afa-b0e6-41b8-9b61-41f6e6f79373/Untitled.png)
  
  ```jsx
  {
          type: 'button',
          props: {
                  className: 'bg-green',
  ```
  
  - 실제 렌더링된 객체
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3d76855d-92bf-41af-a013-641f4eee98d0/Untitled.png)

- 리액트의 컴포넌트 객체
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ac45134e-a843-440f-afc8-37414a1be3e7/Untitled.png)

- 실제 생김새

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c37bcc36-e4a7-4e4e-852d-ec3a41d9b579/Untitled.png)

- 실제 동작하는 과정
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f8ab983-f829-44f1-8aad-996b87e87283/Untitled.png)
  
  - ConfirmDialog의 컴포넌트
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b16a5a4f-762c-444e-a244-3c8221b1bfc0/Untitled.png)
    
    - 최종적인 Element의 모습
      
      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/08472179-6695-440f-92c1-b8d7089a7c50/Untitled.png)

- 요약 : 컴포넌트 렌더링을 위해서 모든 컴포넌트가 create element 함수를 통해 element로 변환됨.

## Elements의 특징 및 렌더링하기

### Elements의 특징

- immutable : 변할 수 없는 → 불변성
  
  - 한번 생성된 엘리먼트는 변하지 않음
  - elements 생성 후에는 children이나 attributes를 바꿀 수 없다.
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d0890076-a59d-4abb-8350-c21a17db706b/Untitled.png)
  
  - element를 변경하는 것이 아니라 새로 만들면 됨.

### Elements 렌더링하기

- Root DOM Node
  
  ```jsx
  <div id="root"></div>
  ```
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f482ecc-3db4-469d-bb0f-9dc6c2c36c70/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cba86f9b-69d1-4d49-aafb-4486fef808f6/Untitled.png)

- 리액트 엘리먼트와 돔 엘리먼트는 다름.

### 렌더링된 Elements를 업데이트 하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f3ec7118-57f2-4dbe-813a-3a70e00ff7b4/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f742ce26-dec2-4be9-8d32-9d55a786e415/Untitled.png)

## 실습. 시계 만들기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/83130204-404f-4e13-ada6-ee1583fd19b7/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8d781714-76d0-4021-b989-4e66f122e844/Untitled.png)
