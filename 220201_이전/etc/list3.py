# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
nums = [1, 7, 3, 6, 5, 2, 13, 14]
for n in nums:
    numbers.append(n)

print(numbers)

# numbers에서 홀수 제거
# 홀수면 인덱스를 늘리지 않고, 짝수면 늘린다.
i = 0
while i <= len(numbers) - 1:
    if numbers[i] % 2:
        del numbers[i]
    else:
        i += 1

print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)
