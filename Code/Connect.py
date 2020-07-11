import math
import random
import numpy as np


# get_component(n,mat)
#   Gets the component that includes the node 
#
#   Inputs:  node node
#   Outputs: The list of nodes in the component
def get_component(node,mat):

    N = len(mat)
    components = set([node])
    preList = set( np.nonzero(mat[node])[0] )
    components.update(preList)

    while True:
        curList = set()
        for p in preList:
            neighbors = np.nonzero(mat[p])[0]

            for n in neighbors:
                if n not in components:
                    components.add(n)
                    curList.add(n)

        if len(curList) == 0:
            break 
        else:
            preList = curList

    return list(components)



# is_connected(mat)
#   Gets random component and checks if it is the same size as the graph
#
#   Inputs:  adjacency matrix mat
#   Outputs: True/False

def is_connected(mat):

    component = get_component(0,mat)
    return len(component) == len(mat)



# find_components(mat):
#   Finds all connected components in a graph
#   prints one component per line
#   If verbose = True, prints output
#   
#   Inputs:  adjacency matrix: mat
#   Outputs: the list of connected components: conncomp

def find_components(mat, verbose=True):
    
    N = len(mat)
    nodes = [i for i in range(N)]

    components = []

    while len(nodes) != 0:
        root = nodes[0]
        component = get_component(root, mat)
        components.append( component )
        nodes = [ n for n in nodes if n not in component ]

    if verbose:
        for idx, component in enumerate(components):
            print( 'Component #%d:' % (idx) )
            print( '[%s]\n' % (','.join(map(str,sorted(component)))) )

    return components
