

# DFS

---

DFS(깊이 우선 탐색)를 파이썬으로 구현하려면, 일반적으로 재귀 함수를 사용하여 구현할 수 있습니다.

아래는 간단한 예제 코드입니다.

```python
# 인접 리스트를 사용한 DFS 구현 예제
def dfs(v, visited, adj_list):
    visited[v] = True  # 현재 노드를 방문 처리
    print(v, end=' ')  # 현재 노드 출력

    for i in adj_list[v]:  # 현재 노드와 인접한 노드 중
        if not visited[i]:  # 방문하지 않은 노드가 있다면
            dfs(i, visited, adj_list)  # 해당 노드를 방문

# 예제 그래프
adj_list = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [1, 2, 5],
    5: [2, 4, 8],
    6: [3, 7],
    7: [3, 6],
    8: [5]
}

visited = [False] * 9  # 각 노드 방문 여부를 저장할 리스트
dfs(1, visited, adj_list)  # 1번 노드에서 DFS 탐색 시작

```

위 코드에서 `dfs()` 함수는 인접 리스트 `adj_list`와 현재 노드의 인덱스 `v`, 그리고 각 노드의 방문 여부를 저장할 리스트 `visited`를 입력으로 받습니다.

`visited[v] = True`와 `print(v, end=' ')`는 현재 노드를 방문하고 출력하는 부분입니다.

그리고 `for`문에서는 현재 노드와 인접한 노드들을 하나씩 방문하면서, 이미 방문한 노드는 무시하고 방문하지 않은 노드만 방문하는 재귀적인 함수 호출을 수행합니다.

최초로 `dfs()` 함수를 호출할 때는 시작 노드의 인덱스와 방문 여부를 저장할 리스트를 입력으로 넣어주면 됩니다.







네, DFS 구현 시 스택(Stack)을 사용하는 방법도 있습니다. 스택은 후입선출(LIFO) 구조이므로, DFS에서는 현재 노드와 인접한 노드 중 방문하지 않은 노드가 있으면 해당 노드를 스택에 삽입하고 방문 처리합니다. 그리고 스택에서 꺼낸 노드를 다시 시작점으로 하여 인접한 노드 중 방문하지 않은 노드가 있으면 스택에 삽입하고 방문 처리합니다. 이 과정을 스택이 빌 때까지 반복하면 됩니다.

아래는 스택을 사용하여 DFS를 구현한 예제 코드입니다.



```python
# 스택을 사용한 DFS 구현 예제
def dfs(start, adj_list):
    visited = [False] * len(adj_list)  # 각 노드의 방문 여부를 저장할 리스트
    stack = [start]  # 시작 노드를 스택에 삽입

    while stack:
        v = stack.pop()  # 스택에서 노드를 꺼내어
        if not visited[v]:  # 방문하지 않은 노드라면
            visited[v] = True  # 해당 노드를 방문 처리하고 출력
            print(v, end=' ')

            # 해당 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 삽입
            for i in adj_list[v]:
                if not visited[i]:
                    stack.append(i)

# 예제 그래프
adj_list = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [1, 2, 5],
    5: [2, 4, 8],
    6: [3, 7],
    7: [3, 6],
    8: [5]
}

dfs(1, adj_list)  # 1번 노드에서 DFS 탐색 시작

```



위 코드에서 `dfs()` 함수는 시작 노드의 인덱스와 인접 리스트 `adj_list`를 입력으로 받습니다.

`visited` 리스트는 각 노드의 방문 여부를 저장합니다. 스택은 `stack` 리스트에 저장되며, 최초로 시작 노드를 스택에 삽입합니다.

그리고 `while`문에서는 스택이 빌 때까지 노드를 꺼내어 방문하지 않은 노드면 방문 처리하고 출력한 후, 해당 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 삽입합니다.

최초로 `dfs()` 함수를 호출할 때는 시작 노드의 인덱스와 인접 리스트를 입력으로 넣어주면 됩니다.







# BFS

---

BFS(Breadth-First Search)는 큐(Queue)를 이용하여 구현할 수 있습니다. 큐는 선입선출(FIFO) 구조이므로, BFS에서는 현재 노드와 인접한 노드 중 방문하지 않은 노드가 있으면 해당 노드를 큐에 삽입하고 방문 처리합니다. 그리고 큐에서 꺼낸 노드를 다시 시작점으로 하여 인접한 노드 중 방문하지 않은 노드가 있으면 큐에 삽입하고 방문 처리합니다. 이 과정을 큐가 빌 때까지 반복하면 됩니다.

아래는 큐를 사용하여 BFS를 구현한 예제 코드입니다.

```python
# 큐를 사용한 BFS 구현 예제
from collections import deque

def bfs(start, adj_list):
    visited = [False] * len(adj_list)  # 각 노드의 방문 여부를 저장할 리스트
    queue = deque([start])  # 시작 노드를 큐에 삽입

    while queue:
        v = queue.popleft()  # 큐에서 노드를 꺼내어
        if not visited[v]:  # 방문하지 않은 노드라면
            visited[v] = True  # 해당 노드를 방문 처리하고 출력
            print(v, end=' ')

            # 해당 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 삽입
            for i in adj_list[v]:
                if not visited[i]:
                    queue.append(i)

# 예제 그래프
adj_list = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [1, 2, 5],
    5: [2, 4, 8],
    6: [3, 7],
    7: [3, 6],
    8: [5]
}

bfs(1, adj_list)  # 1번 노드에서 BFS 탐색 시작

```



위 코드에서 `bfs()` 함수는 시작 노드의 인덱스와 인접 리스트 `adj_list`를 입력으로 받습니다.

`visited` 리스트는 각 노드의 방문 여부를 저장합니다. 큐는 `deque()` 함수를 사용하여 `queue` 리스트를 생성하며, 최초로 시작 노드를 큐에 삽입합니다.

그리고 `while`문에서는 큐가 빌 때까지 노드를 꺼내어 방문하지 않은 노드면 방문 처리하고 출력한 후, 해당 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 삽입합니다.

최초로 `bfs()` 함수를 호출할 때는 시작 노드의 인덱스와 인접 리스트를 입력으로 넣어주면 됩니다.









# DP

---

DP(Dynamic Programming)는 이전에 계산한 값을 저장해 놓고 재활용하여 중복 계산을 줄이는 알고리즘 기법입니다. 파이썬에서는 DP를 구현하는 방법은 여러가지가 있습니다. 여기서는 Memoization 방식과 Bottom-up 방식을 예제 코드로 설명하겠습니다.

### Memoization 방식

Memoization은 이전에 계산한 값을 저장하고 재활용하는 방식입니다. 이전에 계산한 값이 필요할 때마다 값을 조회하여 사용합니다. Memoization 방식은 보통 재귀 함수와 함께 사용됩니다.

아래는 Memoization 방식을 사용하여 피보나치 수열을 구하는 예제 코드입니다.

```python
# Memoization 방식으로 구현한 피보나치 수열 예제
memo = [0] * 100  # 메모이제이션을 위한 리스트

def fibonacci(n):
    if n <= 1:
        return n

    if memo[n] != 0:  # 이미 계산한 값이라면 그 값을 리턴
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)  # 계산한 값을 메모이제이션
    return memo[n]

# 피보나치 수열의 10번째 수 출력
print(fibonacci(10))

```



위 코드에서 `memo` 리스트는 메모이제이션을 위한 리스트입니다. 이전에 계산한 값을 저장하기 위해 전역 변수로 선언되어 있습니다. `fibonacci()` 함수는 재귀 함수로, 피보나치 수열의 n번째 값을 계산합니다.

먼저 n이 1보다 작거나 같은 경우에는 n을 그대로 리턴합니다. 이때, `memo[n]` 값이 0이 아니라면 이미 계산한 값이므로 그 값을 바로 리턴합니다.

만약 `memo[n]` 값이 0이라면, 이전에 계산하지 않은 값이므로 `memo[n]`에 `fibonacci(n-1)`과 `fibonacci(n-2)`의 합을 저장한 후, `memo[n]` 값을 리턴합니다.

### Bottom-up 방식

Bottom-up 방식은 작은 문제부터 해결하여 큰 문제를 해결하는 방식입니다. 보통 반복문을 사용하여 구현합니다.

아래는 Bottom-up 방식으로 피보나치 수열을 구하는 예제 코드입니다.

```python
# Bottom-up 방식으로 구현한 피보나치 수열 예제
n = 10  # 구하고자 하는 피보나치 수열의 크기
dp = [0] * (n + 1)  # DP를 위한 리스트

dp[0], dp[1] = 0, 1  # 초기값 설정

for i in range(2, n + 1):  # Bottom-up 방식으로 DP 계산
    dp[i] = dp[i - 1] + dp[i - 2]

# 피보나치 수열의 10번째

```







# 완전 탐색

---

완전탐색(Brute-force)은 가능한 모든 경우를 검사하여 답을 찾는 알고리즘 기법입니다. 파이썬에서는 다음과 같이 완전탐색을 구현할 수 있습니다.

### 예제1: 주어진 리스트에서 최대값 찾기

```python
def find_max(lst):
    max_value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
    return max_value

# 주어진 리스트에서 최대값 찾기
lst = [3, 1, 5, 2, 4]
print(find_max(lst))

```



위 코드에서 `find_max()` 함수는 주어진 리스트에서 최대값을 찾아 리턴합니다. `max_value` 변수에 리스트의 첫번째 값을 할당하고, 반복문을 통해 리스트의 각 요소를 검사하면서 `max_value`보다 큰 값이 나오면 `max_value`에 해당 값을 할당합니다. 반복문을 마치고 나면 `max_value`에는 리스트의 최대값이 저장되어 있습니다.

### 

### 예제2: 비밀번호 만들기

주어진 문자열 집합으로 가능한 모든 비밀번호 조합을 생성하는 예제입니다.

```python
def find_max(lst):
    max_value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
    return max_value

# 주어진 리스트에서 최대값 찾기
lst = [3, 1, 5, 2, 4]
print(find_max(lst))

```



위 코드에서는 `itertools` 모듈의 `product()` 함수를 사용하여 가능한 모든 조합을 생성합니다. `chars` 리스트에서 `n`개의 문자를 선택하여 가능한 모든 조합을 생성합니다. 각 조합은 튜플 형태로 반환되므로, `join()` 함수를 사용하여 문자열로 변환한 후 출력합니다.
