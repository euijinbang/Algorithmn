class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # The ord() function returns an integer
        # representing the Unicode character.

        """
        문자열 돌면서 ord로 변경, 각 자릿수를 더하고 10으로 나눈
        몫, 나머지 => 몫은 다음 자릿수에 추가, 나머지는 답에 추가
        while 문으로 반복 ex. 123 + 9 면 3번 반복
        """
        # str은 pop할 수 없으므로 list
        num1, num2 = list(num1), list(num2)
        result = []
        carry = 0

        while len(num1) > 0 or len(num2) > 0:
            n1, n2 = 0, 0
            if num1:
                n1 = ord(num1.pop()) - ord('0')
            if num2:
                n2 = ord(num2.pop()) - ord('0')
            carry, remainder = divmod(n1+n2+carry, 10)
            result.append(remainder)

        if carry:
            result.append(carry)

        return "".join(str(x) for x in result)[::-1]  # 문자열 join 후 거꾸로 반환