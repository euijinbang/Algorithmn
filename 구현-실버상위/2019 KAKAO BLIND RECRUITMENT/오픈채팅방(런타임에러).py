def solution(record):
    room = []
    left = []

    for r in record:
        if len(r.split()) == 3:
            state, uid, nick = r.split()
        else:
            state, uid = r.split()
            nick = ''

        if state == "Enter":
            flag = False
            for l in left:
                if l[0] == uid:
                    flag = True

            # id 가 left 에 없다면(처음 들어온 사람이라면)
            if not flag:
                room.append([uid, nick, "님이 들어왔습니다."])
            # id 가 left 에 있다면(중간에 나간 사람이라면)
            elif flag and len(left):
                # 닉네임이 같으면 left에서 빼서 같은 닉네임으로 넣음
                for idx in range(len(left)):
                    if left[idx][0] == uid:
                        if left[idx][1] == nick:
                            room.append([left[idx][0], nick, "님이 들어왔습니다."])
                            left.pop(idx)
                            # 아이디는 같은데 닉네임이 다르면 left에서 빼서 닉네임 수정해서 넣고 기존 정보도 수정함
                        else:
                            room.append([left[idx][0], nick, "님이 들어왔습니다."])
                            left.pop(idx)
                            for r in room:
                                if r[0] == uid:
                                    r[1] = nick

        elif state == "Leave":
            for r in room:
                if r[0] == uid:
                    nick = r[1]
            room.append([uid, nick, "님이 나갔습니다."])
            left.append([uid, nick, "님이 들어왔습니다."])

        else: # Change
            for r in room:
                if r[0] == uid:
                    r[1] = nick

    result = list(map(lambda x: x[1] + x[2], room))
    return result

# record = ["Enter uid1234 Muzi", "Change uid1234 Muzi", "Leave uid1234", "Enter uid1234 Prodo"]
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))