import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edge(0, 1)
G.add_edge(0, 3)
G.add_edge(1, 2)
G.add_edge(1, 4)
G.add_edge(2, 4)
G.add_edge(2, 3)
G.add_edge(2, 5)
G.add_edge(3, 5)
G.add_edge(4, 5)

# explicitly set positions
pos = {0: (1000, 2400), 1: (2800, 3000), 2: (2400, 2500), 3: (4000, 0), 4: (4500, 3800), 5: (6000, 6000)}

options = {
    "node_color": "black",
    "node_size": 50*3,
    "linewidths": 0,
    "width": 0.1,
}
nx.draw_networkx(G, pos, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
