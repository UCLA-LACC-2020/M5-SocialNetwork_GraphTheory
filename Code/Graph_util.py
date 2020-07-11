import math
import numpy as np  # NumPy
import matplotlib.pyplot as plt  # For plotting graphs
from Connect import find_components

# graph_gen(N, p, d)
#   Generates a graph of N nodes with edge probability p and distance threshold d
#   The nodes have coordinates within [0,1]
#
#   Inputs:  graph size N, edge probability p, distance threshold d
#   Outputs: x_coords, y_coords, adjacency matrix mat

def graph_gen(N, p, d, seed):

    np.random.seed(seed)

    # Generates N number of random x and y coordinates that are within [0,1] 
    x_coords = np.random.uniform(0, 1, N)   
    y_coords = np.random.uniform(0, 1, N)

    # Pairs the x_coords and y_coords together
    nodes = np.array( list(zip(x_coords, y_coords)) )
    
    # Initialize the adjacency matrix (size is NxN)
    mat = np.zeros( (N,N) )

    # For every two nodes: 
    #   if distance < d, then there is a chance p of generating an edge
    for i in range(N):
        for j in range(i+1,N):
            if np.linalg.norm( nodes[i]-nodes[j] ) < d and np.random.uniform(0,1,1)[0] < p:
                mat[i][j] = 1
                mat[j][i] = 1

    return x_coords, y_coords, mat



# cluster_graph(mat, seed)
#   Generates a graph using the adjacency matrix mat such that nodes in the same
#   connected components are close together
#   By graph theory:
#       random graphs often have large connected components rather than uniform ones
#
#   Inputs:  adjacency matrix mat
#   Outputs: x_coords, y_coords, adjacency matrix mat

def cluster_graph(mat, seed):

    np.random.seed(seed)

    components = find_components(mat, verbose=False)

    N = len(mat)                        # number of nodes
    numComp = len(components)           # number of components
    m = math.ceil(math.sqrt(numComp))   # number of separations for clustering 
    
    x_coords = np.zeros(N)
    y_coords = np.zeros(N)
    

    for k in range(m):                  # separation on x axis
        for r in range(m):              # separation on y axis
            ind = k*m + r
            if ind < numComp:
                for node in components[ind]:
                    x_coords[node] = np.random.uniform( k, k+1, 1 )[0]
                    y_coords[node] = np.random.uniform( r, r+1, 1 )[0]

    
    plot_graph(x_coords, y_coords, mat, annotate=False)

    return x_coords, y_coords, mat



# plot_graph(x_coords, y_coords, mat, annotate)
#   Plots the graph
#   If annotate is True, adds labels to each node
#
#   Inputs:  x coordinates x_coords, y coordinates y_coords, adjacency matrix mat
#   Outputs: N/A

def plot_graph(x_coords, y_coords, mat, annotate=True):

    N = len(x_coords)
    
    # Plot the nodes first
    plt.scatter(x_coords, y_coords, label='nodes', color='green', marker='*', s=30, zorder=2 )

    if annotate:
        for n in range(N):
            plt.annotate( str(n), xy=(x_coords[n], y_coords[n]), xytext=(x_coords[n]+0.01, y_coords[n]+0.01),fontsize=12 )

    # Draw edges
    for i in range(N):
        for j in range(i+1,N):
            if mat[i][j] == 1:
                plt.plot( [x_coords[i], x_coords[j]], [y_coords[i], y_coords[j]], color='grey', zorder=1 )




# plot_path(x_coords, y_coords, path):
#   Plots the path 
#
#   Inputs:  x coordinates x_coords, y coordinates y_coords, path path
#   Outputs: N/A

def plot_path(x_coords, y_coords, path):
    
    root = path[0][0]
    dest = path[-1][1]

    for node1, node2 in path:
        plt.plot( [x_coords[node1], x_coords[node2]], [y_coords[node1], y_coords[node2]], color='red', zorder=2 )
        
    plt.scatter( x_coords[root], y_coords[root], label='nodes', color='blue', marker='o', s=30, zorder=3 )
    plt.scatter( x_coords[dest], y_coords[dest], label='nodes', color='blue', marker='o', s=30, zorder=3 )



# plot_cycle(x_coords, y_coords, cycle):
#   Plots the cycle
#
#   Inputs:  x coordinates x_coords, y coordinates y_coords, cycle path cycle
#   Outputs: N/A

def plot_cycle(x_coords, y_coords, cycle):
    
    for node1, node2 in cycle:
        plt.plot( [x_coords[node1], x_coords[node2]], [y_coords[node1], y_coords[node2]], color='blue' )
