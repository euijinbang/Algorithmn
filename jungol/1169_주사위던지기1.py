N, M = 3, 1
path = []


def run(lev):
    if lev == 6:
        print(path)
        return

    for i in range(4):
        path[lev] = i
        run(lev+1)


run(0)
