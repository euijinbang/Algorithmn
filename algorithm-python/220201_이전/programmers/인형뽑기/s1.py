def solution(board, moves):
    stack = []
    cnt = 0
    for move in moves:
        for row in board:
            if row[move - 1] != 0:
                if stack:
                    if stack[-1] == row[move - 1]:
                        stack.pop()
                        cnt += 2
                        break
                    else:
                        stack.append(row[move - 1])
                        row[move - 1] = 0
                        break
                else:
                    stack.append(row[move - 1])
                    row[move - 1] = 0
                    break
    return cnt

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))