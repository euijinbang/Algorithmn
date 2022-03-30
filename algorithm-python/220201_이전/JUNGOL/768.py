import sys
sys.stdin = open("input.txt")

for i in range(2):
    singer = input()
    song = input()
    print(f'{singer}: {song}', end='')  # 한 줄 공백을 없애기 위한 end=''
    print('')   # 줄 바꿈을 위한 print('')
