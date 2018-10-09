import networkx as nx
import matplotlib.pyplot as plt
import collections
import numpy as np


# Read the graph
G = nx.read_graphml('airlines.graphml')

plt.figure(3,figsize=(30, 30)) 


pos = nx.spring_layout(G, scale=1)
colors = range(G.number_of_edges())
node_colors = range(G.number_of_nodes())
nx.draw(G, pos, node_color=node_colors, edge_color=colors,
        width=4, edge_cmap=plt.cm.Blues, with_labels=False)
plt.savefig('network_drawings/spring_uniform.png')
plt.show()


####################################################################################
#    PUT NEXT BLOCK ON SEPARATED CELL
####################################################################################


plt.figure(3,figsize=(30, 30)) 

d = nx.degree(G)
d = dict(d)


pos = nx.spring_layout(G, scale=1)
edge_colors = range(G.number_of_edges())
node_colors = range(G.number_of_nodes())
nx.draw(G, pos, node_color=node_colors, edge_color=edge_colors,
        width=4, edge_cmap=plt.cm.Blues, with_labels=False, node_size=[v * 100 for v in d.values()])
plt.savefig('network_drawings/spring_degree.png')
plt.show()


"""

####################################################################################
#    PUT NEXT BLOCK ON SEPARATED CELL
####################################################################################




plt.figure(3,figsize=(30, 30)) 


d = nx.degree(G)

node_info = nx.get_node_attributes(G, 'tooltip')

colors = []
for u, v in d:
    if(node_info[u][0:3] == 'ATL'):
        colors += 'w'
    else:
        colors += 'k'

d = dict(d)

nx.draw(G, nodelist=d.keys(), node_color=colors, node_size=[v * 100 for v in d.values()], edge_color=edge_colors,
        width=4, edge_cmap=plt.cm.Blues)
plt.show()
#https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.clustering.html
#https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.centrality.html
"""
