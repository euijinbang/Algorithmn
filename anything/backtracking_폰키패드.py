keypad = {
    '2': ['a', 'b', 'c'],
    '5': ['j', 'k', 'l'],
    '9': ['w', 'x', 'y', 'z']
}

nums = '259'
result = []


def bt(index, letter):
    if index == len(nums):
        result.append(letter)
        return

    num = nums[index]
    chars = keypad[num]

    for c in chars:
        letter += c
        bt(index + 1, letter)
        sliced_letter = letter[0:len(letter)-1]
        letter = sliced_letter

    return result


print(bt(0, ''))
