# 변수(variable)

---

- let

- const

- var
  
  - 한번 선언된 변수를 다시 선언할 수 있다.
    
    ```javascript
    let name = 'Mike'
    console.log(name) // Mike
    
    let name = 'Jane' // error!
    console.log(name)
    ```
  
  - 선언하기 전에 사용할 수 있다.
    
    ```javascript
    var name; // 호이스팅
    console.log(name); // undefined
    name = 'Mike'
    
    // 선언은 호이스팅, 할당은 호이스팅 x
    ```
  
  - 호이스팅 : 스코프 내부 어디서든 변수 선언은 최상위에 선언된 것처럼 행동
    
    ```javascript
    console.log(name); // RefenrenceError
    let name = 'Mike'
    ```

TDZ(Temperal Dead Zone)

```javascript
let age = 30;

// TDZ
function showAge(){
    console.log(age);
    let age = 20;
}
// TDZ

showAge();
```



- 변수의 생성 과정
  
  1. 선언
  
  2. 초기화
  
  3. 할당

- var
  
  1. 선언 및 초기화 단계
  
  2. 할당 단계
     
     - 초기화 : undefined를 할당해 주는 단계

- let
  
  1. 선언
  
  2. 초기화
  
  3. 할당

- const
  
  1. 선언 + 초기화 + 할당
