from utilities import *
# =========================================
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
    coninfo = lines[i]
    connections.append((coninfo[0], coninfo[1]))
# =======================================
# CONSTRUCT THE GRAPH
# =======================================
graph = {}
for i in range(v):
    graph[i] = []

for A, B in connections:
    weigth = euclidean_distance(nodes[A], nodes[B])
    graph[A].append( (B, weigth))
    graph[B].append((A, weigth))
# print(graph)
# =======================================
# =======================================
# DIJKSTRA IMPLEMENTATION: The Lazy One
# USING: Heap and Priorty Q
# =======================================
# =======================================
def optimized_dijkstras(graph, root,  end, paths, dist, visited, n):
    distchanges      = [] # keep what nodes we update its value during the algorithm
    visitedchanges = [] # keep what nodes we update its value during the algorithm
    dist[root] = 0
    paths[root] = [root]
    pq = [(0, root)]
    while  pq:
        _ , u = heapq.heappop(pq)
        if visited[u]: continue
        visited[u] = True
        visitedchanges.append(u)
        if  dist[end] != Inf and visited[end]  and paths[end]:
            break
        for  v, l  in  graph[u]:
            if  dist[u] + l  <  dist[v]:
                dist[v] = round(dist[u] + l, 1)
                distchanges.append(v)
                paths[v] = paths[u] + [v]
                heapq.heappush(pq, (dist[v], v))

    return dist, visited, paths, distchanges, visitedchanges
# # ================================
# # ================================
# CALLING DIJKSTRA
# # ================================
# # ================================
# READ INPUT FILES: QUERIES: Switch Here:
# filename = 'SampleCase\Routes.txt'
filename = 'USACase\ShortRoutes100.txt'
# filename = 'USACase\LongRoutes100.txt'
# # ================================
# # ================================
routes_lines = read_txt_file(filename)
# # ================================
# # ================================
# WRITE OUTPUT FILES:  Switch Here:
output_filename = 'sampleout.txt'
# output_filename = 'usaout.txt'
# # ================================
# # ================================
outputFileHandler = open(output_filename, 'w')
queries = routes_lines[1:]
n     = len(graph)
dist = [Inf]*n
visited = [False]*n
start_time = time.time()                       ##  START time
queryIndex = 0
for query in queries:
    src = query[0]
    end = query[1]
    dijkstra, populatedvisited,  routes, distchanges, visitedchanges = optimized_dijkstras(graph, src, end, {}, dist, visited, n)
    shortest_path = routes.get(end, [None])
    for i in range(len(shortest_path)):
        outputFileHandler.write(str(shortest_path[i])+'  ')
    outputFileHandler.write('\n')
    outputFileHandler.write(str(dijkstra[end]))
    outputFileHandler.write('\n')
    dist      = dijkstraToOrigin(dijkstra,  distchanges)
    visited = visitedToOrigin(populatedvisited, visitedchanges)
    queryIndex += 1
    print('query  ', queryIndex , 'ended. ')
outputFileHandler.close()
print("--- %s miliseconds ---" % ( (time.time() - start_time) *10 ))    ## END time
