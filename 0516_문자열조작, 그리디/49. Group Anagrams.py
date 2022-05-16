"""
sorted 를 문자열에 쓰면 정렬된 리스트로 반환
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            d[sorted_word].append(word)
        return d.values()