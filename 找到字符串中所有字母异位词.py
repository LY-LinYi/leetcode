"""
    给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

    示例 1:
    输入: s = "cbaebabacd", p = "abc"
    输出: [0,6]
    解释:
    起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
    起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

    示例 2:
    输入: s = "abab", p = "ab"
    输出: [0,1,2]
    解释:
    起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
    起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
    起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
"""
class Solution(object):
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return []
        s_list = [0] * 26
        p_list = [0] * 26
        ans = []

        for i in range(p_len):
            s_list[ord(s[i]) - 97] += 1
            p_list[ord(p[i]) - 97] += 1

        if s_list == p_list:
            ans.append(0)

        for i in range(s_len-p_len):
            s_list[ord(s[i]) - 97] -= 1
            s_list[ord(s[i+p_len]) - 97] += 1
            if s_list == p_list:
                ans.append(i+1)
                
        return ans
    
    def findAnagrams2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return []
        ans = []
        tmp_list = [0] * 26

        for i in range(p_len):
            tmp_list[ord(s[i]) - 97] += 1
            tmp_list[ord(p[i]) - 97] -= 1
            
        differ = [c != 0 for c in tmp_list].count(True)

        if differ == 0:
            ans.append(0)
            
        for i in range(s_len - p_len):
            if tmp_list[ord(s[i]) - 97] == 1:
                differ -= 1
            elif tmp_list[ord(s[i]) - 97] == 0:
                differ += 1
                
            tmp_list[ord(s[i]) - 97] -= 1
            
            if tmp_list[ord(s[i + p_len]) - 97] == 0:
                differ += 1
            elif tmp_list[ord(s[i + p_len]) - 97] == -1:
                differ -= 1

            tmp_list[ord(s[i+p_len]) - 97] += 1
            
            if differ == 0:
                ans.append(i+1)
        return ans
        

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))