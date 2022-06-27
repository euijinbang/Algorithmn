"""
4408. 자기방으로 돌아가기
<< 배열 counting >>

1. 복도 만들기 (num + 1)//2
2. 복도 길이(201)만큼 배열 생성
3. 학생의 이동경로 돌면서 카운드 + 1
4. 최대값 반환

"""
T = int(input())


def div(num):
    return (int(num)+1) // 2


for tc in range(1, T+1):
    N = int(input())
    students = [list(map(div, input().split())) for _ in range(N)]

    corr = [0] * 201

    for i in range(N):
        # 작은 복도에서 큰 복도로만 이동하도록 swap
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1]+1):
            corr[j] += 1

    print("#{} {}".format(tc, max(corr)))
