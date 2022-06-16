class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        #         val = 0

        #         for op in operations:
        #             if op == "--X" or op == "X--":
        #                 val -= 1
        #             if op == "++X" or op == "X++":
        #                 val += 1

        #         return val

        # hash 활용 => 속도개선
        op_dict = {"--X" : -1, "X--" : -1,
                   "++X" : 1, "X++" : 1}

        return sum(op_dict[op] for op in operations)
