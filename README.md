# Algorithm


### 2차원 배열에서 max값 구하기
```python
    data = [[1,2,2],[3,8,2],[5,3,5]]

    max_data = max(max(data, key=max))  # 8
    
    max([data[col][row] for col in range(n) for row in range(m)])  # 8
```
#
### 집합(hashSet) 활용하기
```python
    hashSet
    - 교집합 없으면 True ...  x1.isdisjoint(x2)
    - 교집합 찾기 ... x1 & x2
    - 차집합 찾기 ... x1 - x2
    - 합집합 찾기 ... x1 | x2
    - 여집합 찾기 ... x1 ^ x2
```
#
### 문자열 다중 sorting
1) dict.items()의 key와 val을 기준으로 정렬한다.
```python
    # count갯수(value) 내림차순 정렬 후 이름(key) 내림차순 정렬 ... 각각 - 가 아니라 한번에 reverse 처리
    sorted_counter = sorted(counter.items(), key=lambda item: (item[1], item[0]), reverse=True)
```
2) 최댓값 구하기 -> 순위리스트 구하기 -> 길이 1이면 리턴, 아니면 그 리스트를 정렬
```python
    max_val = max(counter.values())
    ranks = []
    for name, val in counter.items():
        if val == max_val:
            ranks.append(name)

    if len(ranks) == 1: return ranks[-1]
    else:
        ranks.sort()
        return ranks[-1]
```
3) 갱신하기 : 임시변수 생성 -> 반복문 돌면서 갱신, max와 동일하다면 이름으로 임시정렬 만들기
```python

    max_val = float('-inf')
    max_name = ''

    for name, val in counter.items():
        if val > max_val:
            max_val = val
            max_name = name
        if val == max_val:
            temp = sorted([max_name, name], key=str, reverse=True)  # Bob, Charlie -> Charlie, Bob
            max_name = temp[0]
```
#

### Java Sort : x[1] 기준 내림차순 reverse 정렬

```python
# python
arr.sort(key= lambda x:x[1], reverse=True)
```

```java
// java 
// 1번 ****
Arrays.sort(arr, (a, b) -> Integer.compare(b[1], a[1]));
// 2번
Arrays.sort(arr, (a, b) -> b[1] - a[1]);   
```

#

### Java Comparator & Lambda(Java8)

```java
Comparator<Integer> c = new Comparator<>() {
  @Override
  public int compare(Integer a, Integer b) {
    return Integer.compare(a, b);
  }
}
```

```java
// Lambda
Comparator<Integer> c = (a, b) -> Integer.compare(a, b);

////////////////////////////////
(a, b) -> Integer.compare(a, b); 
// a < b : return -1 왼쪽정렬(오름차순)
// a = b : return 0
// a > b : return 1  오른쪽정렬(내림차순)
```



#

### collections.Counter 활용

map으로 key의 자료형을 변경할 수 있다.

{0:2, 3:1} str:int  => int:int
```python

    counter = collections.Counter(map(int, num))

```
#
### dictonary keyError를 막아보자 1;
```python
    dict = collections.defaultdict(int)
    dict = collections.defaultdict(set)
    dict = collections.defaultdict(list)
```
#
### dictionary keyError를 막아보자 2; dict.get(key, default)
```python
    for i in range(len(num)):
        if int(num[i]) != counter.get(i, 0): # key i 없으면 0을 반환
            return False
    return True
```
#
### all(iterable) 활용
반복문 모든 요소 True->True
```python
    seen = [False] * len(rooms)
    all(seen) #False
    
    seen = [True] * len(rooms)
    all(seen) #True
```
#
### 4방, 8방탐색
```python
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dirs = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
            dfs(nx, ny)
            ...
```



## Topological Sort

> ordering on the nodes of the graph

- 노드의 순서가 필요한 경우 
- ex. School class prerequisites, Program dependences, Event Scheduling
- O(V+E)



### topological ordering?

- a directed graph 에서 각각의 directed edge (A to B) 가 있을 때, nodeA가 nodeB에 선행되어야 하는 경우



### Directed Acyclic Graphs(DAG)

- Graphs with `directed edges` and **no** `cycles`.



### Topological Sort Algorithm

1. 방문하지 않는 노드 선택
2. 선택한 노드로부터 DFS를 진행
3. DFS 재귀 콜백시 현재 노드를 위상정렬 순서에 `reverse order`로 추가

- cycle 존재시 [] 반환

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        WHITE: 방문 안한 상태
        GRAY : 방문은 했고 stack 에 추가는 안한 상태
        BLACK: 방문도 했고 인접노드가 없어서 stack에 추가한 상태
        """
        
        WHITE = 1
        GRAY = 2
        BLACK = 3
        
        # 1. 그래프 생성: [A, B] B가 A에 선행되어야 하므로 B에서 A로 가는 엣지를 만든다.
        graph = collections.defaultdict(list)
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            
        stack = [] # 차례로 담아 나중에 거꾸로 출력
        is_possible = True # cycle이면 False
        
        color = {k: WHITE for k in range(numCourses)} # key는 노드, val = 1로 세팅
        
        def dfs(v):
            nonlocal is_possible
            
            # cycle 존재시 함수종료
            if not is_possible:
                return
            
            # 방문처리
            color[v] = GRAY
            
            for adj in graph[v]:
                if color[adj] == WHITE:
                    dfs(adj)
                elif color[adj] == GRAY: #cycle
                    is_possible = False
                
            # no more adj nodes to process. Recursion ends
            color[v] = BLACK
            stack.append(v)

            
        # 0부터 n-1까지 for로 돈다. dfs가 돌다가 완료되면 다음 노드부터 다시 시작한다.
        for i in range(numCourses):
            if color[i] == WHITE:
                dfs(i)

        return stack[::-1] if is_possible else []
                    
```





## Priority Queue(heap)

> heapq 모듈은 최소 우선순위 큐를 지원한다.

```python
from heapq import heappush, heappop

h = []
heappush(h, (4, 'kim'))
heappush(h, (3, 'lee'))
heappush(h, (1, 'jong'))
heappush(h, (2, 'seo'))

print(h) # [(1, 'jong'), (2, 'seo'), (3, 'lee'), (4, 'kim')]
while h:
  print(heappop(h)) #(1, 'jong'), (2, 'seo'), (3, 'lee'), (4, 'kim')
```

```python
from heapq import heappush, heappop

h2 = []
heappush(h2, 4)
heappush(h2, 2)
heappush(h2, 1)
heappush(h2, 3)

print(h2) #  [1, 3, 2, 4]
while h2:
    print(heappop(h2)) # 1, 2, 3, 4 순서로 출력
```



## Priority Queue(maxHeap)

> 음수를 넣고 뺄 때 기호를 바꾸면 maxHeap 을 구현할 수 있다.

```python
# 630. Course Schedule III

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        1. lastDay 마감 빠른 순, duration 작은 순으로 정렬
        2. duration < lastDay 이면서
        3. time + duration <= lastDay 이면 maxHeap 에 추가하고 time 업데이트
            위의 조건이 아니라면
                maxHeap[0] > duration 이라면
                maxHeap[0] 을 pq에서 제거하고 새로운 duration을 넣고
                time 에서 maxHeap[0] 을 빼고 새 duration을 더한다.
        4. maxHeap 의 길이를 리턴한다.
        """
        
        courses.sort(key=lambda x: (x[1], x[0]))
        maxHeap = []
        time = 0
        
        for duration, lastDay in courses:
            if duration <= lastDay:
                if duration + time <= lastDay:
                    time += duration
                    heapq.heappush(maxHeap, -duration)
                else:
                    if -maxHeap[0] > duration:
                        max_duration = -maxHeap[0]
                        heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap, -duration)
                        time -= max_duration
                        time += duration
                    
        return len(maxHeap)
```



## Intersection over Union(IoU)

> 최대로 겹치는 사각형의 면적
>
> https://gaussian37.github.io/math-algorithm-iou/
>
> https://tibyte.kr/228

```python
arr = [[2, 3, 8, 7], [3, 2, 10, 6], [6, 1, 11, 4]]

x1, y1 = 0, 0
x2, y2 = 100, 100
for rec in arr:
    x1, y1 = max(x1, rec[0]), max(y1, rec[1])
    x2, y2 = min(x2, rec[2]), min(y2, rec[3])

area = (x2 - x1) * (y2 - y1)
```



## BFS_dijkstra+dp

> dp 이차원 배열과 다익스트라가 혼합된 문제 유형이다.
>
> 다음과 같은 조건을 전제한다.
>
> ```
> dp[i][j] : 시작점에서부터 (i, j)로 가는 걸리는 최소 난이도
> 
> 다익스트라 문제 특징
> 1. 모든 경로의 난이도는 0 이상의 정수이다.
> 2. 시작점에서 최소 난이도의 경로로 갱신해나가면 모든 점에서의 최소 난이도가 기록된다.
> 3. 문제가 한 점에서 특정 점까지의 최소 난이도를 구한다.
> ```

```python
# 1631. Path With Minimum Effort

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        dijkstra
        1. 최대값으로 채운 거리용 이차원 배열, pq, visited 세팅
        2. new_w(이전 노드까지의 max effort 와 현 노드 effort 중 더 큰 값)
        가 costs배열보다 작으면 new_w로 갱신한다.
        """

        m, n = len(heights), len(heights[0])
        dst = (m-1, n-1)

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        costs = [[float('inf')]*n for _ in range(m)]  # 최대값으로 배열을 채운다.

        pq = [(0, 0, 0)]  # w, sx, sy
        visited = set()

        while pq:
            w, x, y = heapq.heappop(pq)
            visited.add((x, y))

            if (x, y) == dst:
                return w

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    new_w = max(w, abs(heights[nx][ny] - heights[x][y]))
                    if new_w < costs[nx][ny]:
                        costs[nx][ny] = new_w
                        heapq.heappush(pq, (new_w, nx, ny))

        return -1

```

```python
# 암벽등반

from heapq import heappop, heappush

m, n = 5, 6
wall = [
    [0, 1, 1, 1, 0, 0],
    [3, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [2, 1, 1, 1, 1, 1]
]

# 최댓값 : 높이 차의 최대
dp = [[50] * n for _ in range(m)]

# 도착지 및 시작지 찾기
for i in range(m):
    for j in range(n):
        if wall[i][j] == 3:
            e = (i, j)
        if wall[i][j] == 2:
            s = (i, j)


def bfs(x, y):
    pq = [(x, y, 0)]

    while pq:
        r, c, dist = heappop(pq)

        if dp[r][c] <= dist:
            continue

        dp[r][c] = dist

        # 아래로 이동
        for nr in range(r+1, m):
            if wall[nr][c] == 0: continue
            ndist = max(dist, nr - r)
            if ndist >= dp[nr][c]: continue
            heappush(pq, (nr, c, ndist))

        # 위로 이동
        for nr in range(r-1, -1, -1):
            if wall[nr][c] == 0: continue
            ndist = max(dist, r - nr)
            if ndist >= dp[nr][c]: continue
            heappush(pq, (nr, c, ndist))

        # 오른쪽으로 이동
        for nc in range(c+1, n):
            if wall[r][nc] == 0: break
            if dist >= dp[r][nc]: continue
            heappush(pq, (r, nc, dist))

        # 왼쪽으로 이동
        for nc in range(c-1, -1, -1):
            if wall[r][nc] == 0: break
            if dist >= dp[r][nc]: continue
            heappush(pq, (r, nc, dist))


bfs(s[0], s[1])

# 구하고자 하는 것 : 도착 좌표까지 가는 난이도의 최솟값
print(dp[e[0]][e[1]])

```



#



## Median vs. Mean

### Median 

- 배열을 좌, 우 같은 갯수의 수로 나누게 하는 중간값
- **배열은 반드시 오름차순으로 정렬되어 있어야 한다.**
- [1, 2, 4] => 인덱스 1인 2가 `median`이다.

### Mean

- 전체 배열 엘리먼트의 평균값
- [1, 3, 5] => (1+3+5)/3 = 3 이 `mean` 이다.



> median은 어떻게 구하나?
>
> "정렬된" 배열 길이가 "홀수" 라는 전제 하에 전체 길이 // 2 가 median 의 인덱스이다.

```python
# 462. Minimum Moves to Equal Array Elements II
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n//2
        nums.sort()
        res = 0
        for i in range(n):
            res += abs(nums[i]-nums[mid])
            
        return res
```

```java
class Solution {
    public int minMoves2(int[] nums) {
        int n = nums.length;
        int mid = n / 2;
        Arrays.sort(nums);
        int res = 0;
        for (int i=0; i<n; i++) {
            res += Math.abs(nums[i] - nums[mid]);
        }
        return res;
    }
}
```



#

## Sorting

### Bubble Sort

> 앞에서부터 두 개씩 비교, 뒤부터 정렬!

Traverse through all array elements.
Last i elements are in place when we finish one traverse!

https://www.geeksforgeeks.org/bubble-sort/



### Selection Sort

> 미정렬 구간을 반복하면서 가장 작은 밸류의 인덱스를 찾아 정렬구간 맨 앞과 교환, 앞부터 정렬!

Sorts an array by repeatedly finding the minimun element from

unsorted part and putting it at the beginning. 

2 Subarrays : 1) The subarray which is already sorted. 2) Remaining subarray which is unsorted.

In every iteration, the minimum element from the unsorted subarray is picked and moved to the sorted array.

https://www.geeksforgeeks.org/selection-sort/



### Insertion Sort

> 앞에서부터 하나 뽑아서 그 앞 카드들과 비교, 뽑은 수보다 작은 수의 바로 뒤에 두고 나머지는 하나씩 뒤로 밀기!

Pick a key form unsorted part.

Compare the key to its predecessor.

If the key is smaller than its predecessor, move the greater elements one position up,

until key becomes greater than one of the (decreasing index)predecessors or go till the end.(to start)

Then, place the key in the correct position.

https://www.geeksforgeeks.org/insertion-sort/

### Quick Sort
> list[0] = Pivot, return quick_sort(left) + [pivot] + quick_sort(right)
- 시간복잡도 O(nlogn) , merge sort와 동일
- 증명 https://ninefloor-design.tistory.com/175 

## 

## Dynamic Programming & Divide and Conquer
> 동적 계획 프로그래밍과 분할 정복

### 분할 정복
- 문제를 나눌 수 없을 때 까지 나누어서 각각의 문제를 풀고, 다시 합병하여 답을 얻는다.
- 부분 문제는 서로 중복되지 않는다.
- `Top-down`
- `Recursive` 사용

> 분할 정복의 경우 중복되는 함수가 생긴다.
> 피보나치를 생각해보면 재귀로 구현시 계속해서 연산이 반복된다. 시간 초과가 날 수 있다는 뜻이다.
> 이것을 보완하는게 메모이제이션을 활용한 동적 계획법이다.
> 부분 문제를 재활용 하는 것이 핵심이다.

### 동적 계획법
- 작은 부분문제를 해결한 후, 해당 부분문제의 해를 활용해 최종적으로 전체 문제를 해결한다.
- 부분 문제는 중복되어, 상위 문제 해결시 재활용이 된다.
- `Bottom-up`
- `Momoization` 사용 : [0 for x in range(n+1)]



## Graph

> 실제 세계의 현상이나 사물을 정점(Vertex)/노드(Node) 와 간선(Edge)로 표현한 것

### Terms
- `Node`, `Vertex`
- `Edge`
- `Undirected` vs. `Directed`
- `Weighted Graph` : weight on each edge

### BFS(Breadth First Search)
- use 2 queues 
- visited & need_to_visit
- `O(V+E)` : 시간복잡도 = 노드 수 + 간선 수

### DFS(Depth First Search)
- use 1 queue and 1 stack
- visited(queue) & need_to_visit(stack)
- `O(V+E)` : 시간복잡도 = 노드 수 + 간선 수

### Dijkstra (최단 경로 알고리즘 중 하나)
- weighted & directional graph 
- single-source shortest path problem : 그래프 내의 특정 노드 u와 그래프 내 다른 모든 노드 각각의 가장 짧은 경로를 찾는 문제
- 하나의 node 에서 다른 모든 nodes 간의 거리 중 가장 짧은 거리를 구한다.
- A-B, A-C, A-D ... which one is the shortest path?
- use 1 array, 1 heap-queue(min-heap)

#### 1. 탐색할 그래프의 시작 정점과 다른 정점 간의 최단거리 구하기
#### 2. 탐색할 그래프의 시작 정점과 다른 정점 간의 최단거리 + 최단경로 구하기
<img src="https://www.fun-coding.org/00_Images/dijkstra.png" width=300>


### Floyd Warshall
- BOG_11404_플로이드
- https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/?ref=gcse