# KLD_estimation

Estimation of Kullback-Leibler divergence (KLD) based on DOI:10.1109/ISIT.2008.4595271
--------------------------------------------

The present code is based on Section II of Fernando Pérez-Cruz's paper "Kullback-Leibler Divergence Estimation of Continuous Distributions". From two independent datasets of continuous variables, the KLD (aka relative entropy) is estimated by the construction of cumulative probability distributions and the comparison between their slopes at specific points.

Estimating the probability distributions and directly evaluating KLD's definition leads to a biased estimation, whereas the present method leads to an unbiased estimation. This is particularly important in practical applications due to the finitude of collected statistics.

The code is written in python and can be collected in the first cell of the notebook kl_calculation.ipynb. Its usage is illustrated in the entropy production inference scheme introduced in arxiv.org/abs/2203.07427, which explores the relation between KLD and entropy production, a key physical quantity in nonequilibrium thermodynamics. I encourage researchers in this field to learn and use good estimators for KLD.

Comments are welcome: pedroharunari [at] gmail.com

I acknowledge Ariel Yssou's help to make this code more efficient.
