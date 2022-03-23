class Item:
    def __init__(self, name, count, price, rate):
        self.name = name
        self.count = count
        self.price = price
        self.rate = rate

pen = Item('pen', 20, 100, 50.5)
note = Item('note', 5, 95, 35.3)
eraser = Item('eraser', 110, 97, 14.2)

print('item'.rjust(10, " "), end='')
print('count'.rjust(10, " "), end='')
print('price'.rjust(10, " "), end='')
print('rate'.rjust(10, " "), end='')
print('')

items = [pen, note, eraser]

for item in items:
    print(f'{item.name.rjust(10, " ")}', end='')
    print(f'{str(item.count).rjust(10, " ")}', end='')
    print(f'{str(item.price).rjust(10, " ")}', end='')
    print(f'{str(item.rate).rjust(10, " ")}', end='')
    print('')