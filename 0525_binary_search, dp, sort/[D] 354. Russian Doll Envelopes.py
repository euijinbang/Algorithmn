"""
1996번 _ 300번 합친 유형
w는 asc, h 는 desc 정렬 후 h만 가지고
가장 긴 부분증가 수열의 len을 구한다.
"""

class Solution(object):
    def maxEnvelopes(self, envs):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # sort first by increasing width
        # within each subarray of same-width envelopes
        # sort by decreasing height
        envs.sort(key=lambda (w,h): (w,-h))

        # now find the length of the longest increasing subsequence of heights.
        # Since each same-width block was sorted non-increasing,
        # we can only pick at most one height within each block
        # otherwise, the sequence would be non-increasing
        tails=[]
        for (w,h) in envs:
            idx=bisect.bisect_left(tails, h) # h가 tails에 들어갈 때 순서 유지하는 위치의 index
            if idx==len(tails): # h가 tail 의 모든 원소들 보다 큰 원소라면 맨뒤에 더한다.
                tails.append(h)
            elif idx==0 or tails[idx-1]<h: # h가 들어갈 index 앞 수보다 크다면 index위치 값을 h로 바꾼다.
                tails[idx]=h
        return len(tails)