class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 알파벳 문자 외에 모두 공백으로 치환, 이후 공백기준 split, banned 포함단어 제외
        only_words = [x for x in re.sub('[^\w]', ' ', paragraph).lower().split()
                      if x not in banned]


        # sol1. defautdict 사용
        counts = collections.defaultdict(int)
        for word in only_words:
            counts[word] += 1

        # 딕셔너리에서 값이 가장 큰 키를 가져온다.
        return max(counts, key=counts.get)


        # sol2. Counter 사용, most_common 메서드 사용
        counts = collections.Counter(only_words)
        return counts.most_common(1)[0][0]