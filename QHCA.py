from qiskit import IBMQ
IBMQ.save_account('3ccb2d17a0f19c3ce64cf44b3e1c90d3369ea562672f7315624ee8d92bb4350e10b643e3b2af92eef73c029e051518c2a833fb0ffa2e600b2c6c65ed5dd29d40')
IBMQ.load_account()
from qiskit import *
import math 
import numpy as np
import time
from copy import deepcopy
from qiskit import QuantumRegister, QuantumCircuit, ClassicalRegister, Aer
from qiskit.quantum_info import state_fidelity
#simulators
S_simulator = Aer.backends(name = 'statevector_simulator')[0]
M_simulator = Aer.backends(name = 'qasm_simulator')[0]
U_simulator = Aer.backends(name = 'unitary_simulator')[0]
#provider = IBMQ.get_provider(hub = 'ibm-q-research')

def decimalToBinary(n,N):  # bin returns the binary representation of an integer.  n is the input decimal and N is the length of the string 
    bin1=bin(n).replace("0b", "")
    bin2='0'*(N-len(bin1))+bin1
    return bin2

def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)   

def distance(x1,y1,x2,y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)
distance(0,0,3,4)

#function to pick k largest elements in the matrix. 
#We will need to flatten the matrix to an array, 'arr' 
def kLargest(arr, k):
    # Sort the given array arr in reverse # order.
    kL=[]
    arr.sort(reverse = True)
    # Print the first kth largest elements
    for i in range(k):
        kL.append(arr[i]) 
    FD=list(set(kL))
    return FD


dist_mat =  np.array(np.zeros((130, 130), dtype = float))


dist_symm = (dist_mat + dist_mat.T)/2
city_matrix= dist_symm
City_mat =  np.array(np.zeros((130, 130), dtype = int))
for i in range(len(city_matrix)):
    for j in range(len(city_matrix)):
        City_mat[i][j] = (city_matrix[i][j])


#FD is the largest element in the city_matrix, i.e., the largest distance between the cities. 

FD = kLargest(list(City_mat.flatten()),1)# .fltten, flattens the function to 1D
#We need the cities corresponding to this distance. They will serve as the centres of our 
#first two clusters
for i in range(len(City_mat[0])):  # O(n)
    for j in range(len(City_mat[0])): # O(n)

        for k in range(len(FD)): #O(n)
            if City_mat[i][j] == FD[k]:
                k2=i   ####
                k1=j  ####

print('cities with the largest distances are:', k1, 'and', k2)
print('The distance between cities', k1, 'and', k2, 'is', FD[0], 'km')


#For now we choose any of the two cities as origin, and sort the cities according to their distances from the origin
# city_matirx[][] first one is row indices and second one is column index 
org  = k1 # chossing k1 as origin 
list_dist = []
list_cities=[]
for i in range(len(city_matrix[0])):
    list_dist.append(city_matrix[k1][i])
    list_cities.append(i)

city_dict = dict(zip(list_cities, list_dist))    
city_dict_sorted = dict(sorted(city_dict.items(), key=lambda item: item[1]))
print(city_dict_sorted)
nq = int(math.log(FD[0]/10,2))+ 1  # representing the distances in terms of qubit 
int_list_dist=[int(i) for i in list_dist]
bin_dist = [decimalToBinary(int(i),nq) for i in list_dist] # all the distances from city k1 = 14 in binary form 
print(int_list_dist)
print(list_dist)

num_clusters = 4
M = int(math.log(num_clusters,2))  # based on clusters 
M
c = ClassicalRegister(nq+M)
# we have N qubits and all are in state x2
# and we apply controlled not to rest of the M qubits(ancillas).
#quantum circuit
q=QuantumRegister(nq+M) # 18 qubits 
#c=ClassicalRegister(N+M)
qc = QuantumCircuit(q,c)
qc.initialize(x2, [i+M for i in range(nq)]) # prepare x2 state on the first 8 qubits  
# qc.initialize(params, qubits=None)
# qubits = quantumregister or a list. these are genreally qubits that are to be initialized
for j in range(M):
    qc.cx(nq+j,j)

job = execute(qc, backend=S_simulator, optimization_level=0)
psi_block2 = job.result().get_statevector(qc, decimals=16) # gives the final statevector of the experiment upto 16 decimal places

qc.measure(range(nq+M),range(nq+M)) # this is a way to do all the qc.measure(qr8[j],cr8[j]) at once

qobj = assemble(qc, shots=8125)
Counts = S_simulator.run(qobj).result().get_counts()

anc_key = list(set([list(Counts.keys())[i][nq:nq+M] for i in range(len(list(Counts.keys())))])) ## last 4 qubits are for the clusters which is bascically ancilla qubits 
List_cluster=[]
for i in range(len(anc_key)):
    cluster=[]
    for j in range(len(list(Counts.keys()))):
        if anc_key[i] == list(Counts.keys())[j][nq:nq+M]:
            cluster.append(list(Counts.keys())[j][0:nq])
    List_cluster.append(cluster)

print('The clusters are:', List_cluster)