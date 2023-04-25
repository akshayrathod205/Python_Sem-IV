def moving_avg(*args):
    arr = []
    for i in args:
        arr += i
    window = 3 
    val = len(arr) - window + 1
    for i in range(val):
        y = 0
        x = []
        for j in range(i, i + window):
            y += arr[j]
            x.append(arr)
        print('y', i + 1, ' = ', y / window)
        x.clear()
        
a = moving_avg([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
print(a)
