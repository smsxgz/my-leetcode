# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def print_node(out):
    l = []
    while True:
        if not out:
            break
        l.append(out.val)
        out = out.next
    print(l)


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        a = head
        c = head
        for _ in range(n):
            head = head.next
        if not head:
            return c.next
        while True:
            head = head.next
            if not head:
                c.next = c.next.next
                return a
            c = c.next


if __name__ == '__main__':
    x = ListNode(1)
    y = x
    for i in range(2, 5):
        y.next = ListNode(i)
        y = y.next

    print_node(x)

    s = Solution()
    out = s.removeNthFromEnd(x, 1)

    print_node(out)
