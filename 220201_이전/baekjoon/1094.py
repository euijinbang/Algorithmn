arr = [64]
x = int(input())

while sum(arr) != x:
    if sum(arr) > x:
        target = arr.pop()
        arr.append(target//2)
        arr.append(target//2)
        if sum(arr[:len(arr)-1]) >= x:
            arr.pop()
        else:
            pass

    else:
        result = 1

result = len(arr)
print(result)