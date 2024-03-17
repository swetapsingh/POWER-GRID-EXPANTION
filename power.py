class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

def power_grid_expansion(G, max_length):
    # Create a mapping of vertex names to integer indices
    vertex_map = {}
    for u, v, _ in G:
        if u not in vertex_map:
            vertex_map[u] = len(vertex_map)
        if v not in vertex_map:
            vertex_map[v] = len(vertex_map)
    
    # Initialize empty list for MST edges
    MST_edges = []
    
    # Sort edges by cost
    G.sort(key=lambda x: x[2])
    
    # Initialize disjoint set
    uf = UnionFind(len(vertex_map))
    
    # Iterate through edges
    for u, v, weight in G:
        # Get integer indices of vertices
        u_idx, v_idx = vertex_map[u], vertex_map[v]
        # Check if edge satisfies environmental constraints
        if weight <= max_length:
            # Find parent nodes in disjoint set
            pu, pv = uf.find(u_idx), uf.find(v_idx)
            # If not in the same connected component
            if pu != pv:
                # Add edge to MST
                MST_edges.append((u, v))
                # Merge connected components
                uf.union(pu, pv)
    
    # Return MST edges
    return MST_edges

# Example usage:
graph = [('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 4), ('B', 'D', 5), ('C', 'D', 6), ('C', 'E', 1), ('D', 'E', 3)]
max_length = 4  # Maximum allowed length for transmission lines in environmentally sensitive areas

min_spanning_tree = power_grid_expansion(graph, max_length)
print("Minimum Spanning Tree (Edges):", min_spanning_tree)
