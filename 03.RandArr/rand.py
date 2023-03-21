import numpy as np

print("Generate an array of random numbers")
print(np.random.random((3, 3)))
print()

print("Generate an array of random integers in a certain interval")
print(np.random.randint(0, 10, (3, 3)))
print()

print("Generate an array of random integers that considered normal distribution, avg, std deviation")
print(np.random.normal(0, 1, (3, 3)))
print()

print("Generate an array of random numbers considering uniform distribution")
print(np.random.rand(3, 3))
print()

print("Generate an array of random numbers considering standard normal distribution")
print(np.random.randn(3, 3))
