import math
n = int(input("Enter no. of elements: ")) 
yin = 0
for i in range(0,n): 
    x=float(input("x= ")) 
    w=float(input("w= ")) 
    yin = yin + (x*w)
b = float(input("b= ")) 
yin = yin + b
print(' ')
print("yin",yin)
print(' ')
binary_sigmoidal = (1/(1+(math.e**(-yin)))) 
print("Binary Sigmoidal= ",round(binary_sigmoidal,3)) 
print(' ')
 
bipolar_sigmoidal = (2/(1+(math.e**(-yin)))) - 1 
print("Bipolar Sigmoidal= ",round(bipolar_sigmoidal,3))
