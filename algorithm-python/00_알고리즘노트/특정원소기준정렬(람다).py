data = [(1, 400), (2, 300), (3, 100)]

data.sort(key=lambda x: x[1])
data.sort(key=lambda x: x[0], reverse=True)

print(data)
