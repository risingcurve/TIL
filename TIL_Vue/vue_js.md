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
