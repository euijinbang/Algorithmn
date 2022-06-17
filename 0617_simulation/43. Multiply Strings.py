# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         n1 = n2 = 0
#         len1, len2 = len(num1), len(num2)

#         for i in range(len1):
#             n1 += (ord(num1[i]) - 48) * (10**(len1-i-1))

#         for j in range(len2):
#             n2 += (ord(num2[j]) - 48) * (10**(len2-j-1))

#         return str(n1*n2)



class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {'1':1 , '2':2 , '3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9 , '0':0}

        d = e = 0
        num1, num2 = list(num1), list(num2)

        while len(num1) > 0:
            d = d * 10 + dic[num1[0]]
            num1.pop(0)

        while len(num2) > 0:
            e = e * 10 + dic[num2[0]]
            num2.pop(0)

        return str(d*e)