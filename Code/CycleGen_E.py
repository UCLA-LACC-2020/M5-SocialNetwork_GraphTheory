# LACC 2019
# Graph Theory easy exercises for Social Networks module
#
# Extra Exercise for detecting cycles in a graph containing multiple components

import numpy as np
from Connect import find_components
from LACC2019 import shortest_path


#*************************************
# detect_cycle_gen(mat)
#
# Detects if cycle exists in each component of a disconnected graph
# Input:  adj. matrix
# Output: a 2D list 'components', and a 2D list 'cycles'
#
# Notes:
#   1. The i-th item in 'components' should list all nodes within that connected component
#
#   2. The i-th item in 'cycles' should list a cycle within the i-th component ([] if no cycles)
#
# Hints:
#   1. Is it necessary to entirely rewrite this function? Can some previous functions be re-used?
#
#   2. Find the connected components first, then find cycles in each component
#
#*************************************
def detect_cycle_gen(mat):
    
    return components, cycles 



# Simple helper function to check if the cycles found are correct
def check_cycles(mat, cycles):

    errorCycles = []

    for cycle in cycles:
        if len(cycle) - sum([ mat[n1][n2] for n1,n2 in cycle ]) != 0:
            errorCycles.append(cycle)

    if len(errorCycles) == 0:
        print('Congratulations! All cycles are correct')
    else:
        for c in errorCycles:
            print('The cycle %s does not exist' % (cycles))
