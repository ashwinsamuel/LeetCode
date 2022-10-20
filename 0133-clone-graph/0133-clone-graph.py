from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mem_dict = {}
        
        if not node: return node
        
        clone = Node(1)
        mem_dict[1] = clone
        
        que = deque()
        que.append(node)

        while que:
            out = que.popleft()
            current = mem_dict[out.val]
            
            for nd in out.neighbors:
                if nd.val not in mem_dict:
                    que.append(nd)

                    current_n = Node(nd.val)
                    mem_dict[nd.val] = current_n
                    current.neighbors.append(current_n)
                else:
                    current.neighbors.append(mem_dict[nd.val])
        
        return clone
        
        