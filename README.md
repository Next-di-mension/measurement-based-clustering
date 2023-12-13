# Measurement based quantum clustering algorithms 
This repository contains a code for implementing the algorithms developed in the paper: 

[ S. Patil, S. Banerjee, P. K. Panigrahi, Measurement-based quantum clustering algorithms, arXiv preprint
arXiv:2302.00566 (2023).](https://arxiv.org/abs/2302.00566). The code is written in Python 3.8.10 The code is tested on Ubuntu 18.04.5 LTS.
 


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

<div align="center">
    <img src="https://github.com/Next-di-mension/measurement-based-clustering/assets/98448938/29167b6f-27aa-4b34-aad1-126143dd7cec" width="500">
</div>





# Results
## Concentric circle data set
The data set consists of 1000 data points with 2 features. The data points are generated using the following code:
```python
from sklearn.datasets import make_circles
X, y = make_circles(n_samples=1000, noise=0.05, factor=0.5)
```


<div align="center">
    <img src="https://github.com/Next-di-mension/measurement-based-clustering/assets/98448938/694ebc87-f4c2-43d0-80b5-8aafad98157a" width="300">
    <img src="https://github.com/Next-di-mension/measurement-based-clustering/assets/98448938/c7409d17-514e-40c5-a962-375efe2a233e" width="300">
    <img src="https://github.com/Next-di-mension/measurement-based-clustering/assets/98448938/ee65c883-9063-4f6c-8527-731882e60b66" width="300">
</div>

Dataset of 400 points generated using sklearn with noise ratio of 0.1. (Middle) Classification of the dataset using the traditional classical divisive clustering algorithm. (Right) Classification of the dataset using the QHCA. Different colors represent different clusters. 








