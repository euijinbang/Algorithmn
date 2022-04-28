"""
다시풀기..
"""
def reverseWords(s):
    l, r = 0, 0
    res = ''
    while r < len(s):
        if s[r] != ' ':
            r += 1
        elif s[r] == ' ':
            res += s[l:r+1][::-1]
            r += 1
            l = r

    res += ' '
    res += s[l:r][::-1]
    return res[1:]

print(reverseWords('hi there'))
