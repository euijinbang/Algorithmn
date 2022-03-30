# data = ['1', '2', '3', '4', '5', '6']

data = []
for i in range(6):
    data.append(input('Element? '))

new_data = []
for i in range(len(data)//2):
    new_data.append(data[2*i])

for i in range(len(data)//2):
    new_data.append(data[2*i+1])

print(new_data)