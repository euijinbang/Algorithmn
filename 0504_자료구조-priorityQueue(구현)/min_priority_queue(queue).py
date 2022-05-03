from queue import PriorityQueue

q = PriorityQueue()
q1 = PriorityQueue(maxsize=10)

q1.put((1, 'kim'))
q1.put((4, 'park'))
q1.put((2, 'lee'))
q1.put((3, 'seo'))

res = []
while not q1.empty():
    # print(q1.get())  # Remove and return an item from the queue
    res.append(q1.get())

# 최대우선순위 대로 뽑기
print(res[::-1])
