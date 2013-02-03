import matplotlib
matplotlib.use('Agg')
import networkx as nx
import matplotlib.pyplot as plt

G=nx.path_graph(8)
nx.draw(G)
plt.savefig("simple_path.png") # save as png


