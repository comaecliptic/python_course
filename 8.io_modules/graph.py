import networkx as nx
import matplotlib.pyplot as plt


graph = nx.Graph()

graph.add_nodes_from(['Keter', 'Binah', 'Chokhmah', "Da'at", 'Gevurah', 'Chesed',
                      'Tipheret', 'Hod', 'Netzach', 'Yesod', 'Malkuth'])

graph.add_edges_from([
    ('Keter', 'Binah'), ('Keter', 'Chokhmah'), ('Keter', 'Tipheret'),
    ('Binah', 'Chokhmah'), ('Binah', 'Gevurah'), ('Binah', 'Tipheret'),
    ('Chokhmah', 'Tipheret'), ('Chokhmah', 'Chesed'), ('Chokhmah', 'Gevurah'),
    ("Da'at", 'Binah'), ("Da'at", 'Chokhmah'), ("Da'at", 'Gevurah'),
    ("Da'at", 'Chesed'),
    ('Gevurah', 'Hod'), ('Gevurah', 'Chesed'), ('Gevurah', 'Tipheret'),
    ('Chesed', 'Tipheret'), ('Chesed', 'Netzach'),
    ('Tipheret', 'Hod'), ('Tipheret', 'Netzach'), ('Tipheret', 'Yesod'),
    ('Hod', 'Netzach'), ('Netzach', 'Yesod'), ('Yesod', 'Malkuth')
])

nx.draw(graph, with_labels=True)
plt.show()
