# Reverse a string using extended slice
def reverse1(str):
    return str[::-1]

# Reverse a string using loop
def reverse2(str):
    reverse_str = ""
    for i in str:
        reverse_str = i + reverse_str
    return reverse_str

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print(reverse1(first_name), " ", reverse1(last_name))
print(reverse2(first_name), " ", reverse2(last_name))
