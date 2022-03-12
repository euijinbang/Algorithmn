"""
그리디, 구현-브론즈, 부르트포스
"""

def solution(money, costs):
    coins_input = [1, 5, 10, 50, 100, 500]
    costs_input = costs
    n = money

    coins = []
    for i in range(6):
        coins.append((coins_input[i], (costs_input[i] / coins_input[i])))

    coins.sort(key=lambda x: x[1])
    # print(coins)

    costs = []
    for i in range(6):
        costs.append((costs_input[i], (costs_input[i] / coins_input[i])))

    costs.sort(key=lambda x: x[1])
    # print(costs)

    n_coins = []
    for coin in coins:
        n_coins.append(coin[0])
    # print(n_coins)

    n_costs = []
    for cost in costs:
        n_costs.append(cost[0])
    # print(n_costs)

    board = {}
    for ncoin in n_coins:
        board[ncoin] = 0

    # print(board)
    for ncoin in n_coins:
        board[ncoin] += n // ncoin
        n = n % ncoin
        print(n)

    counts = []
    for count in board.values():
        counts.append(count)

    # print(counts)
    total = 0
    for i in range(6):
        total += counts[i] * n_costs[i]
    # print(total)
    return total

