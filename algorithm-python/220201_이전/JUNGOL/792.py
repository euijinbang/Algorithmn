color = []
animal = []
for i in range(4):
    color, animal = input('Input? ').split()
    color.append(color)
    animal.append(animal)

print(f'Color: {color}')
print(f'Animal: {animal}')
