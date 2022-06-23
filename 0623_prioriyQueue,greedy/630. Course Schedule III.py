from itertools import permutations
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        1. lastDay 마감 빠른 순, duration 작은 순으로 정렬
        2. duration < lastDay 이면서
        3. time + duration <= lastDay 이면 maxHeap 에 추가하고 time 업데이트
            위의 조건이 아니라면
                maxHeap[0] > duration 이라면
                maxHeap[0] 을 pq에서 제거하고 새로운 duration을 넣고
                time 에서 maxHeap[0] 을 빼고 새 duration을 더한다.
        4. maxHeap 의 길이를 리턴한다.
        """

        courses.sort(key=lambda x: (x[1], x[0]))
        maxHeap = []
        time = 0

        for duration, lastDay in courses:
            if duration <= lastDay:
                if duration + time <= lastDay:
                    time += duration
                    heapq.heappush(maxHeap, -duration)
                else:
                    if -maxHeap[0] > duration:
                        max_duration = -maxHeap[0]
                        heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap, -duration)
                        time -= max_duration
                        time += duration

        return len(maxHeap)

        # cf. Brute Force(모든 순열 확인) => 시간초과
#         perms = list(permutations(courses, len(courses)))

#         max_result = 0
#         for courses in perms:
#             result, start = 0
#             for duration, lastday in courses:
#                 if start + duration <= lastday:
#                     start += duration
#                     result += 1
#             max_result = max(max_result, result)

#         return max_result



