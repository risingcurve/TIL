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

# 

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

# 

# DP

---

DP(Dynamic Programming)는 이전에 계산한 값을 저장해 놓고 재활용하여 중복 계산을 줄이는 알고리즘 기법입니다. 파이썬에서는 DP를 구현하는 방법은 여러가지가 있습니다. 여기서는 Memoization 방식과 Bottom-up 방식을 예제 코드로 설명하겠습니다.

### 

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

### 

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

# 

# 완전 탐색

---

완전탐색(Brute-force)은 가능한 모든 경우를 검사하여 답을 찾는 알고리즘 기법입니다. 파이썬에서는 다음과 같이 완전탐색을 구현할 수 있습니다.

### 

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

# 

# 그리디

---

그리디(Greedy) 알고리즘은 현재 상황에서 가장 좋은 선택을 하는 것을 반복하여 최적해를 구하는 알고리즘 기법입니다. 파이썬에서는 다음과 같이 그리디 알고리즘을 구현할 수 있습니다.

### 

### 예제: 동전 거스름돈 문제

`n`원의 동전을 거슬러 주어야 할 때, 거슬러 줄 동전의 개수가 최소가 되도록 하려면 어떻게 거슬러 줘야 할까요? 예를 들어, 1260원을 거슬러 주어야 할 때, 500원, 100원, 50원, 10원 동전이 각각 몇 개씩 필요한지 구하는 문제입니다.

```python
def change(n):
    coins = [500, 100, 50, 10]  # 동전 종류
    count = 0  # 거슬러 준 동전 개수
    for coin in coins:
        count += n // coin  # 동전 개수 누적
        n %= coin  # 거슬러 줘야 할 돈 계산
    return count

# 1260원 거슬러 주기
print(change(1260))  # 출력 결과: 6
```

위 코드에서 `change()` 함수는 `n`원을 거슬러 줄 때, 최소한의 동전 개수를 계산하여 리턴합니다. 동전 종류를 리스트로 정의하고, 반복문을 통해 각 동전 종류마다 거슬러 줘야 할 동전 개수를 계산합니다. 거슬러 줘야 할 돈을 계산하기 위해 나머지 연산자(`%`)를 사용합니다. 마지막으로 거슬러 준 동전 개수를 리턴합니다.

### 

### 예제1: 동전 거스름돈

동전의 종류와 거스름돈의 금액이 주어졌을 때, 거슬러줘야 할 동전의 최소 개수를 구하는 예제입니다.

```python
def coin_change(coins, amount):
    coins.sort(reverse=True)  # 동전의 큰 단위부터 검사
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    if amount == 0:
        return count
    else:
        return -1

# 동전 거스름돈 문제 예제
coins = [500, 100, 50, 10]
amount = 1260
print(coin_change(coins, amount))
```

위 코드에서 `coin_change()` 함수는 주어진 동전의 종류와 거스름돈의 금액을 받아 거슬러줘야 할 동전의 최소 개수를 구합니다. 동전의 종류를 큰 단위부터 검사하면서 거슬러줘야 할 금액(amount)보다 작은 동전을 가능한 많이 거슬러주면 됩니다. 거슬러줘야 할 금액이 동전의 종류로 나누어 떨어지지 않는 경우, 거스름돈을 정확히 거슬러줄 수 없으므로 -1을 리턴합니다.

### 

### 예제2: 회의실 배정

주어진 회의 일정 중 겹치지 않게 최대한 많은 회의를 할 수 있는 예제입니다.

```python
def meeting_rooms(intervals):
    intervals.sort(key=lambda x: x[1])  # 종료시간 기준으로 정렬
    count = 0
    end_time = 0
    for interval in intervals:
        if interval[0] >= end_time:
            end_time = interval[1]
            count += 1
    return count

# 회의실 배정 문제 예제
intervals = [(0, 30), (5, 10), (15, 20)]
print(meeting_rooms(intervals))
```

위 코드에서 `meeting_rooms()` 함수는 주어진 회의 일정 중 겹치지 않게 최대한 많은 회의를 할 수 있는 개수를 구합니다. 회의 일정을 종료시간을 기준으로 정렬하면서, 현재 회의가 이전 회의의 종료시간보다 뒤에 시작하는 경우에만 회의를 할 수 있습니다. 이전 회의의 종료시간을 갱신하고, 회의를 할 수 있는 개수를 증가시킵니다.

# 

# 분할정복

---

분할정복(Divide and Conquer) 알고리즘은 큰 문제를 작은 문제로 분할한 후, 각 작은 문제를 해결하고, 이를 합쳐서 큰 문제를 해결하는 알고리즘입니다. 파이썬에서는 다음과 같이 분할정복 알고리즘을 구현할 수 있습니다.

### 예제: 이진 탐색

주어진 정렬된 리스트에서 특정한 값의 위치를 찾는 문제입니다. 이진 탐색은 리스트의 중간 위치의 값을 검사하여 찾고자 하는 값이 리스트의 중간 위치보다 큰지 작은지를 비교하여 검색 범위를 절반으로 줄여가면서 값을 찾아갑니다.

```python
def binary_search(lst, x):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# 정렬된 리스트에서 5의 위치 찾기
lst = [1, 3, 5, 7, 9]
x = 5
print(binary_search(lst, x))  # 출력 결과: 2
```

위 코드에서 `binary_search()` 함수는 주어진 정렬된 리스트 `lst`에서 값을 찾는 이진 탐색 알고리즘을 구현합니다. 검색 범위를 나타내는 변수 `start`와 `end`를 초기화하고, 반복문을 통해 검색 범위를 절반씩 줄여나가면서 값을 찾습니다. 중간 위치의 값을 `mid`에 저장하고, 찾고자 하는 값 `x`와 비교하여 검색 범위를 조절합니다. 값을 찾으면 해당 위치를 리턴하고, 값이 없으면 -1을 리턴합니다.

# 

# 백트래킹

---

백트래킹(Backtracking)은 해를 찾는 도중에 가능성이 없는 부분을 차단하여 불필요한 탐색을 줄이는 알고리즘입니다. 파이썬에서는 다음과 같이 백트래킹 알고리즘을 구현할 수 있습니다.

### 예제: N-Queen 문제

N x N 크기의 체스판 위에 N개의 퀸을 놓는 문제입니다. 퀸은 가로, 세로, 대각선 방향으로 모두 공격할 수 있으므로, 서로 공격할 수 없도록 N개의 퀸을 놓는 문제입니다. 백트래킹 알고리즘을 사용하여 퀸을 놓을 수 있는 모든 경우의 수를 구합니다.

```python
def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or \
            candidate[queen_row] - queen_row == current_col - current_row or \
            candidate[queen_row] + queen_row == current_col + current_row:
            return False
    return True

def dfs(n, current_row, current_candidate, final_result):
    if current_row == n:
        final_result.append(current_candidate[:])
        return
    for candidate_col in range(n):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            dfs(n, current_row + 1, current_candidate, final_result)
            current_candidate.pop()

def solve_n_queens(n):
    final_result = []
    dfs(n, 0, [], final_result)
    return final_result

# 4-Queen 문제 풀이
print(solve_n_queens(4))  # 출력 결과: [[1, 3, 0, 2], [2, 0, 3, 1]]
```

위 코드에서 `is_available()` 함수는 현재 퀸이 놓을 수 있는 위치인지 검사하는 함수입니다. `dfs()` 함수는 백트래킹 알고리즘을 구현한 함수로, 현재 놓을 수 있는 퀸의 후보를 찾아서 재귀적으로 탐색합니다. 모든 행에 대해 재귀적으로 탐색을 마치면 결과를 `final_result` 리스트에 추가합니다. `solve_n_queens()` 함수는 전체 문제를 해결하기 위해 `dfs()` 함수를 호출하는 함수입니다.

위 코드에서는 4-Queen 문제를 풀이하였습니다. `solve_n_queens(4)`를 호출하면, 결과로 [[1, 3, 0, 2], [2, 0, 3, 1]]와 같이 2개의 가능한 경우의 수를 구할 수 있습니다.

# 

# 그래프

---

파이썬에서 그래프를 구현하는 방법은 여러 가지가 있습니다. 이 중에서 대표적인 방법은 인접 리스트와 인접 행렬입니다.

### 인접 리스트

인접 리스트(Adjacency List)는 그래프를 연결 리스트로 표현하는 방식입니다. 파이썬에서는 딕셔너리를 이용하여 각 노드에 연결된 노드들을 리스트로 저장합니다. 예를 들어, 다음과 같은 그래프를 인접 리스트로 표현할 수 있습니다.

![graph_example](https://upload.wikimedia.org/wikipedia/commons/5/5d/Simple_graph.svg)

위 그래프를 인접 리스트로 구현하면 다음과 같습니다.

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}
```

위 코드에서 `graph` 딕셔너리는 각 노드와 그에 대한 연결 리스트를 저장합니다. 예를 들어, 'A' 노드와 연결된 노드들은 'B'와 'C'이며, 'B' 노드와 연결된 노드들은 'A', 'C', 'D'입니다.

### 

### 인접 행렬

인접 행렬(Adjacency Matrix)은 그래프를 2차원 배열로 표현하는 방식입니다. 파이썬에서는 이차원 리스트로 구현할 수 있습니다. 인접 행렬에서 i번째 행과 j번째 열이 1이면 i와 j가 연결된 것이고, 0이면 연결되지 않은 것입니다. 예를 들어, 위 그래프를 인접 행렬로 구현하면 다음과 같습니다.

```python
graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
]
```

`graph = [     [0, 1, 1, 0, 0, 0],     [1, 0, 1, 1, 0, 0],     [1, 1, 0, 1, 1, 0],     [0, 1, 1, 0, 1, 1],     [0, 0, 1, 1, 0, 0],     [0, 0, 0, 1, 0, 0] ]`

위 코드에서 `graph` 리스트는 2차원 배열로, 행과 열의 번호가 각각 노드의 번호와 대응됩니다. 예를 들어, 0행 1열은 'A'와 'B'가 연결되어 있는지를 나타냅니다. 0행 1열이 1이므로 'A'와 'B'가 연결된 것입니다.

그리고 딕셔너리(Dictionary)를 사용하여 구현할 수 있습니다. 딕셔너리는 각각의 키(Key)에 대해 값을 저장할 수 있는 자료형으로, 그래프의 노드를 키(Key)로, 각 노드의 인접 노드를 값(Value)으로 저장할 수 있습니다.

### 

### 예제: 무방향 그래프 구현

다음은 무방향 그래프를 구현하는 예제입니다.

```python
graph = {}

# 그래프에 노드 추가
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'D']
graph['D'] = ['B', 'C', 'E']
graph['E'] = ['D']

print(graph)
```

위 코드에서는 딕셔너리 `graph`에 각 노드를 키(Key)로, 각 노드의 인접 노드를 값(Value)으로 추가합니다. 예를 들어, 'A' 노드의 인접 노드는 'B'와 'C'입니다.

출력 결과는 다음과 같습니다.

```python
{'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}
```

### 

### 예제: 유향 그래프 구현

다음은 유향 그래프를 구현하는 예제입니다.

```python
graph = {}

# 그래프에 노드 추가
graph['A'] = ['B', 'C']
graph['B'] = ['D']
graph['C'] = ['D']
graph['D'] = ['E']
graph['E'] = []

print(graph)
```

위 코드에서는 딕셔너리 `graph`에 각 노드를 키(Key)로, 각 노드의 인접 노드를 값(Value)으로 추가합니다. 예를 들어, 'A' 노드의 인접 노드는 'B'와 'C'입니다. 'E' 노드는 인접 노드가 없으므로 빈 리스트([])로 초기화합니다.

출력 결과는 다음과 같습니다.

```python
{'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []
```

# 오일러 경로

---

오일러 경로(Eulerian path)는 그래프의 모든 간선을 한 번씩만 방문하면서 출발점과 도착점이 다른 경로입니다. 파이썬으로 오일러 경로를 구하는 알고리즘은 다음과 같습니다.

1. 그래프가 오일러 경로가 되는지 확인합니다. 이를 위해서는 그래프가 무방향 그래프이고 모든 정점의 차수가 짝수이거나, 정확히 두 개의 정점의 차수가 홀수이어야 합니다.
2. 오일러 경로가 있다면 시작 정점을 선택합니다. 시작 정점은 차수가 홀수인 정점 중 임의의 하나를 선택하거나, 그렇지 않으면 아무 정점이나 선택할 수 있습니다.
3. 시작 정점에서 출발하여 갈 수 있는 경로가 있는 동안 이동합니다. 이동한 경로는 스택에 저장합니다.
4. 이동한 경로의 마지막 노드에서 출발하여 갈 수 있는 경로가 있는 동안 이동합니다. 이동한 경로도 스택에 저장합니다.
5. 경로를 이동할 수 없을 때, 스택에서 경로를 하나씩 꺼내면서 경로를 출력합니다.

파이썬 코드로 구현하면 다음과 같습니다.

```python
def find_eulerian_path(graph):
    # 그래프가 오일러 경로가 되는지 확인
    odd_degree_vertices = [v for v in graph if len(graph[v]) % 2 == 1]
    if len(odd_degree_vertices) not in [0, 2]:
        return None

    # 시작 정점 선택
    start_vertex = odd_degree_vertices[0] if len(odd_degree_vertices) == 1 else list(graph.keys())[0]

    # DFS로 경로 탐색
    stack = [start_vertex]
    path = []
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            stack.append(u)
        else:
            path.append(stack.pop())

    return path[::-1]
```

이 함수는 인접리스트 형태의 그래프를 입력으로 받아, 오일러 경로를 반환합니다. 만약 그래프에 오일러 경로가 없다면 `None`을 반환합니다.

# 해밀턴 경로

---

해밀턴 경로(Hamiltonian path)는 그래프에서 모든 정점을 한 번씩만 방문하면서 이동하는 경로입니다. 파이썬으로 해밀턴 경로를 구하는 알고리즘은 다음과 같습니다.

1. 그래프의 모든 정점에 대해, 해당 정점을 시작점으로 해서 DFS 탐색을 시작합니다.
2. DFS 탐색에서, 이미 방문한 정점은 다시 방문하지 않도록 체크합니다.
3. DFS 탐색에서, 모든 정점을 방문한 경우에는 해당 경로를 반환합니다.
4. DFS 탐색에서, 방문하지 않은 정점을 선택해서 다음 DFS 탐색을 수행합니다.

파이썬 코드로 구현하면 다음과 같습니다.

```python
def find_hamiltonian_path(graph):
    def dfs(current, visited, path):
        visited[current] = True
        path.append(current)

        if len(path) == len(graph):
            return path

        for neighbor in graph[current]:
            if not visited[neighbor]:
                result = dfs(neighbor, visited, path)
                if result:
                    return result

        visited[current] = False
        path.pop()
        return None

    for start in graph:
        visited = {node: False for node in graph}
        path = []
        result = dfs(start, visited, path)
        if result:
            return result

    return None
```

이 함수는 인접리스트 형태의 그래프를 입력으로 받아, 해밀턴 경로를 반환합니다. 만약 그래프에 해밀턴 경로가 없다면 `None`을 반환합니다.
