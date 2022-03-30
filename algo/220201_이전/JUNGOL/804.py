w = 60
# w = '{:.2f}'.format(w)

w = float(input())

if w <= 50.80:
    print('Flyweight')
elif w <= 61.23:
    print('Lightweight')
elif w <= 72.57:
        print('Middleweight')
elif w <= 88.45:
        print('Cruiserweight')
else:
    print('Heavyweight')