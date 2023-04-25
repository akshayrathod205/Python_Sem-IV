def extract_nth_element(test_list, n):
    result = list(map (lambda x:(x[n]), test_list))
    return result

students = [('Pranav Patil', 98, 99), ('Akshay Rathod', 97, 96), ('Shashank Gupta', 91, 94), ('Deep Prajapati', 94, 98)]
print ("Original list:")
print(students)
for n in range(0,3):
    print("\nExtract nth element ( n =",n,") from the said list of tuples:")
    print(extract_nth_element(students, n))

