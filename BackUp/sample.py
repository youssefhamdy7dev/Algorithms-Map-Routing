from utilities import *
# ===========================
# ===========================
# ===========================
# # READING MAP FILES: SWITCH HERE:
filename = 'USACase\Map.txt'
# filename = 'SampleCase\Map.txt'
# ===========================
# ===========================
nodes = [ ]
connections = [ ]
lines = read_txt_file(filename)
v, e =  lines[0]
for i in range(1, v+1):
    nodeinfo = lines[i]
    nodes.append((nodeinfo[1], nodeinfo[2]))
for i  in  range(v+1, (v+1)+e):
    conninfo = lines[i]
    connections.append((conninfo[0], conninfo[1]))
# =======================================
# CONSTRUCT THE GRAPH
# =======================================
graph = {}
for i in range(v):
    graph[i] = []

for A, B in connections:
    weigth = euclidean_distance(nodes[A], nodes[B])
    graph[A].append((B, weigth))
    graph[B].append((A, weigth))
# print(graph)
# =======================================
# =======================================
# DIJKSTRA IMPLEMENTATION: The Optimized One.
# USING: Heap and Priorty Q
# Avoiding: Re_Initialization according to Idea 1.
# =======================================
# =======================================
def  optimized_dijkstras (graph,  root, paths, distances, visitedVs, n):
    dist              =  re_init_dist(distances, n)
    dist[root]     = 0
    visited         = clear_visited(visitedVs, n)
    paths[root]  = [root]
    pq               = [(0, root)]
    while pq:
        _ ,  u  =  heapq.heappop(pq)
        if visited[u]: continue
        visited[u] = True
        for v, l in graph[u]:
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
# filename = 'SampleCase\Routes.txt'
filename = 'USACase\LongRoutes100.txt'
# # ================================
# # ================================
routes_lines = read_txt_file(filename)
# =================================
# # ================================
# WRITE OUTPUT FILES:  Switch Here:
# output_filename = 'sampleout.txt'
output_filename = 'usaout.txt'
# # ================================
# # ==========================================
outputFileHandler = open(output_filename, 'w')
queries = routes_lines[1:]
n     = len(graph)
dist = [Inf]*n
visited = [False]*n
start_time = time.time()                       ##  START time
for query in queries:
    src  = query[0]
    end =  query[1]
    dijkstra_output, routes  = optimized_dijkstras(graph, src, {}, dist, visited, n)
    print(routes[src])
    # print(routes[end])
    print(routes.get(end, [None]))
    shortest_path = routes.get(end,  [None])




    for i in range(len(shortest_path)):
        outputFileHandler.write(str(shortest_path[i])+'  ')
    outputFileHandler.write('\n')
    outputFileHandler.write(str(dijkstra_output[end]))
    outputFileHandler.write('\n')
outputFileHandler.close()
print("--- %s miliseconds ---" % ( (time.time() - start_time) * 10 ) )    ## END time
# ===
