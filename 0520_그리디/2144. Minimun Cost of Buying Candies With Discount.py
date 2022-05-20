def minimunCost(self, cost: List[int]) -> int:
    cost.sort(reverse=True)
    for i in range(len(cost)//3):
        cost[i*3+2] = 0
    return sum(cost)