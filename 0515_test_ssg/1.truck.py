"""
시간초과? 또는 프로그래머스 에러..
"""
from heapq import heapify
def solution(v, a, b):
    answer = 0
    v = [-x for x in v]
    while True:
        heapify(v)
        if -v[0] < a:
            return answer
        v[0] += a
        for i in range(1, len(v)):
            if -v[i] < b:
                return answer
            v[i] += b
        answer += 1
    return answer