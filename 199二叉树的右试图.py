"""
    给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

    示例 1：
    输入：root = [1,2,3,null,5,null,4]
    输出：[1,3,4]

    示例 2：
    输入：root = [1,2,3,4,null,null,null,5]
    输出：[1,3,4,5]

    示例 3：
    输入：root = [1,null,3]
    输出：[1,3]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        先递归右子树，再递归左子树，当某个深度首次到达时，对应的节点就在右视图中
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        def dfs(root, depth):
            if root is None:
                return
            if depth == len(ans):
                ans.append(root.val)
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)
        dfs(root, 0)
        return ans