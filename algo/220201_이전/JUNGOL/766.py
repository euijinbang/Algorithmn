import sys
sys.stdin = open("input.txt")

# input = 'beauty and the beast'

# word_list = [input().split()]
# [['beauty', 'and', 'the', 'beast']]


# word_list = input().split()
# word_list = [x for x in input().split()]
word_list = list(input().split())
# ['beauty', 'and', 'the', 'beast']


print(word_list)
for i in range(len(word_list)-1, -1, -1):
    print(word_list[i], end=' ')
