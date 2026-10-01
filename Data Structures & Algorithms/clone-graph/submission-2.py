"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        adjMap = {}
        visited = set()
        to_visit = deque()
        visited.add(node)
        to_visit.append(node)
        while len(to_visit)>0:
            curr = to_visit.popleft()
            val = curr.val
            neigh = curr.neighbors
            adjMap[val] = [n.val for n in neigh]
            for n in neigh:
                if n.val in visited:
                    continue
                visited.add(n.val)
                to_visit.append(n)
        
        print(adjMap)
        

        node_map = dict()
        node_map[1] = Node(val=1)
    
        to_visit = deque()
        to_visit.append(1) #create the node before adding to queue
        while len(to_visit)>0:
            print(to_visit)
            curr = to_visit.popleft()
            print(curr)
            for neigh in adjMap[curr]:
                if neigh in node_map:
                    if node_map[neigh] not in node_map[curr].neighbors:
                        node_map[curr].neighbors.append(node_map[neigh])
                    if node_map[curr] not in node_map[neigh].neighbors:
                        node_map[neigh].neighbors.append(node_map[curr])
                else:
                    node_map[neigh] = Node(val=neigh)
                    to_visit.append(neigh)
        

        # print(node_map[1])
        # print(node_map[3].neighbors)
        # for n in node_map[3].neighbors:
        #     print(n.val)
        return node_map[1]

        

