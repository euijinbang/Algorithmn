# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        if some_list[i] == value:
            return True
        else:
            i += 1

    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))



# 피타고라스
for a in range(1, 400):
    for b in range(a, 400):
        c = 400 - a - b
        if a**2 + b**2 == c**2 and a+b+c == 400:
            print(a * b * c)


# 리스트 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(len(numbers) // 2):
    # 좌측과 우측의 인덱스 설정
    right = len(numbers) - left - 1

    # 위치바꾸기
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("뒤집어진 리스트: " + str(numbers))

