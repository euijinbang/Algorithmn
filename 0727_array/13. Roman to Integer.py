class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = 0

        for i in range(0, len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:   # 예외사항의 경우
                result -= roman[s[i]]
            else:
                result += roman[s[i]]

        return result + roman[s[-1]]    # 마지막 수는 항상 더한다.

#         main = {"I": 1,
#                 "V": 5,
#                 "X": 10,
#                 "L": 50,
#                 "C": 100,
#                 "D": 500,
#                 "M": 1000}

#         sub = {"IV": 4,
#               "IX": 9,
#               "XL": 40,
#               "XC": 90,
#               "CD": 400,
#               "CM": 900}

#         result, i = 0, 0
#         while True:
#             if i == len(s):
#                 break

#             if len(s) == 1 or i == len(s)-1:
#                 result += main[s[i]]
#                 break

#             if s[i] + s[i+1] in sub:
#                 result += sub[s[i]+s[i+1]]
#                 i += 2
#                 continue

#             if s[i] in main:
#                 result += main[s[i]]
#                 i += 1

#         return result


