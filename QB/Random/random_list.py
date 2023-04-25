import random

print("List of random integers")
population = range(0, 100)
num_list = random.sample(population, 10)
print(num_list)

no_elements = 5
print(f"Randomly select {no_elements} item(s) from list")
result = random.sample(num_list, no_elements)
print(result)