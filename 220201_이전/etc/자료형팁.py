# 문자열
# +, * 연산보다는 join 사용하기
import time
start = time.time()

s = ''
# for i in range(10000):
#     s = s + str(i)
s = s.join([str(i) for i in range(10000)])

print(s)
print("time :", (time.time() - start) * 1000) # 현재시각-시작시각

############
chr(65)  # A
ord('A') # 65

############ short circuit
# or 연산의 앞 항이 참이면 뒤는 확인하지 않음
# and 연산의 앞 항이 거짓이면 뒤는 확인하지 않음

############ list comprehension 이 append 반복보다 더 빠름
list_arr = [i for i in range(1000000)]

list_arr2 = []
for i in range(1000000) : list_arr.append(i)

#### sorted()는 원래 값은 바꾸지 않음, sort()는 바꿈

#### slicing 활용
lst = [2, 3, 4, 5]
# 0 번째 인덱스에 1 넣는 두 가지 방법
# lst = [1] + lst
lst[:0] = [1] # [1, 2, 3, 4, 5]

print(lst)