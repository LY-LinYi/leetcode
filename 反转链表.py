"""
    给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
    
    示例 1：
    输入：head = [1,2,3,4,5]
    输出：[5,4,3,2,1]

    示例 2：
    输入：head = [1,2]
    输出：[2,1]

    示例 3：
    输入：head = []
    输出：[]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = None
        current = head
        while current:
            tmp = current.next
            current.next = result
            result = current
            current = tmp
        return result
        

if __name__ == "__main__":
    pass