import networkx as nx
import matplotlib.pyplot as plt
import collections
import numpy as np


# Reat the graph
G = nx.read_graphml('airlines.graphml')

# https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.clustering.html
# https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.centrality.html

# How big the medium trip is
print("Average Path Length: ", nx.average_shortest_path_length(G))

# How popular are the airports that connect to the popular/unpopular airports
print("Average Degree Connectivity (mean k): ", nx.average_degree_connectivity(G))

# Average times that airports B<->C given that A<->C and A<->B
# print("Average Clustering: ", nx.average_clustering(G))

# Gives us how close each airport is to the others. Can compute the airport closest to every other in the world
print("Closeness Centrality: ", nx.closeness_centrality(G))

# The node that appears more times in the shortest paths between two other nodes
print("Closeness Centrality: ", nx.betweenness_centrality(G))

#TODO degree distribution histogram



###################################################################################
#Computing degree of the nodes and the respective number of nodes that have that degree
###################################################################################

# Get list with degrees of each node
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)

print("###################################################################################")

# Dic with how much time each degree appeared
degreeCount = collections.Counter(degree_sequence)

# Separate dic into two separated tuples
deg, cnt = zip(*degreeCount.items())
cnt = list(cnt)


# Normalize cnt getting %
total_sum = sum(cnt)
for i in range(len(cnt)):
	cnt[i] = cnt[i]/total_sum


###################################################################################
# Plotting the power law in a log log scale ---- Non cummulative plot
###################################################################################

ax = plt.subplot(211)

plt.loglog(deg, cnt, 'o')

plt.title("Degree Distribution (log/log)")
plt.ylabel("log₁₀ P(k)")
plt.xlabel("log₁₀ k")

plt.show()


###################################################################################
# Plotting the power law in a log log scale ---- Cummulative plot
###################################################################################


# Build cummulative vector
cnt_cdf = []
for i in range(len(cnt)):
	cnt_cdf += [sum(cnt[0:i+1])]

ax = plt.subplot(212)

plt.loglog(deg, cnt_cdf, 'o')

plt.title("Cumulative Degree Distribution (log/log)")
plt.ylabel("log₁₀ P_cum(k)")
plt.xlabel("log₁₀ k")

plt.show()

###################################################################################
#  Plot the degree distribution based on the deg and cnt lists
###################################################################################


fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.5, color='b', tick_label=[d for d in deg])

plt.title("Degree Distribution")
plt.ylabel("Probability P(k)")
plt.xlabel("Degree k")

plt.show()
