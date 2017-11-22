# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        x = self
        res = [str(x.val)]
        while x.next:
            x = x.next
            res.append(str(x.val))
        return '->'.join(res)


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        s = t = ListNode(0)
        t.next = head
        while True:
            nodes = [s]
            n0 = s
            for _ in range(k):
                n1 = n0.next
                if n1 is None:
                    return t.next
                nodes.append(n1)
                n0 = n1
            next_nodes = [nodes[-1], nodes[-1].next] + nodes[1:k]
            for node, node_next in zip(nodes, next_nodes):
                node.next = node_next
            s = nodes[1]
        return t.next

    def reverseKGroup1(self, head, k):
        if head is None or head.next is None or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while True:
            start, end = prev.next, prev
            for i in range(k):
                end = end.next
                if end is None:
                    return dummy.next
            newstart = end.next
            self.reverse(start, end)
            prev.next = end
            start.next = newstart
            prev = start

    def reverse(self, start, end):
        next = start.next
        prev, cur = start, start
        while cur != end:
            cur = next
            next = cur.next
            cur.next = prev
            prev = cur


if __name__ == '__main__':
    s = head = ListNode(0)
    for i in range(1, 10):
        s.next = ListNode(i)
        s = s.next
    s = Solution()
    s.reverseKGroup(head, 2)
