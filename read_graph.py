import networkx as nx
import matplotlib.pyplot as plt



#read graph
G = nx.read_graphml('airlines.graphml')



print("Average Path Length: ", nx.average_shortest_path_length(G))


print(G['1'])
nx.draw(G)


plt.show()