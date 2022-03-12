import string

"""
소문자 알파벳을 구하기 위해 String 모듈 사용
출력이 가장 마지막일 경우 공백제거
한번 찾고나면 break문으로 for문을 나가야 중복출력이 되지 않는다.
"""
# S = "baekjoon"
S = input()

alphas = string.ascii_lowercase
last = len(alphas) - 1

for idx_alpha, alpha in enumerate(alphas):
    flag = False
    for idx, char in enumerate(S):
        if char == alpha:
            if idx_alpha == last:
                print(idx, end="")
            else:
                print(idx, end=" ")
            flag = True
            break

    if flag == False:
        if idx_alpha == last:
            print(-1, end="")
        else:
            print(-1, end=" ")
