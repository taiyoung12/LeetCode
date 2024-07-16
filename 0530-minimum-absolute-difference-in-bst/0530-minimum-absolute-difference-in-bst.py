class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
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

        min_diff = 999999
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])

        return min_diff

        