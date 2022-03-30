# sort() => O(nlogn)

text = input()
int_arr = list()

for t in text:
    int_arr.append(int(t))

int_arr.sort(reverse=True)

sorted_arr = list()
for num in int_arr:
    sorted_arr.append(str(num))


result = ''.join(sorted_arr)
print(result)
