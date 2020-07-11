# LACC 2020
# Graph Theory easy exercises for Social Networks module

import numpy as np

#*************************************
# This is where you write your code
#
# matrix_load()
#
# Loads an adjacency matrix for a graph from a file
#
# Input:  none
# Output: matrix containing each node 
# 
# Notes: 
#   1. You can open a file using 'with open(filename) as f:'
# 
#   2. You can get a list containing each line with f.readlines()
#
# Hints:
#   1. To remove the annoying '\n', check out the function 'strip()'
#
#   2. How do you turn a string into a list of characters?
#       e.g. '00100' to [ '0', '0', '1', '0', '0' ]
#
#   3. How do you turn a list of characters into a list of integers?
#       e.g. [ '0', '0', '1', '0', '0' ] to [ 0, 0, 1, 0, 0 ]
#
#   4. Check out 'append()' to make 2D lists
#
#*************************************
def matrix_load(filename):
    
    mat = []

    with open( filename ) as f:
        data = f.readlines()

    for row in data:
        mat.append( [int(c) for c in row.strip()] )

    return mat
	
#*************************************
# This is where you write your code
#
# print_degrees(mat)
#
# Prints the degrees of all nodes in a graph given an adj. matrix 
#
# Input:  the adjacency matrix of the graph
# Output: none
# 
# Print format:
#   Degree of Node x : y
#
# Note: 
#   1. You don't need to return anything. 
#
#   2. Effectively, you'll need to count the number of 1s in each row (or col)
#
#
# Hints:
#   1. Remember how to use for loops with range. What should be the range?
#
#   2. Check out the in-built function 'sum()'
#
#   3. Check out 'format()' or the '%' symbol for fancy printing
#
#*************************************

def print_degrees(mat):

    for i in range(len(mat)):
        print( 'Degree of Node %d: %d' % (i, sum(mat[i])) )
        
	
#*************************************
# This is where you write your code
#
# shortest_path(mat,node1,node2)
#
# Find the shortest path from node1 to node2 in a graph given an adj. matrix 
#
# Input:  the adjacency matrix of the graph,node1,node2
# Output: 'The path is: ' appended with all edges on the path if there is one, otherwise print out 'No such path'
#
#
# Note: 
#   1. Also return a list containing all the nodes on the path.
#      If no path exists, return an empty list
#
#   2. Remember to print the path from node1 to node2
#
#   3. If verbose = True, prints output
#
# Hints:
#   1. No idea how to start? Check out the intuitive animation on wiki:
#       https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm
#       https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode
#
#   2. Already know this? Are there any other ways to do this? 
#      Is it recursive or iterative? Can you modify it into the other?
#
#*************************************

def shortest_path(mat, node1, node2, verbose=True):

    path = []
    N = len(mat)

    mat = np.array(mat)     # Change to numpy array for its functions

    queue   = [ node1 ]     # Use a list for the queue
    parents = [ -2 ] * N    # Initialize all node's parents to be -2

    parents[node1] = -1     # Use -1 to symbolize the root node

    foundPath = False

    while len(queue) != 0 and foundPath == False:

        current_node = queue.pop(0)
        neighbors = np.nonzero( mat[current_node] )[0]
        
        for n in neighbors:
            if parents[n] == -2:   # If n's parent is -1, then it has not been traversed
                queue.append(n)
                parents[n] = current_node
    
            if n == node2:         # If n is node2, we found the path
                foundPath = True
                current_node = node2
                while current_node != node1:
                    parent = parents[current_node]
                    path.append( (parent, current_node) )
                    current_node = parent

                path.reverse()          # Reverse the path 
                break

    if verbose:
        if foundPath:                   # Backtrack the path if found
            print('The path is: ')
            for edge in path:
                print( edge )

        else:
            print('No such path')

    return path
	

#*************************************
# This is where you write your code
#
# detect_cycle(mat)
#
# Detect the cycle in a graph given an adj. matrix 
#
# Input:  the adjacency matrix of the graph
# Output: 'Found a cycle consisting of the following edges: ' appended with the edges on the cycle, otherwise print out 'No cycle in the graph'
# 
# Note: 
#   1. Also return a list containing all the nodes on the cycle.
#      If no cycle exists, return an empty list
#
#   2. If vebose = True, prints output
#
# Hints:
#   1. In this exercise, it is assumed that the graphs are connected
#
#   2. Check out this:
#       https://www.me.utexas.edu/~bard/IP/Handouts/cycles.pdf
#
#   3. Recursive? Iterative? Try out both
#*************************************

def detect_cycle(mat, verbose=True):

    root = 0        # Graphs are connected: Use arbitrary starting node
    cycle = []

    N = len(mat)
    visited = [0]*N
    parents = [-2]*N

    
    stack = [ (root, -1) ]

    while len(stack) != 0 and len(cycle) == 0:

        node,parent = stack.pop()
        visited[node] = 1
        parents[node] = parents

        for n in np.nonzero( mat[node] )[0]:

            if visited[n] == 0:
                stack.append( (n,node) )

            elif parent != n:
                mat[n][node] = mat[node][n] = 0
                cycle.append( (node,n) )
                cycle.extend( shortest_path( mat, node, n, verbose=False ) )
                mat[n][node] = mat[node][n] = 1

                break

    if verbose:
        if len(cycle) == 0:
            print('No cycle in the graph')

        else:
            print('Found a cycle consisting of the following edges:')
            for edge in cycle:
                print(edge)

    return cycle



def detect_cycle_recursive(mat, verbose=True):

    root = 0        # Graphs are connected: Use arbitrary starting node
    cycle = []

    N = len(mat)
    visited = [0] * N

    back_edge = dfs(mat, root, visited, -1)

    if len(back_edge) != 0:

        n1, n2 = back_edge

        mat[n1][n2] = mat[n2][n1] = 0
        cycle.append( back_edge )
        cycle.extend( shortest_path(mat, n1, n2, verbose=False) )
        mat[n1][n2] = mat[n2][n1] = 1

    if verbose:
        if len(back_edge) == 0:
            print('No cycle in the graph')

        else:
            print('Found a cycle consisting of the following edges:')
            for edge in cycle:
                print(edge)

    return cycle

def dfs(mat, node, visited, parent):

    back_edge = []
    visited[node] = 1

    for n in np.nonzero(mat[node])[0]:
        if visited[n] == 0:
            back_edge = dfs(mat, n, visited, node)
         
        elif parent != n:
            back_edge = (n, node)


    return back_edge












