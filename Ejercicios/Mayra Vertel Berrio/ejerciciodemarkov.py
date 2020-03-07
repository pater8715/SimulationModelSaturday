import numpy as np
p=np.array([
    [ 0 , 0.5,0,0,0.5],
    [ 0.5 , 0,0.5,0,0],
    [ 0 , 0.5,0,0.5,0],
    [ 0 , 0,0.5,0,0.5],
    [ 0.5 , 0,0,0.5,0]
   
    ])
 
for n in range(1, 11, 1):print(n,np.linalg.matrix_power(p,n))