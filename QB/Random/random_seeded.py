import random

print("Seeded random number")
print(random.Random().random())
print(random.Random(2).random())

print("Float between 0 and 1, excluding 1")
print(random.random())