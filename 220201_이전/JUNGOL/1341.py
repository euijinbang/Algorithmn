s, e = 4, 3

# s, e = map(int, input().split())

def googoodan(s, e):
    if s <= e:
        for i in range(s, e+1):
            cnt = 0
            for j in range(1, 10):
                print(f'{i} * {j} = {str(i * j).rjust(2, " ")}', end='   ')
                cnt += 1
                if cnt % 3 == 0:
                    print('')
            print('')

    else:
        for i in range(s, e - 1, -1):
            cnt = 0
            for j in range(1, 10):
                print(f'{i} * {j} = {str(i * j).rjust(2, " ")}', end='   ')
                cnt += 1
                if cnt % 3 == 0:
                    print('')
            print('')

googoodan(s, e)