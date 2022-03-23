

def check_target(count, current):




def solution(numbers, target):
    global nums_count, info, calc, visited, answer

    answer = 0                 # 타겟 넘버를 만드는 방법의 수
    info = dict()              # key : 시작 숫자 value : 도착 숫자
    nums_count = len(numbers)  # 사용 가능한 숫자의 갯수

    info[0] = [numbers[0], -numbers[0]]

    for idx, number in enumerate(numbers):
        if idx + 1 < nums_count:
            info[number] = [numbers[idx+1], -numbers[idx+1]]
            info[-number] = [numbers[idx+1], -numbers[idx+1]]

    check_target(0, 0)   # 사용한 숫자의 수, 시작 수

    return answer


numbers = [4, 1, 2, 1]
target = 4

solution(numbers, target)



