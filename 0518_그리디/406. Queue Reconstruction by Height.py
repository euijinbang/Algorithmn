from heapq import heappop, heappush
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        max heap 구현하고 키 큰 순으로 빼서 해당 인덱스에 insert
        뒤로 갈수록 키가 더 작은 사람이 나오기 때문에 인데스가 적으면 앞에 넣어지게 된다.
        인덱스 == 내 앞에 있는 내 키 이상인 사람의 수 이기 때문에.
        점점 키가 작은 사람이 나오는데... 앞으로 끼어드는?구조
        """
        # pq로 구현시
        heap = []
        for person in people:
            heappush(heap, (-person[0], person[1]))

        result = []
        while heap:
            person = heappop(heap) #가장 키 큰 사람의 - 를 리턴
            result.insert(person[1], [-person[0], person[1]])

        return result



########################
        # sort로 구현시
        result = []
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for person in people:
            result.insert(person[1], person)
        return result