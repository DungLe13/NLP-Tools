# Implementation of the Forward Algorithm
"""
    forward_algo.py: Forward Algorithm 
    Computing Likelihood: Given an HMM with two hidden states (A, B) and
    an observation sequence O, determine the likelihood P(O|(A, B))
    Author: Dung Le (dungle@bennington.edu)
    Date: 10/16/2017
"""

import numpy as np

def forward(observations, states, a, b):
    T = len(observations)
    N = len(states)

    # a probability matrix 
    forward_prob = np.zeros((N, T))

    for s in range(N):
        # since matrix b is [[0.2 0.4 0.4]
        #                    [0.5 0.4 0.1]]
        # with column refers to number of ice cream {1, 2, 3} respectively & 1st row is H, 2nd row is C
        # this means that the column index is (num_ice_cream - 1)
        col_index = observations[0] - 1
        forward_prob[s, 0] = a[0, s] * b[s, col_index]

    for t in range(1, T):
        col_index = observations[t]-1
        for s in range(N):
            # since a[0, s] represent the probabilities P(H|start) or P(C|start)
            # here we calculate P(H or C | H or C), therefore, must increment index s1 by 1
            forward_prob[s, t] = sum([(forward_prob[s1, t-1] * a[s1+1, s] * b[s, col_index]) for s1 in range(N)])

    return forward_prob


if __name__ == "__main__":
    a = np.array([[0.8, 0.2], [0.7, 0.3], [0.4, 0.6]])
    b = np.array([[0.2, 0.4, 0.4], [0.5, 0.4, 0.1]])
    obs = [3, 1, 3]
    obs1 = [3, 3, 1, 1, 2, 2, 3, 1, 3]
    obs2 = [3, 3, 1, 1, 2, 3, 3, 1, 2]
    states = ['H', 'C']
    print(forward(obs, states, a, b))
