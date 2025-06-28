import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)

#  Integer, Integer, Listof Tuples, Listof Number ->  Listof Integer
# consumes a source Node, a destination Node, Connections Information,
# and  The Dijkstra Algorithm Output.
# produces a list of Nodes Indecies that takes us from src to end whith
# shortest path, by Reverse Engineering the proccess.

# 0  5
# [0, 1897.4, 2537.7, 3841.9, 3776.2, 6274.0]
#   {0: [(1, 1897.4), (3, 3841.9)],
#    1: [(0, 1897.4), (2, 640.3), (4, 1878.8)],
#   2: [(1, 640.3), (4, 2469.8), (3, 2968.2), (5, 3736.3)],
#   3: [(0, 3841.9), (2, 2968.2), (5, 2500.0)],
#  4: [(1, 1878.8), (2, 2469.8), (5, 2745.9)],
# 5: [(2, 3736.3), (3, 2500.0), (4, 2745.9)]}
# 0 1 2 5
def detect_path(src, end, graph, dijkstra, sp):
    sp.append(end)
    if src == end:
        return sp
    else:
        for prev, d in graph[end]:
            overallcost = dijkstra[end]
            if int(overallcost - d) == int(dijkstra[prev]):
                end = prev
        return  detect_path(src, end, graph, dijkstra, sp)


# NOT SOLVED

 # 57134  57184       sp = 5039.3
 # 60551  60554     sp = 2.0
# sp = []
# dijkstra_output = lazy_dijkstras(graph, 60551)
# shortest_path   = detect_path(60551, 60554, graph, dijkstra_output, sp)
# print(shortest_path)

# SOLVED
#  23741  23768    sp = 85.7
# sp = []
# dijkstra_output = lazy_dijkstras(graph, 23741)
# shortest_path   = detect_path(23741, 23768, graph, dijkstra_output, sp)
# print(shortest_path)
