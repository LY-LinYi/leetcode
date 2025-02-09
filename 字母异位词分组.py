"""
    给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

    字母异位词 是由重新排列源单词的所有字母得到的一个新单词

    输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str_ in strs:
            str_sort = ''.join(sorted(str_))
            if str_sort not in dic.keys():
                dic[str_sort] = [str_]
            else:
                dic[str_sort].append(str_)
        
        return list(dic.values())
        
        

if __name__ == "__main__":
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs = ["s","s","s"]
    solution = Solution()
    print(solution.groupAnagrams(strs))
