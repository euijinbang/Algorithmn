data = []

for i in range(6):
    data.append(input('Element? '))

start = int(input('Index? '))
print(data[start:len(data)+1])