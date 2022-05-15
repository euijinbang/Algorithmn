from collections import defaultdict
def solution(logs):
    answer = []
    st = set()
    d = defaultdict()
    for log in logs:
        id, problem, score = log.split()
        st.add(id)
        d[id] = {}

    for log in logs:
        id, problem, score = log.split()
        d[id][problem] = score

    new = {}
    for key, val in d.items():
        tmp_id = key
        tmp_problems = sorted([x for x in val.keys()])
        tmp_scores = sorted([x for x in val.values()])
        new[tmp_id] = [tmp_problems, tmp_scores]
        print(tmp_id, tmp_problems, tmp_scores)

    lst = list(st)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if new[lst[i]] == new[lst[j]] and len(new[lst[i]][0]) >= 5:
                answer.append(lst[i])
                answer.append(lst[j])
    print(answer)
    if len(answer) == 0: return ["None"]
    return sorted(list(set(answer)))