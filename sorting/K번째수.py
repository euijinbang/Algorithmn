def solution(array, commands):
    ans = []
    for c in commands:
        i, j, k = c[0], c[1], c[2]
        temp = array[i-1:j]
        temp.sort()  # 원본을 변경시키는 정렬
        ans.append(temp[k-1])

    return ans


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
