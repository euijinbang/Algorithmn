import sys
sys.stdin = open("2514.txt")

arr = list(input())
cnt1, cnt2 = 0, 0
for i in range(len(arr)-3+1):
    if ''.join(arr[i:i+3]) == "KOI":
        cnt1 += 1
    elif ''.join(arr[i:i+3]) == "IOI":
        cnt2 += 1

print(cnt1)
print(cnt2)

# 리스트의 문자열을 합치는 join 함수
# a = ['a', 'b']
# b = ''.join(a)
# print(b) #=> 'ab'