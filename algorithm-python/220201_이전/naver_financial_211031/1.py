id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
k = 3
# 딕셔너리 초기화
my_dict = {}
for day in id_list:
    ids = sorted(day.split())
    for id in ids:
        my_dict[id] = 0


for day in id_list:
    ids = sorted(set(day.split()))
    for id in ids:
        if my_dict[id] >= k:
            continue
        my_dict[id] += 1

print(sum(my_dict.values()))
##########

def solution(id_list, k):
    my_dict = {}
    for day in id_list:
        ids = sorted(day.split())
        for id in ids:
            my_dict[id] = 0

    for day in id_list:
        ids = sorted(set(day.split()))
        for id in ids:
            if my_dict[id] >= k:
                continue
            my_dict[id] += 1

    answer = sum(my_dict.values())
    return answer