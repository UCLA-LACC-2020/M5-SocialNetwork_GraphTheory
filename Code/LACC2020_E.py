
# Graph Theory easy exercises for Social Networks module
# LACC 2020

import numpy as np

#*************************************
# This is where you write your code
#
# matrix_load()
#
# Loads an adjacency matrix for a graph from a file
#
# input: none
# output: matrix containing each node 
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
	
    return mat

#*************************************
# This is where you write your code
#
# print_degrees(mat)
#
# Prints the degrees of all nodes in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph
# output: none
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
        
	
#*************************************
# This is where you write your code
#
# shortest_path(mat,node1,node2)
#
# Find the shortest path from node1 to node2 in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph,node1,node2
# output: 'The path is: ' appended with all edges on the path if there is one, otherwise print out 'No such path'
#
#
# Note: 
#   1. Also return a list containing all the nodes on the path.
#      If no path exists, return an empty list
#
#   2. Remember to print the path from node1 to node2
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

def shortest_path(mat, node1, node2):

    return path
	

#*************************************
# This is where you write your code
#
# detect_cycle(mat)
#
# Detect the cycle in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph
# output: 'Found a cycle consisting of the following edges: ' appended with the edges on the cycle, otherwise print out 'No cycle in the graph'
# 
# Note: 
#   1. Also return a list containing all the nodes on the cycle.
#      If no cycle exists, return an empty list
#
# Hints:
#   1. In this exercise, it is assumed that the graphs are connected
#
#   2. Check out this:
#       https://www.me.utexas.edu/~bard/IP/Handouts/cycles.pdf
#
#   3. Can you use 'shortest_path()' to help get the cycle?
#
#   4. Recursive? Iterative?
#*************************************


def detect_cycle(mat):

    return cycle
                    


