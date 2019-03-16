
import math
import numpy

if __name__=='__main__':
    
    
    arr = list(map(float, input("Enter the numbers\n").split(",")))
    
    n = len(arr)
    squareplus = 0.00
    mean =0.00
    rms = 0.00
    
    
    
    for i in range(0,n):
        squareplus = squareplus + (arr[i]**2)
    
    
    mean = (squareplus/float(n))
    
    rms = math.sqrt(mean)
    
    print("The Root mean Square value is :")
    print("%.4f" % rms);

    
