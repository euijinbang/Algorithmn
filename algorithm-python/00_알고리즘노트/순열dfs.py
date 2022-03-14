def permutation(arr, r):
    # 사용된 원소를 저장할 배열을 만든다.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used, num):
        num += 1
        print("{}번째로 함수를 실행합니다".format(num))

        # 선택리스트에 순열의 원소를 저장하다가 갯수가 r개가 되면 출력 후 함수를 종료한다.
        if len(chosen) == r:
            print("3개가 다 차서 결과를 알려드립니다.순열결과{}".format(chosen))
            print("이제 리턴합니다-----")
            return

        # 반복문을 돌면서
        for i in range(len(arr)):
            print("반복문을 실행합니다.")
            # 아직 사용하지 않았다면
            if not used[i]:
                # 선택리스트에 저장하고 방문체크한다.
                chosen.append(arr[i])
                used[i] = 1
                print("재귀함수호출전{}".format(used))

                # 다시 generate 함수를 반복한다.
                generate(chosen, used, num)

                print("리턴했습니다--------")
                # 하나의 순열이 만들어지면 다시 uncheck한다.
                used[i] = 0
                print("체크를 해제했어요{} 지금은 {}번째 함수입니다.".format(used, num))
                chosen.pop()

    generate([], used, 0)



permutation([1, 2, 3, 4], 3)
