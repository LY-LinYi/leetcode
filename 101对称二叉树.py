"""
    给你一个二叉树的根节点 root ， 检查它是否轴对称。

    示例 1：
    输入：root = [1,2,2,3,4,4,3]
    输出：true

    示例 2：
    输入：root = [1,2,2,null,3,null,3]
    输出：false
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isSameTree(root.left, root.right)
        
    def isSameTree(self, p, q):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)