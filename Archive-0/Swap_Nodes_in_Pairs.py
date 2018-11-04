# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t = ListNode(0)
        t.next = head

        s = t
        while True:
            n0 = s.next
            if n0 is None:
                break
            n1 = n0.next
            if n1 is None:
                break
            e = n1.next

            s.next, n0.next, n1.next = n1, e, n0
            s = n0

        return t.next
