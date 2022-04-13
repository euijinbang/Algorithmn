phone_book = ["119", "97674223", "1195524421"]


def solution(phone_book):
    number_dict = {}

    # 해시테이블 저장 first_digit : phone number list
    for phone_num in phone_book:
        try:
            number_dict[phone_num[0]].append(phone_num)
        except: # key error 발생시 리스트 밸류 생성
            number_dict[phone_num[0]] = [phone_num]

    for num_value in number_dict.values():
        num_value.sort()
        for i in range(1, len(num_value)):  # ['119', '1195524421']
            if num_value[i].startswith(num_value[i-1]):  # String 검사
                return False

    return True


print(solution(phone_book))
