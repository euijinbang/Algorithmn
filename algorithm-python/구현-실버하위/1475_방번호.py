N = input()

# 숫자 세트 딕셔너리 생성
num_set = dict()
for i in range(10):
    num_set[i] = 1

ans = 1


# 딕셔너리 전체에 1씩 더한다
def add_num_set():
    global num_set
    for key, value in num_set.items():
        num_set[key] += 1


for num in N:
    cur_num = int(num)
    if num_set[cur_num] <= 0:  # 현재 숫자의 남은 판수가 0 이하라면 대체 가능한지 확인
        if num == '6' and num_set[9] >= 1:
            num_set[9] -= 1
        elif num == '9' and num_set[6] >= 1:
            num_set[6] -= 1

        else:   # 대체 불가할 경우 세트를 추가
            ans += 1
            add_num_set()
            num_set[cur_num] -= 1
    else:
        num_set[cur_num] -= 1

print(ans)

