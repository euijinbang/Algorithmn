input_data = 'a1'

row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# (1, 1)

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

print(result)
