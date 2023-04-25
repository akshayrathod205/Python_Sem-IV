import numpy as np
from scipy import linalg

# 1. Solve the system of linear equations
# Define the coefficients matrix and the constants vector
A = np.array([[9, 6, -5, 2],
              [4, 5, -7, 3],
              [-3, -4, 2, -5],
              [6, 1, 9, -1]])
b = np.array([17, 10, 20, 23])

# Solve the system of linear equations
x = linalg.solve(A, b)
print("Solution of the system of linear equations:")
print(x)
print()

# 2. Perform the following operations on a matrix
# Define matrix A and matrix B
A = np.array([[5, 3, 2],
              [6, 9, -3],
              [1, 7, 4]])
B = np.array([[3, -1],
              [2, -5]])

# a. Find Inverse of matrix A
A_inv = linalg.inv(A)
print("Inverse of matrix A:")
print(A_inv)
print()

# b. Find Kronecker product of A with B
A_kron_B = np.kron(A, B)
print("Kronecker product of matrix A and matrix B:")
print(A_kron_B)
print()

# c. Find determinant of matrix A
A_det = linalg.det(A)
print("Determinant of matrix A:")
print(A_det)
