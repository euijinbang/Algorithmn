class Solution:
    def firstUniqChar(self, s: str) -> int:
        #방법1. 해시맵 이용하여 출연횟수가 1이면 리턴
        if not s : return -1

        d = collections.defaultdict(int) #key가 없으면 0을 넣어준다.
        for char in s:
            d[char] += 1

        for i, val in enumerate(s):
            if d[val] < 2:
                return i
        return -1


        #방법2. set, dict 같이 사용하여 set에 인덱스를 값으로 저장, 최소 인덱스를 리턴
        d = dict()
        seen = set()

        for idx, char in enumerate(s):
            if char not in seen:
                d[char] = idx
                seen.add(char)
            else:
                if char in d:
                    del d[char]

        return min(d.values()) if d else -1
    