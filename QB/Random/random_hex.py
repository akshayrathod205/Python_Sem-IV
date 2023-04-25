import random
import string

print("Random Color Hex")
print("#{:06x}".format(random.randint(0, 0xFFFFFF)))

print("Random alphabetical string")
max_length = 255
s = ""
for i in range(random.randint(1, max_length)):
    s += random.choice(string.ascii_letters)
print(s)

print("Random value bteween 2 integers (inclusive)")
print(random.randint(-4, 10))

print("Random multiple of 7 between 0 and 70")
print(random.randint(0, 10) * 7)

print("Generate a random alphabetical character:")
print(random.choice(string.ascii_letters))

print("\nGenerate a random alphabetical string of a fixed length:")
str1 = ""
for i in range(10):
    str1 += random.choice(string.ascii_letters)
print(str1)