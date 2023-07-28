1. var / val

2. Int / Int?

3. String / String?

4. 타입 추론



# 형태

```kotlin
var 변수명 : 타입
```



# 1. var / val

- var : 읽기, 쓰기 가능

- val : 읽기만 가능
  
  ```kotlin
  fun main(args: Array<String>) {
      
      var i : Int = 10
      val j : Int = 10
  
      i = 20
      // j = 20
      // val은 변경 불가
  
      println(i)
      println(j)
  
  }
  ```

# 2. Int / Int?

- Kotlin의 Int는 null을 허용하지 않음

- null을 허용하려면 타입에 ? 붙여서 선언
  
  ```kotlin
  fun main(args: Array<String>) {
      
      var i : Int = 10
      val j : Int? = 10
  
      // i = null // Int는 null을 허용하지 않음
      j = null
  
      println(i)
      println(j)
  
  }
  ```

# 3. String / String?
