# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            out = ListNode(l1.val)
            out.next = self.mergeTwoLists(l1.next, l2)
        else:
            out = ListNode(l2.val)
            out.next = self.mergeTwoLists(l1, l2.next)
        return out

    def mergeTwoLists1(self, l1, l2):
        dummy = ListNode(None)
        newHead = dummy
        while l1 and l2:
            if l1.val < l2.val:
                newHead.next = l1
                l1 = l1.next
            else:
                newHead.next = l2
                l2 = l2.next
            newHead = newHead.next
        if l1:
            newHead.next = l1
        elif l2:
            newHead.next = l2
        return dummy.next
