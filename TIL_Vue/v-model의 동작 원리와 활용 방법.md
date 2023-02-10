# v-model의 동작 원리와 활용 방법

- ###### 목차

- [들어가며](https://joshua1988.github.io/web-development/vuejs/v-model-usage/#%EB%93%A4%EC%96%B4%EA%B0%80%EB%A9%B0)

- [v-model 속성](https://joshua1988.github.io/web-development/vuejs/v-model-usage/#v-model-%EC%86%8D%EC%84%B1)

- [v-model은 어떻게 동작할까?](https://joshua1988.github.io/web-development/vuejs/v-model-usage/#v-model%EC%9D%80-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%8F%99%EC%9E%91%ED%95%A0%EA%B9%8C)

- [그럼 v-model이 더 편하니까 이거 쓰면 되는거죠?](https://joshua1988.github.io/web-development/vuejs/v-model-usage/#%EA%B7%B8%EB%9F%BC-v-model%EC%9D%B4-%EB%8D%94-%ED%8E%B8%ED%95%98%EB%8B%88%EA%B9%8C-%EC%9D%B4%EA%B1%B0-%EC%93%B0%EB%A9%B4-%EB%90%98%EB%8A%94%EA%B1%B0%EC%A3%A0)

- [v-model 문법을 이용해서 한국어를 처리할 순 없을까요?](https://joshua1988.github.io/web-development/vuejs/v-model-usage/#v-model-%EB%AC%B8%EB%B2%95%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%ED%95%9C%EA%B5%AD%EC%96%B4%EB%A5%BC-%EC%B2%98%EB%A6%AC%ED%95%A0-%EC%88%9C-%EC%97%86%EC%9D%84%EA%B9%8C%EC%9A%94)

- [마무리](https://joshua1988.github.io/web-development/vuejs/v-model-usage/#%EB%A7%88%EB%AC%B4%EB%A6%AC)

- [글보다 더 쉽게 배우는 온라인 강좌](https://joshua1988.github.io/web-development/vuejs/v-model-usage/#%EA%B8%80%EB%B3%B4%EB%8B%A4-%EB%8D%94-%EC%89%BD%EA%B2%8C-%EB%B0%B0%EC%9A%B0%EB%8A%94-%EC%98%A8%EB%9D%BC%EC%9D%B8-%EA%B0%95%EC%A2%8C)

## 들어가며

오랜만에 글을 쓰네요. 오늘은 Vue.js로 Form 요소를 개발할 때 사용하는 `v-model` 속성에 대해서 살펴보려고 합니다. 이 속성은 그냥 사용하면 그렇게 어렵지 않은데 실제 애플리케이션을 개발할 때는 꽤 주의해서 다뤄야 합니다. 그럼 `v-model`의 동작 원리와 활용 방법 등에 대해서 알아볼게요!

## v-model 속성

공식 문서에 안내된 v-model 속성의 사용법은 아래와 같습니다.

```html
<input v-model="inputText">
```

```js
new Vue({
  data: {
    inputText: ''
  }
})
```

이렇게 사용자의 입력을 받는 UI 요소들에 `v-model`이라는 속성을 사용하면 입력 값이 자동으로 뷰 데이터 속성에 연결됩니다.

![v-model](https://joshua1988.github.io/images/posts/web/vuejs/v-model/v-model.gif)

## v-model은 어떻게 동작할까?

`v-model` 속성은 `v-bind`와 `v-on`의 기능의 조합으로 동작합니다. 매번 사용자가 일일이 `v-bind`와 `v-on` 속성을 다 지정해 주지 않아도 좀 더 편하게 개발할 수 있게 고안된 문법인 거죠. 앞에서 살펴본 코드를 아래와 같이 변경하더라도 동일하게 동작합니다.

```html
<input v-bind:value="inputText" v-on:input="updateInput">
```

```js
new Vue({
  data: {
    inputText: ''
  },
  methods: {
    updateInput: function(event) {
      var updatedText = event.target.value;
      this.inputText = updatedText;
    }
  }
})
```

위 코드를 이해하기 위해서는 다음 3가지 사실을 알고 있어야 합니다.

- `v-bind` 속성은 뷰 인스턴스의 데이터 속성을 해당 HTML 요소에 연결할 때 사용한다.
- `v-on` 속성은 해당 HTML 요소의 이벤트를 뷰 인스턴스의 로직과 연결할 때 사용한다.
- 사용자 이벤트에 의해 실행된 뷰 메서드(methods) 함수의 첫 번째 인자에는 해당 이벤트(`event`)가 들어온다.

HTML 입력 요소의 종류에 따라 `v-model` 속성이 각각 다음과 같이 구성됩니다.  
(1) input 태그에는 `value / input`  
(2) checkbox 태그에는 `checked / change`  
(3) select 태그에는 `value / change`

## 그럼 v-model이 더 편하니까 이거 쓰면 되는거죠?

빠르게 기능을 구현하고 프로토타이핑 해나갈 때는 `v-model`을 사용해도 상관없습니다. 다만, 현재 시점에서는 [IME 입력](https://en.wikipedia.org/wiki/Input_method)(한국어, 일본어, 중국어)에 대해서 아래와 같은 한계점이 있습니다.

![v-model-ime](https://joshua1988.github.io/images/posts/web/vuejs/v-model/v-model-ime.gif)

위 화면을 보면 한글 입력의 경우 한 글자에 대한 입력이 끝나야지만 `inputText` 데이터가 인풋 박스의 텍스트 값과 동기화됩니다. 아마 조금 전에 살펴봤던 화면을 보면 더 쉽게 비교가 될 겁니다.

![v-model](https://joshua1988.github.io/images/posts/web/vuejs/v-model/v-model.gif)

위와 같은 `v-model`의 한계점 때문에 뷰 공식 문서에서는 한국어 입력을 다룰 때 `v-bind:value`와 `v-on:input`를 [직접 연결해서 사용하는 것을 권고하고](https://vuejs.org/v2/guide/forms.html#Basic-Usage) 있습니다.

## v-model 문법을 이용해서 한국어를 처리할 순 없을까요?

이렇게 매번 한국어 입력을 처리할 때 `v-model` 대신에 직접 이벤트와 값을 조합해서 바인딩 하는 것이 귀찮게 느껴질 수 있습니다. 이럴 땐 아래와 같이 인풋 컴포넌트를 별도의 컴포넌트로 분리하면 `v-model`로 편하게 처리할 수 있습니다.

```html
<!-- BaseInput.vue - 싱글 파일 컴포넌트 구조-->
<template>
  <input v-bind:value="value" v-on:input="updateInput">
</template>

<script>
export default {
  props: ['value'],
  methods: {
    updateInput: function(event) {
      this.$emit('input', event.target.value);
    }
  }
}
</script>
```

위 코드의 동작을 간단하게 설명하자면 다음과 같습니다.

- `BaseInput` 컴포넌트의 상위 컴포넌트에서 `props`로 받은 `value`를 인풋 태그에 값으로 연결합니다.
- 인풋 태그에서 값이 입력되면 인풋 태그에서 `input` 이벤트가 발생하고 `updateInput` 메서드가 실행됩니다.
- `updateInput` 메서드에서 인풋 태그에 입력된 값을 상위 컴포넌트에 `input` 이벤트로 올려 보냅니다.

이제 이 컴포넌트를 등록해서 아래와 같이 사용할 수 있습니다.

```html
<!-- App.vue - 싱글 파일 컴포넌트 구조 -->
<template>
  <div>
    <base-input v-model="inputText"></base-input>
  </div>
</template>

<script>
import BaseInput from './BaseInput.vue';

export default {
  components: {
    'base-input': BaseInput  },
  data: function() {
    return {
      inputText: ''
    }
  }
}
</script>
```

여기서 주의 깊게 살펴볼 만한 부분은 상위 컴포넌트에서 정의한 데이터 값을 하위 컴포넌트로 내려보내는 부분입니다.

평소에 사용하던 프롭스 속성 대신에 `v-model`을 사용했는데요. 이미 앞 [v-model은 어떻게 동작할까?](https://joshua1988.github.io/web-development/vuejs/v-model-usage/#v-model%EC%9D%80-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%8F%99%EC%9E%91%ED%95%A0%EA%B9%8C) 챕터에서 `v-model` 속성은 `v-bind:value`와 `v-on:input`을 조합해서 만들었다는 것을 배웠기 때문에 `v-model` 속성에 연결한 값이 하위 컴포넌트에 `value` 라는 프롭스 속성으로 내려간다는 사실을 추론할 수 있습니다.
