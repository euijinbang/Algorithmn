import itertools

# N = 10
# a1, b1 = 4, 5
# a2, b2 = 6, 2
# a3, b3 = 10, 2
T = int(input())


def check(spots, min_distance, door, position, waiting, flag):
    global count
    # 종료조건
    if waiting == 0:
        count = 0
        return min_distance

    if 1 <= position <= N:
        if spots[position] == 0:
            spots[position] = 1
            min_distance += 1 + abs(door[0] - position)
            waiting -= 1

            if flag == False:
                count += 1

            if flag:
                check(spots, min_distance, door, door[0] - count, waiting, flag=False)

            else:
                check(spots, min_distance, door, door[0] + count, waiting, flag=True)

    return min_distance


def get_distance(spots, min_distance, door, position):  #(4, 5) 5
    distance = check(spots, min_distance, door, door[0], door[1], flag=True)
    min_distance += distance
    return min_distance


distances = []

for tc in range(T):
    N = int(input())
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    a3, b3 = map(int, input().split())
    doors = [(a1, b1), (a2, b2), (a3, b3)]
    count = 0

    #순열을 구한다.
    for x in itertools.permutations(doors, 3):
        # 각 순열마다 최소 이동거리를 구한다. (낚시터 리셋)
        spots = [0] * (N+1)
        spot_doors = list(x)
        # print(spot_doors)
        min_distance = 0
        result = 0
        for door in spot_doors:  #[(4, 5), (6, 2), (10, 2)]
            result += get_distance(spots, min_distance, door, door[0])

        distances.append(result)

    print("#{} {}".format(tc+1, min(distances)))
