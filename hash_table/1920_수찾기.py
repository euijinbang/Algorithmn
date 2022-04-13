# import hashlib
# print(hashlib.sha256('3'.encode()).hexdigest()) => 못외울거같아서 패스

# 기타방법 - 카운터 함수 (딕셔너리) print(Counter(nums))
# 기타방법 - set 자료구조 print(set(nums))


# print('3'.encode())  # 문자열을 해싱가능하게 바이트로 인코딩.
# print(hash('3'.encode()))  # 바이트를 해싱.

N = 5
data = ['4', '1', '5', '2', '3']
check_data = ['1', '3', '7', '9', '5']

# N = int(input())
# a = input().split()
# M = int(input())
# b = input().split()

# 해시테이블을 딕셔너리로 만든다.
hash_table = dict()

# 딕셔너리의 key를 해싱한 키로, value를 해당 데이터로 담는다.
for i in data:
    encoded_i = i.encode()
    key = str(hash(encoded_i))
    hash_table[key] = i


for i in check_data:
    encoded_i = i.encode()
    key = str(hash(encoded_i))
    try:
        if hash_table[key]:
            print(1)
    except:  # key-error
        print(0)

print(hash_table)
