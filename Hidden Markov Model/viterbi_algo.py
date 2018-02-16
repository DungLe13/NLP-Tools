# Implementation of the Viterbi Algorithm
"""
    viterbi_algo.py: Viterbi Algorithm
    Decoding: Given as input an HMM with two hidden states (A, B) and
    an observation sequence O, find the most probable sequence of states
    Q = q1q2q3q4...qT
    Author: Dung Le (dungle@bennington.edu)
    Date: 10/17/2017
"""

import numpy as np

def viterbi(observations, states, a, b):
    T = len(observations)
    N = len(states)

    # a probability matrix + a best_path matrix to keep track of the most probable path
    viterbi_prob = np.zeros((N, T))
    best_path = np.zeros((1, T))

    for s in range(N):
        col_index = observations[0] - 1
        viterbi_prob[s, 0] = a[0, s] * b[s, col_index]

    for t in range(1, T):
        col_index = observations[t]-1
        for s in range(N):
            # since a[0, s] represent the probabilities P(H|start) or P(C|start)
            # here we calculate P(H or C | H or C), therefore, must increment index s1 by 1
            viterbi_prob[s, t] = max([(viterbi_prob[s1, t-1] * a[s1+1, s] * b[s, col_index]) for s1 in range(N)])

    for t in range(T-1,0,-1): # states of (last-1)th to 0th time step
        best_path[0, t] = np.argmax(viterbi_prob[:, t])

    return (viterbi_prob, best_path)

if __name__ == "__main__":
    a = np.array([[0.8, 0.2], [0.7, 0.3], [0.4, 0.6]])
    b = np.array([[0.2, 0.4, 0.4], [0.5, 0.4, 0.1]])
    obs = [3, 1, 3]
    #obs1 = [3, 3, 1, 1, 2, 2, 3, 1, 3]
    #obs2 = [3, 3, 1, 1, 2, 3, 3, 1, 2]
    states = ['H', 'C']
    print(viterbi(obs, states, a, b))
