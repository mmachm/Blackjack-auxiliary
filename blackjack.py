import numpy as np
from matplotlib.pyplot import plot, show
import math
from winfunction import p_win
from stopwatch import Stopwatch
from distribution import Distribution

def run(res = 5):
    dist = Distribution(res)
    watch = Stopwatch()
    binary_search(dist)
    print("Binary search took " + str(watch.split_time()) + " seconds. \n")
 
def binary_search(dist):
    maximal_min = 0
    optimal_threshold = 0
    # p1 and p2 for (your) thresholds
    p1, p2 = 0, dist.res-1
    while p2 - p1 > 1:
        # c for center
        c = math.floor((p1 + p2)/2)
        if find_worst_case(dist, c) <= find_worst_case(dist, c+1):
            p1 = c
        else:
            p2 = c
    m1, m2 = find_worst_case(dist, p1), find_worst_case(dist, p2)
    if m1 > m2:
        optimal_threshold, maximal_min = p1, m1
    else:
        optimal_threshold, maximal_min = p2, m2
    print("\nThe best threshold is " + str(optimal_threshold) + " (i.e. play to get " + str(optimal_threshold+1) + "). Minimum is " + str(maximal_min) + ". [BINARY SEARCH 2 O(  n log^2(n)  )]")

def find_worst_case(dist, t):
    # t for (your) threshold, p1, p2 for enemy thresholds
    p1, p2 = 0, dist.res-1
    while p2 - p1 > 1:
        # c for center
        c = math.floor((p1 + p2)/2)
        if p_win(t, c, dist) >= p_win(t,  c+1, dist):
            p1 = c
        else:
            p2 = c    
    return min(p_win(t, p1, dist), p_win(t, p2, dist))


# WARNING: This function has O(n^3) runtime! Mostly only useful for debug.
def full_search(dist, print_matrix=False):
    win_matrix = []
    mins = []
    for t1 in range(dist.res):
        win = []
        for t2 in range(dist.res):
            win.append(p_win(t1, t2, dist))
        win_matrix.append(win)
        mins.append(min(win))
    maximal_min = max(mins)
    for i, minimum in enumerate(mins):
        if minimum == maximal_min:
            print("The best threshold is " + str(i) + " (i.e. play to get " + str(i+1) + "). Minimum is " + str(mins[i]) + ". [FULL SEARCH O(n^3)]")
    if print_matrix:
        print(np.array(win_matrix))


    
