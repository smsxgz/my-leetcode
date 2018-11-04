# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, i=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (not l1) and (not l2):
            if i == 0:
                return None
            else:
                return ListNode(1)
        elif not l1:
            return self.addTwoNumbers(ListNode(i), l2, 0)
        elif not l2:
            return self.addTwoNumbers(ListNode(i), l1, 0)
        else:
            s = l1.val + l2.val + i
            output = ListNode(s % 10)
            output.next = self.addTwoNumbers(l1.next, l2.next, s // 10)
            return output
