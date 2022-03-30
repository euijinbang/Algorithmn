# 0은 홈, 1은 돌기
# 홈이 맞는다 = key와 lock 각 좌표의 합이 모두 1이다.

def rotate_90_degree(arr):
    n = len(arr)
    m = len(arr[0])
    r_arr = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            r_arr[j][n-1-i] = arr[i][j]
    return r_arr


# 새 자물쇠 중간 부분이 모두 1이면 True를 리턴
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠 크기를 기존의 3배로 변환
    new_lock = [[0]*(n*3) for _ in range(n*3)]

    # 새 자물쇠에 중앙에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 90도, 180도, 270도, 360도 회전시마다 모든 좌표 확인
    for _ in range(4):
        key = rotate_90_degree(key)

        # 인덱스 0 부터 n*2-1 까지 확인
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠를 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 자물쇠와 열쇠가 맞는지 확인
                if check(new_lock) == True:
                    return True
                # 안맞으면 자물쇠에서 열쇠를 다시 뺀다.
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    # 네 방향으로 모두 검사했는데 불일치시 채울 수 없다.
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))

