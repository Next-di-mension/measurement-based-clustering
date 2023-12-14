

import numpy as np


# defining similarity measure as Euclidean distance from some origin (0,0)
def distance(x,y,):
    return (x**2 + y**2  )**(1)

def super(int_dist_list):

    '''This function takes a list of integers and returns a superposed vector of the integers.'''

    num_qubits = int(np.log2(max(int_dist_list))) + 1
    superposed_vector = np.zeros(2**num_qubits,dtype = int)  
    for i in range(2**num_qubits):    # i ranges from 0 to 2**N, 2^N also represents the range of distance
        if i in int_dist_list: 
            superposed_vector[i]=1
    normalized_vector = np.array([superposed_vector / np.linalg.norm(superposed_vector)])

    return normalized_vector

#delta = 0.5 
def Gaussian(delta, y, x):
    return ((2*np.pi*(delta**2))**(-1/2))*np.exp(-(y-x)**2/(2*delta**2))


# effect operator
def Effect_op(y,delta):
    '''args: 
       y: distance from the origin, 
       delta: standard deviation of the Gaussian
       returns: effect operator E_y
    '''

    k = 0 
    diagonal = []
    E_00000000 =  np.array(np.zeros((256, 256), dtype = int))
    for i in range(len(E_00000000[0])):
        #for j in range(len(E_000000[0])):
        #   if i == j:
        diagonal.append( (10**4)*Gaussian(delta,y,i ))
    
    #print(diagonal )
    for i in range(len(E_00000000[0])):
        for j in range(len(E_00000000[0])):
            if i == j:
                E_00000000[i][j] = diagonal[k]
                k += 1
        diagonal = (np.diag(E_00000000))
    return diagonal