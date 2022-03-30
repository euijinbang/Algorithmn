import itertools


def solution(relation):
    N = len(relation[0])
    key_idx = list(range(N))  # [0, 1, 2, 3]
    candidate_keys = []
    for i in range(1, N + 1):
        for comb in itertools.combinations(key_idx, i):  # i개씩 조합으로 돈다
            history = []
            for rel in relation:
                current_key = [rel[c] for c in comb]     # 튜플의 c 번째 인덱스 값을 현재키로 잡는다.
                if current_key in history:
                    break                                # 기록에 현재 키가 있다면 for 문을 종료하고 else 로 넘어가지 않는다.
                else:
                    history.append(current_key)
            else:
                for ck in candidate_keys:
                    if set(ck).issubset(set(comb)):   # 기존에 있던 후보키가 현재 후보키의 부분집합이라면 더하지 않는다.
                        break
                else:
                    candidate_keys.append(comb)       # 중복없이 기록되었고 후보키에도 같은 조합이 없다면 후보키에 등록한다.

    return len(candidate_keys)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],
            ["300","tube","computer","3"],["400","con","computer","4"],
            ["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))