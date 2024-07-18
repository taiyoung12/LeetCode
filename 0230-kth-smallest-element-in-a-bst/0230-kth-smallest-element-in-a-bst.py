# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root : 
            return []
        q = deque()
        q.append(root)
        values = []

        while q :
            depth = len(q)
            for _ in range(depth) : 
                node = q.popleft()
                values.append(node.val)
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
        values.sort()
        return values[k-1]