# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        curr = [root]
        nums = []

        while curr:
            temp = []
            res = 0
            for c in curr:
                res+=c.val
                if c.left != None:
                    temp.append(c.left)
                if c.right != None:
                    temp.append(c.right)
            nums.append(res)
            curr = temp
        nums.sort(reverse=True)
        return -1 if k > len(nums) else nums[k-1]