"""
regex
tuple, set 활용
index 활용(sort쪽 문제지않을까싶긴 한데...tuple은 순서가 있으니까..set으로 바꿀때 다른 튜플로 인식)
"""

import re
from itertools import product

def solution(user_id, banned_id):
    # regex = '^' + ''.join([x if x != '*' else '.' for x in bi]) + '$'
    # r = re.compile(regex)

    # id 가 아닌 idx(인덱스) 넣어야...

    matched = (
        [idx for idx, x in enumerate(user_id) if re.match('^' + ''.join([x if x != '*' else '.' for x in bi]) + '$', x)]
        for bi in banned_id
    )

    selected = (set(x) for x in product(*matched))
    selected = set(tuple(x) for x in selected if len(x) == len(banned_id))
    return len(selected)



################################


import re
from itertools import product

def solution(user_id, banned_id):
    matched_id = (
        [i for i, id in enumerate(user_id) if re.match(f"^{p.replace('*', '.')}$", id)]
        for p in banned_id
    )
    # selected_id = [set(id) for id in product(*matched_id)]  # <- 시간초과
    selected_id = (set(id) for id in product(*matched_id))  # <- 통과
    selected_id = set(tuple(id) for id in selected_id if len(id) == len(banned_id))
    return len(selected_id)


