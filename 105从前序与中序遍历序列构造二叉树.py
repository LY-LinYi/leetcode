"""
    给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， 
    inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

    示例 1:
    输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    输出: [3,9,20,null,null,15,7]

    示例 2:
    输入: preorder = [-1], inorder = [-1]
    输出: [-1]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        递归
        时间复杂度：O(n^2)
        空间复杂度：O(n^2)
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return None
        left_size = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:1+left_size],inorder[:left_size])
        right = self.buildTree(preorder[1+left_size:],inorder[left_size+1:])
        return TreeNode(preorder[0], left, right)
    
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        递归优化：哈希表存储index, 递归参数改成子数组下标区间左右端点
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        index = {x: i for i, x in enumerate(inorder)}
        def dfs(pre_l, pre_r, in_l, in_r):
            if pre_l == pre_r:
                return None
            left_size = index[preorder[pre_l]] - in_l
            left = dfs(pre_l+1, pre_l+1+left_size, in_l, in_l+left_size)
            right = dfs(pre_l+1+left_size, pre_r, in_l+1+left_size, in_r)
            return TreeNode(preorder[pre_l], left, right)
            
        return dfs(0, len(preorder), 0, len(inorder))