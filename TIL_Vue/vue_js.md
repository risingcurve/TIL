# Vue.js

## Vue intro

---

### 사전 준비

- VSCode Vetur extension 설치
  - 문법 하이라이팅, 자동완성, 디버깅 기능 제공
- Chrome Vue devtools extensions 설치 및 설정
  - 크롬 브라우저 개발자 도구에서 vue 디버깅 기능 제공

### 개요

- 우리가 앞으로 할 일은 JavaScript를 활용한 Front-end 개발
- Back-end 개발은 Django로 진행
- Front-end 개발은?
  - Vue.js
  - Vue.js === JavaScript Front-end Framework

## Why Vue

### Vue는 정말 쉬울까?

- Vue 구조는 매우 직관적임

- FE Framework를 빠르고 쉽게 학습하고 활용 가능

- 추후 필요하다면, 다른 FE Framework 학습 시 빠르게 적응 가능
  
  ```jsx
  // 01_vue_intro.vue
  ```

### Vue 없이 코드 작성하기

- 입력 받은 값을 name 뒤에 출력하기

- `02_html_only.html`에서 진행
  
  ```jsx
  // 02_html_only.html
  ```
  
  1. input tag 선택
  2. P tag 선택
  3. addEventListener 추가

- 입력 받은 데이터를 p tag에 추가하려고 한다면?

- 기존에 가지고 있었던 text도 신경써야 함
  
  - data를 관리하기 위한 추가 작업이 필요함
    
    ```jsx
    // 02_html_only.html
    ```

### Vue CDN

- Vue로 작업을 시작하기 위하여 CDN을 가져와야 함

- Django == Python Web Framework
  
  - pip install

- Vue === JS Front-end Framework
  
  - Bootstrap에서 사용하였던 CDN 방식 제공
  - npm 활용은 추후에 진행 예정

- Vue CDN을 위하여 Vue2 공식 문서 접속
  
  - [https://v2.vuejs.org/](https://v2.vuejs.org/)
1. Getting Started
2. Installation
3. Development version CDN 복사

### Vue로 코드 작성하기

- 입력 받은 값을 name 뒤에 출력하기

- `03_html_vue.html`에서 진행
  
  ```jsx
  // 03_html_vue.html
  ```
1. Vue CDN 가져오기

2. Vue instance 생성
   
   - Vue instance - 1개의 Object
   - 정해진 속성명을 가진 Object

3. `el, data` 설정
   
   - data에 관리할 속성 정의

4. 선언적 렌더링 `{{}}`
   
   - Vue data를 화면에 렌더링
   
   ```jsx
   // 03_html_vue.html
   ```
- input tag에 `v-model` 작성
  
  - input에 값 입력 → Vue data 반영
  - Vue data → DOM 반영
  
  ```jsx
  // 03_html_vue.html
  ```

### [참고]Dev Tools 확인

- Vue devtools에서 data 변경 → DOM 반영
- 눈에 보이는 화면을 조작하는 것이 아닌 Vue가 가진 data를 조작

### Facebook 예시

- 한 명의 유저가 이름을 변경한다면 화면에서 조작해야할 영역이 매우 많음
- Vue를 통해 데이터를 관리한다면? = 변경 사항도 한 번에 반영

## Vue 2 vs Vue 3

---

### Vue3

- 2022년 2월부터 Vue 프레임워크의 기본 버전이 3버전으로 전환
- 대체적인 설정들이 Vue3을 기본으로 적용되어 있음
  - ex) 공식문서, CDN, npm 등

### Vue2

- 여전히 Vue2가 많이 사용됨(legacy code)
- 사용된 기간이 긴 만큼 상대적으로 많은 문서의 양, 참고자료, 질문/답변
- 안정적인 측면에서는 아직 vue2가 우세한 편

## Vue instance

---

### MVVM Pattern

- 소프트웨어 아키텍처 패턴의 일종
- 마크업 언어로 구현하는 그래픽 사용자 인터페이스**(view)**의 개발을 Back-end**(model)**로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/732b4023-9b9a-4fe8-a3df-dbf5b1d2425f/Untitled.png)

- `View` - 우리 눈에 보이는 부분 = DOM

- `Model` - 실제 데이터

- `View Model` (Vue)
  
  - View를 위한 Model
  - View와 연결(binding)되어 Action을 주고 받음
  - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
  - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨

- 정리
  
  - MVC 패턴에서 Controller를 제외하고 View Model을 넣은 패턴
  
  - View는 Model을 모르고, Model도 View를 모른다
    
    == DOM은 Data를 모른다, Data도 DOM을 모른다(독립성 증가, 적은 의존성)
  
  - View에서 데이터를 변경하면 View Model의 데이터가 변경되고, 연관된 다른 View도 함께 변경된다.

### Vue instance

- `04_vue_start.html`에서 작업 진행
  
  1. Vue CDN 가져오기
  2. new 연산자를 사용한 생성자 함수 호출
     - vue instance 생성
  3. 인스턴스 출력 및 확인
  
  ```jsx
  // 04_vue_start.html
  ```

- Vue instance === 1개의 객체

- 아주 많은 속성과 메서드를 이미 가지고 있고, 이러한 기능들을 사용하는 것

### [참고] 생성자 함수

- `05_constructor_func.js`에서 진행

- JS에서 객체를 하나 생성한다면 하나의 객체를 선언하여 생성
  
  ```jsx
  const member = {
          name: 'aiden',
          age: 22,
          sId: 2022311491,
  }
  ```

- 동일한 형태의 객체를 또 만든다면 또 다른 객체를 선언하여 생성
  
  ```jsx
  const member2 = {
          name: 'haley',
          age: 20,
          sId: 2022311492,
  }
  ```

- 동일한 구조의 객체를 여러개 만들고 싶다면?

- 생성자 함수는 특별한 함수를 의미하는 것이 아님

- `new` 연산자로 사용하는 함수

- 함수 이름은 반드시 대문자로 시작

- 생성자 함수를 사용할 때는 반드시 `new` 연산자를 사용

### el(element)

- Vue instance와 DOM을 mount(연결)하는 옵션
  
  - View와 Model을 연결하는 역할
  - HTML id 혹은 class와 마운트 가능

- Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음
  
  - Vue 속성 및 메서드 사용 불가

- `04_vue_start.html` 에서 작업 진행

- 새로운 Vue instance 생성

- 생성자 함수 첫번째 인자로 `Object` 작성

- el 옵션에 `#app` 작성 = DOM 연결

- 인스턴스 출력

- Vue와 연결되지 않은 div 생성
  
  - 두 div 모두에 `{{ message }}` 작성
  - 결과 확인

- message 속성이 정의되지 않았다는 경고와

- `{{ message }}`가 그대로 출력되는 차이

### data

- Vue instance의 **데이터 객체** 혹은 **인스턴스 속성**

- 데이터 객체는 반드시 기본 객체 **{}(Object)**여야 함

- 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음

- 정의된 속성은 `interpolation {{}}`을 통해 view에 렌더링 가능함(보간법)

- Vue instance에 `data` 객체 추가

- data 객체에 `message` 값 추가

- 결과 확인

- 추가된 객체의 각 값들은 `this.message` 형태로 접근 가능

### methods

- Vue instance의 method들을 정의하는 곳

- methods 객체 정의
  
  - 객체 내 print method 정의
  - print method 실행 시 Vue instance의 data 내 message 출력

- 콘솔창에서 app.print() 실행

- method를 호출하여 data 변경 가능
  
  - 객체 내 bye method 정의
  - print method 실행 시 Vue instance의 data 내 message 변경

- 콘솔창에서 app.bye() 실행
  
  - DOM에 바로 변경된 결과 반영
  - Vue의 강력한 반응성(reactivity)

### [주의] methods with Arrow Function

- **메서드를 정의할 때, Arrow Function을 사용하면 안 됨**

- Arrow Function의 this는 함수가 선언될 때 상위 스코프를 가리킴

- 즉 this가 상위 객체 window를 가리킴

- 호출은 문제 없이 가능하나 this로 Vue의 data를 변경하지 못함
  
  ```jsx
  const app = new Vue({
        el: '#app',   // id가 app인 element를 연결
  
        // 3. data
        data: {
          message: 'Hello, Vue!'
        },
  
        // 4. methods
        methods: {
          print: function () {
            console.log(this.message) // this == new Vue
            // console.log(this.$data.message)
          },
  
          arrowBye: () => {
            this.message = 'Arrow?' // this가 window를 가리킴
            console.log(this.message)
          },
  ```

## Basic of Syntax

---

### Template Syntax

- Vue2 guide > template syntax 참고
- **렌더링 된 DOM**을 기본 Vue instance의 data에 **선언적으로 바인딩**할 수 있는 **HTML 기반 template syntax를 사용**
  - 렌더링 된 DOM - 브라우저에 의해 보기 좋게 그려질 HTML 코드
  - HTML 기반 template syntax - HTML 코드에 직접 작성할 수 있는 문법 제공
  - 선언적으로 바인딩 - Vue instance와 DOM을 연결

### Text Interpolation

- 가장 기본적인 바인딩(연결) 방법

- 중괄호 2개로 표기

- DTL과 동일한 형태로 작성

- Template interpolation 방법은 HTML을 **일반 텍스트**로 표현
  
  ```jsx
  const app = new Vue({
    el: '#app',
    data: {
      msg: 'Text interpolation',
      rawHTML: '<span style="color:red"> 빨간 글씨</span>'
    }
  })
  ```

## Directives

### Directives 기본 구성

`v-on:submit.prevent=”onSubmit”`

`name / Argument / Modifier / Value`

### v-text

- Template Interpolation과 함께 가장 기본적인 바인딩 방법

- {{ }}와 유사한 역할
  
  - 정확히 동일한 역할은 아님

### v-html

- RAW HTML을 표현할 수 있는 방법

- 단, 사용자가 입력하거나 제공하는 컨텐츠에는 **절대 사용 금지**
  
  - XSS 공격 참고

### v-show

- 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정
  - boolean 값이 변경될 때마다 반응
- 대상 element의 display 속성을 기본 속성과 none으로 toggle
- 요소 자체는 항상 DOM에 렌더링 됨
- 바인딩된

### v-if

- v-show와 사용 방법은 동일
- isAcitve의 값이 변경될 때 반응
- 단, 값이 false인 경우 DOM에서 사라짐
- v-if v-else-if v-else 형태로 사용

### v-show VS v-if

- v-show(Expensive initial load, cheap toggle)
  - 표현식 결과와 관계 없이 렌더링 되므로 초기에 렌더링에 필요한 비용은 v-if 보다 높을 수 있음
  - display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음
- v-if
  - 표현식 결과가 false인 경우 렌더링 조차 되지 않으므로

### v-for

### [참고] 특수 속성 key

- **v-for 사용 시 반드시 key 속성을 각 요소에 작성**
- 주로 v-for directive 작성 시 사용
- vue 화면 구성 시 이전과 달라진 점을 확인하는 용도로 활용
  - 따라서 key가 중복되어서는 안 됨
- 각 요소가 고유한 값을 가지고 있다면 생략할 수 있음

### v-on

- method를 통한 data 조작도 가능
- method에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식
- ‘:’을 통해 전다된 인자에 따라 특별한 modifiers(수식어)가 있을 수 있음.

### v-bind

- Vue data의 변화에 반응하여 DOM

### v-model

- `09_basic_of_syntax_4.html`에서 작성
- **양방향 바인딩**
- Vue data 변경 시 v-model로 연결된 사용자 입력 element에도 연결됨

## Vue advanced

---

### computed

- Vue instance가 가진 options 중 하나
- computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
  - 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 값을반환
- `10_computed.html`에서 methods와의 차이 확인

### methods VS computed

- methods
  - 호출될 때 마다 함수를 실행
  - 같은 결과여도 매번 새롭게 계산
- computed
  - 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
  - 종속 대상이 변하지 않으면

### watch

- 특정 데이터의 변화를 감지하는 기능
  
  1. watch 객체를 정의
  2. 감시할 대상 data를 지정
  3. data가 변할 시 실행할 함수를 정의

- 첫 번째 인자는 변동 전 data

- 두 번째 인자는 변동 후 data

- 실행 함수를 Vue method로 대체 가능
  
  1. 감시 대상 data의 이름으로 객체 생성
  2. 실행하고자 하는 method를 handler에 문자열 형태로 할당

- Array, Object의 내부 요소 변경을 감지를 위해서는 `deep` 속성 추가 필요

### filters

- 텍스트 형식화를 적용할 수 있는 필터
- interpolation 혹은 v-bind를 이용할 때 사용 가능
- 필터는 자바스크립트 표현식 마지막에 `‘|’`(파이프)와 함께 추가되어야 함
- 이어서 사용(chaning) 가능

## Vue Style Guide

---

### Vue Style Guide

- Vue의 스타일 가이드 규칙은 우선순위를 기준으로 4가지 범주를 설정
- 우선순위
  - A : 필수
  - B : 적극 권장
  - C : 권장
  - D : 주의 필요

### 우선 순위 특징

- A : 오류를 방지하는데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수
- B : 규칙을 어겨도 코드는 여전히 실행되겠지만, 규칙 위반은 드물어야 함
- C : 일관성을 보장하도록 임의의 선택을 할 수 있음
- D : 잠재적 위험 특성을 고려함

### 우선순위 A

1. v-for는 항상 key와 함께 사용하기
   - 내부 컴포넌트 상태를 일관되게 유지하기 위해 v-for에 항상 key를 사용하기
2. v-for를 쓴 엘리먼트에 절대 v-if를 사용하지 말기
   - 데이터의 예측 가능한 행동을 유지 시키기(객체 불변성)
   - 함께 쓸 수 있다고 생각되는 2가지 경우
     - 목록의 항목을 필터링할 때
       - v-if가 먼저 계산되고, 해당 처리 시점에 반복 변수인 user가 존재하지 않기 때문에 에러 발생
       - Vue가 디렉티브를 처리할 때, v-if가 v-for 보다 높은 우선순위를 가짐
     - 숨김 목록의 렌더링을 피할 때
       - v-if를 컨테이너 엘리먼트로 옮기기
         - 더 이상 목록의 사용자에 대해

### 우선순위 B

# Vue CLI

## Node.js

### Node.js

- 자바스크립트는 브라우저를 조작하는 유일한 언어
  - 하지만 브라우저 밖에서는 구동할 수 없었음
- 자바스크립트를 구동하기 위한 런타임 환경인 Node.js로 인해 브라우저가 아닌 환경에서도 구동할 수 있게 됨
  - Chrome V8 엔진을 제공하여 여러 OS 환경에서 실행할 수 있는 환경을 제공
  - Browser만 조작 가능했으나, Server-side-programming 또한 가능

### NPM

- 자바스크립트 패키지 관리자
  - Python에 pip가 있다면 Node.js에는 npm
  - pip와 마찬가지로 다양한 의존성 패키지를 관리
- Node.js의 기본 패키지 관리자
- Node.js 설치 시 함께 설치됨

## Vue CLI

### Vue CLI

- Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- 확장 플러그인, GUI, Babel등 다양한 tool 제공

### Vue CLI Quick Start

- 설치
  
  - `$ npm install -g @vue/cli` (-g는 글로벌)

- 프로젝트 생성
  
  - **vscode terminal에서 진행**
  - `$ vue create vue-cli`

- Vue 버전 선택(Vue 2)
  
  - `Default ([Vue 2] babel, eslint)`

- ## 프로젝트 생성 성공

- 서버 켜기
  
  - `npm run serve`

```jsx
Local : 로컬 주소
Newwork : 모바일 접속 주소
```

## Vue CLI 프로젝트 구조

### node_modules - Babel

- 자바스크립트 컴파일러
- 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환해 주는 도구
- 자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
  - 최신 문법을 사용해도 브라우저의 버전 별로 동작하지 않는 상황이 발생
  - 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고, 이러한 문제를 해결하기 위한 도구
  - 원시 코드(최신 버전)를 목적 코드(구버전)으로 옮기는 번역기가 등장하면서 _ _상 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않는

### Babel 동작 예시

### node_moduls - Webpack

- static module bundler
- 모듈 간의 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함

### Module

- 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐
- 따라서 자연스럽게 팡리을 여러 개로 분리하여 관리하게 되었고, 이 때 분리된 파일 각각이 모듈 즉 js 파일 하나가 하나의 모듈
- 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨
- 여러 모듈 시스템

### Module의 의존성 문제

- 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
  - Webpack은 이 모듈 간의 의존성 문제를 해결하기 위해 등장

### Bundler

- 모듈 의존성 문제를 해결해 주는 작업이 Bundling
- 이러한 일을 해주는 도구가 번들러고, 웹팩은 다양한 번들러 중 하나
- 모듈들을 하나로 묶어주고 묶인 파일은 하나(또는 여러개)로 만들어짐
- 번들링된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작하게 됨
- 스노우팩, 파슬, 롤업제이에스 등의 웹팩 이외에도 다양한 모듈 번들러 존재

### node_modules의 의존성 깊이

- 태양, 블랙홀 보다 훨씬 깊음

### Webpack - static module bundler

### package.json

### package-lock.json

- node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
- 사용할 패키지의 버전을 고정
- 개발 과정 간의 의존성 패키지 충동 방지
- python의 requirements.txt 역할

### publick/index.html

- Vue 앱의 뼈대가 되는 html 파일
- Vue 앱과 연결될 요소가 있음

### src

- src/asset
  - 정적 파일을 저장하는 디렉토리
- src/components
  - 하위 컴포넌트들이 위치
- src/App.vue
  - 최상위 컴포넌트
  - public/index.html
- scr/main.js
  - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
  - public/index.html과

# SFC

---

## Component

---

### Component

- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
  - 즉, 기능별로 분화한 코드 조각
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임
  - Web 시간에 배운 HTML 요소들의 중첩들을 떠올려보자
    - Body tag를 root node로 하는 tree의 구조이다.
    - 마찬가지로, Vue에서는 src/App.

### Django에서의 예시

- 우리는 base.html과 index.html을 분리하여 작성하였지만, 하나의 화면으로 볼 수 있다.
  - 즉, 한 화면은 여러개의 컴포넌트로 이루어질 수 있음
- base.html을 변경하면 이를 extends하는 모든 화면에 영향을 미침
  - 유지 보수를 쉽게 해 줌
- index.html 에서 for문을 통해 여러 게시글들을

### Component based architecture 특징

- 관리가 용이

## SFC

---

### component in Vue

- 그렇다면 Vue에서 말하는 component란 무엇일까?
  - 이름이 있는 재사용 가능한 Vue instance
- 그렇다면 Vue instance란?
  - 앞서 수업에서

### SFC(Single File Component)

- 하나의 .vue 파일이 하나의 Vue instance이고, 하나의 컴포넌트이다.
  - 즉 싱글 파일 컴포넌트
- Vue instance에서는 HTML, CSS, Javascript 코드를 한번에 관리,
  - 이 Vue instance를 기능 단위로 작성하는 것이 핵심!
- 컴포넌트 기반 개발의 핵심 기능

### 정리

- HTML, CSS, 그리고 Javascript를 .vue라는
- 이 파일을 Vue instance, 또는 Vue component
- Vue CLI가 Vue를 Component based하게 사용

## Vue component

---

### Vue component 구조

- 템플릿
- 스크립트
  - 자바스크립트 코드가 작성되는 곳
  - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨
  - 문법이 약간 바뀜(ex. const app = new Vue () 안 함)
- 스타일
  - CSS가 작성되며 컴포넌트의 스타일을 담당

### Vue component 구조 정리

- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
- root 에 해당하는 최상단의 component가 App.vue
- 이 App. vue를 index.html과 연결
- 결국 index.html 파일 하나만을 rendering
  - 이게 바로 SPA

### 현재 구조

- Vue CLI를 실행하면 이미 HelloWorld.vue라는 컴포넌트가 생성되어 있고 App.vue에 등록되어 사용되고 있음
  - npm run serve 명령어를 진행했을 때 나온 화면의 대부분이 HelloWorld.vue

### MyComponent.vue

1. src/components/ 안에 생성
2. script에 이름 등록
3. template에 요소 추가
   - 주의) templates 안에는 반드시 하나의 요소

### component 등록 3단계

1. 불러오기
2. 등록하기
3. 보여주기

### 불러오기

- `import {instance name} from {위치}`
- instance name은 instance 생성 시 작성한 name
- `@`는 src의 shortcut
- `.vue` 생략 가능

# Pass Props &

## Data in components

### Data in components

- 우리는 정적 웹페이지가 아닌, 동적 웹페이지를 만들고 있음
  
  - 즉, 웹페이지에서 다뤄야 할 데이터가 등장

- MyChild에도 똑같은 data를 정의
  
  - MyComponent의 data와 MyChild의 데이터가 동일한 data가 맞는가?
  - MyComponent의 data가 변경된다면 MyChild도 같이 변경이 될까?
  - 아니다. 각 Component는 독립적이므로 서로 다른 data를 갖게 될 것이다.
  - 그렇다면 완전히 동일한 data를

- 필요한 컴포넌트들끼리 데이터를 주고 받으면 될까?

- 데이터의 흐름을 파악하기 힘듦

- 개발 속도 저하

- 유지보수 난이도 증가

- 컴포넌트는 부모-자식 관계를 가지고 있으므로, 부모-자식 관계만 데이터를 주고받게 하자!

- 데이터의 흐름을 파악하기 용이

- 유지 보수하기 쉬워짐

- 부모 → 자식으로의 데이터의 흐름
  
  - pas props

- 자식 → 부모로의 데이터 흐름
  
  - emit event

### Pass Props

- 요소의 속성을 사용하여 데이터 전달
- props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props 명시적으로 선언해야 함
- 부모 ⇒ 자식으로의 data 전달 방식을 pass props라고 함
- 정적인 데이터를 전달하는 경우 static props 라고 명시하기도 함
- 요소에 속성을 작성하듯이 사용 가능하여, prop-data-name=”value”의 형태로 데이터를 전달
  - 이 때 속성의 키 값은 kebab-case를 사용
- Props

### props in HelloWorld

- 사실, 우리의 Vue app은 이미 props를 사용하고 있었다
- Vue CLI를 설치할 때 만들어주었던 App.vue의 HelloWorld 컴포넌트를 살펴보면
- App.vue의 <HelloWorld/> 요소에 msg=”~” 라는 property를 살펴보면

### MyComponent to MyChild

- 부모에서 넘겨주는 props
- 자식에서 받는 props
- 부모 템플리셍서 kebab-case로 넘긴 변수를 자식의 스크립트에서 자동으로 camelCase로

### Dynamic props

- 변수를 props로 전달할 수 있음
- v-bind directive를 사용해 데이터를 동적으로 바인딩
- 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨

### 컴포넌트의 data 함수

- 각 vue 인스턴스는 같은 data객체를 공유하므로 새로운 data 객체를 반환하여 사용해야 함
  
  ```jsx
  data : function () {
      return {
          // component's data in here    
      }
  }
  ```

### Pass Props

- :dynamic-props = dynamicProps
- dd
- v-bind로 묶어있는 “” 안의 구문은 자바스크립트의 구문으로 볼 수 있다
  - 따라서 dynamicProps 라고 하는 변수에 대한 data를 전달할 수 있는 것
- 그렇다면 숫자를 props로 전달하기 위해서 다음 두 방법 중 어떤 게 맞을까?

### 단방향 데이터 흐름

- 모든 props 는 부모에서 자식으로 즉 아래로 단방향 바인딩을 형성
- 부모 속성이 업데이트되면 자식으로 흐르지만 반대 방향은 아님
  - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop들이 최신 값으로 새로고침 됨
- 목적
  - 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지
- 하위 컴포넌트에서 prop를 변경하려고 시도해서는 안 되며 그렇게 하면 Vue는 콘솔에서 경고함

### Emit Event

- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 이벤트를 발생시킴
- 이벤트를 발생시키는 게 어떻게 데이터를 전달하는 것이냐?
  1. 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
  2. 상위 컴포넌트는 해당 이벤트를 통해 데이터를 받음

### $emit

- $emit 메서드를 통해 부모 컴포넌트에 이벤트를 발생
  - $emit

### Emit Event

1. 자식 컴포넌트에 버튼을 만들고 클릭 이벤트를 추가
2. $emit을 통해 부모 컴포넌트에게 child-to-parent

### Emit Event 흐름 정리

1. 자식 컴포넌트에 있는 버튼을 클릭 이벤트를 청취하여 연결된 핸들러 함수(ChildToParent) 호출
2. 호출된 함수에서 $emit을 통해 상위 컴포넌트에 이벤트 발생
3. 상위 컴포넌트는 자식 컴포넌트가 발생시킨 이벤트(child-to-parent)를 청취하여 연결되

### emit with data

이렇게 전달한 데이터는 이벤트와 연결된 부모 컴포넌트의 핸들러

# Vuex

## Vuex

---

### 개요

- 상태 관리가 무엇인지 이해하기
- Vuex가 무엇인지, 왜 필요한지 이해하기
- Vuex 기본 문법 알아보기

### 상태 관리

`State Management`

- 상태란?
  
  - 현재에 대한 정보(data)

- 나의 상태가 어때? 라는 질문에 어떻게 대답할 수 있을까?
  
  - 배가 고픈 상태야
  - 밤새 공부했더니 졸린 상태야
  - 강의를 열심히 들었더니 자신감이 넘치는 상태야

- 우리는 여러개의 컴포넌트를 조합해서 하나의 App을 만들고 있음

- 각 컴포넌트는 독립적이기 때문에 각각의 상태를 가짐

- 하지만 결국 이러한 컴포넌트들이 모여서 하나의 App을 구성할 예정
  
  즉 여러 개의 컴포넌트가 같은 상태를 유지할 필요가 있음
  
  → 상태 관리 필요

### Pass Props & Emit Event

- 지금까지 우리는 props와 event를 이용해서 상태 관리를 하고 있음

- 각 컴포넌트는 독립적으로 데이터를 관리

- 같은 데이터를 공유하고 있으므로, 각 컴포넌트가 동일한 상태를 유지하고 있음

- 데이터의 흐름을 직관적으로 파악 가능

- 그러나 컴포넌트의 중첩이 깊어지면 데이터 전달이 쉽지 않음

- 공통의 상태를 유지해야 하는 컴포넌트가 많아지면 데이터 전달 구조가 복잡해짐

- 만약 A에서 B로 데이터를 전달해야 한다면?
  
  → 어떻게 하면 쉽게 해결할 수 있을까?

### Centralized Store

- 중앙 저장소에 데이터를 모아서 상태 관리
- 각 컴포넌트는 중앙 저장소의 데이터를 사용
- 컴포넌트의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경할 수 있음
- 중앙 저장소의 데이터가 변경되면 각각의 컴포넌트는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영함
- 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리

### Vuex

- “state management pattern + Library” for vue.js(상태 관리 패턴 + 라이브러리)
- 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경될 수 있도록 하는 규칙을 설정하며, Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공
- Vue의 공식 도구로서 다양한 기능을 제공

### 프로젝트 with vuex

```bash
$ vue create vuex-app  // Vue 프로젝트 생성

$ cd vuex-app          // 디렉토리 이동

$ vue add vuex         // Vue CLI를 통해 vuex plugin 적용
```

- src / store / index.js가 생성됨

- vuex의 핵심 컨셉 4가지
  
  1. state
  2. getters
  3. mutations
  4. actions
  
  ```jsx
  // index.js
  
  import Vue from 'vue'
  import Vuex from 'vuex'
  
  Vue.use(Vuex)
  
  export default new Vuew.Store({
      state: {
      },
      getters: {
      },
      mutations: {
      },
      actions: {
      },
      modules: {
      },
  })
  ```

### Vue와 Vuex 인스턴스 비교

```jsx
< Vue 인스턴스 >

export default {
    name: 'VueInstance',
    data: function() {
        return {
        }
    },
    computed: {
    },
    methods: {
    },
}
```

```jsx
< Vuex 인스턴스 >

export default new Vuex.Store({
    state: {
    },
    getters: {
    },
    mutationss: {
    },
    actions: {
    },
    modules: {
    }
})
```

### 1. State

- vue 인스턴스의 data에 해당
- **중앙에서 관리하는 모든 상태 정보**
- 개별 컴포넌트는 state에서 데이터를 가져와서 사용
  - 개별 컴포넌트가 관리하던 데이터를 중앙 저장소에서 관리하게 됨
- state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 컴포넌트도 자동으로 다시 렌더링
- `$store.state`로 state 데이터에 접근

### 2. Mutations

- **실제로 state를 변경하는 유일한 방법**
- vue 인스턴스의 methods에 해당하지만 Mutations에서 호출되는 핸들러 함수는 반드시 `동기적`이어야 함
  - 비동기 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화의 시기를 특정할 수 없기 때문
- 첫 번째 인자로 `state`를 받으며, 컴포넌트 혹은 Actions에서 `commit()` 메서드로 호출됨
- mutations, action에서 호출되는 함수를 handler 함수라고 함

### 3. Actions

- mutations와 비슷하지만 `비동기` 작업을 포함할 수 있다는 차이가 있음
- **state를 직접 변경하지 않고 commit() 메서드로 mutations를 호출해서 state를 변경함**
- context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음
- component에서 `dispatch()` 메서드에 의해 호출됨

### Mutations & Actions

- 뷰 컴포넌트의 메서드 역할이 vuex에서는 아래와 같이 분화됨
- Mutations
  - state를 변경
- Actions
  - state 변경을 제외한 나머지 로직

### 4. Getters

- vue 인스턴스의 computed에 해당
- **state를 활용하여 계산된 값을 얻고자 할 때 사용**
- state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
- computed와 마찬가지로 getters의 결과는 캐시(cache)되며, 종속된 값이 변경된 경우에만 재계산됨
- getters에서 계산된 값은 state에 영향을 미치지 않음
- 첫번째 인자로 `state`, 두번째 인자로 `getter`를 받음

### 그럼 이제 모든 데이터를 Vuex에서 관리해야 할까?

- Vuex를 사용한다고 해서 모든 데이터를 state에 넣어야 하는 것은 아님
- Vuex에서도 여전히 pass props, emit event를 사용하여 상태를 관리할 수 있음
- 개발 환경에 따라 적절하게 사용하는 것이 필요함

### 정리

- state
  - 중앙에서 관리하는 **모든 상태 정보**
- mutations
  - **state를 변경**하기 위한 methods (동기 작업)
- actions
  - **비동기 작업이 포함될 수 있는(외부 API와의 소통 등)** methods
  - state를 변경하는 것 외의 모든 로직 진행
- getters
  - state를 활용해 **계산한 새로운 변수 값**
- component에서 데이터를 조작하기 위한 데이터의 흐름
  - **component ⇒ (actions) ⇒ mutations ⇒ state**
  - 별다른 액션이 필요하지 않은 경우도 있음(생략 가능)
- component에서 데이터를 사용하기 위한 데이터의 흐름
  - state ⇒ (getters) ⇒ component

<<<<<<< HEAD

# Vue Router

---

## Routing

---

### Routing

- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
  - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
- 예시
  - /articles/index/에 접근하면 articles의 index에 대한 결과를 보내 줌

### Routing in SSR

- Server가 모든 라우팅을 통제 (← 장고의 경우 views.py가 통제)
- URL로 요청이 들어오면 응답으로 완성된 HTML 제공
  - Django로 보낸 요청의 응답 HTML은 완성본인 상태였음
- 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐

### Routing in SPA / CSR

- 서버는 하나의 HTML(index.html) 만을 제공
- 이후에 모든 동작은 하나의 HTML 문서 위에서 자바스크립트 코드를 활용
  - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
- 즉 하나의 URL만 가질 수 있음

### Why routing?

- 그럼 동작에 따라 URL이 반드시 바뀌어야 하나?
  
  그렇지는 않다. 단 유저의 사용성 관점에서는 필요함

- Routing이 없다면,
  
  - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
  - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - 새로고침 시 처음 페이지로 돌아감
    - 링크를 공유할 시 처음 페이지만 공유 가능
  - 브라우저의 뒤로 가기 기능을 사용할 수 없음

## Vue Router

---

### Vue Router

- Vue의 공식 라우터
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
  - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
  - SPA의 단점 중 하나인 “URL이 변경되지 않는다.”를 해결
- [참고] MPA(Multiple Page Application)
  - 여러 개의 페이지로 구성된 애플리케이션
  - SSR 방식으로 렌더링

### Vue Router 시작하기

- Vuex와 마찬가지의 방식으로 설치 및 반영
  
  ```bash
  $ vue create vue-router-app    // Vue 프로젝트 생성
  
  $ cd vue-router-app            // 디렉토리 이동
  
  $ vue add router               // Vue CLI를 통해 router plugin 적용
  ```

- history mode 사용여부 → Yes
  
  ```bash
  ? Use history mode for router? (Requires proper server setup for index fallback 
  in production) (**Y**/n)
  ```

### History mode

- 브라우저의 History API를 활용한 방식
  
  - 새로고침 없이 URL 이동 기록을 남길 수 있음

- 우리에게 익숙한 URL 구조로 사용 가능
  
  - 예시) http://localhost:8080/index

- [참고] History mode를 사용하지 않으면 Default 값인 hash mode로 설정됨(’#’을 통해 URL을 구분하는 방식)
  
  - 예시) [http://localhost:8080#index](http://localhost:8080#index)

- App.vue
  
  - router-link 요소 및 router-view가 추가됨

### router-link

- a 태그와 비슷한 기능 → URL을 이동시킴
  - routes에 등록된 컴포넌트와 매핑됨
  - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
  - 목표 경로는 ‘to’ 속성으로 지정됨
  - 기능에 맞게 HTML에서 a 태그로 rendering 되지만, 필요에 따라 다른 태그로 바꿀 수 있음

### router-view

- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미
- router-link를 클릭하면 route에 매핑된 컴포넌트를 렌더링
- Django에서의 block tag와 비슷함
  - App.vue는 base.html의 역할
  - router-view는 block 태그로 감싼 부분

### src/router/index.js

- 라우터에 관련된 정보 및 설정이 작성되는 곳
- Django에서의 urls.py에 해당
- routes에 URL와 컴포넌트를 매핑
- Django와의 비교

### src/Views

- router-view에 들어갈 component 작성

- 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나누어짐

- 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님# Vue Router
  
  ---
  
  ## Routing
  
  ---
  
  ### Routing
  
  - 네트워크에서 경로를 선택하는 프로세스
  - 웹 서비스에서의 라우팅
    - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
  - 예시
    - /articles/index/에 접근하면 articles의 index에 대한 결과를 보내 줌
  
  ### Routing in SSR
  
  - Server가 모든 라우팅을 통제 (← 장고의 경우 views.py가 통제)
  - URL로 요청이 들어오면 응답으로 완성된 HTML 제공
    - Django로 보낸 요청의 응답 HTML은 완성본인 상태였음
  - 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐
  
  ### Routing in SPA / CSR
  
  - 서버는 하나의 HTML(index.html) 만을 제공
  - 이후에 모든 동작은 하나의 HTML 문서 위에서 자바스크립트 코드를 활용
    - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
  - 즉 하나의 URL만 가질 수 있음
  
  ### Why routing?
  
  - 그럼 동작에 따라 URL이 반드시 바뀌어야 하나?
    
    그렇지는 않다. 단 유저의 사용성 관점에서는 필요함
  
  - Routing이 없다면,
    
    - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
    - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
      - 새로고침 시 처음 페이지로 돌아감
      - 링크를 공유할 시 처음 페이지만 공유 가능
    - 브라우저의 뒤로 가기 기능을 사용할 수 없음
  
  ## Vue Router
  
  ---
  
  ### Vue Router
  
  - Vue의 공식 라우터
  - SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
  - 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
    - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
    - SPA의 단점 중 하나인 “URL이 변경되지 않는다.”를 해결
  - [참고] MPA(Multiple Page Application)
    - 여러 개의 페이지로 구성된 애플리케이션
    - SSR 방식으로 렌더링
  
  ### Vue Router 시작하기
  
  - Vuex와 마찬가지의 방식으로 설치 및 반영
    
    ```bash
    $ vue create vue-router-app    // Vue 프로젝트 생성
    
    $ cd vue-router-app            // 디렉토리 이동
    
    $ vue add router               // Vue CLI를 통해 router plugin 적용
    ```
  
  - history mode 사용여부 → Yes
    
    ```bash
    ? Use history mode for router? (Requires proper server setup for index fallback 
    in production) (**Y**/n)
    ```
  
  ### History mode
  
  - 브라우저의 History API를 활용한 방식
    
    - 새로고침 없이 URL 이동 기록을 남길 수 있음
  
  - 우리에게 익숙한 URL 구조로 사용 가능
    
    - 예시) http://localhost:8080/index
  
  - [참고] History mode를 사용하지 않으면 Default 값인 hash mode로 설정됨(’#’을 통해 URL을 구분하는 방식)
    
    - 예시) [http://localhost:8080#index](http://localhost:8080#index)
  
  - App.vue
    
    - router-link 요소 및 router-view가 추가됨
  
  ### router-link
  
  - a 태그와 비슷한 기능 → URL을 이동시킴
    - routes에 등록된 컴포넌트와 매핑됨
    - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
    - 목표 경로는 ‘to’ 속성으로 지정됨
    - 기능에 맞게 HTML에서 a 태그로 rendering 되지만, 필요에 따라 다른 태그로 바꿀 수 있음
  
  ### router-view
  
  - 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
  - 실제 component가 DOM에 부착되어 보이는 자리를 의미
  - router-link를 클릭하면 route에 매핑된 컴포넌트를 렌더링
  - Django에서의 block tag와 비슷함
    - App.vue는 base.html의 역할
    - router-view는 block 태그로 감싼 부분
  
  ### src/router/index.js
  
  - 라우터에 관련된 정보 및 설정이 작성되는 곳
  - Django에서의 urls.py에 해당
  - routes에 URL와 컴포넌트를 매핑
  - Django와의 비교
  
  ### src/Views
  
  - router-view에 들어갈 component 작성
  
  - 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나누어짐
  
  - 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
    =======
    
    ## Vuex 실습

### 시작하기 전 - Object method shorthand

- 이제부터는 객체 메서드 축약형을 사용할 것
  
  ```jsx
  // before
  const obj1 = {
      addValue: function (value) {
          return value
      },
  }
  
  // after
  const obj2 = {
      addValue(value) {
          return value
      },
  }
  ```

### src / store / index.js

- vuex의 핵심 컨셉 4가지
  
  - state
  
  - getters
  
  - mutations
  
  - actions
    
    ```jsx
    // store/index.js
    
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      state: {
      },
      getters: {
      },
      mutations: {
      },
      actions: {
      },
      modules: {
      }
    })
    ```

### state

- 중앙에서 관리하는 모든 상태 정보

- `$store.state`로 접근 가능

- store의 state에 message 데이터 정의
  
  ```jsx
  // store/index.js
  
  import Vue from 'vue'
  import Vuex from 'vuex'
  
  Vue.use(Vuex)
  
  export default new Vuex.Store({
    state: {
          message: 'message in store'
    },
    getters: {
    },
    mutations: {
    },
    actions: {
    },
    modules: {
    }
  })
  ```

- component에서 state 적용
  
  ```jsx
  // App.vue
  
  <template>
    <div id="app">
      <h1>{{ $store.state.message }}</h1>
    </div>
  </template>
  ```

- $store.state로 바로 접근하기 보다 computed에 정의 후 접근하는 것을 권장
  
  ```jsx
  // App.vue
  
  <template>
    <div id="app">
      <h1>{{ message }}</h1>
    </div>
  </template>
  
  <script>
      export default {
        name: 'App',
        computed: {
          message() {
            return this.$store.state.message
          },
        }
      }
  </script>
  ```

- Vue 개발자 도구에서의 Vuex

- 관리 화면을 Vuex로 변경

- 관리되고 있는 state 확인 가능

### actions

- state를 변경할 수 있는 **mutations 호출**

- component에서 **`dispatch()`에 의해 호출됨**

- `dispatch(A, B)`
  
  - A : 호출하고자 하는 actions 함수
  - B : 넘겨주는 데이터(payload)

- actions에 정의된 changeMessage 함수에 데이터 전달하기

- component에서 actions는 dispatch()에 의해 호출됨
  
  ```jsx
  <template>
    <div id="app">
      <h1>{{ message }}</h1>
      <input type="text" @keyup.enter="changeMessage" v-model="inputData">
    </div>
  </template>
  
  <script>
      export default {
          ...
        data() {
          return {
            inputData: null,
          }
        },
        methods: {
          changeMessage() {
            const newMessage = this.inputData
            **this.$store.dispatch('changeMessage', newMessage)**
            this.inputData = null
          },
        },
      }
  </script>
  ```

- actions의 첫 번째 인자는 `context`
  
  - context는 store의 전반적인 속성을 모두 가지고 있으므로 context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능
  - dispatch()를 사용해 다른 actions도 호출할 수 있음
  - **단 actions에서 state를 직접 조작하는 것은 삼가야 함**

- actions의 두 번째 인자는 `payload`
  
  - 넘겨준 데이터를 받아서 사용
  
  ```jsx
  // store/index.js
  
  export default new Vuex.Store({
      ...
      actions: {
      changeMessage(context,newMessage) {
        // console.log(context)
        // console.log(message)
      },
    },
      ...
  })
  ```

### mutations

“actions에서 commit()을 통해 mutations 호출하기”

- mutations는 state를 변경하는 유일한 방법

- component 또는 actions에서 **commit()에 의해 호출됨**

- `commit(A, B)`
  
  - A : 호출하고자 하는 mutations 함수
  - B : payload
  
  ```jsx
  // store/index.js
  
  export default new Vuex.Store({
      ...
  
      actions: {
        changeMessage(context,newMessage) {
        **context.commit('CHANGE_MESSAGE', newMessage)**
      },
    },
      ...
  })
  ```

“mutations 함수 작성하기”

- mutations는 state를 변경하는 유일한 방법

- mutations 함수의
  
  - 첫 번째 인자는 state
  - 첫 번째 인자는 payload
  
  ```jsx
  // store/index.js
  
  export default new Vuex.Store({
      ...
  
      mutations: {
        CHANGE_MESSAGE(state, newMessage) {
          // console.log(state)
          // console.log(newMessage)
          state.message = newMessage
        }
      },
      ...
  })
  ```

### getters

“getters 사용해 보기”

- **getters는 state를 활용한 새로운 변수**

- getter 함수의
  
  - 첫 번째 인자는 state
  - 첫 번째 인자는 getters
  
  ```jsx
  export default new Vuex.Store({
  ...
  
  getters: {
      messageLength(state) {
        return state.message.length
      },
    },
      ...
  })
  ```

“getter의 다른 함수 사용해 보기”

```jsx
// store/index.js

export default new Vuex.Store({
    ...

  getters: {
    messageLength(state) {
      return state.message.length
    },

    // messageLength를 이용해서 새로운 값을 계산
    doubleLength(state, getters) {
      return getters.messageLength * 2
    },
  },
    ...
})
```

“getters 출력하기”

- getters 역시 state와 마찬가지로 computed에 정의해서 사용하는 것을 권장
  
  ```jsx
  // App.vue
  
  ...
  <script>
      export default {
          ...
          computed: {
      message() {
        return this.$store.state.message
      },
      messageLength() {
        return this.$store.getters.messageLength
      },
      doubleLength() {
        return this.$store.getters.doubleLength
      },
    },
      ...
  }
  </script>
  ```
  
  ```jsx
  // App.vue
  
  <template>
    <div id="app">
      <h1>{{ message }}</h1>
      <h2>입력된 문자의 길이는 {{ messageLength }}</h2>
      <h3>x2 : {{ doubleLength }}</h3>
      <input type="text" @keyup.enter="changeMessage" v-model="inputData">
    </div>
  </template>
  ```

# Lifecycle Hooks

---

## Lifecycle Hooks

---

### Lifecycle Hooks

- 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
  - Vue 인스턴스가 생성된 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM를 업데이트하는 경우 등
- 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
- 이를 Lifecycle Hooks이라고 함

### Lifecycle Hooks 맛보기

### created

- Vue instance가 생성된 후 호출됨

- data, computed 등의 설정이 완료된 상태

- 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적합

- 단 mount되지 않아 요소에 접근할 수 없음

- 자바스크립트에서 학습한 Dog API 활용 실습의 경우 버튼을 누르면 강아지 사진을 보여줌

- 버튼을 누르지 않아도 첫 실행 시 기본 사진이 출력되도록 하고 싶다면?
  
  ⇒ created 함수에 강아지 사진을 가져오는 함수를 추가
  
  ```jsx
  // components/DogComponent.vue
  
  export default {
      ...
      created() {
          this.getDogImage()
      },
  ```

### mounted

- Vue instance가 요소에 mount된 후 호출됨

- mount된 요소를 조작할 수 있음
  
  ```jsx
  // components/DogComponent.vue
  
  export default {
      ...
      mounted() {
          const btn = document.querySelector('button')
          btn.innerText = '멍멍!'
      },
  ```

- created의 경우, mount되기 전이기 때문에 DOM에 접근할 수 없으므로 동작하지 않음

- mounted는 주석 처리

### updated

- 데이터가 변경되어 DOM에 변화를 줄 때 호출됨

### Lifecycle Hooks 특징

- instance마다 각각의 Lifecycle을 가지고 있음

- Lifecycle Hooks는 컴포넌트 별로 정의할 수 있음

- 현재 해당 프로젝트는
  
  App.vue 생성 ⇒ ChildComponent 생성 ⇒ ChildComponent 부착 ⇒ App.vue 부착 ⇒ ChildComponent 업데이트 순으로 동작한 것

# Todo with Vuex

---

### 개요

- Vuex를 사용한 Todo 프로젝트 만들기
- 구현 기능
  - Todo CRUD
  - Todo 개수 계산
    - 전체 Todo
    - 완료된 Todo
    - 미완료된 Todo
- 컴포넌트 구성

### 중간 정리

- Vue 컴포넌트의 method에서 dispatch()를 사용해 actions 메서드를 호출
- Actions에 정의된 함수는 commit()을 사용해 mutations를 호출
- Mutations에 정의된 함수가 최종적으로 state를 변경

# Vue Router

---

## Routing

---

### Routing

- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
  - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
- 예시
  - /articles/index/에 접근하면 articles의 index에 대한 결과를 보내 줌

### Routing in SSR

- Server가 모든 라우팅을 통제 (← 장고의 경우 views.py가 통제)
- URL로 요청이 들어오면 응답으로 완성된 HTML 제공
  - Django로 보낸 요청의 응답 HTML은 완성본인 상태였음
- 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐

### Routing in SPA / CSR

- 서버는 하나의 HTML(index.html) 만을 제공
- 이후에 모든 동작은 하나의 HTML 문서 위에서 자바스크립트 코드를 활용
  - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
- 즉 하나의 URL만 가질 수 있음

### Why routing?

- 그럼 동작에 따라 URL이 반드시 바뀌어야 하나?
  
  그렇지는 않다. 단 유저의 사용성 관점에서는 필요함

- Routing이 없다면,
  
  - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
  - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - 새로고침 시 처음 페이지로 돌아감
    - 링크를 공유할 시 처음 페이지만 공유 가능
  - 브라우저의 뒤로 가기 기능을 사용할 수 없음

## Vue Router

---

### Vue Router

- Vue의 공식 라우터
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
  - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
  - SPA의 단점 중 하나인 “URL이 변경되지 않는다.”를 해결
- [참고] MPA(Multiple Page Application)
  - 여러 개의 페이지로 구성된 애플리케이션
  - SSR 방식으로 렌더링

### Vue Router 시작하기

- Vuex와 마찬가지의 방식으로 설치 및 반영
  
  ```bash
  $ vue create vue-router-app    // Vue 프로젝트 생성
  
  $ cd vue-router-app            // 디렉토리 이동
  
  $ vue add router               // Vue CLI를 통해 router plugin 적용
  ```

- history mode 사용여부 → Yes
  
  ```bash
  ? Use history mode for router? (Requires proper server setup for index fallback 
  in production) (**Y**/n)
  ```

### History mode

- 브라우저의 History API를 활용한 방식
  
  - 새로고침 없이 URL 이동 기록을 남길 수 있음

- 우리에게 익숙한 URL 구조로 사용 가능
  
  - 예시) http://localhost:8080/index

- [참고] History mode를 사용하지 않으면 Default 값인 hash mode로 설정됨(’#’을 통해 URL을 구분하는 방식)
  
  - 예시) [http://localhost:8080#index](http://localhost:8080#index)

- App.vue
  
  - router-link 요소 및 router-view가 추가됨

### router-link

- a 태그와 비슷한 기능 → URL을 이동시킴
  - routes에 등록된 컴포넌트와 매핑됨
  - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
  - 목표 경로는 ‘to’ 속성으로 지정됨
  - 기능에 맞게 HTML에서 a 태그로 rendering 되지만, 필요에 따라 다른 태그로 바꿀 수 있음

### router-view

- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미
- router-link를 클릭하면 route에 매핑된 컴포넌트를 렌더링
- Django에서의 block tag와 비슷함
  - App.vue는 base.html의 역할
  - router-view는 block 태그로 감싼 부분

### src/router/index.js

- 라우터에 관련된 정보 및 설정이 작성되는 곳
- Django에서의 urls.py에 해당
- routes에 URL와 컴포넌트를 매핑
- Django와의 비교

### src/Views

- router-view에 들어갈 component 작성
- 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나누어짐
- 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님

## Vue Router 실습

---

### 주소를 이동하는 2가지 방법

1. 선언적 방식 네비게이션
2. 프로그래밍 방식 네비게이션

### 선언적 방식 네비게이션

- router-link의 ‘to’ 속성으로 주소 전달
  - routes에 등록된 주소와 매핑된 컴포넌트로 이동

### 프로그래밍 방식 네비게이션

- Vue 인스턴스 내부에서 라우터 인스턴스에 $router로 접근할 수 있음
- 다른 URL로 이동하려면 this.$router.push를 사용
  - history stack에 이동할 URL을 넣는(push) 방식
  - history stack에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음
- 결국 <router-link :to=”…”>를 클릭하는 것과 $router.push(…)를 호출하는 것은 같은 동작

### Dynamic Route Matching

- 동적 인자 전달
  - URL의 특정 값을 변수처럼 사용할 수 있음
- ex) Django에서의 variable routing

### Dynamic Route Matching - 선언적 방식 네비게이션

### lazy-loading

- 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림
- 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
  - 모든 파일을 한 번에 로드하지 않아도 되기 때문에 최초에 로드하는 시간이 빨라짐
  - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심

## Navigation Guard

---

### 네비게이션 가드

- Vue router를 통해 특정 URL에 접근할 때 다른 url로 redirect를 하거나 해당 URL로의 접근을 막는 방법
  - Ex) 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함

### 네비게이션 가드의 종류

- 전역 가드
  - 애플리케이션 전역에서 동작
- 라우터 가드
  - 특정 URL에서만 동작
- 컴포넌트 가드
  - 라우터 컴포넌트 안에 정의

## 전역 가드

---

### Global Before Guard

- 다른 url 주소로 이동할 때 항상 실행
- router/index.js에 `router.beforeEach()`를 사용하여 설정
- 콜백 함수의 값으로 다음과 같이 3개의 인자를 받음
  - to : 이동할 URL 정보가 담긴 Route 객체
  - from : 현재 URL 정보가 담긴 Route 객체
  - next : 지정한 URL로 이동하기 위해 호출하는 함수
    - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
    - 기본적으로 to에 해당하는 URL로 이동
- URL이 변경되어 화면이 전환되기 전 router.beforeEach()가 호출됨
  - 화면이 전환되지 않고 대기 상태가 됨
- 변경된 URL로 라우팅하기 위해서는 next()를 호출해 줘야 함
  - next()가 호출되기 전까지 화면이 전환되지 않음

### Global Before Guard 실습

- ‘/home’으로 이동하더라도 라우팅이 되지 않고 아래와 같이 로그만 출력됨
- next()가 호출되지 않으면 화면이 전환되지 않음
- next()가 호출되어야 화면이 전환됨
- About으로 이동해 보기
  - to에는 이도앟ㄹ

## 컴포넌트 가드

---

### 컴포넌트 가드

- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
- `beforeRouteUpdate()`
  - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

### Params 변화 감지

- about에서 jun에게 인사하는 페이지로 이동

## 404 Not Found

---

### 404 Not Found

- 사용자가 요청한 리소스가 존재하지 않을 때 응답

### 요청한 리소스가 존재하지 않는 경우

### 형식은 유효하지만 특정 리소스를 찾을 수 없는 경우

- 예시) Django에게 articles/1 로 요청을 보냈지만, 1번 게시글이 삭제된 상태
  - 이때는 path: ‘*’를 만나 404 page가 렌더링 되는 것이 아니라 기존에 명시한 articles/:id/에 대한 component가 렌더링됨





---

# Vue.js props 사용 방법

### ⭐️ props 란 ?

부모 컴포넌트에서 자식 컴포넌트로

데이터를 전달할때 사용되어지는

단방향 데이터 전달 방식이다

### ⭐️ 사용 방법

부모 컴포넌트에서 자식 컴포넌트를 호출시

자식 컴포넌트 태그 내 v-bind나 : 키워드를통해

데이터를 전달하고 자식 컴포넌트에서

props객체를 통해 데이터를 전달받는 방식이다

### ⭐️ 기본 형태

```xml
<!--부모 컴포넌트--><template><!--첫번째, 두번째 모두 같은 결과--><!--첫번째 방법-->
    <자식컴포넌트이름 :props이름="전달데이터"/>
    <!--두번째 방법-->
    <자식컴포넌트이름 v-bind:props이름="전달데이터"/>
</template>
```

### ⭐️ 샘플예제 (로직)

쇼핑몰 상품 리스트가 출력되는

예제를 만들어 보았다.

App은 부모 컴포넌트,

Menu와 Product는 자식 컴포넌트이고

각 자식 컴포넌트는 props를 통하여

해당하는 데이터를 전달 받아 출력하는 형식이다

### ⭐️ App 컴포넌트 (부모컴포넌트)

```xml
<!--UI--><template><Menu :menu="menu"/><nav><ul><Product v-for="product,i in products" :key="i" v-bind:product="product"/></ul></nav></template><!--Script--><script>
import Menufrom './components/Menu.vue';
import Productfrom './components/Product.vue';

exportdefault {
  name : 'App',
  data (){
return {
      menu : ['HOME','ABOUT' ,'PRODUCTS', 'ETC'],
      products : [
        {id : '0', title : 'Sample Product1', price : 10000, img : '<https://dummyimage.com/200/F6A9A9/464660>'},
        {id : '1', title : 'Sample Product2', price : 50000, img : '<https://dummyimage.com/200/FFBF86/464660>'},
        {id : '2', title : 'Sample Product3', price : 30000, img : '<https://dummyimage.com/200/FFF47D/464660>'},
        {id : '3', title : 'Sample Product5', price : 70000, img : '<https://dummyimage.com/200/C2F784/464660>'},
      ]
    }
  },
  components : {
    //ES6 부터 key, value의 변수명이 같을때 생략이 가능하다//Menu : Menu
    Menu,Product
  }
}
</script><!--CSS--><style></style>
```

### ⭐️ Menu 컴포넌트 (자식 컴포넌트 - 메뉴)

```xml
<template><nav><ul class="menu"><li class="menu--item" v-for="item,i in menu" :key="i"><a :href="'/'+item">{{item}}</a></li></ul></nav></template><script>
exportdefault {
  name : 'Menu',
  props : {
    menu : Array
  }
}
</script><style>
  .menu {
display: flex;
justify-content: center;
padding: 10px;
border-radius: 5px;
background: steelblue;
list-style: none;
  }

  .menu--item {
padding: 10px;
  }

  .menu--itema {
color: white;
text-decoration: none;
  }
</style>
```

### ⭐️ Product 컴포넌트 (자식 컴포넌트-상품)

```xml
<template><li class="product"><img :src="product.img"/><div class="product--content"><h3 class="content--title">{{product.title}}</h3><div class="content--price">상품가 : {{product.price}} 원</div></div></li></template><script>
exportdefault {
    name : 'Product',
    props : {
        product : Object
    }
}
</script><style>
    .product {
display: flex;
flex-direction: row;
justify-content: center;
flex-wrap: wrap;
align-items: center;
list-style: none;
margin: 10px;
    }

    .product--content {
margin-left: 10px;
    }
</style>
```

### 🌈 출력 결과

![https://blog.kakaocdn.net/dn/FISjE/btrb8hQOsvQ/bHGbLxInnkE945L0NXsNUk/img.png](https://blog.kakaocdn.net/dn/FISjE/btrb8hQOsvQ/bHGbLxInnkE945L0NXsNUk/img.png)
