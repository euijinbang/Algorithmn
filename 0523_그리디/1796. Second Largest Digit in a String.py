class Solution:
    def secondHighest(self, s: str) -> int:
        # set, sort 활용
        digits = set()
        for d in s:
            if d.isdigit(): digits.add(d)
        r = sorted(list(digits), reverse=True)
        return r[1] if len(r) > 1 else -1