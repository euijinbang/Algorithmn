"""
딕셔너리 키는 중복을 허용하지 않으므로 1번 케이스 사용불가! 주의

key : DFS 를 2번 사용하는 것! 매번 2번씩 재귀가 호출됨.

배열이나 visited 개념이 아니라 인덱스로 접근하면 된다.
숫자를 다 사용한 경우 == 인덱스를 다 돈 경우
"""

# 타겟 넘버를 만드는 방법의 수
answer = 0


def find_target(idx, numbers, target, value):
    global answer
    """
    Args:
        idx: 숫자 배열의 인덱스이자 현재까지 사용한 숫자의 수
        numbers: 숫자 정보
        target: 목표 숫자
        value: 연산 결과

    Returns:
        타겟 넘버를 찾은 경우 True, 아닌 경우 False
    """

    # 숫자를 다 사용한 경우
    if idx == len(numbers):
        # 타겟 넘버를 만든 경우
        if value == target:
            answer += 1
            return
        # 타겟 넘버를 못만든 경우
        else:
            return

    find_target(idx+1, numbers, target, value+numbers[idx])
    find_target(idx+1, numbers, target, value-numbers[idx])


def solution(numbers, target):
    global answer
    find_target(0, numbers, target, 0)    # 사용한 숫자의 수, 숫자 정보, 타겟 넘버, 연산결과
    return answer


numbers = [4, 1, 2, 1]
# numbers = [1, 1, 1, 1, 1]
target = 4

print(solution(numbers, target))



