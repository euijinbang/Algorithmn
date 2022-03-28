nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
extra = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
to_roman = [
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],   # 0, 1, ..., 9
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],   # 0, 10, 20, ..., 90
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],   # 0, 100, 200, ..., 900
    ['', 'M', 'MM', 'MMM'],                                         # 0, 1000, 2000
]


def roman_to_num1(roman):
    check = [0] * len(roman)
    total = 0
    for i in range(len(roman)):
        if not check[i]:
            if i+1 < len(roman) and roman[i:i+2] in extra:
                tmp = roman[i:i+2]
                total += extra[tmp]
                check[i:i+1] = 1, 1
            else:
                total += nums[roman[i]]
                check[i] = 1
    return total


def roman_to_num2(roman):
    num = 0
    # 예외 상황을 먼저 필터링
    for r, n in extra.items():
        if r in roman:
            num += n
            roman = roman.replace(r, "")

    # 해당 문자가 몇 개 들어있는지 세서 value * 갯수를 더한다.
    for r, n in nums.items():
        num += (n * roman.count(r))

    return num


def nums_to_roman(num):
    roman = ""
    i = 0

    # 10으로 나눈 몫과 나머지를 구해 리스트에서 찾아 문자열에 추가한다.
    while num:
        num, rest = divmod(num, 10)
        roman = to_roman[i][rest] + roman
        i += 1

    return roman


# A = 'DLIII'
# B = 'MCMXL'
A = input()
B = input()
total = roman_to_num2(A) + roman_to_num2(B)

print(total)
print(nums_to_roman(total))

