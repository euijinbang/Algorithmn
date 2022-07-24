from itertools import combinations

def is_duplicate(columns, relation):
    """
    columns 가 (1, 2)라면
    1번과 2번을 합친 값을 구하고 중복확인
    """
    # 튜플 자료형 columns
    new_set = set()

    # 모든 tuple 돌면서 해당 column 의 문자열을 더해 set 에 있는지 확인
    for tupl in relation:
        candidate_str = ''
        for column in columns:
            candidate_str += tupl[column]

        if candidate_str in new_set:
            return True
        else:
            new_set.add(candidate_str)

    return False



def solution(relation):
    # 후보키의 수
    answer = 0

    attr_num = len(relation[0])
    tuple_num = len(relation)

    # 후보키면 해당 튜플을 False로 변경
    is_candidate = [True] * attr_num

    # 후보키
    keys = list()

    # k 개(1~튜플 갯수)의 튜플 뽑기
    for k in range(1, attr_num + 1):
        maybe_candidate_keys = list(combinations([x for x in range(attr_num)], k))
        print(maybe_candidate_keys)
        for maybe_candidate_key in maybe_candidate_keys:
            flag = True
            if not is_duplicate(maybe_candidate_key, relation): # 유일성 인정
                maybe_candidate_key = set(maybe_candidate_key)

                if len(keys):
                    for key in keys: # 0   # subset 이면 pass (최소성 미인정)
                        if key.issubset(maybe_candidate_key):
                            flag = False
                            break

                if flag:
                    keys.append(maybe_candidate_key)
                    answer += 1 # 후보키 갯수 + 1

    return answer