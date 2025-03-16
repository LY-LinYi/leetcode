"""
    给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
    有效 二叉搜索树定义如下：
    节点的左子树只包含 小于 当前节点的数。
    节点的右子树只包含 大于 当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
    
    示例 1：
    输入：root = [2,1,3]
    输出：true

    示例 2：
    输入：root = [5,1,4,null,null,3,6]
    输出：false
    解释：根节点的值是 5 ，但是右子节点的值是 4 。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np

class Solution1(object):
    def isValidBST(self, root):
        """
        前序遍历法
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isValid(root)
    
    def isValid(self, root, left=-np.inf, right=np.inf):
        if root is None:
            return True
        x = root.val
        return left < x < right and self.isValid(root.left, left, x) and self.isValid(root.right, x, right)
    

class Solution2(object):
    pre = -np.inf
    def isValidBST(self, root):
        """
        中序遍历法
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        if not self.isValidBST(root.left) or root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
    

class Solution3(object):
    def isValidBST(self, root):
        """
        后续遍历法
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):
            if root is None:
                return np.inf, -np.inf
            l_min, l_max = dfs(root.left)
            r_min, r_max = dfs(root.right)
            x = root.val
            if x <= l_max or x >= r_min:
                return -np.inf, np.inf
            return min(l_min, x), max(r_max, x)
        return dfs(root)[1] != np.inf