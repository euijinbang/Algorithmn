class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:     # LOOP... false
                return False
            if preMap[crs] == []:   # no prerequisite... true (backtrack)
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):    # if one is false -> return false
                    return False

            # no false at all ..!
            visitSet.remove(crs)    # no longer visit(already visited)
            preMap[crs] = []        # can be completed!

            # crs can be completed!
            return True

        # call it for every single number....
        # any of them false => false
        for crs in range(numCourses):    # key in dict
            if not dfs(crs):
                return False
        # when all courses can be completed
        return True
