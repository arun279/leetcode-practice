class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None 
        visited = {}
        return self.dfs(node, visited)
    
    def dfs(self, node, visited):
        if node in visited:
            return visited[node]
        
        new_node = Node(val=node.val, neighbors=[])
        visited[node] = new_node
        for neighbor in node.neighbors:
            new_neighbor = self.dfs(neighbor)
            new_node.neighbors.append(new_neighbor)
        return new_node

# Test cases

# Example 1
adjList = [[2,4],[1,3],[2,4],[1,3]]
nodes = [Node(i+1, []) for i in range(len(adjList))]
for i, neighbors in enumerate(adjList):
    for j in neighbors:
        nodes[i].neighbors.append(nodes[j-1])

result = Solution().cloneGraph(nodes[0])
print([[n.val for n in node.neighbors] for node in result]) # Output: [[2, 4], [1, 3], [2, 4], [1, 3]]

# Example 2
adjList = [[]]
nodes = [Node(1, [])]

result = Solution().cloneGraph(nodes[0])
print([[n.val for n in node.neighbors] for node in result]) # Output: [[]]

# Example 3
adjList = []
nodes = []

result = Solution().cloneGraph(nodes[0] if nodes else None)
print([[n.val for n in node.neighbors] for node in result]) # Output: []