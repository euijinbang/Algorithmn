tc = int(input())

for t in range(tc):
    rep_char, text = input().split()
    rep = int(rep_char)

    new_list = []
    for t in text:
        for count in range(rep):    # 문자열 n번 반복하여 새 리스트에 넣는다.
            new_list.append(t)

    print(''.join(new_list))
