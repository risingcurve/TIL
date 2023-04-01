리액트에서 디바이스 내 이미지나 영상을 등록하는 컴포넌트를 만들려면, `input` 요소를 사용할 수 있습니다.

먼저, `input` 요소를 사용하여 파일을 선택할 수 있는 버튼을 만듭니다. 이 버튼을 클릭하면 파일 창이 열리고 사용자가 이미지나 영상 파일을 선택할 수 있습니다. 선택된 파일은 `onChange` 이벤트를 통해 컴포넌트의 상태에 저장됩니다.

예를 들어, 다음과 같이 코드를 작성할 수 있습니다.

```jsx
import React, { useState } from 'react';

function FileUploadComponent() {
  const [file, setFile] = useState(null);

  const handleFileUpload = (event) => {
    const uploadedFile = event.target.files[0];
    setFile(uploadedFile);
  };

  return (
    <div>
      <label htmlFor="file-upload">Choose a file:</label>
      <input
        type="file"
        id="file-upload"
        accept="image/*,video/*"
        onChange={handleFileUpload}
      />
      {file && <p>Selected file: {file.name}</p>}
    </div>
  );
}
```

이 코드는 파일 선택 버튼과 선택된 파일 이름을 표시하는 간단한 컴포넌트를 생성합니다. `input` 요소의 `type` 속성이 `file`로 설정되어 있으며, `accept` 속성으로 이미지와 영상 파일만 선택하도록 제한됩니다. `onChange` 이벤트 핸들러는 파일을 선택할 때마다 호출되며, 선택된 파일은 상태 변수인 `file`에 저장됩니다. 저장된 파일은 선택된 파일 이름을 표시하는 `p` 요소를 렌더링할 때 사용됩니다.

이러한 방식으로 구현하면 디바이스 내 이미지나 영상을 등록하는 컴포넌트를 만들 수 있습니다. 다만, 이 컴포넌트에서 파일을 업로드하려면 서버 사이드에서도 추가적인 처리가 필요합니다.



---

---



# Tailwind CSS 팁

## Arbitrary values 줄이기

```html
<p class="text-[14px]">
  <!-- ... -->
</p>
```

Tailwind는 주로 사용하는 CSS를 모아둔 집합으로 보아도 무방합니다. fontSize를 예시로 들면, 크기를 나타내는 숫자에 무한한 값이 올 수 있는데, Tailwind에는 주로 사용되는 숫자를 모아두고 이 중에서 사용할 수 있도록 해줍니다. fontSize는 ‘xs’, ‘sm’, ‘base’, ‘lg’, ‘xl’, ‘2xl’, …, ‘9xl’ 의 크기만 지원하고 있어서 이 중에서 선택하여 사용할 수 있습니다. 이 크기만으로 디자인이 구성되면 문제가 없겠지만 이 외의 값으로 크기를 설정해야 하는 경우 Tailwind에서는 대괄호로 감싸서 [arbitrary value를 입력할 수 있는 기능](https://tailwindcss.com/docs/adding-custom-styles#using-arbitrary-values)을 제공하고 있습니다. 그런데 때에 따라 이 ‘Arbitrary values’ 기능을 매우 자주 사용해야 하는 경우도 발생합니다. 예를 들어 `rem`이 아닌 `px` 단위로 디자인 요구사항을 맞추어야 하는 경우에는 상당히 빈번하게 사용해야 합니다.

예시로

```html
<div className="p-[8px] h-[35px] text-[12px] rounded-[5px]">
```

와 같은 코드를 작성하게 될 수도 있죠. 이는 작성할 때도 피로하고, 한 줄이 차지하는 너비가 길어지므로 코드를 읽는 개발자에게도 좋지 않습니다.

이러한 부분들은 테마를 커스터마이징하여 해결할 수 있습니다.

만약 `px`단위로 디자인 요구사항을 충족해야 하는 경우라면 다음과 같이 미리 `px`에 대한 프리셋을 전부 ‘extend’로 등록할 수 있습니다.

```js
// tailwind.config.js
const px0_10 = { ...Array.from(Array(11)).map((_, i) => `${i}px`) };
const px0_100 = { ...Array.from(Array(101)).map((_, i) => `${i}px`) };
const px0_200 = { ...Array.from(Array(201)).map((_, i) => `${i}px`) };

module.exports = {
  theme: {
    extend: {
      borderWidth: px0_10,
      fontSize: px0_100,
      lineHeight: px0_100,
      minWidth: px0_200,
      minHeight: px0_200,
      spacing: px0_200,
      ...
    }
  }
}
```

이렇게 한 번 등록하고 나면 고민 없이 디자인 명세에 표기된 수치를 그대로 옮기기만 하면 되어 편리합니다.

위에 꺼냈던 예시도 다음과 같이 보다 간단한 형태로 작성할 수 있습니다.

```html
// BEFORE
<div className="p-[8px] h-[35px] text-[12px] border-[2px] rounded-[5px]">
```

```html
// AFTER
<div className="p-8 h-35 text-12 border-2 rounded-5">
```

코드에서 사용할 크기에 대한 단위를 `rem`이나 `px` 등으로 통일하고, Tailwind에서 제공하는 기본 범위보다 조금 더 촘촘하고 넓은 범위로 미리 ‘extend’에 등록한 결과라고 할 수 있습니다. ‘arbitrary value’ 중에 필요한 부분들을 모두 alias 설정하는 것으로 이해해도 되겠네요.

단, 테마가 생각보다 세분화되어 있어 꽤 많은 프리셋을 등록해야 합니다. 예를 들어 ‘spacing’은 `padding`, `margin`, `width`, `height`, `maxHeight`, `top`, `gap` 등 크기에 대한 많은 것을 다루기는 하지만, `minWidth`, `minHeight`에 대해 alias를 등록하려면 ‘theme extend’에 `spacing`이 아닌 `minWidth`, `minHeight`를 별개로 등록해야 합니다. 크기를 지정할 때 쓰이는 `fontSize`, `borderWidth`, `lineHeight` 등도 마찬가지로 ‘theme extend’에 추가해주어야 하므로, 주로 사용하는 CSS가 ‘theme extend’에 등록되었는지 확인한 후 축약된 표현을 사용해야 합니다. 위의 tailwind.config.js 예시에 ‘extend’에 등록된 것이 꽤 많았던 것도 이러한 이유입니다.

참고로 Tailwind가 v2에서 v3으로 업데이트되면서 “flex-[2_2_0%]”, “col-[2/-2]” 등 여러 숫자를 조합하는 CSS의 arbitrary value도 지원합니다. 이렇게 조합하는 케이스는 미리 ‘extend’에 등록해두려면 경우의 수가 많기 때문에 만일 아직 Tailwind 버전이 v3이 아니라면 v3으로 업데이트하여 오히려 arbitrary value를 적극적으로 사용하는 것을 추천합니다.

## [](https://fe-developers.kakaoent.com/2022/220303-tailwind-tips/#preflight-%EC%B2%98%EB%A6%AC)Preflight 처리

[Preflight](https://tailwindcss.com/docs/preflight) 는 사전적 의미는 `비행 전의`라는 의미입니다. 디자인 시스템을 따라 Tailwind를 적용하다 보면 브라우저에서 기본적으로 설정하는 스타일과 충돌이 발생할 수 있는데, 이를 피하고자 브라우저에서 기본적으로 설정하는 스타일을 무효화 혹은 백지화하는 것입니다. 예를 들면 heading element인 h1, h2, …, h6 등에는 다음과 같이 설정되어 있습니다.

```css
h1,h2,h3,h4,h5,h6 {
  font-size: inherit;
  font-weight: inherit;
  margin: 0;
}
```

이러한 preflight는 `@tailwind base` 에 설정이 되어 있습니다.

또 다른 예시로 svg의 경우는 다음과 같이 적용되어 있습니다.

```css
svg {
  display: block;
  vertical-align: middle;
}
```

무심코 `h1` 태그를 사용하면서 폰트 크기가 크게 출력될 것으로 예상하는 실수를 범할 수 있으니 주의해야 합니다.

Preflight를 원치 않는 경우 다음처럼 config 파일을 설정하여 비활성화시킬 수도 있습니다.

```js
// tailwind.config.js
module.exports = {
  corePlugins: {
    preflight: false,
  }
}
```

## [](https://fe-developers.kakaoent.com/2022/220303-tailwind-tips/#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EC%97%90-classname%EC%9C%BC%EB%A1%9C-%EC%A7%81%EC%A0%91-%EC%8A%A4%ED%83%80%EC%9D%BC-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)컴포넌트에 className으로 직접 스타일 설정하기

React를 예시로 ConfirmButton이라는 컴포넌트를 구현해본다고 가정하겠습니다. 컴포넌트에 style variant를 주기 위해 다음과 같이 바탕은 흰색이고 글자는 파란색이며 rounded 처리된 스타일( 예시 )을 미리 등록해놓고 사용하는 방법이 있습니다.

```js
<ConfirmButton
  styleVariant='bgWhite.textBlue.rounded'
/>
```

혹은 다음과 같이 className을 컴포넌트의 props로 넘겨주며 무한한 variant로 스타일을 지정할 수도 있습니다.

```js
<ConfirmButton
  className="bg-white text-blue-400 rounded"
/>
```

디자인 시스템이 견고하게 짜여 있는 경우 주로 디자인의 변화가 줄어들게 되어, 바로 위와 같이 스타일의 자유도가 높은 설계는 거의 마주할 일이 없습니다. 하지만 Tailwind의 장점인 className으로부터 스타일을 바로 유추할 수 있다는 점을 활용하여 개발자의 편의상 컴포넌트에 직접 className을 props로 받아 스타일을 변경할 수 있도록 설계하는 경우도 간혹 발생하게 됩니다. 위의 두 방법 중 전자의 형태가 조금 더 바람직한 설계로 생각되지만, 부득이하게 후자의 형태로 컴포넌트를 설계한다고 가정해 보겠습니다.

결론부터 이야기하면, 이때 흔히 마주하게 되는 문제가 있고, 이의 해결책으로 [twin.macro](https://github.com/ben-rogerson/twin.macro) 를 활용하면 그 문제를 쉽게 해결할 수 있습니다. 이제 이 문제와 해결책을 살펴보도록 하겠습니다.

### [](https://fe-developers.kakaoent.com/2022/220303-tailwind-tips/#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EC%97%90-classname-props%EB%A5%BC-%EC%B6%94%EA%B0%80%ED%95%A0-%EB%95%8C-%ED%9D%94%ED%9E%88-%EA%B2%AA%EB%8A%94-%EB%AC%B8%EC%A0%9C)컴포넌트에 className props를 추가할 때 흔히 겪는 문제

컴포넌트의 내부 구현을 최대한 단순하게 다음과 같이 구성해 보았습니다.

```js
const ConfirmButton = (props) => {
  const { className, ...rest } = props;
  return (
    <button
      className={classnames(
        'bg-black text-red-400',
        className,
      )}
      {...rest}
    ></button>
  );
});
```

default로 설정된 스타일이 존재하고, className을 props로 전달받은 경우에 default로 설정된 스타일이 아니라 props로 전달받은 스타일을 적용하려는 의도입니다.

하지만 의도한 대로 동작할까요?

```js
<ConfirmButton
  className="bg-white text-blue-400 rounded"
/>
```

위의 코드는 다음과 같은 결과물로 보여집니다.

결과

className으로 설정한 흰색 바탕과 파란 글자가 아니라 컴포넌트 내부에서 default로 설정해둔 검은색 바탕에 붉은 글자가 출력됩니다. default로 설정된 className과 props로 넘겨받은 className을 병합하려고 할 때 의도대로 동작하지 않는 문제입니다.

이 현상을 조금 더 단순한 형태로 변경하여 살펴보겠습니다.

### [](https://fe-developers.kakaoent.com/2022/220303-tailwind-tips/#tailwind-class%EC%9D%98-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84)Tailwind Class의 우선순위

예를 들어, 다음의 경우에 우선순위는 명확합니다. child에 위치한 `text-blue-400` 가 적용되는 것을 쉽게 예측할 수 있습니다.

```html
<div className="text-red-400">
  <div className="text-blue-400">Hello world</div>
</div>
```

결과: Hello world

다음의 경우는 어떠할까요?

```html
<div className="text-red-400 text-blue-400">Hello world</div>
```

결과: Hello world

하나의 element에서 두 클래스가 color라는 같은 CSS 속성을 다루고 있습니다. 이 경우, 아무리 `text-red-400`, `text-blue-400`의 순서를 바꾸어도 `text-red-400`이 적용됩니다. 😭

Tailwind CSS 빌드의 결과물을 살펴보면 원인을 알 수 있습니다.

```bash
> npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch
```

```css
// dist/output.css....text-blue-400 {
    --tw-text-opacity: 1;
    color: rgb(96 165 250 / var(--tw-text-opacity));
}

.text-red-400 {
  --tw-text-opacity: 1;
  color: rgb(248 113 113 / var(--tw-text-opacity));
}
...
```

Tailwind에서는 수많은 클래스들을 사용할 수 있지만, 이 중에서 소스 코드에 선언된 클래스를 검출하여 스타일을 구성합니다. 이때 소스 코드에서 클래스가 출현한 빈도나 출현한 순서와는 상관없이 Tailwind에서 정의한 순서에 따라 output.css처럼 스타일을 구성합니다. 따라서 하나의 element에 위의 두 클래스가 동시에 적용되면 뒤에 선언된 `.text-red-400`이 cascading에 의해 `.text-blue-400` 보다 항상 우선하게 됩니다. 이러한 우선순위를 간과하는 경우가 많고, default로 설정된 className과 props로 넘겨받은 className을 병합하는 과정에서 뒤에 위치한 className이 적용될 것으로 착각하면 의도하지 않은 결과를 낳을 수 있습니다.

### [](https://fe-developers.kakaoent.com/2022/220303-tailwind-tips/#tailwind-class-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%EC%B2%98%EB%A6%AC-%EB%B0%A9%EC%95%88)Tailwind Class 우선순위 처리 방안

하나의 엘리먼트에 같은 속성을 정의하는 CSS가 두 개 이상 설정되어 경합이 발생할 수 있는 경우에 [twin.macro](https://github.com/ben-rogerson/twin.macro) 가 해결책이 될 수 있습니다. twin.macro는 className에 선언된 여러 클래스 중에 뒤에 위치한 클래스가 최종적으로 적용되도록 해줍니다.

twin.macro를 사용하여 다음과 같이 className을 선언하면 뒤에 위치한 `text-blue-400`이 더 높은 우선순위를 갖게 됩니다.

```js
tw`text-red-400 text-blue-400`
```

twin.macro는 혹여나 개발자가 실수로 같은 속성의 스타일을 하나의 요소에 중복으로 설정하더라도 결과를 명확히 예측할 수 있기 때문에 생산성 측면에도 도움이 됩니다.

참고로 아직까지 twin.macro가 Tailwind v3에서 완전히 사용할 수 있는 단계는 아닙니다. 현재 [‘Tailwind v3 updates’](https://github.com/ben-rogerson/twin.macro/issues/589)라는 이슈를 통해 업데이트 중입니다.

twin.macro의 원리를 간단하게 살펴보겠습니다.

**twin.macro 동작 원리**

요약하면, className에 선언된 클래스의 CSS 속성을 key로 하여 key에 값을 덮어쓰는 원리입니다. className의 앞에 선언된 class부터 일종의 맵처럼 CSS 속성을 key로, 값을 value로 하여 Object에 덮어쓰는 과정을 반복합니다. 이 과정에서 key가 같아서 경합이 발생하면 뒤에 선언된 스타일이 앞에 선언된 스타일을 덮어씁니다.

![Headwind example](https://fe-developers.kakaoent.com/static/4a32ad43f117e9f76a01af07c804c32a/f058b/twinmacro.png "Headwind example")

세부적인 과정은 다음과 같습니다.

1. babelPluginMacros 로 매크로를 등록합니다.
2. 노드를 순회하며 twin.macro로 선언된 스타일들을 전부 찾습니다.
3. `string[]` 으로 선언된 스타일을 `Object`로 변환합니다.
4. className을 순회하며 `Object`에 스타일을 계속 덮어씁니다.

## [](https://fe-developers.kakaoent.com/2022/220303-tailwind-tips/#plugin---headwind)Plugin - HeadWind

하나의 element에 많은 CSS를 설정해야 하는 경우가 있습니다.

```text
<div className="sticky top-0 bg-white z-10 flex sm:grid items-center sm:items-end grid-cols-2 sm:grid-cols-3 p-10 border-b pt-15 border-gray top-0">
```

이런 경우에 한눈에 모든 내용이 다 들어오지 않기 때문에 자칫하다가는 앞에 있는 CSS를 인지하지 못하고 뒤에 똑같은 CSS를 또 기입하는 휴먼 에러가 발생할 수 있습니다. (위의 예시에는 top-0 이 중복으로 들어가 있습니다)

이런 부분을 조금 해소할 수 있는 플러그인이 있는데, Tailwind의 클래스를 정렬해주는 기능을 하는 [Headwind](https://marketplace.visualstudio.com/items?itemName=heybourn.headwind) 입니다. 알파벳 순의 정렬은 아니고 스타일의 카테고리대로 정렬해주어 코드를 이해하는데에도 조금 더 수월해집니다.

![Headwind example](https://fe-developers.kakaoent.com/3b9a23dd1c886da470e44e1179b4b171/headwind.gif)
