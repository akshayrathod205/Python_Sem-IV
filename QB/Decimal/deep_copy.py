import copy
nums_x = [1, [2, 3, 4]]
print("Original list: ", nums_x)
nums_y = copy.deepcopy(nums_x)
print("\nDeep copy of the said list:")
print(nums_y)

nums_x = {"a":1, "b":2, 'cc':{"c":3}}
print("Original dictionary: ", nums_x)
nums_y = copy.deepcopy(nums_x)
print("\nDeep copy of the said list:")
print(nums_y)
print("\nChange the value of an element of the original dictionary:")
nums_x["cc"]["c"] = 10
print(nums_x)
print("\nSecond dictionary (Deep copy):")
print(nums_y)
