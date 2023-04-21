list = []
even_sum = 0
odd_sum = 0
n = int(input("Enter number of elements in list: "))
print("Enter the elements: ")
for i in range(n):
    list.append(int(input()))
    if list[i] % 2 == 0:
        even_sum += list[i]
    else: 
        odd_sum += list[i]
        
sum = (even_sum, odd_sum)
print("Sum of even and odd numbers respectively: ", sum)
