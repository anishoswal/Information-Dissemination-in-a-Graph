#!/usr/bin/env python
import numpy as np
import pandas as pd

import scipy
from scipy.io import mmread
from scipy.sparse.linalg import eigs
from scipy.sparse import lil_matrix
import copy
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import *


# karate dataset to adjacency matrix
adj_mat = scipy.io.mmread('../data/soc-karate/soc-karate.mtx')

# netshield computes and returns k nodes that can be removed to reduce information dissemination
def netshield(adj_mat, k):
    n = adj_mat.shape
    n = n[0]
    B = []

    csr = adj_mat.tocsr()
    eig_val, eig_vecs  = eigs(adj_mat, k=1)
    u = eig_vecs
    csr = adj_mat.tocsr()
    diag = []
    for j in range(0,n):
        row = csr[j,:]
        row = row.A
        diag.append(row[0][j])


    v=[]
    for j in range(0,n):
        value = (2*eig_val - diag[j]) * (eig_vecs[j])**2
        v.append(value)

    B_list=[]
    S = set()
    max = -1
    index = -1
    EV = []
    A = csr
    b = np.zeros((n, 1))

    S.add(index)
    col = A[:, j]
    col = col.A
    col = col.ravel()
    B_list.append(col)
    B = np.asarray(B_list)


    for i in range(0, k):
        b = B * u[i]
        max = -1
        for j in range(0, n):
            score = v[j] - 2 * b[0][j] * u[j]
            if(j in S):
                score = -1
            if (score > max):
                max = copy.deepcopy(score)
                index = j

        S.add(index)
        col = A[:, j]
        col = col.A
        col = col.ravel()
        B_list.append(col)
        B = np.asarray(B_list)

    S.remove(-1)    
    return S


# To remove the set of S nodes from graph G
def remove_nodes(G, S):
    for node in S:
        if G.has_node(node):
            G.remove_node(node)
    
def remove_nodes_char(G, S, node_map):
    for node in S:
        if G.has_node(node_map[node]):
            G.remove_node(node_map[node])


# Plot the resulting graph
def plot_graph(x, subtitle):
    fig = plt.figure()
    fig.suptitle(subtitle, fontsize=20)
    nx.draw_networkx(x)
    plt.savefig(subtitle+".png")


S = netshield(adj_mat, 4)

G = nx.from_scipy_sparse_matrix(adj_mat)
G = G.to_directed()


# Plots the before and after removing k nodes
plot_graph(G, 'Before')
remove_nodes(G, S)
plot_graph(G, 'After')


def get_nodes_mapping(nodes_list):
    node_dict = {}
    counter = 0
    for node in nodes_list:
        node_dict[counter] = node
        counter = counter + 1
    return node_dict



# An example graph to better visualize the netshield algorithm
nodes = ['a','b','c','d','p','q','r','s','t','m','n','o','w','x','y','z']
node_map = get_nodes_mapping(nodes)
edges = [('a','b'), ('b','c'), ('a','c'), ('c','d'), ('w','x'), ('x','y'), ('w','y'), ('x','z'), ('y','z'), ('p','q'), ('q','r'), ('r','s'), ('s','t'), ('q','t'), ('q','s'), ('t','r'), ('s','p'), ('m','n'), ('n','o'), ('o','m'), ('d','w'), ('c','q'), ('q','m'), ('d','q'), ('s','o'), ('y','q'), ('w','a'), ('b','n')]

G1 = nx.DiGraph()
G1.add_nodes_from(nodes)
G1.add_edges_from(edges)
G1_undirected = G1.to_undirected()
adj = nx.to_scipy_sparse_matrix(G1)
adj = adj.astype(float)
adj = adj.tocoo()
S1 = netshield(adj, 3)

# Plot of before and after for the example graph
plot_graph(G1_undirected, 'Before')
print(G1_undirected.nodes)
remove_nodes_char(G1_undirected, S1, node_map)
plot_graph(G1_undirected, 'After')

# computes the max-flow for given graph
def max_flow(G):
    degrees = G.degree(G)
    nodes = G.nodes()
    for e in G.edges():
        G[e[0]][e[1]]['capacity'] =  max(degrees[e[0]], degrees[e[1]])

    length = len(nodes)
    maximum = 0  
    for i in range(length): 
        for j in range(length):
            if(i!=j):
                maximum = max(maximum, nx.maximum_flow(G,nodes[i],nodes[j],capacity ='capacity' )[0])

    print(maximum)




# to compute strongly connected components for the example graph
n = 16
strong_score_map = {}
for k in range(1, n):
    
    nodes = ['a','b','c','d','p','q','r','s','t','m','n','o','w','x','y','z']
    edges = [('a','b'), ('b','c'), ('a','c'), ('c','d'), ('w','x'), ('x','y'), ('w','y'), ('x','z'), ('y','z'), ('p','q'), ('q','r'), ('r','s'), ('s','t'), ('q','t'), ('q','s'), ('t','r'), ('s','p'), ('m','n'), ('n','o'), ('o','m'), ('d','w'), ('c','q'), ('q','m'), ('d','q'), ('s','o'), ('y','q'), ('w','a'), ('b','n')]
    
    G1 = nx.DiGraph()
    G1.add_nodes_from(nodes)
    G1.add_edges_from(edges)
    G1_undirected = G1.to_undirected()

    adj = nx.to_scipy_sparse_matrix(G1)
    adj = adj.astype(float)
    adj = adj.tocoo()
    
    S = netshield(adj, k)

    remove_nodes_char(G1, S, node_map)
    strong_score = number_strongly_connected_components(G1)
    strong_score_map[k] = strong_score
    
print(strong_score_map)

# to compute strongly connected components for the karate dataset
n = 34
strong_score_map = {}
for k in range(1, n):
    
    S = netshield(adj_mat, k)
    remove_nodes(G, S)
    print(G.nodes)
    strong_score = number_strongly_connected_components(G)
    strong_score_map[k] = strong_score
    
print(strong_score_map)

