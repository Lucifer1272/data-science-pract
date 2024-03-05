import numpy as np
x1 = np.array([1,-1,-1,1,-1,-1,1,1,1,1])
x2 = np.array([1,-1,1,1,-1,1,1,1,1,1])
y = np.array([1,-1]) 
b = 0
wtold = np.zeros((9,)).astype(int) 
wtnew = np.zeros((9,)).astype(int) 
print("--",wtold)
print("First input with target 1") 
for i in range(0,9):
    wtnew[i] = wtold[i] + x1[i]*y[0] 
wtold = wtnew
b = b + y[0]
 
print("New Weights:",wtnew) 
print("Bias Value:",b) 
print("Second input with target -1") 
for i in range(0,9):
    wtnew[i] = wtold[i] + x2[i]*y[1] 
b = b + y[1]
print("New Weights:",wtnew) 
print("Bias Value:",b)
