# Measurement based quantum clustering algorithms 
This repository contains a code for implementing the algorithms developed in the paper: [Measurement based quantum clustering algorithms](https://arxiv.org/abs/2302.00566). The code is written in Python 3.8.10 The code is tested on Ubuntu 18.04.5 LTS.
 


## Cloning and handling dependencies 
Clone the repo:
```
 git clone https://github.com/Next-di-mension/measurement-based-quantum-clustering.git
```
# Repository structure
```
.
├── data
│   ├── ch130.tsp.gz
├── LICENSE
├── breast_cancer_clustering.ipynb
├── breast_cancer_unsharp.ipynb
├── churrtiz_clustering.ipynb
├── concentric_circle_clustering.ipynb
├── README.md

```

# Overview of the work 
We propose two novel measurement-based clustering algorithms are proposed based on quantum parallelism and entanglement. The Euclidean distance metric is used as a measure of `similarity' between the data points. The first algorithm follows a divisive approach. The second algorithm is based on unsharp measurements where we construct the set of effect operators with a Gaussian probability distribution to cluster similar data points. One major advantage of both the proposed algorithms is that they are simplistic in nature and easy to implement. We have successfully applied both algorithms on a concentric circle data set where the classical clustering approach fails. It is found that the presented clustering algorithms perform better than the classical divisive one; both in terms of clustering and time complexity which is found to be $O(kN(\text{log}N)^2)$ and $O(N^2)$ respectively. Alongside, we also implemented the algorithm on the Churrtiz data set of cities and the Wisconsin breast cancer dataset; where we found that the clustering approach performs well to distinguish data based on spacial similarity which for the latter algorithm it is achieved by the appropriate choice of the variance of the Gaussian window. Both of our algorithms are easy to implement as they do not require the black box, unlike other quantum clustering algorithms.

![Quantum Hierarchical Clustering Algorithm](Images\QCHA.png)





