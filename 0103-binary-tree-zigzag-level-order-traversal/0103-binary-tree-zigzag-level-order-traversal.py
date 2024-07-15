class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : 
            return []
        
        q = deque()
        q.append(root)
        direction = True 
        result = []

        while q : 
            depth = len(q)
            comp = []
            for _ in range(depth) :
                node = q.popleft()
                comp.append(node.val)
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
                    
            direction = not direction
            if direction : 
                comp.reverse()
            result.append(comp)
            
        return result