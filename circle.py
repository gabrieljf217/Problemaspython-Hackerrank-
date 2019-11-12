import numpy as np
import math

diametro = 11
radio = int(diametro/2)
epsilon = 2.2

arr = np.zeros((diametro, diametro))

for angle in range(0, 360, 5):
    x = radio * math.sin(math.radians(angle)) + radio
    y = radio * math.cos(math.radians(angle)) + radio
    arr[int(round(y))][int(round(x))] = 1
    
print(arr)