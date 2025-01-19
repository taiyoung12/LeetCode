class Solution {
    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        if(preorder.isEmpty() || inorder.isEmpty()) return null 

        val rootVal = preorder[0]
        val root = TreeNode(rootVal)

        val rootIndex = preorder.indices.find{ i -> inorder[i] == rootVal } ?: return null 
        
        root.left = buildTree(
            preorder.slice(1 until rootIndex+1).toIntArray(),
            inorder.slice(0 until rootIndex).toIntArray()
        )

        root.right = buildTree(
            preorder.slice(rootIndex + 1 until preorder.size).toIntArray(),
            inorder.slice(rootIndex + 1 until inorder.size).toIntArray()
        )

        return root
    }
}