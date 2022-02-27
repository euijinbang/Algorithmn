"""
대소문자 미구분
가장 많이 사용된 알파벳이 여러개 존재하는 경우 ? 출력
-error-
abccc 의 경우 ab에서 빠져나와버림 -> 코드수정
"""
dict_num = {}
text_list = list(input())

for t in text_list:
    dict_num[t.upper()] = 0

for t in text_list:
    dict_num[t.upper()] += 1


def max_alpha():
    global dict_num
    max_key = ''
    max_val = 0
    for key, val in dict_num.items():
        if val > max_val:
            max_val = val
            max_key = key

    cnt = 0
    for key in dict_num.keys():
        if dict_num[key] == max_val:
            cnt += 1

    if cnt > 1:
        print("?")
        return
    else:
        print(max_key)


max_alpha()