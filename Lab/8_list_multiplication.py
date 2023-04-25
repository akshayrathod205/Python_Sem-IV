numbers = [1, 2, 3, 4]
multiplier = [5, 6, 7, 8]
result = []
try:
    for i in range(len(numbers)):
        result.append(multiplier[i] * numbers[i])

except IndexError:
    print("Multiplier list exhausted")
    
except NameError:
    print("List does not exist")
    
finally:
    if len(result) > 0:
        print("Multiplication for two lists is done")
        print(result)