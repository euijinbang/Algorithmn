soldiers = [x+1 for x in range(20)]
k = 5

# 죽는 인덱스
killIndex = 0

# 한 명의 군사가 남을 때 까지 반복
while len(soldiers) > 1:

    # kill 인덱스 증가
    killIndex += k-1

    # 만약 kill 인덱스가 배열 길이보다 크면 나머지로 처
    if killIndex >= len(soldiers):
        killIndex = killIndex % len(soldiers)

    # 군인 삭제
    print(f"{soldiers[killIndex]}번 군사가 죽습니다.")
    soldiers.pop(killIndex)


# 남은 군사의 위치 반환
print(soldiers[0])

