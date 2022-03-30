# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자',
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기',
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name in vote_counter.keys():  # 이름이 사전에 있으면 1을 더한다.
        vote_counter[name] += 1
    else:
        vote_counter[name] = 1  # 이름이 사전에 없으면 1로 생성한다.

# 후보별 득표수 출력
print(vote_counter)




def mask_security_number(security_number):
    result = security_number[:len(security_number)-4] + '****'
    return result

def mask_security_number(security_number):
    num_list = list(security_number)

    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = '*'

    num_list = ''.join(num_list)
    return num_list

# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))


