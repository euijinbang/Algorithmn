class Solution:
    def digitCount(self, num: str) -> bool:
        counter = collections.Counter(map(int, num))

        for i in range(len(num)):
            if int(num[i]) != counter.get(i, 0):
                return False
        return True

######################################################


class Solution:
    def digitCount(self, num: str) -> bool:
        # 1. counter로 숫자 등장횟수를 만든다. map으로 key의 자료형을 변경할 수 있다.
        # {0:2, 3:1} str:int  => int:int
        counter = collections.Counter(map(int, num))

        # 2.
        # i-key, val-val
        # dict.get(key, 0)의 경우 keyerror 대신 0을 반환
        for i in range(len(num)):
            if int(num[i]) != counter.get(i, 0): #get(key)
                return False
        return True

        # 방법 2. all(iterable) 의 경우 반복문 모든 요소 True->True
        # return all(counter[i] == int(v) for i, v in enumerate(num))