"""
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。

    示例 1:
    输入: s = "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

    示例 2:
    输入: s = "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

    示例 3:
    输入: s = "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。 
    请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

"""
    //外层循环扩展右边界，内层循环扩展左边界
    for (int l = 0, r = 0 ; r < n ; r++) {
        //当前考虑的元素
        while (l <= r && check()) {//区间[left,right]不符合题意
            //扩展左边界
        }
        //区间[left,right]符合题意，统计相关信息
    }
"""

class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)
        if n < 2:
            return n
        hashSet = set()
        left = 0
        for right in range(n):
            ch = s[right]
            while ch in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(ch)
            ans = max(ans, right - left + 1)
        return 
    
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashSet = set()
        n = len(s)
        right = -1
        ans = 0
        for i in range(n):
            if i != 0:
                hashSet.remove(s[i - 1])
            while right + 1 < n and s[right + 1] not in hashSet:
                hashSet.add(s[right + 1])
                right += 1
            ans = max(ans, right - i + 1)
        return ans
             

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring2("pwwkew"))