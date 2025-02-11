"""
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

    示例 1: 
    输入: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6
    解释: 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
    
    示例 2: 
    输入: height = [4,2,0,3,2,5]
    输出: 9
"""
class Solution(object):
    def trap_dynamic(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_max = [height[0]] + [0] * (n - 1)
        ans = 0
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            
        right_max = [0] * (n - 1) + [height[n-1]]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
            
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans
    
    def trap_stack(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        stack = list()
        ans = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currendWidth = i - left - 1
                currendHeight = min(height[left], h) - height[top]
                ans += currendWidth * currendHeight
            stack.append(i)
        return ans
    
    def trap_point(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        n = len(height)
        left, right = 0, n-1
        leftMax, rightMax = 0, 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans
        

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap_dynamic(height))
    print(Solution().trap_stack(height))
    print(Solution().trap_point(height))