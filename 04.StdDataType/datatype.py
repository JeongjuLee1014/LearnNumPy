import numpy as np

print("Generate array with int elements and init val is 0")
print(np.zeros(20, dtype=int))
print()

print("Generate array with bool elements and init val is True(default)")
print(np.ones((3, 3), dtype=bool))
print()

print("Generate array with float elements and init val is 1.0")
print(np.full((3, 3), 1.0, dtype=float))
