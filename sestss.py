import numpy as np
size = int(input("Enter the size of matrix:")) 
power=int(input("enter the number of times to multiply: "))
print("enter the matrix values row wise: ")
a = [[int(input()) for x in range (size)] for y in range(size)]
print("The Resultant matrix will be: ")
print(np.linalg.matrix_power(a, power))
