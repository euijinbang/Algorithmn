class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        #key가 A,B,C이고 value가 [5,0,0]... 인 카운터 만들기
        d = {}
        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char] = [0]*len(vote)
                d[char][i] += 1


        #방법1. 알파벳 순으로 정렬 후 items 를 역순 정렬
        sorted_counter = sorted(d.items(), key=lambda k:k[0])
        s = sorted(sorted_counter, key=lambda k:k[1], reverse=True)
        result = ""
        for char, _ in s:
            result += char
        return result


        #방법2. 알파벳 순서로 정렬(동점 대비) 후 value 기준으로 역순 정렬
        voted_teams = sorted(d.keys())
        teams = sorted(voted_teams, key=lambda x:d[x], reverse=True)
        return "".join(teams)


# def rankTeams(self, votes: List[str]) -> str:
#     d = {}
#
#     for vote in votes:
#         for i, char in enumerate(vote):
#             if char not in d:
#                 d[char] = [0] * len(vote)
#             d[char][i] += 1
#
#     voted_names = sorted(d.keys())
#     return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))
#
#
#
# def rankTeams(votes: List[str]) -> str:
#     counter = {k:[0]*len(votes[0]) for k in votes[0]}
#
#     for val in votes:
#         for i,ch in enumerate(val):
#             counter[ch][i]-=1 # - as we need to sort in reverse
#     sorted_counter = sorted(counter.items(), key=lambda k:(k[1],k[0]))
#     ans = ""
#     for ch,_ in sorted_counter:
#         ans+=ch
#     return ans