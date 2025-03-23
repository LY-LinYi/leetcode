"""
    二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。
    同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
    路径和 是路径中各节点值的总和。
    给你一个二叉树的根节点 root ，返回其 最大路径和 。

    示例 1：
    输入：root = [1,2,3]
    输出：6
    解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

    示例 2：
    输入：root = [-10,9,20,null,null,15,7]
    输出：42
    解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
"""
import numpy as np

class Solution(object):
    def maxPathSum(self, root):
        """
        递归
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = -np.inf
        def dfs(root):
            if root is None:
                return 0
            max_left = dfs(root.left)
            max_right = dfs(root.right)
            nonlocal ans
            ans = max(ans, root.val+max_left+max_right)
            
            return max(max(max_left, max_right)+root.val, 0)
            
        dfs(root)
        return ans