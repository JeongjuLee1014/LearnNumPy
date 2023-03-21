import numpy as np

print("<Test Three dimensional array a3>")
a3 = np.array([ [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ],
				[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ],
				[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] ]) 
print("a3 :")
print(a3)
print("type(a3) :", end=" ")
print(type(a3))
print("a3.shape :", end=" ")
print(a3.shape)
print("some elements of a3 :", end=" ")
print(a3[0, 0, 0], a3[1, 1, 1], a3[2, 2, 2])
a3[0, 0, 0] = 100
a3[1, 1, 1] = 100
a3[2, 2, 2] = 100
print("Changed a3 :")
print(a3)
