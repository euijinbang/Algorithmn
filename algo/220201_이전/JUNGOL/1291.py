s, e = map(int, input().split())

def googoodan(s, e):
    if s <= e:
        for j in range(1, 10):
            for i in range(s, e+1):
                print(f'{i} * {j} = {str(i * j).rjust(2, " ")}', end = '   ')
            print('')
    else:
        for j in range(1, 10):
            for i in range(s, e-1, -1):
                print(f'{i} * {j} = {str(i * j).rjust(2, " ")}', end = '   ')
            print('')

def input_check(s, e):
    if (2 <= s <= 9) and (2 <= e <= 9):
        googoodan(s, e)
    else:
        print("INPUT ERROR!")
        s, e = map(int, input().split())
        input_check(s, e)

input_check(s, e)

# 문자열 패딩 : width 는 원하는 길이, fillchar에는 원하는 문자열을 넣는다.
# ljust(width, fillchar) 우측으로 패딩
# rjust(width, fillchar) 좌측으로 패딩
# center(width, fillchar) 양측으로 패딩