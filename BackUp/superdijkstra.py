# OUR IDEA
#  exploiting the problem geometric nature, Instead of a complete exhaustive search of the given Graph, we can tight the graph by imposing boundries contains the source , the destination and their connections, swap away the away all other Vertices.
# It is guaranteed because of Weights(distances) is real, work with respect to Mathmatics Calculations and Rules.
from utilities import *
# ===========================
# ===========================
# ===========================
# # READING MAP FILES: SWITCH HERE:
# filename = 'USACase\Map.txt'
filename = 'SampleCase\Map.txt'
# ===========================
# ===========================
nodes = [ ]
connections = [ ]
lines = read_txt_file(filename)
v, e =  lines[0]
for i in range(1, v+1):
    nodecoord = lines[i]
    nodes.append((nodecoord[1], nodecoord[2]))
for i  in  range(v+1, (v+1)+e):
    conninfo = lines[i]
    connections.append((conninfo[0], conninfo[1]))
# =======================================
# CONSTRUCT THE GRAPH
# =======================================
Graph = {}
for i in range(v):
    Graph[i] = []

for A, B in connections:
    weigth = euclidean_distance(nodes[A], nodes[B])
    Graph[A].append( (B, weigth))
    Graph[B].append((A, weigth))
print(Graph)

# # ================================
# # ================================
# { 0: [(1, 1897.4), (3, 3841.9)],
#   1: [(0, 1897.4), (2, 640.3), (4, 1878.8)],
#  2: [(1, 640.3), (4, 2469.8), (3, 2968.2), (5, 3736.3)],
#  3: [(0, 3841.9), (2, 2968.2), (5, 2500.0)],
#  4: [(1, 1878.8), (2, 2469.8), (5, 2745.9)],
#  5: [(2, 3736.3), (3, 2500.0), (4, 2745.9)]}

def tight_Graph(vertices, src, end):
    x1, y1 = vertices[src]
    x2, y2 = vertices[end]
    filtered_vertices = []
    for x, y in vertices:
        if  ( x >= min(x1, x2) and  x <= max(x1, x2) ) and ( y >= min(y1, y2) and  y <= max(y1, y2) ):
            filtered_vertices.append((x, y))
    return filtered_vertices


src  = 0
end = 2
# tighted_graph = tight_Graph(nodes, src, end)
# print(tighted_graph)
# # # ================================
# # ================================
# =======================================
# =======================================
# DIJKSTRA IMPLEMENTATION: The Optimized One.
# USING: Heap and Priorty Q
# Avoiding: Re_Initialization according to Idea 1.
# =======================================
# =======================================
def  re_init_dist(dist, n):
    i = 0
    while dist[i] != Inf :
        dist[i] = Inf
        i += 1
        if i >= n :
            break
    return dist
def  clear_visited(visited, n):
    i = 0
    while visited[i] != False :
        visited[i] = False
        i += 1
        if i >= n :
            break
    return visited

def  optimized_dijkstras (Graph,  root, paths, distances, visitedVs, n):
    #
    dist              =  re_init_dist(distances, n)
    dist[root]     = 0
    visited         = clear_visited(visitedVs, n)
    paths[root]  = [root]
    pq               = [(0, root)]
    while len(pq) > 0:
        _ ,  u  =  heapq.heappop(pq)
        if visited[u]: continue
        visited[u] = True
        for v, l in Graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = round(dist[u] + l, 1)
                paths[v] = paths[u] + [v]
                heapq.heappush(pq, (dist[v], v))
    return dist, paths
# # # ================================
# # ================================
# # ================================
# # ================================
# READ INPUT FILES: QUERIES: Switch Here:
filename = 'SampleCase\Routes.txt'
# filename = 'USACase\ShortRoutes100.txt'
# # ================================
# # ================================
routes_lines = read_txt_file(filename)
# =================================
# # ================================
# WRITE OUTPUT FILES:  Switch Here:
output_filename = 'Output\samplecaseOut.txt'
# output_filename = 'Output/usacaseOut.txt'
# # ================================
# # ==========================================
# outputFileHandler = open(output_filename, 'w')
# queries = routes_lines[1:]
# n     = len(Graph)
# dist = [Inf]*n
# visited = [False]*n
start_time = time.time()                       ##  START time
#
# paths = {}
# for i in range(n):
#     paths[i] = []
# for src, end in queries:
#
#     focusedGraph = tight_Graph(Graph, src, end)
#     dijkstra_output, routes  = optimized_dijkstras(focusedGraph, src, paths, dist, visited, n)
#     shortest_path = routes[end]
#     for i in range(len(shortest_path)):
#         outputFileHandler.write(str(shortest_path[i])+'  ')
#     outputFileHandler.write('\n')
#     outputFileHandler.write(str(dijkstra_output[end]))
#     outputFileHandler.write('\n')
# outputFileHandler.close()
print("--- %s seconds ---" % (time.time() - start_time))    ## END time
# ===
