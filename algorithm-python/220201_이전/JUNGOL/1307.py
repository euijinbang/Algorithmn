n = 6

n = int(input())

# 알파벳 나열하기
def listAlphabet():
    return list(map(chr, range(65, 91)))

list_alpha = listAlphabet()

arr = [[0] * n for _ in range(n)]
s = 0
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if s == 26:   # 인덱스 26이면 27번째이므로 다시 A로 리셋
            s = 0
        arr[j][i] = list_alpha[s]
        s += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print('')
