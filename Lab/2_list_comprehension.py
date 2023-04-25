list = ['x', 'y' ,'z']
pattern1 = []
pattern2 = []
[pattern1.append(list[i]*j) for i in range(len(list)) for j in range(1,4)]
[pattern2.append(list[i]*j) for j in range(1,4) for i in range(len(list))]
print(pattern1)
print(pattern2)
