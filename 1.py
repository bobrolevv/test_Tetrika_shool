def task(array):
    for i in range(len(array)):
        if array[i] == '0':
            return i

print(task("111111111110000000000000000"))

