import collections

def getUsedTime(start, end):
    # start, end == 5자리 문자열
    # 이용시간(int)를 반환

    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))

    if em >= sm:
        h = eh - sh
        m = em - sm
    else:
        h = (eh - 1) - sh
        m = (em + 60) - sm

    return h * 60 + m

def solution(fees, records):
    answer = []

    # 번호별 이용시간 구하기
    IOCheck = collections.defaultdict(list) # {'번호': [('IN', '시각'), ('OUT', '시각'), ...]}
    usedTime = collections.defaultdict(int) # {'5961': 146, '0000': 34, '0148': 670})

    for record in records:
        time, carNum, IO = record.split(' ')
        IOCheck[carNum].append((IO, time))

    for carNum, times in IOCheck.items():
        isIO = [False, False]
        for idx, time in enumerate(times):

            ut = 0

            # 입차는 되었는데 출차가 안된 경우
            if idx == len(times) - 1 and time[0] == "IN":
                st = time[1]
                et = "23:59"
                ut = getUsedTime(st, et)
                usedTime[carNum] += ut
                continue

            if time[0] == 'IN':
                st = time[1]
                isIO[0] = True

            else:
                et = time[1]
                isIO[1] = True

            if sum(isIO) == 2:
                ut = getUsedTime(st, et)
                usedTime[carNum] += ut
                isIO = [False, False]

    # 요금 계산
    bTime, bFee, dTime, dFee = fees[0], fees[1], fees[2], fees[3]
    result = [] # [(carNum, fee), ...]

    for carNum, usedT in usedTime.items():
        fee = 0
        if usedT <= bTime:
            fee += bFee
            result.append((carNum, fee))
            continue

        else:
            calcTime = usedT - bTime
            fee += bFee
            if not calcTime % dTime:
                fee += dFee * (calcTime // dTime)
            else:
                fee += dFee * ((calcTime // dTime) + 1)

        result.append((carNum, fee))

    result.sort()
    for r in result:
        answer.append(r[1])

    return answer