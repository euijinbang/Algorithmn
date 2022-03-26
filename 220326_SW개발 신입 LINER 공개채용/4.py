def solution(arr, brr):
    def longer(i):
        global answer
        diff = brr[i] - arr[i]
        arr[i] += diff
        arr[i+1] -= diff
        answer += 1

    def shorter(i):
        global answer
        diff = arr[i] - brr[i]
        arr[i] -= diff
        arr[i+1] += diff
        answer += 1

    global answer
    answer = 0
    for i in range(len(arr)-1):
        if arr[i] > brr[i]:
            longer(i)
        if arr[i] < brr[i]:
            shorter(i)

    return answer

arr = [3, 7, 2, 4]
brr = [4, 5, 5, 2]
