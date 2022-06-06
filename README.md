# KLD_estimation
--------------------------------------------
Estimation of Kullback-Leibler divergence (KLD) based on DOI:10.1109/ISIT.2008.4595271
--------------------------------------------

The present code is based on Section II of Fernando Pérez-Cruz's paper "Kullback-Leibler Divergence Estimation of Continuous Distributions". From two datasets of continuous variables, the KLD (also known as relative entropy) is estimated by the construction of cumulative probability distributions and the comparison between their slopes.

Estimating the probability distributions and directly evaluating KLD's definition leads to a biased estimation, whereas the present method leads to an unbiased estimation. This is particularly important in practical applications due to the finitude of collected statistics.

The code was written by Pedro Harunari and Ariel Yssou for the analysis presented in the paper arxiv.org/abs/2203.07427, which explores the relation between KLD and entropy production, a key physical quantity in nonequilibrium thermodynamics.

Comments about possible issues and suggestions are welcome.
