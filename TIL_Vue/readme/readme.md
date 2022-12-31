상위-하위 컴포넌트 간의 데이터 전달 방법

우선 상위 - 하위 컴포넌트 간의 데이터 전달 방법이다.

상위 -> 하위 로는 props라는 특별한 속성을 전달하고,

하위 -> 상위 로는 기본적으로 이벤트만 전달 가능하다.







<!--parentComponent.vue-->

<template>
  <div>
    <ChildComponent />
  </div>
</template>

<script>
import ChildComponent from "@/components/childComponent.vue";
export default {
  name: "ParentComponent",
  components: { ChildComponent },
};
</script>

상위-하위 컴포넌트 간의 데이터 전달 방법에 대해 설명하기 위해 ParentComponent에 ChildComponent를

등록한 모습이다.

Root Instance (main.js)

└─ 최상위 컴포넌트 (App.vue)

```
       └─ ParentComponent
               └─ ChildComponent
```

=> 현재 컴포넌트 트리 모습

Props 속성 이용하여 상위 -> 하위 컴포넌트 데이터 전달
상위 컴포넌트에서 버튼을 누르면 하위 컴포넌트에게 상위 컴포넌트의 데이터 값을 알 수 있게 하는 예제를 진행해보겠다.

<!-- parentComponent -->

<template>
  <div>
    하위 컴포넌트에 데이터 값을 알려줍니다.
    <ChildComponent v-bind:childVaule="parentVaule" />
  </div>
</template>

<script>
import ChildComponent from "@/components/childComponent.vue";
export default {
  name: "ParentComponent",
  components: { ChildComponent },
  data: function () {
    return {
      parentVaule: 20,
    };
  },
};
</script>

'v-bind:하단 컴포넌트에서 받을 props 이름'을 사용하여 하단 컴포넌트에서 데이터를 전달 받을 수 있다.

v-bind는 생략 가능하며, ':하단 컴포넌트에서 받을 props 이름'로 사용해도 된다.

<!--childComponent-->

<template>
  <div>{{ this.childVaule }} : 상위 컴포넌트로부터 받아온 값</div>
</template>

<script>
export default {
  name: "ChildComponent",
  props: ["childVaule"],
};
</script>

props에 v-bind에 등록해준 이름을 써주면 하단 컴포넌트에서도 쉽게 사용가능하다.

하위 -> 상위 컴포넌트 데이터 전달
이번에는 하위 컴포넌트에서 버튼을 누르면 상위 컴포넌트의 데이터가 증가하는 예제를 해보겠다.

<!--childComponent-->

<template>
  <button @click="updateParentValue">클릭시 부모의 데이터 값이 증가합니다.</button>
</template>

<script>
export default {
  name: "ChildComponent",
  methods: {
    updateParentValue() {
      this.$emit("childEvent");
    },
  },
};
</script>

버튼을 클릭하면 이벤트를 보내는 메소드가 실행되도록 리스너를 등록했다.

this.$emit("상위에서 받을 이벤트 이름") 을 사용하여 상위 컴포넌트에 이벤트를 보낸다.

<template>
  <div>
    <ChildComponent v-on:childEvent="updateParentValue" />
  </div>
</template>

<script>
import ChildComponent from "@/components/childComponent.vue";
export default {
  name: "ParentComponent",
  components: { ChildComponent },
  data: function () {
    return {
      parentVaule: 20,
    };
  },
  methods: {
    updateParentValue() {
      this.parentVaule++;
      console.log(this.parentVaule) // 21, 22, 22, 누를때마다 증가하는 것 확인 가능
    },
  },
};
</script>

이벤트를 받는 것은 v-on:을 사용하여 받을 수 있다.

이 예제에서는 childEvent 라는 이벤트가 받아진다면 그때 updateParentValue 메소드를 실행하는 것을 알 수 있다.

버튼을 누를때마다 1씩 증가하는 것을 콘솔에서 확인할 수 있었다.

그 밖의 관계를 가진 컴포넌트 간의 데이터 전달 방법
(형제 컴포넌트, 손자컴포넌트)

그렇담 그 밖의 관계를 가진 컴포넌트 간의 데이터 전달은 어떻게 이루어지는 것일까?

Vue.js에는 이벤트버스 라는 것이 있다.

독립적인 컴포넌트끼리 이벤트를 통신해야할 때 단순히 EventBus를 활용해서 간단하게 처리할 수 있다.

부모 - 자식 컴포넌트가 아닌 관계의 컴포넌트끼리 데이터 통신 예제를 진행하기 위해서

아래와 같은 컴포넌트 트리 구조를 만들었다.

Root Instance (main.js)

└─ 최상위 컴포넌트 (App.vue)

```
  ├─ Component A
           ├─ Component B

              └─ Component C

           └─ Component D
```

=> 현재 컴포넌트 트리

아직 컴포넌트 등록 방법이 헷갈린다면

2020/12/20 - [Vue.js] - Vue.js 시작하기 - 인스턴스 & 컴포넌트 를 참고하길 바란다.

Event Bus
관계없는 Component D와 Component C 간 eventBus를 사용하여 서로의 버튼을 클릭하면

버튼에 있는 value alert 창을 띄워보는 예제를 진행해보겠다.

//main.js

import Vue from 'vue'
import App from './App'
import router from './router'

export const eventBus = new Vue()
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
 el: '#app',
 router,
 components: { App },
 template: '<App/>'
})
먼저 Root에서 export const type으로 eventBus를 등록하면 다른 컴포넌트에서

import 를 하여 eventBus를 사용할 수 있다.

<!--ComponentD-->

<template>
  <div>
    {{ this.textComponentD }}
    <button @click="clickComponentDButton">
      {{ this.ComponentDBtnVaule }}
    </button>
  </div>
</template>

<script>
import { eventBus } from "@/main.js";
export default {
  name: "ComponentD",
  data: function () {
    return {
      textComponentD: "ComponentD 입니다.",
      ComponentDBtnVaule: "D의 버튼",
    };
  },
  created() {
    eventBus.$on("clickComponentCButton", (componentCButtonValue) => {
      window.alert(componentCButtonValue);
    });
  },
  beforeDestroy() {
    eventBus.$off("clickComponentCButton");
  },
  methods: {
    clickComponentDButton() {
      eventBus.$emit("clickComponentDButton", this.ComponentDBtnVaule);
    },
  },
};
</script>

<!--ComponentC-->

<template>
  <div>
    {{ this.textComponentC }}
    <button @click="clickComponentCButton">
      {{ this.ComponentDBtnVaule }}
    </button>
  </div>
</template>

<script>
import { eventBus } from "@/main.js";
export default {
  name: "ComponentC",
  data: function () {
    return {
      textComponentC: "ComponentC 입니다.",
      ComponentDBtnVaule: "C의 버튼",
    };
  },
  created() {
    eventBus.$on("clickComponentDButton", (componentCButtonValue) => {
      window.alert(componentCButtonValue);
    });
  },
  beforeDestroy() {
    eventBus.$off("clickComponentDButton");
  },
  methods: {
    clickComponentCButton() {
      eventBus.$emit("clickComponentDButton", this.ComponentDBtnVaule);
    },
  },
};
</script>

각 컴포넌트에서 버튼을 누르게 되면 @click으로 인하여 methods 단에 있는 clickComponentDButton / clickComponentCButton를 호출하게 된다.

그 안에 있는 event.$emit 로 이벤트를 보내게 된다.

이때 첫번째 parameter에 있는 것은 이벤트의 이름이다. 위의 예제에서 함수와 이름이 같지만 달라도 상관없다.

두번째 parameter에 있는 것은 그 이벤트에 같이 보낼 값이다. 물론 값을 보내지 않아도 될 경우에는 보내지 않아도

상관은 없다. ex) 버튼의 눌림 여부만 check 하고 싶을 경우.

created() 안에는 eventBus.$on로 이벤트를 받을 수 있다.

created()는 다음에 설명할 라이프 사이클 훅 중 하나인데,

쉽게말해 컴포넌트가 시작할 시점(created)에 이벤트 받는 것을 항상 on 시켜둔다(eventBus.$on)고 이해하면 될 것같다.

=> off 되기 이전까지 항상 이벤트를 받을 수 있다.

eventBus on 첫번째 parameter는 받을 이벤트의 이름을 의미한다. 앞에서 설명한 event.$emit("A")를 하게 되면

eventBus.$on("A" => (){})로 받게 된다. 두번째는 같이 보내져온 값을 사용하여 콜백 함수를 등록할 수 있다.

위의 예제에서는 보내져온 값을 사용하여 alert 창을 띄운것을 볼 수 있다.

앞서 말했듯 이벤트는 off 되기 이전까지 항상 이벤트를 받을 수 있기 때문에 컴포넌트가 종료(destoryed)된다거나 할때

이벤트를 종료( event.$off("이벤트 이름") ) 시켜주어야한다.

다만, 이벤트버스는 한정된 컴포넌트간의 통신에는 적합하지만 자주 사용하게 된 후,

규모가 커진다면 이벤트 추적 관리에 힘들어지는 단점이 있다.

왜냐하면 Vue 는 일반적으로 단방향 데이터 흐름이며, 여러 View 는 동일한 State 에 의존한다.

즉, 여러 View 가 동일한 State 값을 참조 및 변경하여 View 를 출력하게 된다.

여러 View 가 동일한 State 를 가리키기엔 빈번한 props, $emit 을 사용하게 되고, 이벤트 버스까지 사용하게 되면 컴포넌트와의 관계를 파악하기가 어렵게 된다.

Vuex 는 Vue 의 상태 관리 패턴에다가 쉽게 관리할 수 있게 라이브러리가 추가된 개념이다.

즉 'Vuex = 상태 관리 패턴 + 라이브러리'라고 할 수 있다.

먼저 핵심 내용을 위의 Vuex 기본 구조를 보고 나열하겠다.

저장소에는 State 를 통해 값을 관리한다.

Getter 를 통해 값을 가져올 수 있다.

(직접 Store.state.count 접근 할 수 있지만 추천하지 않는다.)

값을 변경하고 싶을때는 Mutation 을 이용한다.

하지만 Mutation 은 비동기 코드가 동작할 수 없다. 그리고 비용이 큰 연산은 포함하지 않는게 좋다.

위의 Mutation 의 대안으로, Action 을 통해 비동기 작업을 추가할 수 있다.

Mutation 과 달리 Action 은 State 값을 직접 변경할 순 없지만, 비동기 작업과 동시에 다른 Action 혹은 Mutation 을 내부적으로 호출할 수 있다.

비용이 큰 작업들은 Mutation 이 아닌 Action 에서 구현하는 게 좋다.

# Vuex 사용법

## 1. Vuex install

// npm 을 통한 설치 방법
$ npm install --save vuex
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

## 2. 저장소

저장소는 컴포넌트에서 공유된 상태를 추출하고 이를 전역 싱글톤으로 관리한다.

저장소의 특징은 다음과 같다.

애플리케이션 상태 보유한 컨테이터
반응형 - 상태 검색시, 저장소의 상태가 변경되면 효율적으로 대응하고 업데이트함
저장소의 상태를 직접 변경할 수 없고, 오직 Commit 을 이용하여 값을 수정할 수 있다
const store = new Vuex.Store({
 state: {
 count: 0
 },
 mutations: {
 increment (state) {
 state.count++
 }
 }
})
저장소를 생성한다.

const Counter = {
 template: `<div>{{ count }}</div>`,
 computed: {
 count () {
 return store.state.count
 }
 }
}
전역 저장소 단독 항목에 의존하는 경우에는 store.state.count 로 접근할 수 있다.

만약 모든 하위 컴포넌트에 주입시켜 접근하게 하고 싶다면 아래와 같이 Vue 인스턴스 생성시, store 옵션에 store 를 추가한 이후

하위의 모든 컴포넌트에서 this.$store.state.count 로 접근할 수 있다.

new Vue({
 el: '#app',
 store,
 components: { Counter },
 template: ` <div class="app">
 <counter></counter>
 </div> `
})

## 3. State

state 는 저장소 내부의 상태를 가지고 있다. 여기에 접근하여 관리하는 변수들에게 대해 접근할 수 있다.

const store = new Vuex.Store({
 state: {
 count: 0
 }
})
하위 컴포넌트에서 저장소 내부의 상태를 표시할 때는 computed 를 통해 접근할 수 있다.

const Counter = {
 template: ` <div>
 <div>
 count: {{ count }}
 </div>
 </div> `,
 data() {
 return {

```
}
```

},
 computed: {
 count: state => this.$store.state.count
 }
}
mapState 헬퍼를 이용한 방법
컴포넌트에서 저장소 상태 속성들을 선언할 경우, 중복된 코드가 많아지기에 mapState 헬퍼 함수를 사용해 불필요한 코드 입력을 줄일 수 있다.

import Vuex, { mapState } from 'vuex'

const Counter = {
 ...
 computed: mapState({
 count: state => state.count
 })
}
위와 같이 this.$store.state 경로에 대한 입력 코드를 입력하지 않아도 된다.

계산된 속성의 이름이 하위 트리 이름과 같을 경우, 다음과 같이 작성할 수도 있다.

const Counter = {
 ...
 computed: mapState([
 // this.count 를 this.$store.state.count 에 매핑
 'count'
 ])
}
computed 에 mapState 를 이용하여 최종 객체를 전달하고 싶을때는 객체 전개 연산자를 사용한다.

const Counter = {
 ...
 computed: {
 ...mapState([
 'count'
 ]),
 ...mapState([
 'anotherState'
 ]),
 }
}

## 4. Getter

저장소 상태 값을 기반으로 계산해야 할 경우 Getter 를 사용할 수 있다.

상태 값을 가져오는 하위 컴포넌트 입장에서 함수를 이용하여 계산할 수 있지만, 둘 이상의 컴포넌트가 이를 공유할때는 불필요한 코드 복제가 일어난다.

저장소에서 Getter 를 이용해서 계산된 상태 값을 제공할 수 있다.

const store = new Vuex.Store({
 state: {
 count: 0
 },
 mutations: {
 increment (state) {
 state.count++
 }
 },
 getters: {
 getCount_added100: (state) => {
 return state.count + 100;
 },
 getCount_added1000: (state, getters) => {
 return getters.getCount_added100 + 1000;
 }
 }
})
getters 는 store.getters 로 노출이 되는데, getCount_added100 처럼 state 인자 하나만으로 저장소 상태 값에 접근할 수 있다.

getCount_added1000 처럼 두번째 인자로 getters 를 넘기면, 다른 getter 에 접근할 수 있다.

const Counter = {
 template: ` <div>
 <div>
 getCount_added100: {{ getCount_added100 }}
 </div>
 <div>
 getCount_added1000: {{ getCount_added1000 }}
 </div>
 </div> `,
 data() {
 return {

```
}
```

},

computed: {
 //
 ...mapGetters([
 'getCount_added100',
 'getCount_added1000'
 ])
 }
}
mapStates 처럼 mapGetters 헬퍼함수를 이용할 수 있다.

## 5. Mutations

저장소의 특징 중 하나가 오직 Commit 만을 이용해 값을 변이할 수 있다라는 점이다.

Mutations 에 핸들러를 등록하여 Commit 이벤트를 받을 수 있다.

그리고 꼭 알아야 하는 것은 Mutation 내에서는 꼭 동기적 호출만 가능하다. (만약 비동기를 이용하고 싶다면 곧 나올 Actions 를 참고)

const store = new Vuex.Store({
 state: {
 count: 1
 },
 mutations: {
 increment (state) {
 // 상태 변이
 state.count++
 }
 }
})
하위 컴포넌트에서 mutations 을 호출할때는 commit 함수를 이용한다.

this.$store.commit('increment')
payload 를 함께 전달하고 싶을 경우에는 두번째 인자로 payload 값을 넘길 수 있다.

1. 단일값 전달

// ...
mutations: {
 increment (state, n) {
 state.count += n
 }
}
store.commit('increment', 10)
2) 객체 전달

// ...
mutations: {
 increment (state, payload) {
 state.count += payload.amount
 }
}
store.commit('increment', {
 amount: 10
})
실제 사용 예시는 아래를 참고하자.

const store = new Vuex.Store({
 state: {
 count: 0
 },
 mutations: {
 increment (state) {
 state.count++
 },
 increment2 (state, n) {
 state.count += n
 },
 increment3 (state, n) {
 state.count += n
 }
 }
})
const Counter = {
 template: ` <div>
 <div>
 count: {{ count }}
 </div>
 <button @click="increment">+</button>
 <button @click="add(10)">+</button>
 <button @click="add2(100)">+</button>
 </div> `,
 //
 methods: {
 /*
 this.$store.commit('xxx') 를 통해 Mutation 를 호출하거나,
 mapMutations 헬퍼 함수를 이용하여 store.commit 호출에 매핑시킬 수 있다.(루트 store에 주입 필요)
 */
 ...mapMutations([
 'increment'
 ]),
 ...mapMutations({
 add: 'increment2'
 }),
 add2(n) {
 this.$store.commit('increment3', n);
 }
 }
}
mapMutations 헬퍼 함수를 이용하여 methods 에 등록해야 한다.

여기에서 알 수 있는 점은 state 와 getter 는 computed 속성에 선언을 해야 하며,

mutation 과 앞으로 배운 action 은 methods 속성에 정의를 해야 한다.

## 6. Actions

Action 은 Mutation 과 유사하시만 다른 점이 있다.

상태를 변이시키는 것이 아닌 액션으로 변이에 대한 커밋을 한다.

비동기 작업이 포함될 수 있다.

const store = new Vuex.Store({
 mutations: {
 increment (state) {
 state.count++
 },
 increment2 (state, n) {
 state.count += n
 },
 increment3 (state, n) {
 state.count += n
 }
 },
 actions: {
 increment(context) {
 var rn = Math.random();
 context.commit('increment2', Math.floor(rn * 10 + 1));
 },
 increment2({ commit }, n) {
 commit('increment2', n);
 commit('increment2', n);
 },
 incrementAsync({ commit }, n) {
 setTimeout(() => {
 commit('increment2', n)
 }, 1000)
 }
 }
})
increment 액션처럼 context 를 통해 커밋을 할 수 있다.

increment(context) {
 var rn = Math.random();
 context.commit('increment2', Math.floor(rn * 10 + 1));
 },
increment2 액션처럼 commit 객체를 통해 커밋 포인트를 지정하여 Mutation 을 접근할 수 있다.

increment2({ commit }, n) {
 commit('increment2', n);
 commit('increment2', n);
 },
incrementAsync 액션처럼 비동기 작업을 추가하여 Mutation 에 커밋할 수 있다.

incrementAsync({ commit }, n) {
 setTimeout(() => {
 commit('increment2', n)
 }, 1000)
 }
const Counter = {
 template: ` <div>
 <div>
 count: {{ count }}
 </div>
 <button @click="add_random()">add_random()</button>
 <button @click="add_2x(100)">add_2x(100)</button>
 <button @click="incrementAsync(1)">incrementAsync</button>
 </div> `,
 data() {
 return {
 localCount: 10
 }
 },
 methods: {
 ...mapMutations([
 'increment'
 ]),
 ...mapMutations({
 add: 'increment2'
 }),
 add2(n) {
 this.$store.commit('increment3', n);
 },
 ...mapActions({
 add_random: 'increment',
 add_2x: 'increment2',
 incrementAsync: 'incrementAsync'
 })
 }
Promise 적용
actionA 처럼 Promise 객체를 생성 및 리턴하여 동기 처리를 할 수 있다.

actionA ({ commit }) {
 return new Promise((resolve, reject) => {
 setTimeout(() => {
 // mutation 호출
 commit('increment');
 resolve();
 }, 1000)
 })
 }
actionB 처럼 다른 액션을 호출하고 Mutation 을 호출할 수 있다.

actionB ({ commit }) {
 return this.dispatch('actionA').then(() => {
 commit('increment2', 1000);
 })
 }
전체소스)

const store = new Vuex.Store({
 state: {
 count: 0
 },
 mutations: {
 increment (state) {
 state.count++
 },
 increment2 (state, n) {
 state.count += n
 },
 increment3 (state, n) {
 state.count += n
 }
 },
 actions: {
 increment(context) {
 var rn = Math.random();
 context.commit('increment2', Math.floor(rn * 10 + 1));
 },
 increment2({ commit }, n) {
 commit('increment2', n);
 commit('increment2', n);
 },
 incrementAsync({ commit }, n) {
 setTimeout(() => {
 commit('increment2', n)
 }, 1000)
 },

```
actionA ({ commit }) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // mutation 호출
      commit('increment');
      resolve();
    }, 1000)
  })
},
actionB ({ commit }) {
  return this.dispatch('actionA').then(() => {
    commit('increment2', 1000);
  })
}
```

}
})

## 7. 모듈화

const moduleA = {
 state: {
 count: 0
 },
 mutations: {
 increment (state) {
 state.count++
 },
 increment2 (state, n) {
 state.count += n
 },
 increment3 (state, n) {
 state.count += n
 }
 },
 getters: {
 getCount_added100: (state) => {
 return state.count + 100;
 },
 getCount_added1000: (state, getters) => {
 return getters.getCount_added100 + 1000;
 },

```
/*
  computed 는 캐시 기능을 제공하지만, 
  메서드를 통한 getter 는 호출될때마다 캐시가 되지 않는다.
*/
getCountFn: (state) => () => {
  return state.count + 1;
}
```

},
 actions: {
 increment(context) {
 var rn = Math.random();
 context.commit('increment2', Math.floor(rn * 10 + 1));
 },
 increment2({ commit }, n) {
 commit('increment2', n);
 commit('increment2', n);
 },
 incrementAsync({ commit }, n) {
 setTimeout(() => {
 commit('increment2', n)
 }, 1000)
 },

```
actionA ({ commit }) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // mutation 호출
      commit('increment');
      resolve();
    }, 1000)
  })
},
actionB ({ commit }) {
  /*
    action 에서 action 을 호출할때는 모듈 경로를 적어줘야 함
  */
  return this.dispatch('moduleA/actionA').then(() => {
    commit('increment2', 1000);
  })
}
```

}
}
const store = new Vuex.Store({
 modules: {
 moduleA: moduleA
 }  
})
위와 같이 Store 의 modules 옵션을 통해 분리된 모듈들을 합칠 수 있다.

namespaced
모듈간에 네임 스페이스를 구분지을 수 있다.

namespaced 를 지정하지 않으면(default: false) 전역 네임스페이스로 구분이 된다.

const moduleA = {
 namespaced: true,
 state: {
 count: 0
 },
 //
전역 네임스페이스와 지역 네임스페이스 접근 방법 비교
지역 네임스페이스

const Counter = {
 computed: {
 ...mapState({
 count: state => state.moduleA.count,
 }),
 ...mapGetters('moduleA', [
 'getCount_added100',
 'getCount_added1000',
 'getCountFn',
 ])
 },
 methods: {
 ...mapMutations('moduleA', [
 'increment'
 ]),
 ...mapMutations('moduleA', {
 add: 'increment2'
 }),
 add2(n) {
 this.$store.commit('moduleA/increment3', n);
 },
 ...mapActions('moduleA', {
 add_random: 'increment',
 add_2x: 'increment2',
 incrementAsync: 'incrementAsync'
 }),
 ...mapActions('moduleA', {
 actionA: 'actionA',
 actionB: 'actionB'
 })
 }
}
전역 네임스페이스

지역 네임스페이스와 비교했을 때, 저장소의 State 에 대해서만 moduleA 로 구분을 하지, 나머지 getters, mutations, actions 들에 대해서는 모듈 구분이 필요가 없다.

const Counter = {
 computed: {
 ...mapState({
 count: state => state.moduleA.count,
 }),
 ...mapGetters([
 'getCount_added100',
 'getCount_added1000',
 'getCountFn',
 ])
 },
 methods: {
 ...mapMutations([
 'increment'
 ]),
 ...mapMutations({
 add: 'increment2'
 }),
 add2(n) {
 this.$store.commit('increment3', n);
 },
 ...mapActions({
 add_random: 'increment',
 add_2x: 'increment2',
 incrementAsync: 'incrementAsync'
 }),
 ...mapActions({
 actionA: 'actionA',
 actionB: 'actionB'
 })
 }
}
모듈화된 애플리케이션 구조

// ./store/index.vue

import Vue from 'vue'
import Vuex from 'vuex'
import moduleA from './modules/moduleA'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
 modules: {
 moduleA
 },
 strict: debug,
 //plugins: debug ? [createLogger()] : []
})
// ./store/modules/moduleA.vue

const state = () => ({

});

const getters = {

}

const actions = {

}

const mutations = {

}

export default {
 namespaced: true,
 state,
 getters,
 actions,
 mutations
}