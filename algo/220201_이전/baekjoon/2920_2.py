
# 초기 상태를 설정하고 두 원소씩 차례대로 비교하면서 오름/내림차순 여부를 체크한다.
numbers = list(map(int, input().split(' ')))

def song(numbers):

    # 초기 상태 설정
    asc = True
    des = True

    for i in range(1, 8):
        if numbers[i] < numbers[i-1]:
            asc = False
        else:
            des = False

    if asc == True and des == False:
        return "ascending"
    elif asc == False and des == True:
        return "descending"
    else:
        return "mixed"

print(song(numbers))