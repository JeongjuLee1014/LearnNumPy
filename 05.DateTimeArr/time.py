import numpy as np

print("Generate date array")
date = np.array('2020-01-01', dtype=np.datetime64)
print(date)
print()

print("Generate 12 late date with np.arange(12)")
print(date + np.arange(12))
print(date)

print("Generate date array with time")
datetime = np.datetime64('2020-06-01 12:00')
print(datetime)
print()

print("Generate date array with nano sec")
datetime = np.datetime64('2020-06-01 12:00:12.34', 'ns')
print(datetime)
