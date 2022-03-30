from string import ascii_letters
alphas= list(ascii_letters)


def check(content):
    global flag
    for char in content:
        if char not in alphas:
            flag = False
        if char == ' ':
            flag = False


def solution(logs):
    good_count = 0
    global flag
    for log in logs:
        slogs = log.split(' ')
        flag = True
        if len(log) > 100:
            flag = False
        if len(slogs) == 12:
            for i in range(len(slogs)):
                if slogs[0] == 'team_name':
                    check(slogs[2])
                if slogs[3] == 'application_name':
                    check(slogs[5])
                if slogs[6] == 'error_level':
                    check(slogs[8])
                if slogs[9] == 'message':
                    check(slogs[11])
                else:
                    flag = False
        else:
            flag = False

        if flag:
            good_count += 1

    answer = len(logs) - good_count
    return answer

# logs = ["team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever"]
# logs = ["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]
# logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
# print(solution(logs))

