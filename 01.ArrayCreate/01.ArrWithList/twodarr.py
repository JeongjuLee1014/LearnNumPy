import numpy as np

print("<Test two dimensional array a2>")
a2 = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("a2 :")
print(a2)
print("type(a2) :", end=" ")
print(type(a2))
print("a2.shape :", end=" ")
print(a2.shape)
print("main diagonal elements of a2 :", end=" ")
print(a2[0, 0], a2[1, 1], a2[2, 2])
a2[0, 0] = -1
a2[1, 1] = -5
a2[2, 2] = -9
print("Changed a1 :")
print(a2)
