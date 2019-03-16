import math
import numpy

if __name__=='__main__':
    arr = list(map(float, input().split(",")))
    
    n = len(arr)
    squareplus = 0.00
    mean =0.00
    rms = 0.00
    
    
    for i in range(0,n):
        squareplus = squareplus + (arr[i]**2)
    
    print(squareplus)
    
    mean = (squareplus/float(n))
    print(mean)
    
    rms = math.sqrt(mean)
    
    
    print("%.4f" % rms);

    