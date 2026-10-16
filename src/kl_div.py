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
def KLD_PerezCruz(P, Q, eps=None):
    '''KL divergence calculation (inputs assumed continuous; eps kept for compatibility, unused)'''
    P = np.asarray(P, dtype=float).ravel()
    Q = np.asarray(Q, dtype=float).ravel()
    if P.size == 0 or Q.size == 0:
        raise ValueError("P and Q must be non-empty")
    if not (np.all(np.isfinite(P)) and np.all(np.isfinite(Q))):
        raise ValueError("P and Q must be finite")

    #definition of x_0 and x_{n+1}, padding relative to the data range
    lo, hi = min(P.min(), Q.min()), max(P.max(), Q.max())
    if hi == lo:
        raise ValueError("all samples identical")
    pad = (hi - lo) / (P.size + Q.size)

    #unique knots; tied points sit at the midpoint of the CDF jump (U(0)=1/2)
    def knots(x):
        u, c = np.unique(x, return_counts=True)
        return u, (np.cumsum(c) - c / 2) / len(x), c

    uP, vP, cP = knots(P)
    uQ, vQ, _ = knots(Q)
    P_positions, P_counts = np.r_[lo - pad, uP], np.r_[0., vP]
    Q_positions, Q_counts = np.r_[lo - pad, uQ, hi + pad], np.r_[0., vQ, 1.]

    #exact left slope of P_c at each x_i, and of Q_c on the segment containing x_i
    slope_P = np.diff(P_counts) / np.diff(P_positions)
    j = np.searchsorted(Q_positions, uP)
    slope_Q = (Q_counts[j] - Q_counts[j-1]) / (Q_positions[j] - Q_positions[j-1])
    out = np.sum(cP * np.log(slope_P / slope_Q)) / P.size - 1.

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
