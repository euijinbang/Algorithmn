data = [(1, 'dog'), (2, 'cat'), (3, 'chick')]

que = int(input('Number? '))
p = 0
for i in range(len(data)):
    if data[i][0] == que:
        print(data[i][1])
        p += 1

# 다 돌았는데도 없으면 모른다를 출력. if문을 안쓰면 for문 끝난 후 항상 실행된다.
if p == 0:
    print("I don't know.")

