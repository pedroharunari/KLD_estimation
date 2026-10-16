The jupyter notebooks inside this folder illustrates the usage of Pérez-Cruz's estimator.

*KLD_for_EP_inference*: notebook containing the Gillespie simulation of a Markov process, its transition-based coarse-graining (which hides information) and the entropy production rate inference. The latter requires KLD evaluations.

*KLD_from_data*: notebook that imports two timeseries from a biological system (testdata) and analyze the KLD. It also compares the estimate with the standard histogram method. With this dataset the estimate ($D \approx -0.004$) cannot be told apart from noise: splitting a single timeseries into two halves, for which the true KLD is zero, already gives values of the same size (0.0017 and -0.0007 for the two timeseries). The data comes from DOI:10.1088/1367-2630/ac0f18, it features forward and backward oscillation timeseries of the bullfrog's hair-bundle, which are used to quantify irreversibility.
