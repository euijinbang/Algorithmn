class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if expression.isdigit():
            return [int(expression)]

        for index, value in enumerate(expression):
            if value in "+-*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])
                print(left, right)
                results.extend(compute(left, right, value))
        return results