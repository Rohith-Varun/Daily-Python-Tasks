import numpy as np
data = np.arange(1,10,2) #start, stop, step
print(data)

import numpy as np
data = np.linspace(1,25,5) 
print(data)

import numpy as np
data = np.array([1,2,3,4,5,6]) #the each element in the array will be added with 10 
print(data)
print(data + 10) #the data in the array will be added with the value of 10 1 -> 10.

import numpy as np
data = np.array([1,2,3,4,5,6]) 
print(sum(data))
print(min(data))
print(max(data))
print(data.mean())

import numpy as np
data = np.array([1,2,3,4,5,5,6])
print(data.mean())
print(np.mean(data))
