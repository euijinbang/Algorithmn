# 중첩 while 문

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1



# break

i = 100

while True:
    # i가 23의 배수면 반복문을 끝냄
    if i % 23 == 0:
        break
    i = i + 1

print(i)


# continue
i = 0

while i < 15:
    i = i + 1

    # i가 홀수면 print(i) 안 하고 바로 조건 부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)