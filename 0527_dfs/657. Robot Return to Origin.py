class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for d in moves:
            if d == "U": y = y-1
            if d == "R": x = x+1
            if d == "D": y = y+1
            if d == "L": x = x-1

        return x == y == 0