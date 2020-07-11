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
def detect_cycle_gen(mat, verbose=True):
    
    components = find_components(mat, verbose=False)
    cycles = []

    for component in components:
        
        cycle = detect_component_cycle(mat, component)
        cycles.append(cycle)

        if verbose:
            print('The component consisting of the nodes:\n[%s]' % ','.join(map(str,sorted(component))))
            if len(cycle) == 0:
                print('has no cycle\n')
            else:
                print('has a cycle consisting of the nodes:\n[%s]\n' % ','.join(map(str,cycle)))
    

    return components, cycles 



def detect_component_cycle(mat, component):

    cycle = []
    root = component[0]        # Components are connected: Use arbitrary starting node

    N = len(mat)
    visited = [0]*N
    parents = [-2]*N

    stack = [ (root, -1) ]

    while len(stack) != 0 and len(cycle) == 0:

        node,parent = stack.pop()
        visited[node] = 1
        parents[node] = parents

        for n in np.nonzero( mat[node] )[0]:

            if n not in component:
                continue

            if visited[n] == 0:
                stack.append( (n,node) )

            elif parent != n:
                mat[n][node] = mat[node][n] = 0
                cycle.append( (node,n) )
                cycle.extend( shortest_path( mat, node, n, verbose=False ) )
                mat[n][node] = mat[node][n] = 1

                break

    return cycle



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
