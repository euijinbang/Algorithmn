def solution(operations):
    q = []
    answer = [0, 0]
    for oper in operations:
        order, data = oper.split(' ')[0], oper.split(' ')[1]

        if order == 'I':
            num = int(data)
            q.append(num)

        else:
            if data == '1':
                while q:
                    max_idx = q.index(max(q))
                    q.pop(max_idx)
                    break

            else:
                while q:
                    min_idx = q.index(min(q))
                    q.pop(min_idx)
                    break

    if q:
        answer = [max(q), min(q)]
    return answer


# operations = ["I 16","D 1"]
operations = ["I 7","I 5","I -5","D -1"]
print(solution(operations))