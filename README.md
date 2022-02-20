# Algorithm

> Basic



## Searching



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

## Greedy

## Recursive

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