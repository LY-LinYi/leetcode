"""
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

    示例 1：
    输入：l1 = [1,2,4], l2 = [1,3,4]
    输出：[1,1,2,3,4,4]

    示例 2：
    输入：l1 = [], l2 = []
    输出：[]

    示例 3：
    输入：l1 = [], l2 = [0]
    输出：[0]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists1(self, list1, list2):
        """
        哨兵节点
        时间复杂度O(n+m),n 为链表1的长度，m 为链表2的长度
        空间复杂度O(1)  
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ans = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list1 or list2
        return ans.next
    
    def mergeTwoLists2(self, list1, list2):
        """
        递归
        时间复杂度O(n+m),n 为链表1的长度，m 为链表2的长度
        空间复杂度O(n+m)  
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None: return list2
        if list2 is None: return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists2(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists2(list1, list2.next)
        return list2

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    s = Solution()
    res = s.mergeTwoLists(l1, l2)