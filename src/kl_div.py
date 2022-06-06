import numpy as np
from scipy.interpolate import interp1d

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


def kl_div(P, Q, eps=1e-10):
    '''KL divergence calculation '''
    P = sorted(P)
    Q = sorted(Q)
    
    P_positions, P_counts = cumcount_reduced(P)
    Q_positions, Q_counts = cumcount_reduced(Q)
    
    f_P = interp1d(P_positions, P_counts)
    f_Q = interp1d(Q_positions, Q_counts)
    
    x_min = np.max([P_positions[1], Q_positions[1]])
    x_max= np.min([P_positions[-1], Q_positions[-1]])
    
    X = np.array( [x for x in P_positions if ((x >= x_min) & (x <= x_max))] )
    values = (f_P(X) - f_P(X-eps))  / (f_Q(X) - f_Q(X-eps))
    out = np.sum(np.log(values[values > 0]))
    out /= len(X)
    out -= 1.
    return out


def main():
   P = np.random.normal(loc=0.3, scale=1, size=size)
    Q = np.random.normal(loc=1, scale=2, size=size)
    outputs.append(get_delta(P, Q)) 


if __name__ == '__main__':
    main()
