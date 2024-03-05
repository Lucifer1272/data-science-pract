import numpy as np 
np.set_printoptions(precision = 2) 
x = np.zeros((3,))
weights = np.zeros((3,)) 
desired = np.zeros((3,)) 
actual = np.zeros((3,)) 
for i in range(0,3):
    x[i] = float(input("Initial Inputs: ")) 
for i in range(0,3):
    weights[i] = float(input("Initial weights: ")) 
for i in range(0,3):
    desired[i] = float(input("Initial Desired: ")) 
a = float(input("Enter learning rate: ")) 
print("\nActual",actual) 
print("Desired\n",desired)
while True:
    if np.array_equal(desired,actual): 
        break
    else:
        for i in range(0,3):
            weights[i] = weights[i] + a *(desired[i] - actual[i]) 
            actual = x*weights
            print("Weights:",weights) import numpy as np 
np.set_printoptions(precision = 2) 
x = np.zeros((3,))
weights = np.zeros((3,)) 
desired = np.zeros((3,)) 
actual = np.zeros((3,)) 
for i in range(0,3):
    x[i] = float(input("Initial Inputs: ")) 
for i in range(0,3):
    weights[i] = float(input("Initial weights: ")) 
for i in range(0,3):
    desired[i] = float(input("Initial Desired: ")) 
a = float(input("Enter learning rate: ")) 
print("\nActual",actual) 
print("Desired\n",desired)
while True:
    if np.array_equal(desired,actual): 
        break
    else:
        for i in range(0,3):
            weights[i] = weights[i] + a *(desired[i] - actual[i]) 
            actual = x*weights
            print("Weights:",weights) 
