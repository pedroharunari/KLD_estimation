import argparse
import numpy as np
from scipy.interpolate import interp1d

#returns the step function value at each increment of the CDF
def cumcount_reduced(arr):
    '''Cumulative count of a array'''
    sorted_arr = np.array(arr)
    counts = np.zeros(len(arr))
    
    rolling_count = 0
    for idx, elem in enumerate(sorted_arr):
        rolling_count += 1
        counts[idx] = rolling_count

    counts /= len(counts)
    counts -= (1 / (2 * len(counts)))

    return (sorted_arr, counts)

#takes two datasets to estimate the relative entropy between their PDFs
def KLD_PerezCruz(P, Q, eps=1e-11):
    '''KL divergence calculation'''
    P = sorted(P)
    Q = sorted(Q)
    
    P_positions, P_counts = cumcount_reduced(P)
    Q_positions, Q_counts = cumcount_reduced(Q)
    
    f_P = interp1d(P_positions, P_counts)
    f_Q = interp1d(Q_positions, Q_counts)
    
    #alternatively to defining x_0 and x_{n+1}, we only use the intersection between both sets
    x_min = np.max([P_positions[1], Q_positions[1]])
    x_max= np.min([P_positions[-1], Q_positions[-1]])
    
    X = np.array( [x for x in P_positions if ((x >= x_min) & (x <= x_max))] )
    values = (f_P(X) - f_P(X - eps)) / (f_Q(X) - f_Q(X - eps))
    filt = ((values != 0.) & ~(np.isinf(values)))
    values_filter = values[filt]
    out = (np.sum(np.log(values_filter)) / len(values_filter)) - 1.

    return out

def main(avg_1, std_1, avg_2, std_2, size):
    P = np.random.normal(
        loc=avg_1,
        scale=std_1,
        size=size
    )

    Q = np.random.normal(
        loc=avg_2,
        scale=std_2,
        size=size
    )

    return KLD_PerezCruz(P, Q)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Read distribution avg and stds")
    parser.add_argument('avg_1', type=float)
    parser.add_argument('avg_2', type=float)
    parser.add_argument('std_1', type=float)
    parser.add_argument('std_2', type=float)
    parser.add_argument('size', type=int, default=100, nargs='?')

    args = parser.parse_args()

    try:
        out = main(**vars(args))
        print(f'\033[92mKL divergence: {out}\033[0m')
    except Exception as e:
        print(e)
