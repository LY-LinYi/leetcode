"""
    给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

    示例 1：
    输入：head = [1,2,2,1]
    输出：true

    示例 2：
    输入：head = [1,2]
    输出：false
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome1(self, head):
        """
        使用数组存储，再用双指针判断
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type head: Optional[ListNode]
        :rtype: bool
        """
        headList = []
        current = head
        while current:
            headList.append(current.val)
            current = current.next
        i,j = 0, len(headList)
        return headList == headList[::-1]
    
    def isPalindrome2(self, head):
        """
        递归法, 先访问到链表最后一个节点，然后逐步判断开头开始的节点和当前节点是否相等，
        若相等返回上一层，且开头节点向后移动一位继续判断，
        若有一个不相等的情况，则逐层返回False。
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        
        return recursively_check()
    
    def isPalindrome3(self, head):
        """
        快慢指针法，快指针每次走两步，慢指针每次走一步，当快指针到达链表末尾时，慢指针在中间位置，
        使用快慢指针走到链表中间后，反转后半部分链表进行比较。
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if head is None:
            return True
        
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        
        # 判断回文
        result = True
        first_position = head
        second_position = second_half_start
        
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
            
        # 还原链表
        first_half_end.next = self.reverse_list(second_half_start)
        return result
        
    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_list(self, head):
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous



if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(Solution().isPalindrome(head))