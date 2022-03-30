N = input()

for i in range(1, 10):
    result = int(N) * i
    i_text = str(i)
    print(N + ' * ' + i_text + " = ", end="")
    print(result)