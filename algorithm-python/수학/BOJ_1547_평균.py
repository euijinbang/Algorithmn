"""
수학
"""

N = 3
scores = [40, 80, 60]
N = int(input())
scores = list(map(int, input().split()))


def newAvgScore():
    M = max(scores)

    new_score = []
    for score in scores:
        new_score.append(score / M * 100)

    avg = sum(new_score) / N

    return avg


print(newAvgScore())