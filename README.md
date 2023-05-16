# Kullback-Leibler divergence estimation algorithm

The present code is based on Section II of Fernando Pérez-Cruz's paper "Kullback-Leibler Divergence Estimation of Continuous Distributions", DOI:10.1109/ISIT.2008.4595271. From two independent datasets of continuous variables, the KLD (aka relative entropy) is estimated by the construction of cumulative probability distributions and the comparison between their slopes at specific points.

Estimating the probability distributions and directly evaluating KLD's definition leads to a biased estimation, whereas the present method leads to an unbiased estimation. This is particularly important in practical applications due to the finitude of collected statistics.

The code is written in python and can be collected in the first cell of the jupyter notebook kl_calculation.ipynb.

Its usage is illustrated in two scenarios (see applications folder):
  1. Entropy production inference scheme introduced in journals.aps.org/prx/abstract/10.1103/PhysRevX.12.041026, which explores the relation between KLD and entropy production, a key physical quantity in nonequilibrium thermodynamics. I encourage researchers in this field to learn and use good estimators for KLD.
  2. Using data processed from a real biological system, we import and analyze two timeseries in view of KLD estimation using Pérez-Cruz's and the standard method.

If you find this code useful, we kindly ask to cite our work where it is discussed [Phys. Rev. X 12, 041026 (2022)].


Comments are welcome: pedroharunari [at] gmail.com

The estimator implementation was written with the help of Ariel Yssou.
