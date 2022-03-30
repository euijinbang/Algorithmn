# temp 변수와 인덱스 swap
def is_palindrome(word):
    words = list(word)
    for left in range(len(words) // 2):
        right = len(words) - left - 1

        temp = words[left]
        words[left] = words[right]
        words[right] = temp

    words = ''.join(word)
    if words == word: return True
    return False


# tuple과 인덱스 swap
def is_palindrome(word):
    words = list(word)
    for left in range(len(words) // 2):
        right = len(words) - left - 1

        # tuple 활용
        # = 의 오른쪽 튜플이 위치 바뀌기 전의 값을 보관하고
        # 그 값을 = 왼쪽에 각각 할당한다.
        words[left], words[right] = words[right], words[left]

    words = ''.join(word)
    if words == word: return True
    return False

# 인덱스 활용
def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 Fail을 반환
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False
    return True


# for문 활용
def is_palindrome(word):
    words = list(word)
    pals = []
    for i in range(len(words) - 1, -1, -1):
        pals.append(words[i])

    if words == pals: return True
    return False


# 리스트 슬라이싱 활용
def is_palindrome(word):
    words = list(word)  # ['r', 'a', 'c', 'e', 'c', 'a', 'r']
    pals = words[::-1]  # ['r', 'a', 'c', 'e', 'c', 'a', 'r']

    if words == pals: return True
    return False


# reverse 함수 활용
def is_palindrome(word):
    words = list(word)
    words.reverse()     # 변수할당x
    pal_words = ''.join(words)  # 문자열 리스트를 문자로 join

    if word == pal_words: return True
    return False


# reversed 메서드 활용 (reverse는 list에만 활용 가능하나 reversed는 문자열에도 바로 적용이 가능)
def is_palindrome(word):
    pal_word = reversed(word) # <reversed object at 0x7fc6aee92e50>
    print(list(pal_word))     # ['r', 'a', 'c', 'e', 'c', 'a', 'r']
    print(''.join(reversed(word))) # racecar

    if word == ''.join(reversed(word)): return True
    return False


# 테스트
print(is_palindrome("racecar"))
