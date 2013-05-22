import matplotlib
matplotlib.use('Agg')
import networkx as nx
import matplotlib.pyplot as plt

G=nx.path_graph(8)
nx.draw(G)
plt.savefig("simple_path.png") # save as png

plt.clf()

G = nx.Graph()

G.add_edge('a','b')
G.add_edge('a','c')
G.add_edge('c','d')
G.add_edge('c','e')
G.add_edge('c','f')
G.add_edge('a','d')

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)

plt.savefig("simple_path.png") # save as png

plt.clf()

G.add_edge('e','f')
G.add_edge('e','g')
G.add_edge('e','h')

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)

plt.savefig("simple_path.png") # save as png

# plt.clf()

G.add_edge('f','f')
G.add_edge('f','h')

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.savefig("simple_path.png") # save as png
