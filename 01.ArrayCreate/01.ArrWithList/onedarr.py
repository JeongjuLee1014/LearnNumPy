import numpy as np

print("<Test one dimensional array a1>")
a1 = np.array([1, 2, 3, 4, 5])
print("a1 :", end=" ")
print(a1)
print("type(a1) :", end=" ")
print(type(a1))
print("a1.shape :", end=" ")
print(a1.shape)
print("elements of a1 :", end=" ")
print(a1[0], a1[1], a1[2], a1[3], a1[4])
a1[0] = 4
a1[1] = 5
a1[2] = 6
print("Changed a1 :", end=" ")
print(a1)
