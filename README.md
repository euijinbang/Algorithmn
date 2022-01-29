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



## Greedy

## Recursive
