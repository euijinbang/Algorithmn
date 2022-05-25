class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # grouping by attack
        props = sorted(properties, key=lambda x:x[0])
        groups = collections.defaultdict(list)
        for a, d in props:
            groups[a] += [d]

        ans, max_d = 0, -1
        for key in sorted(groups.keys())[::-1]:
            for d in groups[key]:
                if d < max_d:
                    ans += 1
            for d in groups[key]:
                max_d = max(max_d, d)

        return ans


        # stack - 시간초과
        props = sorted(properties, key=lambda x:(x[0], -x[1]))
        ans, stack = 0, []
        for a, d in props:
            while stack and stack[-1] < d:
                ans += 1
                stack.pop()
            stack.append(d)

        return ans
