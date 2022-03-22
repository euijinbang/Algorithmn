airports = {'ICN': ['ATL', 'TTO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

current = 'TTO'


# 현재 공항에서 출발하는 경로가 없는 경우
for airport in airports:    # key를 돌면서 확인
    print(airport)

if current not in airports:
    print("no")
else:
    print("yes")
