The jupyter notebooks inside this folder illustrates the usage of Pérez-Cruz's estimator.

KLD_for_EP_inference: notebook containing the Gillespie simulation of a Markov process, its transition-based coarse-graining (which hides information) and the entropy production rate inference. The latter requires KLD evaluations.

KLD_from_data: notebook that imports two timeseries from a biological system (testdata) and analyze the KLD. Comparison with the standard method shows that the convergence is unbiased and, with such a finite dataset, the result is much closer to the expected value.
