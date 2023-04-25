import pandas as pd

student_data1 = pd.DataFrame({
'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morningstar'],
'marks': [200, 210, 190, 222, 199]})
student_data2 = pd.DataFrame({
'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Macy Meadows'],
'marks': [201, 200, 198, 219, 201]})
print("Original DataFrames:")
print(student_data1)
print(student_data2)

merged_data = pd.merge(student_data1, student_data2,  on='student_id', how='inner')
print("Merged Data (inner join):")
print(merged_data)