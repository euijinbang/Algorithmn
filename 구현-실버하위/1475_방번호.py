num_set = dict()

for i in range(10):
    num_set[i] = 1

N = input()

ans = 1

def check_num_set(num_set):
    for key, value in num_set.items():
        if value < 0:
            return False

def add_num_set(old_num_set):
    for key, value in num_set.items():
        value += 1

for num in N:
    print(num_set)
    if num == '6' and num_set[6] <= 0 and num_set[9] >= 1:
        num_set[9] -= 1

    elif num == '9' and num_set[9] <= 0 and num_set[6] >= 1:
        num_set[6] -= 1

    else:
        num_set[int(num)] -= 1

    print(check_num_set(num_set))
    if check_num_set(num_set) == False:
        ans += 1
        add_num_set(num_set)


print(ans)

