# POWER-GRID-EXPANTION
Kruskal's Approach to Power Grid Expansion


PSEUDOCODE -

PowerGridExpansion(G, max_length):
    // G: The graph representing the power grid
    // max_length: Maximum allowed length for transmission lines in environmentally sensitive areas
    
    // Initialize an empty list to store the edges of the minimum spanning tree
    MST_edges = []
    
    // Initialize a disjoint set data structure to keep track of connected components
    DisjointSet = InitializeDisjointSet()
    
    // Sort all the edges of the graph in non-decreasing order of their weights
    SortEdgesByWeight(G.edges)
    
    // Loop through all the edges in the sorted order
    for each edge (u, v) in G.edges:
        // Get the parent nodes of u and v in the disjoint set
        parent_u = Find(DisjointSet, u)
        parent_v = Find(DisjointSet, v)
        
        // If adding this edge doesn't create a cycle in the minimum spanning tree
        if parent_u != parent_v:
            // Check if the length of the edge is within the maximum allowed length
            if edge_length(u, v) <= max_length:
                // Add this edge to the minimum spanning tree
                MST_edges.append((u, v))
                
                // Union the two sets to merge them into one connected component
                Union(DisjointSet, parent_u, parent_v)
    
    return MST_edges

// Helper function to calculate the length of an edge
edge_length(u, v):
    // Calculate the Euclidean distance between the coordinates of nodes u and v
    return sqrt((u.x - v.x)^2 + (u.y - v.y)^2)

// Helper function to initialize disjoint set data structure
InitializeDisjointSet():
    // Create a disjoint set with each node as its own parent
    return DisjointSet

// Helper function to find the parent of a node in the disjoint set
Find(DisjointSet, node):
    // If the node is its own parent, return the node
    if DisjointSet[node] == node:
        return node
    
    // Otherwise, recursively find the parent of the parent node
    return Find(DisjointSet, DisjointSet[node])

// Helper function to merge two sets in the disjoint set data structure
Union(DisjointSet, x, y):
    // Find the parents of the two sets
    parent_x = Find(DisjointSet, x)
    parent_y = Find(DisjointSet, y)
    
    // Set the parent of one set to be the other set's parent
    DisjointSet[parent_x] = parent_y
