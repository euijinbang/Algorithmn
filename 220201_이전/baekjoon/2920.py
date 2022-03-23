numbers = list(map(int, input().split()))
asc = [x+1 for x in range(8)]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def song(numbers):
    if numbers == asc:
        return 'ascending'
    elif numbers == asc[::-1]:
        return 'descending'
    else:
        return 'mixed'

print(song(numbers))


