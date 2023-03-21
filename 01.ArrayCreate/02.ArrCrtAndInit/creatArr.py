import numpy as np

print("Init all elements to 0")
print(np.zeros(10))
print()

print("Init all elements to 1")
print(np.ones(10))
print()

print("Init all elements to specified value")
print(np.full((3, 3), 1.23))
print()

print("Create unit matrix")
print(np.eye(3))
print()

print("Create trianglur matrix")
print(np.tri(3))
print()

print("Uninitailized array generate. Fast and low cost to generate. Garbage value")
print(np.empty(3))
print()

print("Create array that have same size with other array and filled with 0")
print(np.zeros_like([1, 2, 3, 4, 5]))
print()

print("Create array that have same size with other array and filled with 1")
print(np.ones_like([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]))
print()

print("Create array that have same size with other array and filled with 10")
print(np.full_like([ [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ], 
					 [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ],
					 [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] ], 10))
