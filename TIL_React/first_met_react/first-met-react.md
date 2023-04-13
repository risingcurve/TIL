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

# 섹션 5. Components and Props

---

## Components와 Props의 정의

### Component-Based

- 레고 블록 조립하듯 컴포넌트들을 모아서 개발
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5ad2e974-b4d0-4b06-a6c3-9b3b859b2055/Untitled.png)
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8470af83-95a9-416d-be9c-0cf196ccde15/Untitled.png)
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8a4f6ff8-29b1-4133-a2a1-52fd86426f39/Untitled.png)

### Props

- 컴포넌트에 전달할 다양한 정보를 담고 있는 자바스크립트 객체

- Property의 준말, 즉 속성
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a8583dfc-c149-49f2-9523-41550b2b02fe/Untitled.png)

- 에어비앤비의 컴포넌트
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90b44ad3-a56a-42b5-adde-e888b3bdd302/Untitled.png)

- 에어비앤비의 props
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ef1c59bb-d15a-4fdf-bb56-14c1facd32d3/Untitled.png)

## Props의 특징 및 사용법

### Read-Only

- 값을 변경할 수 없다.
- 새로운 값을 컴포넌트에 전달하여 새로 Element를 생성

### Javascirpt의 함수의 속성

- 퓨어함
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5c2d4b94-cdf2-4e64-9a56-ec97944e1642/Untitled.png)
  
  - Impure
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7f78bbd2-03ca-46a4-8130-96998b27b5e5/Untitled.png)
  
  - All React components must act like pure functions with repect to their props.
  
  - 모든 리액트 컴포넌트는 그들의 Props에 관해서는 Pure 함수 같은 역할을 해야 한다.
  
  - 즉 모든 리액트 컴포넌트는 Props를 직접 바꿀 수 없고, 같은 Props에 대해서는 항상 같은 결과를 보여줄 것.

### Props 사용법

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6803dfae-5d66-4445-b110-16f8cde69350/Untitled.png)

- JSX를 사용한 Props
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8ab259f0-2ac3-4591-8070-0c560eebb76c/Untitled.png)

- JSX 미사용
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/49fa07ff-e7d5-4fae-8385-bca27337533b/Untitled.png)

## Component 만들기

### 컴포넌트

- 종류
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8c15eb15-3832-4042-828e-f9769aba8811/Untitled.png)
  
  - 함수 컴포넌트(Function Component)
    
    ```jsx
    function Welcom(props) {
            return <h1>안녕, {props.name}</h1>;
    }
    ```
  
  - 클래스 컴포넌트(Class Component)
    
    ```jsx
    class Welcom extends React.Component {
            render() {
                    return <h1>안녕, {this.props.name}</h1>;
            }
    }
    ```

### Component의 이름

- Component 이름은 항상 대문자로 시작해야 한다.
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/67356ae8-7258-4706-8702-6431648d14d6/Untitled.png)

### Component 렌더링

```
![Untitled](<https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16bc4908-da30-40b1-a27f-0aecb7619d38/Untitled.png>)
```

- 실제
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ea8b654a-9ac9-4c9b-af13-0d4a9fad8279/Untitled.png)

## Component 합성과 추출

### Component 합성

- Component 안에 또 다른 Component를 쓸 수 있다.

- 복잡한 화면을 여러개의 Component로 나눠서 구현 가능
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6aae14c1-6b06-43ed-a165-23b5a5821e5f/Untitled.png)
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/688c1321-9029-4a42-9bed-a2f41ad38090/Untitled.png)

### Component 추출

- 큰 컴포넌트를 산산조각 내자.

- 재사용성 증가

- 개발 속도 빨라짐

- 과정
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a717914-8b89-4df8-b9bd-47de46a33097/Untitled.png)
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/838b9f11-22fd-4ee6-ae87-9e4ebcaada57/Untitled.png)
  
  1. Avatar 추출하기
     
     ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/46d884af-35e1-40ac-8ac7-4b2fd15b226e/Untitled.png)
     
     ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b91c232c-e911-4e79-a5a2-1bd557980067/Untitled.png)
     
     ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0efcf2d0-753b-485b-be88-b2ecce4dfc81/Untitled.png)
1. UserInfo 추출하기
   
   ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7101376f-8534-4949-b336-000597ba359d/Untitled.png)
   
   ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a0935343-47da-4b40-90ec-642c9c92d64c/Untitled.png)
   
   ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f9746c7a-0194-452d-bae2-7105e024f640/Untitled.png)
- 구조
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9801bbbe-a44a-4833-b37c-200f06e14c9a/Untitled.png)

# 섹션 7. Hooks

## Hooks의 개념과 useState, useEffect

### Hook

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aecf02fe-f276-450d-936d-2440ba7c161e/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d2e3bb06-9b54-4182-a75d-9d92c2357552/Untitled.png)

- 갈고리
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/766c6d72-d8da-42af-aa06-c1888155b532/Untitled.png)
  
  - 이름 앞에 use를 붙어야 함

### useState

- state를 사용하기 위한 Hook
  
  ```jsx
  import React, { useState } from "react";
  
  function Counter(props) {
          var count = 0;
  
          return (
                  <div>
                          <p>총 {count}번 클릭했습니다.</p>
                          <button onClick={() => count++}>
                                  클릭
                          </button>
                  </div>
          );
  } 
  ```

- useState() 사용법
  
  ```jsx
  const [변수명, set함수명] = useState(초기값);
  ```
  
  ```jsx
  import React, { useState } from "react";
  
  function Counter(props) {
          const [count, setCount] = useState(0); // setCount : 변수 각각에 대해 set 함수가 따로 존재
  
          return (
                  <div>
                          <p>총 {count}번 클릭했습니다.</p>
                          <button onClick={() => setCount(count + 1)}>
                                  클릭
                          </button>
                  </div>
          );
  } 
  ```

### useEffect()

- Side effect를 수행하기 위한 Hook

- 리액트에서 Side effect = 효과, 영향
  
  - 일반적인 Side effect = 부작용

- 다른 컴포넌트에 영향을 미칠 수 있으며, 렌더링 중에는 작업이 완료될 수 없기 때문

- 리액트의 함수 컴포넌트에서 Side effect를 실행할 수 있게 해주는 Hook

- useEffect() 사용법
  
  ```jsx
  useEffect(이펙트 함수, 의존성 배열);
  ```
  
  - Effect function이 mount, unmount 시에 단 한 번씩만 실행됨
    
    ```jsx
    useEffect(이펙트 함수, []);
    ```
  
  - 의존성 배열을 생략하면 컴포넌트가 업데이트 될 때마다 호출됨
    
    ```jsx
    import React, { useState, useEffect } from "react";
    
    function Counter(props) {
            const [count, setCount] = useState(0);
    
            // componentDidMount, componentDidUpdate와 비슷하게 작동합니다.
            useEffect(() => {
                    // 브라우저 API를 사용해서 documnet의 title을 업데이트합니다.
                    document.title = `You clicked ${count} times`;
            });
    
            return (
                    <div>
                            <p>총 {count}번 클릭했습니다.</p>
                            <button onClick={() => setCount(count + 1)}>
                                    클릭
                            </button>
                    </div>
            );
    } 
    ```
    
    ```jsx
    import React, { useState, useEffect } from "react";
    
    function UserStatus(props) {
            const [count, setIsOnline] = useState(null);
    
            function handleStatusChange(status) {
                    setIsOnline(status.inOnline);
            }
    
            useEffect(() => {
                    ServerAPI.subscribeUserStatus(props.user.id, handleStatusChange);
                    return () => {
                            ServerAPI.unsubscribeUserStatus(props.user.id, handleStatusChange);
                    };
            });
    
            if (isOnline === null) {
                    return '대기 중...';
            }
            return isOnline ? '온라인' : '오프라인';
    ```
    
    ```jsx
    function UserStatusWithCounter(props) {
            const [count, setCount] = useState(0);
            useEffect(() => {
                    document.title = `총 ${count}번 클릭했습니다.`;
            });
    
            const [isOnline, setIsOnline] = useState(null);
            useEffect(() => {
                    ServerAPI.subcribeUserStatus(props.user.id, handleStatusChange);
                    return () => {
                            ServerAPI.subcribeUserStatus(props.user.id, handleStatusChange);
                    };
            });
    
            function handleStatusChange(status) {
                    setIsOnline(status.isOnline);
            }
    
            // ...
    ```
    
    ```jsx
    useEffect(() => {
            // 컴포넌트가 마운트 된 이후,
            // 의존성 배열에 있는 변수들 중 하나라도 값이 변경되었을 때 실해오딤
            // 의존성 배열에 빈 배열([])을 넣으면 마운트와 언마운트시에 단 한 번씩만 실행됨
            // 의존성 배열 생략 시 컴포넌트 업데이트 시마다 실행됨
            ...
    
            return () => {
                    // 컴포넌트가 마운트 해제되기 전에 실행됨
                    ...
            }
    }, [의존성 변수1, 의존성 변수2, ...]);
    ```

## useMemo, useCallback, useRef

---

### useMemo()

- Memoized value를 리턴하는 Hook

- Memoization : 연산량이 많이 드는 함수의 호출 결과를 저장해 두었다가, 같은 입력값으로 함수를 호출하면 새로 함수를 호출하지 않고, 이전에 저장해 두었던 호출 결과를 반환하는 것.

- 사용법
  
  ```jsx
  const memoizedValue = useMemo(
          () => {
                  // 연산량이 높은 작업을 수행하여 결과를 반환
                  return computeExpensivaValue(의존성 변수1, 의존성 변수2);
          },
          [의존성 변수1, 의존성 변수2]
  );
  
  // 렌더링이 일어나는 동안 실행됨
  ```

- 의존성 배열을 넣지 않을 경우, 매 렌더링마다 함수가 실행됨
  
  ```jsx
  const memoizedValue = useMemo(
          () => computeExpensiveValue(a, b)
  );
  ```

- 의존성 배열이 빈 배열일 경우, 컴포넌트 마운트 시에만 호출됨
  
  ```jsx
  const memoizedValue = useMemo(
          () => {
                  return computeExpensiveValue(a, b);
          },
          []
  );
  ```

### useMemo, useCallback, useRef

- useMemo() Hook과 유사하지만 값이 아닌 함수를 반환

- 사용법
  
  ```jsx
  const memoizedCallback = useCallback(
          () => {
                  do Something(의존성 변수1, 의존성 변수2);
          },
          [의존성 변수1, 의존성 변수2]
  );
  
  // 의존성 배열의 값이 바뀐 경우에만 함수를 새로 정의해서 리턴
  // 함수와 의존성 배열을 파라미터로 받음
  // 파라미터로 받는 함수를 콜백이라고 부름
  // 의존성 배열에 있는 변수 중 하나라도 바뀌면 메모이제이션된 콜백함수를 반환
  // 의존성 배열에 따라 메모이즈드 된 값을 반환하는 것은 useMemo()와 동일
  ```

- 동일한 역할을 하는 두줄의 코드
  
  ```jsx
  useCallback(함수, 의존성 배열);
  useMemo(() => 함수, 의존성 배열);
  ```
  
  ```jsx
  import { useState } from "react";
  
  function ParentComponent(props) {
      const |count, setCount| = useState(0);
  
      // 재렌더링 될 때마다 매번 함수가 새로 정의됨
      const handleClick = (event) => {
          // 클릭 이벤트 처리
      };
  
      return (
          <div>
              <button
                  onClick={() => {
                      setCount(count + 1);
                  }}  
              >
                  {count}
              </button>
  
              <ChildComponent handleClick={handleClick} />
          </div>
      );
  }
  ```
  
  ```jsx
  import { useState } from "react";
  
  function ParentComponent(props) {
      const |count, setCount| = useState(0);
  
      // 재렌더링 될 때마다 매번 함수가 새로 정의됨
      const handleClick = (event) => {
          // 클릭 이벤트 처리
      };
  
      return (
          <div>
              <button
                  onClick={() => {
                      setCount(count + 1);
                  }}  
              >
                  {count}
              </button>
  
              <ChildComponent handleClick={handleClick} />
          </div>
      );
  }
  ```

=======

## 실습. Hooks 사용해보기

### useCounter Hook 만들기

```jsx
import React, { useState } from "react";

function useCounter(initialValue) {
    const [const, setCount] = useState(initialValue);

    const increaseCount = () => setCount((count) => count + 1);
    const decreaseCount = () => setCount((count) => Math.max(count - 1, 0);

    return [count, increaseCount, decreaseCount];
}

export default useCounter;

// useCounter Hook은 초기 카운트 값을 파라미터로 받아서, 
// count라는 이름의 state를 생성하여 값을 제공하고,
// count 증가 및 감소를 편리하게 할 수 있도록 함수를 제공하는 Hook이다.
```

### Accommodate 컴포넌트 만들기

```jsx
import React, { useState, useEffect } from "react";
import useCounter from "./useCounter";

const MAX_CAPACITY = 10; // 최대 수용 인원

function Accomodate(props) {
    const [isFull, setIsFull] = useState(false);
    const [count, increaseCount, decreaseCount] = useCounter(0);

    useEffect(() => {
        console.log("================");
        console.log("useEffect() is called.");
        console.log(`isFull: ${isFull}`);
    });

    useEffect(() => {
        setIsFull(count >= MAX_CAPACITY); 
        console.log(`Current count value: ${count}`);
    }, {count});

    return (
        <div style={{ padding: 16 }}>
            <p>{`총 ${count}명 수용했습니다.`}</p>

            <button onClick={increaseCount} disabled={isFull}>
                입장
            </button>
            <button Click={decreaseCount}>
                퇴장
            </button>

            {isFull && <p style={{ color: "red" }}>정원이 가득찼습니다.</p>}
        </div>
    );
}
```

- 앞에서 만든 useCounter()를 사용하여 count를 관리한다.
- 두 개의 useEffect훅을 사용함 → 의존성 배열 유무
- 의존성 배열이 없는 형태는 컴포넌트가 마운트된 직후 호출, 이 후 컴포넌트가 업데이트 될 때마다 호출
- 의존성 배열이 있는 형태는 컴포넌트가 마운트된 직후 호출, 이 후 카운트 값이 바뀔 때마다 호출, 용량이 가득 찼는지 아닌지를 isFull에 저장

# 

# 섹션 8. Handling Events

## Event의 정의 및 Event 다루기

### Event

- 특정 사건
  
  - 예시 : 사용자가 버튼을 클릭한 사건

- 바인딩 사용하기
  
  ```jsx
  class Toggle extends React.Component {
      constructor(props) {
          super(props);
  
          this.state = { isToggleOn: True };
  
          // callback에서 `this`를 사용하기 위해서는 바인딩을 필수적으로 해줘야 합니다.
          this.handleClick = this.handleClick.bind(this);
      }
  
      // 바인딩 사용
      handleClick() {
          this. setState(prevState => ({
              isToggleOn: !prevState.isToggleOn
          }));
      }
  
      render() {
          return (
              <button onClick={this.handleClick}>
                  {this.state.isToggleOn ? '켜짐' : '꺼짐'}
              </button>
          );
      }
  }
  ```

- 바인딩 대신 Class fields syntax 사용
  
  ```jsx
  class MyButton extends React.Component {
      handleClick = () => {
          console.log('this is:', this);
      }
  
      render() {
          return (
              <button onClick={this.handleClick}>
                  클릭
              </button>
          )
      }
  }
  ```

- Arrow function 사용
  
  ```jsx
  class MyButton extends React.Component {
      handleClick() {
          console.log('this is:', this);
      }
  
      render() {
          // 이렇게 하면 `this`가 바운드됩니다.
          return (
              <button onClick={() => this.handleClick()}>
                  클릭
              </button>
          )
      }
  }
  ```

- 토글 컴포넌트를 함수 컴포넌트로 변환
  
  ```jsx
  function Toggle(props) {
      const [isToggleOn, setIsToggleOn] = useState(true);
  
      // 방법 1. 함수 안에 함수로 정의
      function handleClick() {
          setIstToggleOn((isToggleOn) => !isToggleOn);
      }
  
      // 방법 2. arrow function을 사용하여 정의
      const handleClick = () => {
          setIsToggleOn((isToggleOn) => !isToggleOn);
      }
  
      return (
          <button onClick={handleClick}>
              {isToggleOn ? "켜짐" : "꺼짐"}
          </button>
      );
  }
  ```

(실습)

```jsx
import React from "react"

class ConfirmButton extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            isConfirmed: false,
        }
    }

    this.handleConfirm = this.hanleConfirm.bind(this)
}


    handleConfirm() {
        this.setState(prevState) => ({
            isConfirmed: !prevState.isConfirmed,  
        }))
    }

    render() {
        return (
            <button
                onClick=(this.handleConfirm)
                disabled=(this.state.isConfirmed)
            >
                {this.state.isConfirmed ? "확인됨" : "확인하기"}
            </button>  
        )
    }
}

export default ConfirmButton;
```

# 

# 

# 섹션 9. Conditional Rendering

---

## Conditional Rendering

### Condition

- 조건, 상태를 의미

### Conditional Rendering

- 조건에 따른 렌더링
- 조건부 렌더링
- 어떠한 조건(조건문의 True, False)에 따라서 렌더링이 달라지는 것

```jsx
function Greeting(props) {
    const isLogginedIn = props.isLoggedIn

    if (isLoggedIn) {
        return <UserGreeting />
    }
    return <GuestGreeting />
}
```

### Javascript의 Truthy와 Falsy

- Truthy : Javascript에서 True는 아니지만 True로 여겨지는 값
- Falsy : Javascript에서 False는 아니지만 False로 여겨지는 값

```jsx
// truthy
true
{} (empty object)
[] (empty array)
42 (number, not zero)
"0", "false" (string, not empty)

// falsy
0, -0 (zero, minus zero)
0n (BigInt zero)
'', "", `` (empty string)
null
undefined
NaN(not a number)
```

### Element Variables

- 엘리먼트를 변수처럼 다루는 방법
  
  ```jsx
  function LoginButton(props) {
      return (
          <button onClick={props.onClick}>
              로그인
          </button>
      )
  }
  
  function LogoutButton(props) {
      return (
          <button onClick={props.onClick}>
              로그아웃
          </button>
      )
  }
  ```
  
  ```jsx
  function LogginControl(props) {
      const [isLoggedIn, setIsLoggedIn] = useState(false_
  
      const handleLoginClick = () => {
          setIsLoggedIn(true)
      }
  
      const handleLogoutClick = () => {
          setIsLoggedIn(false)
      }
  
      let button
      if (isLoggedIn) {
          button = <LogoutButton onClick={handleLogoutClick} />
      } else {
          button = <LoginButton onClick={handleLoginClick} />
      }
  
      return (
          <div>
              <Greeting isLoggedIn={isLoggedIn}/>
              {button} // element를 변수처럼 저장
          </div>
      )
  }
  ```

### Inline Conditions

- in + line : 해당 코드 안에 직접 기입
- 조건문을 코드 안에 집어넣는 것.

### Inline if

- if문을 필요한 곳에 직접 집어넣어 사용하는 방법

- if문의 경우 && 연산자를 사용
  
  - 단축 평가 적용
    - true && expression → expression
    - false && expression → false
  
  ```jsx
  function Mailbox(props) {
      const unreadMessages = props.unreadMessages;
  
      return (
          <div>
              <h1>안녕하세요!</h1>
              {unreadMessages.length > 0 &&
                  <h2>
                      현재 {unreadMessages.length}개의 읽지 않은 메시지가 있습니다.
                  </h2>
              }
          </div>
      )
  }
  ```
  
  - && 연산자를 사용할 때 조건문에 false expression을 사용하면 뒤에 나오는 expression은 평가되지 않지만, false expression의 결과 값은 그대로 나옴.
  
  ```jsx
  function Counter(props) {
      const count = 0;
  
      return (
          <div>
              {count && <h1>현재 카운트 : {count}</h1>}
          </div>
      )
  }
  ```

- if else 문의 경우 ? 연산자를 사용
  
  - 삼항 연산자
  - condition ? true : false
  
  ```jsx
  function UserStatus(props) {
      return (
          <div>
              이 사용자는 현재 <b>{props.isLoggedIn ? '로그인' : '로그인하지 않은'}</b> 상태입니다.
          </div>
      )
  }
  ```
  
  ```jsx
  function LogginControl(props) {
      const [isLoggedIn, setIsLoggedIn] = useState(false)
  
      const handleLoginClick = () => {
          setIsLoggedIn(true)
      }
  
      const handleLogoutClick = () => {
          setIsLoggedIn(false)
      }
  
      return (
          <div>
              <Greeting isLoggedIn={isLoggedIn} />
              {isLoggedIn
                  ? <LogoutButton onClick={handleLogoutClick} />
                  : <LoginButton onClick={handleLoginClick} />
          </div>
      )
  }
  ```

### Component 렌더링 막기

- null 리턴
  
  ```jsx
  function WarningBanner(props) {
      if (!props.warning) {
          return null;
      }
  
      return (
          <div>경고!</div>
      )
  }
  ```
  
  ```jsx
  function MainPage(props) {
      const [showWarning, setShowWarning] = useState(false)
  
      const handleToggleClick = () => {
          setShowWarning(prevShowWarning => !prevShowWarning)
      }
  
      return (
          <div>
              <WarningBanner warning={showWarning} />
              <button onClick={handleToggleClick}>
                  {showWarning ? '감추기' : '보이기'}
              </button>
          </div>
      )
  }
  ```

- 컴포넌트의 생명주기에는 영향을 미치지 않음.

## (실습) 로그인 여부를 나타내는 툴바 만들기

```jsx
import React from "react";

const styles = {
    wrapper: {
        padding: 16,
        display: "flex",
        flexDirection: "row",
        borderBottom: "1px solid grey"
    },

    greeting: {
        marginRight: 8,
    },
}

function Toolbar(props) {
    const { isLoggedIn, onClickLogin, onClickLogout } = props

    return (
        <div style={styles.wrapper}>
            {isLoggedIn && <span style={styles.greeting}>환영합니다!</span>}

            {isLoggedIn ? (
                <button onClick={onClickLogout}>로그아웃</button>
            ) : (
                <button onClick={onClickLogin}>로그인</button>
            )}
        </div>
    )
}
```

```jsx
import React, { useState } from "react";
import Toolbar from "./Toolbar"

function LandingPage(props) {
    const [isLoggedIn, setIsLoggedIn] = useState(false)

    const onClickLogin = () => {
        setIsLoggedIn(true)
    }

    const onClickLogout = () => {
        setIsLoggedIn(false)
    }

    return (
        <div>
            <Toolbar
                isLoggedIn={isLoggedIn}
                onClickLogin={onClickLogin}
                onClickLogout={onClickLogout}
            />
            <div style={{ padding: 16 }}>소플과 함께하는 리액트 공부!</div>
        </div>
    )
}

export default LandingPage
```

# 

# 섹션 10. List and Keys

---

## List와 Key

### List

- 목록
- Array (배열) : 자바스크립트의 변수나 객체들을 하나의 변수로 묶어 놓은 것.

### Key

- 각 객체나 아이템을 구분할 수 있는 고유한 값
- 아이템들을 구분하기 위한 고유한 문자열

## 여러개의 Component 렌더링 하기

### map()

- 짝 지어주는 것
  
  ```jsx
  const doubled = numbers.map((number) => number * 2);
  ```
  
  ```jsx
  const numbers = [1, 2, 3, 4, 5]
  const listItems = numbers.map((number) =>
      <li>{number}<li>
  )
  
  ReactDOM.render(
      <ul>{listItems}</ul>,
      document.getElementById('root')
  )
  ```
  
  ```jsx
  ReactDOM.render(
      <ul>
          <li>{1}</li>
          <li>{2}</li>
          <li>{3}</li>
          <li>{4}</li>
          <li>{5}</li>
      </ul>
      document.getElementById('root')
  )
  ```

### 기본적인 List Component

```jsx
function NumberList(props) {
    const { numbers } = props

    const listItems = numbers.map((number) =>
        <li>{number}</li>
    )

    return (
        <ul>{listItems}</ul>
    )
}

const numbers = [1, 2, 3, 4, 5]
ReactDOM.render(
    <NumberList numbers={numbers} />,
    document.getElementById('root')
)

// 각 아이템에 키가 없기 때문에 콘솔에 경고 문구가 출력됨.
```

## Liset의 Key

- Key의 값은 같은 List에 있는 Elemnets 사이에서만 고유한 값이면 된다.
- 두 대학교 사이에서는 학번이 같아도 상관 없듯이 두 list 사이에서는 key가 같아도 상관 없다.
- map() 함수 안에 있는 Elements는 꼭 key가 필요하다.

### key로 값을 사용하는 경우

```jsx
const numbers = [1, 2, 3, 4, 5]
const listItems = numbers.map((number) =>
    <li key={number.toString()}>
        {number}
    </li>
)
```

### key로 id를 사용하는 경우

```jsx
const todoItems = todos.map((todo) =>
    <li key={todo.id}>
      {todo.text}
    </li>
)
```

### key로 index를 사용하는 경우

```jsx
const todoItems = todos.map((todo, index) =>
    // 아이템들의 고유한 id가 없을 경우에만 사용해야 함
    <li key={todo.id}>
      {todo.text}
    </li>
)
```

## (실습) 출석부 출력하기

```jsx
// Attendance.jsx

import React from "react"

const students = [
    {
        id: 1,
        name: "WJ",
    },
    {
        id: 2,
        name: "Steve",
    },
    {
        id: 3,
        name: "Bill",
    },
    {
        id: 4,
        name: "Jeff",
    },
]

function AttendanceBook(props) {
    return (
        <ul>
            {students.map((student) => {
                return <li key={`student-id-${student.id}`}>{student.name}</li>
                // key를 포맷팅 된 문자열로 변경
            })}

            {students.map((student, index) => {
                return <li key={index}>{student.name}</li>
                // key를 index로 변경
            })}

        </ul>
    )
}

export default AttendanceBook
```

# 섹션 11. Forms

---

## Forms Controlled Component

### Form

- 사용자로부터 입력을 받기 위해 사용하는 것

- 리액트와 html의 Form은 차이가 존재함.
  
  - 리액트는 컴포넌트 내부에서 state를 통해 관리
  - html은 엘리먼트 내부에 각각의 state 코드가 존재
  
  ```html
  <form>
      <label>
          이름: 
          <input type="text" name="name" />
      </label>
      <button type="submit">제출</button>
  </form>
  ```

### Controlled Components

- 사용자가 입력한 값에 접근하고 제어할 수 있도록 해주는 컴포넌트

- 즉 값이 리액트의 통제를 받는 Input Form Element
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-11-15-22-25-image.png)

- 위의 html form 응용

```jsx
function NameForm(props) {
    const [value, setValue] = useState('')

    const handleChange = (event) => {
        setValue(event.target.value)
    }

    const handleSubmit = (event) => {
        alert('입력한 이름: ' + value)
        event.preventDefault()
    }

    return (
        <form onSubmit={handleSubmit}>
            <label>
                이름:
                <input type="text" value={value} onChange={handleChange} />
            </label>
            <button type="submit">제출</button>
        </form>
    )
}
```

- 사용자의 입력을 직접적으로 제어할 수 있음.

- 모든 입력값을 대문자로 변경
  
  ```jsx
  const handleChange= (event) => {
      setValue(event.target.value.toUpperCase())
  }
  ```

## 다양한 Forms

### Text area 태그

- 여러 줄에 걸쳐 긴 텍스트를 입력받기 위한 HTML 태그
  
  ```html
  <textarea>
      안녕하세요, 여기에 이렇게 텍스트가 들어가게 됩니다.
  </textarea>
  ```
  
  ```jsx
  function RequestForm(props) {
      const [value, setValue] = useState('요청사항을 입력하세요.')
  
      const handleChange = (event) => {
          setValue(event.target.value)
      }
  
      const handleSubmit = (event) => {
          alert('입력한 요청사항: ' + value)
          event.preventDefault()
      }
  
      return (
          <form onSubmit=handleSubmit}>
              <label>
                  요청사항:
                  <textarea value={value} onChange={handleChange} />
              </label>
              <button type="submit">제출</button>
          </form>
      )
  }
  ```

### Select 태그

- Drop-down 목록을 보여주기 위한 HTML 태그
  
  ```html
  <select>
      <option value="apple">사과</option>
      <option value="banana">바나나</option>
      <option selected value="grape">포도</option>
      <option value="watermelon">수박</option>
  </select>
  ```
  
  ```jsx
  function FruitSelect(props) {
      const [value, setValue] = useState('grape')
  
      const handleChange = (event) => {
          setValue(event.target.value)
      }
  
      const handleSubmit = (event) => {
          alert('선택한 과일: ' + value)
          event.preventDefault()
      }
  
      return (
          <form onSubmit={handleSubmit}>
              <label>
                  과일을 선택하세요: 
                  <select value={value} onChang{handleChange}>
                      <option value="apple">사과</option>
                      <option value="banana">바나나</option>
                      <option selected value="grape">포도</option>
                      <option value="watermelon">수박</option>
                  </select>
              </label>
              <button type="submit">제출</button>
          </form>
      )
  }
  ```

- 여러개의 옵션 선택 가능
  
  ```jsx
    <select multiple={true} value={['B', 'C']}>
  ```

```jsx
// input 태그
<input type="text" value={value} onChange={handleChange} />

// textarea 태그
<textarea value={value}  onChange={handleChange} />

// select 태그
<select value={value} onChange={handleChange}>
    <option value="apple">사과</ㅐ
```

```jsx
// input 태그
<input type="text" value={value} onChange={handleChange} />

// textarea 태그
<textarea value={value}  onChange={handleChange} />

// select 태그
<select value={value} onChange={handleChange}>
    <option value="apple">사과</option>
    <option value="banana">바나나</option>
    <option value="grape">포도</option>
    <option value="watermelon">수박</option>
```

### File input 태그

- 디바이스의 저장 장치로부터 하나 또는 여러개의 파일을 선택할 수 있게 해주는 HTML 태그
  
  ```
  // HTML File input 태그
  
  <input type="file" />
  ```

- Uncontrolled Component
  
  - 값이 리액트의 통제를 받지 않음

### Multiple Inputs

- 하나의 컴포넌트에서 여러 개의 입력을 다루려면 여러 개의 state를 선언하여 각각의 입력에 대해 사용

```jsx
function Reservation(props) {
        const [haveBreakfast, setHaveBreakfast] = useState(true);
        const [numberOfGuest, setNumberOfGuest] = useState(2);

        const handleSubmit = (event) => {
            alert(`아침식사 여부: ${havBreakfast}, 방문객 수: ${numberOfGuset}`);
            event.preventDefault();
        }

        return (
            <form onSubmit={handleSubmit}>
                <label>
                    아침식사 여부:
                    <input
                        type="checkbox"
                        checked={haveBreakfast}
                        onChange={(event) => {
                            setHaveBreakfast(event.target.checked);
                        }} />
                </label>
                <br />
                <label>
                    방문객 수:
                    <input
                        type="number"
                        checked={numberOfGuest}
                        onChange={(event) => {
                            setNumberOfGuest(event.target.value);
                        }} />
                </label>
                <button type="submit">제출</button>
            </form>
        )
}
```

### Input Null Value

```jsx
ReactDOM.render(<input value="hi" />, rootNode);

setTimeout(function() {
    ReactDOM.render(<input value={null} />, rootNode);
}, 1000);
```

## (실습) 사용자 정보 입력 받기

### (실습) 사용자 정보 입력 받기

```jsx
import React, { useState } from "react";

function SignUp(props) {
    const [name, setName] = useState("");

    const handleChangeName = (event) => {
        setName(event.target.value);
    };

    const handleSubmit = (event) => {
        alert(`이름: ${name}`);
        event.preventDefault();
    };

    return (
        // input태그의 value로 내용을 넣어줌. 여기선 name을 ""로 초기화 했었기 때문에 빈 입력으로 들어가 있음
        <form onSubmit={handleSubmit}>
            <label>
                이름:
                <input type="text" value={name} onChange={handleChangeName} />
            </label>
            <button type="submit">제출</button>
        </form>
    );
}

export default SignUp;
```

### (실습)성별 필드 추가하기

```jsx
import React, { useState } from "react";

function SignUp(props) {
    const [name, setName] = useState("");
    const [gender, setGender] = useState("남자");

    const handleChangeName = (event) => {
        setName(event.target.value);
    };

    const handleChangeGender = (event) => {
        setGender(event.target.value);
    };

    const handleSubmit = (event) => {
        alert(`이름: ${name} 성별: ${gender}`);
        event.preventDefault();
    };

    return (
        // input태그의 value로 내용을 넣어줌. 여기선 name을 ""로 초기화 했었기 때문에 빈 입력으로 들어가 있음
        <form onSubmit={handleSubmit}>
            <label>
                이름:
                <input type="text" value={name} onChange={handleChangeName} />
            </label>
            <br />
            <label>
                성별:
                <select value={gender} onChange={handleChangeGender}>
                    <option value="남자">남자</option>
                    <option value="여자">여자</option>
                </select>
            </label>
            <button type="submit">제출</button>
        </form>
    );
}

export default SignUp;
```

# 섹션 12. Lifing State Up

## Shared State

- State에 있는 데이터를 여러 개의 하위 컴포넌트에서 공통적으로 사용하는 경우
- 하위 컴포넌트가 공통된 부모 컴포넌트의 state를 공유하여 사용하는 것
- ex) 부모 컴포넌트:2 자식1:부모x2=4 자식2:부모x3=6 하는 경우 부모 컴포넌트의 스테이트를 공통으로 공유해서 사용하면 됨. 이런 경우를 지칭하는 게 shared state.![](assets/20230411_164333_image.png)

## 하위 컴포넌트에서 State 공유하기

```jsx
function BoilingVerdict(props) {
    if (props.celsius >= 100) {
        return <p>물이 끓습니다.</p>;
    }
    return <p>물이 끓지 않습니다.</p>;
}

function Calculator(props) {
    const [temperature, setTemperature] = useState('');

    const handleChange = (event) => {
        setTemperature(event.target.value);
    }

    return (
        <fieldset>
            <legend>섭씨 온도를 입력하세요.</legend>
            <input
                value={temperature}
                onChange={handelChange} />
            <BoilingVerdict
                celsius={parseFloat(temperature)} />
        </fieldset>
    )
}
```

## 입력 컴포넌트 추출하기

```jsx
const scaleNames = {
    c: '섭씨',
    f: '화씨'
};

function TemperatureInput(props) {
    const [temperature, setTemperature] = useState('');

    const handleChange = (event) => {
        setTemperature(event.target.value);
    }

    return (
        <fieldset>
            <legend>
                온도를 입력해 주세요(단위:{scaleNames[props.scale]}):
            </legend>
            <input value={temperture} onChange={handleChange} />  
        </fieldset>
    )
}
```

## 온도 변환 함수 작성하기

```jsx
function toCelsius(fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

function toFahrenheit(celsius) {
    return (celsius * 9 / 5) + 32'
}

function tryConver(temperature, convert) {
    const input = parseFloat(temperature);
    if (Number.isNaN(input)) {
        return '';
    }
    const output = convert(input);
    const rounded = Mate.round(output * 1000) / 1000;
    return rounded.toString();
}

tryConvert('abc', toCelsius);   // empty string을 리턴
tryConvert('10.22', toFahrenheit);   // '50.396'을 리턴
```

## Shared State 적용하기

- 하위 컴포넌트의 state를 공통 상위 컴포넌트로 올림!
  
  ```jsx
      function TemperatureInput(props) {
          const handleChange = (event) => {
              // 변경 전 : setTemperature(event.target.value);
              props.onTemperatureChange(event.target.value);
          }
  
          return (
              <fieldset>
                  <legend>
                      온도를 입력해 주세요(단위:{scaleNames[props.scale]}):
                  </legend>
                  // 변경 전 : <input value={temperture} onChange={handleChange} />
                  <input value={props.temperture} onChange={handleChange} />   
              </fieldset>
          )
      }
  ```

```jsx
function Calculator(props) {
    const [temperature, setTemperature] = useState(''); 
    const [scale, setScale] = useState('c'); 

    const handleCelsiusChange = (temperature) => {
        setTemperature(temperature);
        setScale('c');
    }

    const handleFahrenheitChange = (temperature) => {
        setTemperature(temperature);
        setScale('f');
    }

    const celsius = scale === 'f' ? tryConvert(temperature, toCelsius) : temperature;
    const fahrenheit = scale === 'c' ? tryConvert(temperature, toFahrenheit) : temperature;

    return (
        <div>
            <TemperatureInput
                scale="c"
                temperature={celsius}
                onTemperatureChange={handleCelsiusChange} />
            <TemperatureInput
                scale="f"
                temperature={fahrenheit}
                onTemperatureChange={handleFahrenheitChange} />
            <BoilingVerdict
                celsius={parseFloat(celcius)} />
        </div>
    )
}
```

![](assets/20230411_174423_image.png)

## (실습) 섭씨온도와 화씨온도 표시하기

```jsx
// TemperatureInput.jsx

const scaleNames = {
    c: "섭씨",
    f: "화씨",
};

function TemperatureInput(props) {
    const handleChange = (event) => {
        props.onTemperatureChange(event.target.value);
    };

    return (
        <fieldset>
            <legend>
                온도를 입력해 주세요(단위 : {scaleNames[props.scale]}):
            </legend>
            <input value={props.temperature} onChange={handleChange} />
        </fieldset>
    );
}

export default TemperatureInput;

## (실습) Calculator 컴포넌트 만들기

// Calculator.jsx

import React, { useState } from "react";
import TemperatureInput from "./TemperatureInput";

function BoilingVerdict(props) {
    if (props.celsius >= 100) {
        return <p>물이 끓습니다.</p>;
    }
    return <p>물이 끓지 않습니다.</p>;
}

function toCelsius(fahrenheit) {
    return ((fahrenheit - 32) * 5) / 9;
}

function toFahrenheit(celsius) {
    return ((celsius * 9) / 5 + 32;
}

function tryConver(temperature, convert) {
    const input = parseFloat(temperature);
    if (Number.isNaN(input)) {
        return "";
    }
    const output = convert(input);
    const rounded = Math.round(output * 1000) / 1000;
    return rounded.toString();
}

function Calculator(props) {
    const [temperature, setTemperature] = useState("");
    const [scale, setScale] = useState("c");

    const handleCelsiusChange = (temperature) => {
        setTemperature(temperature);
        setScale("c");
    };

    const handleFahrenheitChange = (temperature) => {
        setTemperature(temperature);
        setScale("f");
    };

    const celsius = 
        scale === "f" ? tryConvert(temperature, toCelsius) : temperature;
    const fahrenheit = 
        scale === "c" ? tryConvert(temperature, toFahrenheit) : temperature;

    return (
        <div>
            <TemperatureInput
                scale="c"
                temperature={celsius}
                onTemperatureChange={handleCelsiusChange}
            />
            <TemperatureInput
                scale="f"
                temperature={fahrenheit}
                onTemperatureChange={handleFahrenheitChange}
            />
            <BoilingVerdict celsius={parceFloat(celsius)} />
        </div>
    );
}

export default Calculator;
```

# 섹션 13. Composition vs Inheritance

## Composition 방법과 Inheritance

### Composition 방법과 Inheritance

- Composition: 합성이라는 의미에 가까움
- 여러개의 컴포넌트들을 어떻게 조합할 것인가?
  - containment, specialization, inheritance

### Containment

- Contain. 담다. 포함하다.

- 하위 컴포넌트를 포함하는 형태의 합성 방법.

- Sidebar나 Dialog 같은 Box 형태의 컴포넌트는 자신의 하위 컴포넌트를 미리 알 수 없다.

- 기본으로 제공되는 children prop을 사용!
  
  ```jsx
  // children prop을 사용한 FancyBorder 컴포넌트
  
  function FancyBorder(props) {
      return (
          <div className={'FancyBorder FancyBorder-' + props.color}>
              {props.children}
          </div>
      )
  }
  
  // FancyBorder 컴포넌트를 사용
  function WelcomeDialog(props) {
      return (
          <FancyBorder color="blue">
              <h1 className="Dialog-title">
                  어서오세요
              </h1>
              <p className="Dialog-message">
                  우리 사이트에 방문하신 것을 환영합니다.
              </p>
          </FancyBorder>
      )
  }
  ```

- 여러개의 children 집합이 필요한 경우는 어떻게 할까?
  
  - 별도로 props를 정의해서 각각 원하는 컴포넌트를 넣어주면 된다.
    
    ```jsx
    // left, right 각각 props를 정의함.
    function SplitPane(props) {
        return (
            <div className="SplitPane">
                <div className="SplitPane-left">
                    {props.left}
                </div>
                <div className="SplitPane-right">
                    {props.right}
                </div>
            </div>
        )
    }
    
    function App(props) {
        return (
            <SplitPane
                left={
                    <Contacts />
                }
                right={
                    <Chat />
                }
            />
        )
    }
    ```

### Specialization

- WelcomeDialog는 Dialog의 특별한 케이스이다.

- 범용적인 개념을 구체화하는 것 == Specialization

- 기존 객체지향 언어에서는 상속(inheritance)을 이용하여 specialization 구현.

- 리액트에선 Composition을 사용하여 specialization 구현!
  
  ```jsx
  // left, right 각각 props를 정의함.
  function Diglog(props) {
      return (
          <FancyBorder color="blue">
              <h1 className="Dialog-title">
                  {props.title}
              </h1>
              <p className="Dialog-message">
                  {props.message}
              </p>
          </FancyBorder>
      )
  }
  
  function WelcomeDialog(props) {
      return (
          <Dialog
              title="어서오세요"
              message="우리 사이트에 방문하신 것을 환영합니다."
          />
      )
  }
  ```

- Containment와 Specialization을 같이 사용하기
  
  ```jsx
  function Diglog(props) {
  return (
      <FancyBorder color="blue">
          <h1 className="Dialog-title">
              {props.title}
          </h1>
          <p className="Dialog-message">
              {props.message}
          </p>
          {props.children}
      </FancyBorder>
  )
  
  function SignUpDialog(props) {
      const [nickname, setNickname] = useState('');
  
      const handleChange = (event) => {
          setNickname(event.target.value);
      }
  
      const handleSignUp = () => {
          alert(`어서오세요, ${nickname}님!`);
      }
  
      return (
          <Dialog
              // Specialization
              title="화성 탐사 프로그램"
              message="닉네임을 입력해 주세요.">
  
              // Containment
              <input
                  value={nickname}
                  onChange={handleChange} />
              <button onClick={handleSignUp}>
                  가입하기
              </button>
          </Dialog>
      )
  }
  ```

### Inheritance

- 상속
- 부모클래스를 상속받아 자식 클래스에서 부모 클래스의 속성을 그대로 가져가는 것
- 리액트에선 다른 컴포넌트로부터 상속을 받아 새로운 컴포넌트를 만드는 것이라 생각해볼 수 있음
- 하지만 리액트에선 상속이 추천되지 않음
- 리액트에선 Specialization으로 복잡한 컴포넌트를 쪼개 여러 개의 컴포넌트로 만들고, 만든 컴포넌트들을 조합해 새로운 컴포넌트를 만드는 것이 추천됨.

## (실습) Card 컴포넌트 만들기

```jsx
// Card.jsx

function Card(props) {
    const { title, backgroundColor, children } = props;

    return (
        <div
            style={{
                margin: 8,
                padding: 8,
                borderRadius: 8,
                boxShadow: "0px 0px 4px grey",
                backgroundColor: backgroundColor || "white",
            }}
        >
            {title && <h1>{title}</h1>}
            {children}
        </div>
    );
}

export default Card;
```

```jsx
// ProfileCard.jsx

import Card from "./Card";

function ProfileCard(props) {
    return (
        <Card title="Inje Lee" backgroundColor="#4ea04e">
            <p>안녕하세요, 소플입니다.</p>
            <p>저는 리액트를 사용해서 개발하고 있습니다.</p>
        </Card>
    )
}

export default ProfileCard;
```

# 섹션 14. Context

## Context란?

### Context

- 기존엔 컴포넌트의 props로 (부모가 자식에게) 데이터 전달

- 하지만 여러 컴포넌트에서 사용하는 것은 context를 사용하는 것이 효과적

- 컴포넌트 트리를 통해 데이터를 전달하는 방식
  
  - 기존방식
    
    ![](assets/20230412_131508_image.png)
  
  - Context 사용
    
    ![](assets/20230412_131552_image.png)

- Context를 사용하면 좋은 상황 : 여러 개의 컴포넌트들이 접근해야 하는 데이터
  
  - 로그인 여부, 로그인 정보, UI 테마, 현재 언어 등

- 즉 Context는 다른 레벨의 컴포넌트가 특정 데이터를 필요로 하는 경우에 많이 사용

- ```jsx
  function App(props) {
    return <Toolbar theme="dark" />;
  }
  
  function Toolbar(props) {
    // 이 Toolbar 컴포넌트는 ThemedButton에 theme을 넘겨주기 위해서 'theme' prop을 가져야만 합니다.ㅏ
    // 현재 테마를 알아야 하는 모든 버튼에 대해서 props로 전달하는 것은 굉장히 비효율적입니다.
    return (
        <div>
            <ThemedButton theme={props.theme} />
        </div>
    );
  }
  
  function ThemedButton(props) {
    return <Button theme={props.theme} />;
  }
  ```
  
  ```jsx
  // 컨텍스트는 데이터를 매번 컴포넌트를 통해 전달할 필요 없이 컴포넌트 트리로 곧바로 전달하게 해줍니다.
  // 여기에서는 현재 테마를 위한 컨텍스트를 생성하며, 기본값은 'light'입니다.
  const ThemeContext = React.createContext('light');
  
  // Provider를 사용하여 하위 컴포넌트들에게 현재 테마 데이터를 전달합니다.
  // 모든 하위 컴포넌트들은 컴포넌트 트리 하단에 얼마나 깊이 있는지에 관계없이 데이터를 읽을 수 있습니다.
  // 여기에서는 현재 테마값으로 'dark'를 전달하고 있습니다.
  function App(props) {
    return (
        <ThemeContext.Provider value="dark">
            <Toolbar />
        </ThemeContext.Provider>
    );
  }
  
  // 이제 중간에 위차한 컴포넌트는 테마 데이터를 하위 컴포넌트로 전달할 필요가 있습니다.
  function Toolbar(props) {
    return (
        <div>
            <ThemeButton />
        </div>
    )
  }
  
  function ThemedButton(props) {
    // 리액트는 가장 가까운 상위 테마 Provider를 찾아서 해당되는 값을 사용합니다.
    // 만약 해당되는 Provider가 없을 경우 기본값(여기에서는 'light')을 사용합니다.
    // 여기에서는 상위 Provider가 있기 때문에 현재 테마의 값은 'dark'가 됩니다.
    return (
        <ThemeContext.Consumer>
            {value => <Button theme={value} />}
        </ThemeContext.Consumer>
    )
  }
  ```

- 무조건 context를 사용하는 것이 좋은 것은 아님. 컴포넌트와 컴포넌트가 연동되면 재활용성이 떨어지게 되기 때문

- Context를 사용하기 전에 고려할 점
  
  ```jsx
  // Page 컴포넌트는 PageLayout 컴포넌트를 렌더링
  <Page user={user} avatarSiza={avatarSize} />
  
  // PageLayout 컴포넌트는 NavigationBar 컴포넌트를 렌더링
  <PageLayout user={user} avatarSiza={avatarSize} />
  
  // NavigationBar 컴포넌트는 Link 컴포넌트를 렌더링
  <NavigationBar user={user} avatarSiza={avatarSize} />
  
  // Link 컴포넌트는 Avatar 컴포넌트를 렌더링
  <Link href={user.permalink}>
      <Avatar user={user} size={avatarSize} />
  </Link>
  
  // Avatar 컴포넌트를 변수로 설정하여 element variable
  ```
  
  ```jsx
  function Page(props) {
      const user = props.user;
  
      const userLink = (
          <Link href={user.permalink}>
              <Avatar user={user} size={props.avatarSize} />
          </Link>
      )
  
      // Page 컴포넌트는 PageLayout 컴포넌트를 렌더링
      // 이 때 props로 userLink를 함께 전달함.
      return <PageLayout userLink={userLink} />;
  }
  
  // PageLayout 컴포넌트는 NavigationBar 컴포넌트를 렌더링
  <PageLayout userLink={...} />
  
  // NavigationBar 컴포넌트는 props로 전달받은 userLink element를 리턴
  <NavigationLayout userLink={...} />
  ```
  
  ```jsx
  // 하위 컴포넌트를 여러 개의 변수로 나눠서 전달
  // 하위 컴포넌트의 의존성을 상위 컴포넌트와 분리해야 할 때 유용한 방법
  // 렌더링 전에 하위 컴포넌트가 상위 컴포넌트와 통신해야 하는 경우 underprops를 사용하여 처리할 수 있음.
  
  function Page(props) {
      const user = props.user;
  
      const topBar = (
          <NavigationBar>
              <Link href={user.permalink}>
                  <Avatar user={user} size={props.avatarSize} />
              </Link>
          </NavigationBar>
      )
      const content = <Feed user={user} />;
  
      return (
          <PageLayout
              topBar={topBar}
              content={content}
          />
      )
  ```

## Context API

### React.createContext()

- Context 생성
  
  ```jsx
  const MyContext = React.createContext(기본값);
  ```
  
  - 만약 상위 레벨에 매칭되는 Provider가 없다면 기본값이 사용됨.

### Context.Provider

- 데이터를 제공

- Context.Provider 컴포넌트로 하위 컴포넌트를 감싸주면 모든 하위 컴포넌트들 해당 컴포넌트의 데이터에 접근할 수 있음.

- Provider 사용
  
  ```jsx
  <MyContext.Provider value={/* some value */}></MyContext.Provider>
  ```

### Provider value에서 주의해야 할 사항

- Provider 컴포넌트가 재렌더링될 때마다 모든 하위 consumer 컴포넌트가 재렌더링 됨.
  
  ```jsx
  function App(props) {
    return (
        <MyContext.Provider value={{ something: 'something' }}
            <Toolbar />
        </MyContext.Provider>
    )
  }
  ```

// state를 사용하여 불필요한 재렌더링을 막음.
function App(props) {
    const [value, setValue] = useState({ something: 'something' })

    return (
        <MyContext.Provider value={{ something: 'something' }}
            <Toolbar />
        </MyContext.Provider>
    )

}

```
### Class.contextType
```jsx
class MyClass extends React.Component {
    componentDidMount() {
        let value = this.context;
        /* MyContext의 값을 이용하여 원하는 작업을 수행 가능 */
    }
    componentDidUpdate() {
        let value = this.context;
        /* ... */
    }
    componentWillUpmount() {
        let value = this.context;
        /* ... */
    }
    render() {
        let value = this.context;
        /* MyContext의 값에 따라서 컴포넌트들을 렌더링 */
    }
}

MyClass.contextType = MyContext;
```

### Context.Consumer

- Context의 데이터를 구독하는 컴포넌트

- class 컴포넌트에서는 class.context 타입 사용

- 함수형 컴포넌트에서는 바로 Context.Consumer 사용
  
  ```jsx
  <Mycontext.Consumer>
    {value => /* 컨텍스트의 값에 따라서 컴포넌트들을 렌더링 */}
  </Mycontext.Consumer>
  ```

### function as a child

- 컴포넌트의 자식으로 함수를 사용하는 방법
  
  ```jsx
  // children이라는 prop을 직접 선언하는 방식
  <Profile children={name => <p>이름: {name}</p>} />
  ```

// Profile 컴포넌트로 감싸서 children으로 만드는 방식
<Profile>{name => <p>이름: {name}</p>}</Profile>

```
### Context.displayName
```jsx
const MyContext = React.createContext(/* some value */)
MyContext.displayName = 'MyDisplayName'

// 개발자 도구에 "MyDisplayName.Provider"로 표시됨
<MyContext.Provider>

// 개발자 도구에 "MyDisplayName.Consumer"로 표시됨
<MyContext.Consumer>
```

### 여러 개의 Context 사용하기

- Context.Provider를 중첩해서 사용
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-12-15-26-59-image.png)

### useContext()

- 함수 컴포넌트에서 Context를 쉽게 사용하게 해 줌.
  
  ```jsx
  // useContext() Hook을 사용한 예시
  ```

function MyComponent(props) {
    const value = useContext(MyContext);

    return (
        ...
    )

}

```
```jsx
// 올바른 사용법
useContext(MyContext);

// 잘못된 사용법
useContext(MyContext.Consumer);
useContext(MyContext.Provider);
```

## (실습) Context를 사용하여 테마 변경 기능 만들기

```jsx
// ThemeContext.jsx
import React from "react";

const ThemeContext = React.createContext();
ThemeContext.displayName = "ThemeContext";

export default ThemeContext;
```

```jsx
import { useContext } from "react";
import ThemeContext from "./ThemeContext";

function MainContent(props) {
    const { theme, toggleTheme } = useContext(ThemeContext);

    return (
        <div
            style={{
                width: "100vw",
                height: "100vh",
                padding: "1.5rem",
                backgroundColor: theme == "light" ? "white" : "black",
                color: theme == "light" ? "black" : "white",
            }}
        >
            <p>안녕하세요, 테마 변경이 가능한 웹사이트 입니다.</p>
            <button onClick={toggleTheme}>테마 변경</button>
        </div>
    );
}

export default MainContent;
```

```jsx
import { useState, useCallback } from "react";
import ThemeContext from "./ThemeContext";
import MainContent from "./MainContent";

function DarkOrLight(props) {
    const [theme, setTheme] = useState("light");

    const toggleTheme = useCallback(() => {
        if (theme == "light") {
            setTheme("dark");
        } else if (theme == "dark") {
            setTheme("light");
        }
    }, [theme]);

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            <MainContent />
        </ThemeContext.Provider>
    );
}

export default DarkOrLight;
```

# 섹션 15. Styling

## CSS와 selector

### CSS

- Cascading Style Sheets

### Selector

- 선택자
- element에 스타일이 적용되는 규칙

### CSS의 기본 문법

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-12-15-44-01-image.png)

### Selector의 유형

- Element Selector
  
  ```css
  h1 {
      color: green;
  }
  ```

- ID selector
  
  ```css
  <div id="section">
      ...
  </div>
  
  #section {
      backgrount-color: black;
  }
  ```

- Class selector
  
  ```css
  <span class="medium">
      ...
  </span>
  
  <p class="medium">
      ...
  </p>
  
  .medium {
      font-size: 20px;
  }
  
  p.medium {
      font-size: 20px;
  }
  ```

- Element selector와 Class selector를 함께 사용한 예시
  
  ```css
  h1.medium {
      font-size: 20px;
  }
  ```

- Universal selector
  
  ```css
  * {
      font-size: 20px;
      color: blue;
  }
  ```

- Grouping selector
  
  ```css
  h1, h2, p {
      color: black;
      text-align: center;
  }
  ```

- Element의 상태와 관련된 selector
  
  - :hover
    - 마우스 커서가 element 위에 올라왔을 때
  - :active
    - 주로 <a> 태그(link)에 사용되는데, element가 클릭됐을 때를 의미
  - :focus
    - 주로 <input> 태그에서 사용되는데, element가 초점을 갖고 있을 경우를 의미
  - :checked
    - radio button이나 checkbox 같은 유형의 <input> 태그가 체크되어 있는 경우를 의미
  - :first-child, :last-child
    - 상위 element를 기준으로 각각 첫번째 child, 마지막 child일 경우를 의미

## 레이아웃과 관련된 CSS 속성

### 레이아웃과 관련된 속성

- 화면에 Element들을 어떻게 배치할 것인가?
  
  - display
    
    - display 속성의 대표적인 값들
      - display: none;
        - element를 화면에서 숨기기 위해 사용.
        - <script> 태그의 display 속성 기본값은 display: none;
      - display: block;
        - 블록 단위로 element를 배치
        - <p>, <div>, <h1> ~ <h6> 태그의 display 속성 기본값이 display:block;
      - display: inline;
        - element를 라인 안에 넣는 것.
        - <span> 태그의 display 속성 기본값이 display: inline;
      - display: flex;
        - element를 블록 레벨의 flex container로 표시
        - container이기 때문에 내부에 다른 element들을 표시함.
  
  - visibiliy
    
    - visibility 속성의 대표적인 값들
      - visibility: visible;
        - element를 화면에 보이게 하는 것.
      - visibility: hidden;
        - 화면에서 안 보이게 감추는 것.
        - element를 안 보이게만 하는 것이고, 화면에서의 영역은 그대로 차지.
  
  - position
    
    - position 속성의 대표적인 값들
      - static
        - 기본값으로 element를 원래의 순서대로 위치시킴.
      - fixed
        - element를 브라우저 window에 상대적으로 위치시킴.
      - relative
        - element를 보통의 위치에 상대적으로 위치시킴.
      - absolute
        - element를 절대 위치에 위치시킴.

### Flexbox

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-12-16-29-39-image.png)

## Font와 관련된 CSS 속성, 기타 많이 사용하는 CSS 속성

## styled-components

### styled-components 설치

```bash
# npm
npm install --save styled-components

# yarn
yarn add styled-components
```

### 예시

```jsx
import React from "react";
import styled from 'styled-components';

const Wrapper = styled.div`
    padding: lem;
    background: grey;
`;

const Title = styled.h1`
    font-size: 1.5em;
    color: white;
    text-align: center;
`;

function MainPage(props) {
    return (
        <Wrapper>
            <Title>
                안녕, 리액트!
            </Title>
        </Wrapper>
    )
}

export default MainPage;
```

### styled-components 사용법

- tagged template literal

- literal
  
  - 소스코드에 고정된 값
  - 상수와는 다른 개념
  - `let number = 20;`에서 20이 literal

- template literal
  - literal을 template 형태로 사용하는 문법
  - "`"사용
    ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-12-16-45-54-image.png)
    ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-12-16-46-30-image.png)



## (실습) styled-components를 사용하여 스타일링 해보기