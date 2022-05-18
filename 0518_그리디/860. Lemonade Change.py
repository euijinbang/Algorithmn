"""
five 3장보다 ten 1장 + five 1장 거슬러주는게 더 좋다
"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5: five += 1
            elif bill == 10: five, ten = five - 1, ten + 1
            # 20 들어오는 경우 ten이 1개이상있으면 사용하는게 무조건 유리!
            elif ten > 0: five, ten = five - 1, ten - 1
            else: five -= 3

            # 계산 후 5달러 지폐가 0보다 적으면 false 반환
            if five < 0: return False

        return True

class Solution:
    def lemonadeChange(self, bills):
        five = ten = 0
        for num in bills:
            if num == 5:
                five += 1
            elif num == 10 and five:
                ten += 1
                five -= 1
            elif num == 20 and five and ten:
                five -= 1
                ten -= 1
            elif num == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True