import networkx as nx
import matplotlib.pyplot as plt
import collections
import numpy as np


#read graph
G = nx.read_graphml('airlines.graphml')



#https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.clustering.html
#https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.centrality.html


print("Average Path Length: ", nx.average_shortest_path_length(G))

print("Average Degree Connectivity (mean k): ", nx.average_degree_connectivity(G))

#print("Average Clustering: ", nx.average_clustering(G))

print("Closeness Centrality: ", nx.closeness_centrality(G))

#TODO degree distribution histogram 






###################################################################################
#Computing degree of the nodes and the respective number of nodes that have that degree
###################################################################################

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)


degreeCount = collections.Counter(degree_sequence)

deg, cnt = zip(*degreeCount.items())


cnt = list(cnt)


#normalize cnt
total_sum = sum(cnt)
for i in range(len(cnt)):
	cnt[i] = cnt[i]/total_sum

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------





###################################################################################
#Plotting the power law in a log log scale ---- Non cummulative plot
###################################################################################

ax = plt.subplot(211)

plt.loglog(deg, cnt, 'o')


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------


###################################################################################
#Plotting the power law in a log log scale ---- Cummulative plot
###################################################################################


#build cummulative vector
cnt_cdf = []
for i in range(len(cnt)):
	cnt_cdf += [sum(cnt[0:i+1])]

ax = plt.subplot(212)

plt.loglog(deg, cnt_cdf, 'o')

plt.show()

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------











###################################################################################
#  Plot the degree distribution based on the deg and cnt lists
###################################################################################


fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.5, color='b', tick_label=[d for d in deg])

plt.title("Degree Distribution Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")

plt.show()

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------







#nx.draw(G)


plt.show()