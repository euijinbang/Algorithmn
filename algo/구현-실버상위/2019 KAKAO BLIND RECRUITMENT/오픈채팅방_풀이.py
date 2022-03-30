def solution(record):
    result = [] # id, 들어오고 나간 정보만 담는다.
    info = {}   # id와 최종 닉네임을 담는다.
    for r in record:
        r = r.split()
        #들어온 경우
        if r[0] == "Enter":
            result.append([r[1], "님이 들어왔습니다."])
            info[r[1]] = r[2]
        #나간경우
        elif r[0] == "Leave":
            result.append([r[1], "님이 나갔습니다."])
        #변경된 경우
        else:
            info[r[1]] = r[2]
    print(info)
    print(result)
    result = list(map(lambda x: info[x[0]] + x[1], result))
    return result


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))