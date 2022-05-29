class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:

        # 1. senders 돌면서 counter 만들기  index: {name : messages[index]의 갯수}
        counter = collections.defaultdict(int)
        for index, name in enumerate(senders):
            counter[name] += len(messages[index].split())

        # 2. sorting
        # ** 소팅 방법 1) dict.items()의 key와 val을 기준으로 정렬한다.
        # count갯수(value) 내림차순 정렬 후 이름(key) 내림차순 정렬 ... 각각 - 가 아니라 한번에 reverse 처리
        sorted_counter = sorted(counter.items(), key=lambda item: (item[1], item[0]), reverse=True)
        return sorted_counter[0][0]

        # ** 소팅 방법 2) 최댓값 구하기 -> 순위리스트 구하기 -> 길이 1이면 리턴, 아니면 그 리스트를 정렬
        max_val = max(counter.values())
        ranks = []
        for name, val in counter.items():
            if val == max_val:
                ranks.append(name)

        if len(ranks) == 1: return ranks[-1]
        else:
            ranks.sort()
            return ranks[-1]

        # ** 소팅 방법 3) 갱신하기 : 임시변수 생성 -> 반복문 돌면서 갱신, max와 동일하다면 이름으로 임시정렬 만들기
        max_val = float('-inf')
        max_name = ''

        for name, val in counter.items():
            if val > max_val:
                max_val = val
                max_name = name
            if val == max_val:
                temp = sorted([max_name, name], key=str, reverse=True)  # Bob, Charlie -> Charlie, Bob
                max_name = temp[0]

        return max_name