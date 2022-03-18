"""
배열을 만들어서 방문을 체크
나온적이 없으면 방문체크
나온적이 있으면
문자가 바로 전 문자열과 같으면 그룹 단어이므로 계속 진행
문자가 바로 전 문자열과 다르면 그룹 단어가 아니므로 스탑

chr(97) = a
chr(98) = b
...
chr(122) = z
------------
ord('a') = 97
ord('b') = 98
....
ord('z') = 122
"""

N = int(input())

count = 0
for i in range(N):
    text = input()
    # 체킹용 리스트
    check = [False] * 26
    flag = True

    for idx in range(len(text)):
        if not check[97 - ord(text[idx])]:  # 방문 안했다면 방문체크
            check[97 - ord(text[idx])] = True

        else:   # 방문했다면 전 문자열과 비교 (index - 1로 확인)
            if text[idx-1] == text[idx]:  # 같으면 패스
                pass
            else:   # 다르면
                flag = False
                break

    if flag:
        count += 1

print(count)
