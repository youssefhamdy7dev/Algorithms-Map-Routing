# Algorithm-Map-Routing
Project Title: Optimizing Dijkstra’s Algorithm for Efficient Map-Based Shortest Path Computation

Problem Definition:
The objective of this project is to implement the classic Dijkstra’s shortest path algorithm and enhance its performance specifically for map-based applications. The focus is on reducing the computational overhead of each shortest path query while maintaining a balanced memory footprint.

Optimization Strategy:
In a standard implementation, Dijkstra’s algorithm explores all 𝑉 vertices, which can be computationally expensive for large-scale maps. A key optimization involves terminating the algorithm early—specifically, halting the search immediately upon discovering the shortest path to the target node. This early exit strategy significantly limits the search space, reducing the effective number of vertices (𝑉') and edges (𝐸′) explored during computation.

As a result, the runtime per query becomes proportional to 𝐸′ log 𝑉′ , rather than the full graph size. However, this approach introduces new challenges in managing state between queries. Reinitializing the distance and visited arrays to default values (e.g., ∞) in every query would still incur a time cost of 𝑂 (𝑉), which negates some of the optimization benefits.

To address this, the project implements a selective reinitialization technique. Instead of resetting the entire state, only those nodes that were modified during the previous query are updated. This results in substantial time savings for repeated queries and enhances the algorithm’s suitability for dynamic, real-time map-based applications.
