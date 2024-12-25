# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None : 
            return[]
        if root.val == targetSum and root.left == None and root.right == None:
            return [[root.val]]
        def dfs(root, val, answer, targetSum, comp):
            if root:
                comp.append(root.val)
                root.val+=val
                if root.val == targetSum and root.left == None and root.right == None:
                    answer.append(comp)
                else:
                    dfs(root.left, root.val, answer, targetSum, comp[:])
                    dfs(root.right, root.val, answer, targetSum, comp[:])
        
        answer = []

        dfs(root.left, root.val, answer, targetSum, [root.val])
        dfs(root.right, root.val, answer, targetSum, [root.val])

        return answer 