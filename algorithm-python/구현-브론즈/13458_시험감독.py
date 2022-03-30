"""
총감독관이 없어도 되는 것으로 문제를 잘못 이해함.
총감독관은 최소 1명 있어야함

각 시험장별로 감독 수를 구하면 된다.
남은 인원이 있다면 => 거르지 못하면 오답이다.
"""
# N = 5
# students = [10, 9, 10, 9, 10]
# A, B = 7, 20

N = int(input())
students = list(map(int, input().split()))
A, B = map(int, input().split())


count = 0
for i in range(N):
    # 각 시험장에 총감독을 배치한다.
    students[i] -= A
    count += 1

    # 남은 인원이 있다면, 인원수를 부감독으로 나눠서 나머지가 없으면 감독관을 1명, 있으면 1명 더 배치한다.
    if students[i] > 0:  # 이걸 거르지 못하면 오답.. - 가 나올 수도 있기 떄문이다.
        value, left = divmod(students[i], B)
        if left == 0:
            count += value
        else:
            count += value + 1

print(count)
