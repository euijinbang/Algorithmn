def solution(abilities, k):
    my_team = []
    your_team = []

    # even
    if len(abilities) % 2 == 0:
        abilities.sort(reverse=True)
        tmp = abilities.copy()
        max_count = 1
        max_ability = tmp[0]
        while abilities and tmp:
            for tmp_abil in tmp:
                if tmp_abil == max_ability:
                    tmp.pop(0)
                    max_count += 1
            if max_count >= 2:
                while max_count >= 2:
                    your_team.append(abilities.pop(0))
                    my_team.append(abilities.pop(0))
                    max_count = 0
            else:
                if k >=1:
                    k -= 1
                    my_team.append(abilities.pop(0))
                    your_team.append(abilities.pop(0))
                else:
                    your_team.append(abilities.pop(0))
                    my_team.append(abilities.pop(0))

        answer = sum(my_team)

    # odd
    else:
        result = 99999
        ability = 0

        # 데려갈 경우와 안데려갈 경우를 나눔


    return answer



abilities = [2, 8, 3, 6, 1, 9, 1, 9]
k = 2
abilities = [7, 6, 8, 9, 10]
k = 1



