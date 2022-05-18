"""
five 3장보다 ten 1장 + five 1장 거슬러주는게 더 좋다
"""
def lemonadeChange(self, bills):
    five = ten = 0
    for i in bills:
        if i == 5: five += 1
        elif i == 10: five, ten = five - 1, ten + 1
        elif ten > 0: five, ten = five - 1, ten - 1
        else: five -= 3
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