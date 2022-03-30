def solution(num_teams, remote_tasks, office_tasks, employees):

    # 팀별 재택/출근사원 목록
    remote_workers = dict()
    office_workers = dict()
    for i in range(num_teams):
        remote_workers[i+1] = []
        office_workers[i+1] = []

    for idx, employee in enumerate(employees):
        employee_num = idx + 1
        team_num = int(employee[:1])
        works = employee[2:].split()

        # 재택만 가능한 경우 확인
        flag = True
        for work in works:
            if work not in remote_tasks:
                flag = False

        # 재택만 가능한 경우, 그 외의 경우를 분리
        if flag:
            remote_workers[team_num].append(employee_num)
        else:
            office_workers[team_num].append(employee_num)

    # 재택하는 사람들만 결과에 담는다.
    result = []
    for val in remote_workers.values():
        result.extend(val)

    # 팀중에 출근가능한 팀원이 없다면 재택가능한 팀원중 가장 번호가 빠른 사람을 뽑는다.
    for key, val in office_workers.items():
        if not val:
            sorted_rw = sorted(remote_workers[key])
            office_workers[key].append(sorted_rw[0])
            result.remove(sorted_rw[0])

    return result


num_teams = 3
remote_tasks = ["development","marketing","hometask"]
office_tasks = ["recruitment","education","officetask"]
employees = ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]

print(solution(num_teams, remote_tasks, office_tasks, employees))
